# OKALI'S CAFE — Full-stack source package

This package keeps the original React + Vite cafe website and adds a Django REST Framework API with SQLite for menu data, reservations, contact messages, and customer orders.

## Contents
- `frontend/cafe-okali/` — React/Vite frontend (existing layout and components retained; API integration added)
- `backend/` — Django API and admin dashboard
- SQLite is created locally by Django migrations at `backend/db.sqlite3`

## Required software (Windows)
1. **Python 3.12** (check: `py --version`)
2. **Node.js LTS or newer** (check: `node --version`)
3. **npm** (check: `npm --version`)
4. **Visual Studio Code** (recommended extensions: Python, Pylance, ESLint)

## Local setup — first run

### A. Extract and open
1. Extract this ZIP into a folder you can easily find (example: `C:\Users\YOURNAME\Projects\OKALIS-CAFE`).
2. Open that extracted `OKALIS-CAFE` folder in VS Code.

### B. Backend terminal
Open a VS Code terminal, then:

```powershell
cd backend
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
python manage.py migrate
python manage.py seed_menu
python manage.py createsuperuser
python manage.py runserver
```

If PowerShell blocks activating the venv, run this in the same terminal session:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```
The API is now at `http://127.0.0.1:8000/`. Health check: `http://127.0.0.1:8000/api/health/`. Admin: `http://127.0.0.1:8000/admin/`.

### C. Frontend terminal
Keep the backend terminal running. Open a **second** VS Code terminal:
```powershell
cd frontend\cafe-okali
npm install
Copy-Item .env.example .env
npm run dev
```
Vite prints the local URL (normally `http://localhost:5173`). Open that URL. The menu should load from the backend. The frontend still has local fallback menu data if the API is temporarily offline.

## What to check
- Health endpoint returns `{"status":"ok", ...}`.
- Menu endpoint: `http://127.0.0.1:8000/api/menu/` should return 12 menu records after seeding.
- Reservation form: submit a test booking; check **Reservations** in Django Admin.
- Contact form: send a test message; check **Contact messages** in Admin.
- Order: add items to cart, enter checkout details, choose delivery or pickup, and place order; check **Orders** and order items in Admin. Delivery has a ₹40 charge; pickup has no delivery charge.
- Admin menu: edit availability, price, popular flag, and other fields.

## Admin dashboard
Log in with the superuser created during setup. The admin lets you manage menu items, reservations/status, messages/read status, and orders/status. The public API exposes menu reads and form/order creation only; admin records are not exposed through public list endpoints.


## Deployment overview
The static React frontend can be deployed to GitHub Pages, but **GitHub Pages cannot host the Django backend**. Deploy Django to a backend host (such as Render or another Python-capable service) and use a hosted database/persistent storage. SQLite is intended for local development and small demonstrations; standard ephemeral hosting can lose SQLite data on redeploy unless persistent storage is configured. For production, use PostgreSQL if supported by your chosen host.

When the backend is deployed, set `VITE_API_BASE_URL` in the frontend environment to the backend API base URL (including `/api`, e.g. `https://your-backend.example.com/api`) and rebuild/redeploy the frontend. On backend hosting, set `DJANGO_SECRET_KEY` to a strong secret, `DJANGO_DEBUG=0`, `DJANGO_ALLOWED_HOSTS` to the backend domain, and `CORS_ALLOWED_ORIGINS` to the deployed frontend origin(s). Do not commit `.env` files.

## Notes
- The package does not include `node_modules`, a virtual environment, or the SQLite database. Those are installed/generated locally.
- The Gallery import filename capitalization was corrected for case-sensitive filesystems.
- The active menu data in `Menu.jsx` was used as the starter seed because the separate previous `menuData.js` was different.
- Before public production launch, add stronger spam protections, production HTTPS/secret settings, backups, and a real payment provider if payments are needed. This version does not collect or process card/UPI payment details.
