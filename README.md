# 🐱 Stage 0 - Dynamic Profile API (FastAPI)

## 🚀 Overview
This project implements a simple RESTful API endpoint `/me` that returns profile information along with a random cat fact fetched dynamically from the [Cat Facts API](https://catfact.ninja/fact).  
It is built with **FastAPI** and hosted on **Railway**.

---

## 📁 Endpoint

### `GET /me`
**Response Example:**
```json
{
  "status": "success",
  "user": {
    "email": "your_email@example.com",
    "name": "Your Full Name",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-21T12:34:56.789Z",
  "fact": "Cats sleep 70% of their lives."
}
```

---

## ⚙️ Features
- Dynamic timestamp in ISO 8601 UTC format  
- Random cat fact fetched from an external API  
- Proper JSON structure with `Content-Type: application/json`  
- Basic rate limiting using **SlowAPI** (`5 requests per minute per IP`)  
- CORS enabled  
- Logging middleware for request tracking  

---

## 🧩 Tech Stack
- **Python 3.10+**
- **FastAPI**
- **Uvicorn**
- **SlowAPI**
- **Requests**

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/casey216/hng13-stage0-Dynamic-Profile-Endpoint.git
cd hng13-stage0-Dynamic-Profile-Endpoint
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Locally
```bash
python main.py
```
Visit: [http://127.0.0.1:8000/me](http://127.0.0.1:8000/me)

---


## 🧱 Dependencies
```
fastapi
uvicorn
requests
slowapi
```

---

## 🧠 Notes
- Timestamp updates dynamically for every request.  
- If the Cat Facts API is unavailable, a fallback message is returned.  
- API rate limited to 5 requests/minute per IP.

---

## ✍️ Author
**Name:** Kenechi Nzewi  
**Email:** caseynzewi@gmail.com  
**Stack:** Python/FastAPI
