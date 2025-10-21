from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import requests
from datetime import datetime, timezone
import logging
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

# Initialize FastAPI app
app = FastAPI(
    title="hng13-stage0-Dynamic-Profile-Endpoint",
    description="Returns profile info and a random cat fact",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Initialize Limiter (rate limiting)
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Simple middleware to log requests and responses."""
    logger = logging.getLogger("uvicorn.access")
    logger.info(f"Incoming request: {request.method} {request.url.path} from {request.client.host}")
    
    response = await call_next(request)
    
    logger.info(f"Response status: {response.status_code}")
    return response


@app.get("/me")
@limiter.limit("5/minute")
def get_profile(request: Request):
    """Return user info, current UTC time, and a random cat fact."""
    user_info = {
        "email": "caseynzewi@gmail.com",
        "name": "Kenechi Nzewi",
        "stack": "Python/FastAPI"
    }

    timestamp = datetime.now(timezone.utc).isoformat()

    # Fetch cat fact safely
    try:
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        response.raise_for_status()
        cat_fact = response.json().get("fact", "No fact found.")
    except requests.RequestException as e:
        logging.error(f"Cat Facts API error: {e}")
        cat_fact = "Could not fetch cat fact at this time."

    data = {
        "status": "success",
        "user": user_info,
        "timestamp": timestamp,
        "fact": cat_fact
    }

    return JSONResponse(content=data, media_type="application/json")
