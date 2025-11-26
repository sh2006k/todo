📝 Login & Todo Web App

Simple web app with login + todo list. Frontend: HTML/CSS/JS. Backend: Python HTTP server.

Features:

✅ Login (/login)

✅ Add / View Todos (/todos)

✅ Data stored in users.json & todos.json

Run:

Start backend: python server.py → http://127.0.0.1:5001

Open frontend: double-click index.html or python -m http.server 8000 → http://127.0.0.1:8000

Test Users:

amir / 123

acc2 / 123

acc3 / 123

API:

POST /login → {"message":"login ok"} or {"message":"invalid login"}

POST /todos → adds todo

GET /todos → returns all todos

⚠️ For demo only. Single-threaded, passwords are plain-text.
