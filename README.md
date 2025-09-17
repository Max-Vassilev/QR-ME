## What is QRME? 🔗

QRME lets users create a personal profile with their key links (LinkedIn, GitHub, website, etc.) and get a unique QR code.  
Scanning the code opens a clean, mobile-friendly page showing all their links — perfect for quick sharing.

---

## Features ✨

- User registration and login with email & password (JWT auth)  
- Add, view, edit, and delete personal links (up to 5 URLs per user in the free tier)  
- Unique public profile page (`/u/username`)  
- Auto-generated QR code to profile  
- Minimal, mobile-friendly design  

---

## Tech Stack 🛠️

- Frontend: React + Vite + React Router DOM  
- Backend: FastAPI (Python)  
- Auth: Email/password with JWT  
- Database: PostgreSQL  
- Deployment: Docker on AWS EC2  

---

## Future Plans 🚀

- Google OAuth login  
- Custom QR code designs  
- Paid premium plans with increased URL limits and more features  

---

## Deployment 🚢

Dockerize frontend and backend with Docker Compose. Deploy on AWS EC2 with Docker installed. Use Docker Hub or AWS ECR for images.

---

## Why QRME? 💡

A simple, elegant way to share all your essential links via one QR code. Ideal for professionals and creatives wanting an easy digital business card.

---

## Gallery 🖼️

![image](https://github.com/user-attachments/assets/541ffad5-ad96-4277-b8d3-25f6438437dc)

![image](https://github.com/user-attachments/assets/d88992e8-9b9a-4418-99bf-80c06148c4ec)

![image](https://github.com/user-attachments/assets/78bca298-427a-4b74-9b7c-c026494e02f6)

![image](https://github.com/user-attachments/assets/d9f376e1-7925-4f1b-ada8-a0d50325aee8)

---
# Run Project in Development Environment

## Backend:

### Create a virtual environment
```bash
python3 -m venv venv
```

### Activate the virtual environment (Linux/macOS)
```bash
source venv/bin/activate
```

### Install dependencies from requirements.txt
```bash
pip install -r requirements.txt
```

### Apply database migrations
```bash
python3 manage.py migrate
```

### Run backend server
```bash
python3 manage.py runserver
```
## Frontend:

### Install dependencies
```bash
npm i
```

### Run frontend server
```bash
npm run dev
```

# Run Project in Production Environment

python3 manage.py runserver 0.0.0.0:8000
