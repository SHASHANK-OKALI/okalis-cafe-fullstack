# ☕ OKALI'S CAFE

A modern cafe website built with **React, Vite, Django REST Framework, and SQLite**. OKALI'S CAFE combines an elegant customer-facing experience with a backend system for managing menu items, reservations, customer orders, and contact messages.

---

## 📌 About the Project

OKALI'S CAFE is a full-stack web application designed to provide a smooth online cafe experience. Customers can explore the menu, place orders, book tables, and contact the cafe, while the admin panel provides a centralized place to manage cafe data.

The project brings together a responsive React frontend and a Django REST API backend.

## ✨ Features

- ☕ Dynamic menu powered by the backend API
- 🛒 Online food ordering
- 📅 Table reservation system
- 📩 Contact form and message handling
- ⭐ Customer testimonials
- 🖼️ Cafe gallery
- 🔧 Django admin dashboard
- 🗄️ Database-backed menu, orders, reservations, and messages
- 📱 Responsive user interface

## 🛠️ Tech Stack

### Frontend
- React
- Vite
- JavaScript
- Bootstrap / CSS
- React Icons

### Backend
- Python
- Django
- Django REST Framework
- django-cors-headers

### Database
- SQLite

### Tools
- Git & GitHub
- VS Code
- REST API

## 🏗️ Project Structure

```text
okalis-cafe-fullstack/
│
├── backend/
│   ├── config/
│   ├── cafe/
│   ├── manage.py
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   └── cafe-okali/
│       ├── public/
│       ├── src/
│       ├── package.json
│       └── .env.example
│
├── .gitignore
└── README.md
```

## 🔄 Application Workflow

1. Customers browse the cafe website.
2. The React frontend requests data from the Django API.
3. Django processes menu, order, reservation, and contact requests.
4. Data is stored in the database.
5. The cafe administrator manages records through Django Admin.

## 🔌 API Endpoints

| Endpoint | Description |
|---|---|
| `/api/health/` | API health check |
| `/api/menu/` | Retrieve cafe menu |
| `/api/reservations/` | Table reservations |
| `/api/orders/` | Customer orders |
| `/api/contact/` | Contact form submissions |
| `/admin/` | Django administration |

## 🚀 Run Locally

### Prerequisites

Install the following:

- Python
- Node.js & npm
- Git

### 1. Clone the repository

```bash
git clone https://github.com/SHASHANK-OKALI/okalis-cafe-fullstack.git
cd okalis-cafe-fullstack
```

### 2. Setup the backend

```bash
cd backend
py -m venv .venv
```

Activate the virtual environment on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Create your environment file:

```powershell
Copy-Item .env.example .env
```

Run migrations:

```bash
python manage.py migrate
```

Populate the initial cafe menu:

```bash
python manage.py seed_menu
```

Create an administrator account:

```bash
python manage.py createsuperuser
```

Start the Django development server:

```bash
python manage.py runserver
```

Backend: `http://127.0.0.1:8000/`

### 3. Setup the frontend

Open a **new terminal**:

```bash
cd frontend/cafe-okali
```

Install dependencies:

```bash
npm install
```

Create the frontend environment file using the supplied template if required:

```powershell
Copy-Item .env.example .env
```

Start the Vite development server:

```bash
npm run dev
```

Frontend: `http://localhost:5173/`

> Keep both frontend and backend development servers running while using the application locally.

## 🔐 Environment Variables

Environment files are used for configuration and should not contain publicly exposed secrets.

- Backend: `backend/.env`
- Frontend: `frontend/cafe-okali/.env`

Refer to the respective `.env.example` templates to configure your local environment.

**Never commit your real `.env` files, credentials, secret keys, or private configuration.**

## 🖥️ Admin Panel

Access Django Admin locally:

`http://127.0.0.1:8000/admin/`

The admin dashboard allows authorized administrators to manage registered cafe records and data.

## 📸 Screenshots

_Add screenshots of the website here to showcase the interface._

<!-- Add screenshots in a screenshots folder and link them here -->

## 🌐 Deployment

Deployment configuration for the full-stack version is in progress.

- Frontend: React + Vite
- Backend: Django REST Framework
- Production database and hosting configuration: To be configured

## 👨‍💻 Developer

**Shashank Okali**

- GitHub: [SHASHANK-OKALI](https://github.com/SHASHANK-OKALI)

---

⭐ If you like this project, feel free to explore the source code and connect!
