# Backend

## Stack
- **Framework:** Flask
- **Database:** SQLite (via SQLAlchemy)
- **Auth:** JWT (Flask-JWT-Extended)

---

## Setup

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate it
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create your .env file
cp .env.example .env

# 5. Run the server
python run.py
```

Server runs at `http://localhost:5000`

---

## Project Structure

```
backend/
├── run.py                          # Start the server here
├── requirements.txt
├── .env.example
│
└── src/
    ├── app.py                      # Registers all blueprints — DO NOT TOUCH
    ├── config.py                   # App settings — DO NOT TOUCH
    ├── extensions.py               # Flask extensions — DO NOT TOUCH
    │
    ├── core/                       # Shared utilities — DO NOT TOUCH
    │   ├── auth_handler.py         # JWT decorator
    │   ├── response.py             # success_response / error_response
    │   └── helpers.py              # save_file, get_file_size
    │
    ├── models/                     # Database tables — DO NOT TOUCH
    │   ├── user_model.py           # Users table
    │   └── research_model.py      # Research table
    │
    └── features/                   # YOUR WORK GOES HERE
        ├── auth/
        │   ├── login/              # Dustine / Salangad
        │   │   └── validator.py    ← YOUR FILE
        │   └── signup/
        │       ├── username/       # Soliveres
        │       │   └── validator.py ← YOUR FILE
        │       ├── password/       # Luminarias
        │       │   └── validator.py ← YOUR FILE
        │       ├── phone/          # Nodesca
        │       │   └── validator.py ← YOUR FILE
        │       └── email/          # Lagdamen
        │           └── validator.py ← YOUR FILE
        │
        ├── library/                # Ruenz
        │   ├── routes.py           ← YOUR FILE
        │   └── service.py          ← YOUR FILE
        │
        ├── homepage/               # Kurt Chan
        │   ├── routes.py           ← YOUR FILE
        │   └── service.py          ← YOUR FILE
        │
        └── research/
            ├── upload/             # De Guzman + Nodesca + Ruenz
            │   ├── validator.py    ← YOUR FILE
            │   ├── service.py      ← YOUR FILE
            │   └── routes.py       ← YOUR FILE
            └── published/          # Meneses
                ├── service.py      ← YOUR FILE
                └── routes.py       ← YOUR FILE
```

---

## Task Per Member

### Dustine / Salangad — Login Page
**File:** `src/features/auth/login/validator.py`

Validate login input based on the flowchart:
- If username is empty → `"username is required"`
- If password is empty → `"password is required"`

---

### Soliveres — Input Username (Sign Up)
**File:** `src/features/auth/signup/username/validator.py`

Validate username based on the flowchart:
- If empty → `"username is required"`
- If less than 4 characters → `"username must be at least 4 characters"`
- If has special characters → `"username can only contain letters and numbers"`
- If already taken (check database) → `"username already taken"`

---

### Luminarias — Input Password & Confirm Password (Sign Up)
**File:** `src/features/auth/signup/password/validator.py`

Validate password based on the flowchart:
- If less than 8 characters → `"pass at least 8 char"`
- If no letters or no numbers → `"pass must include letters and numbers"`
- If password and confirm password don't match → `"password mismatch"`

---

### Nodesca — Input Phone Number (Sign Up) & Input Authors (Upload)
**Files:**
- `src/features/auth/signup/phone/validator.py`
- `src/features/research/upload/validator.py` → `validate_authors()`

Phone validation based on flowchart:
- If empty → `"phone num is required"`
- If contains letters → `"phone number contain only numbers"`
- If does not start with `09` → `"num should starts +639"`
- If not 11 digits → `"num should 11 digits"`
- If already in use (check database) → `"phone number already in use"`

Authors validation:
- If empty → `"authors is required"`
- If contains numbers → `"Letters only"`

---

### Lagdamen — Input Email (Sign Up)
**File:** `src/features/auth/signup/email/validator.py`

Validate email based on flowchart:
- If empty → `"email is required"`
- If not `name@gmail.com` or `name@plv.edu.ph` format → `"invalid format"`
- If already exists (check database) → `"email is already existed, try another"`

---

### Ruenz — Library Page, Input Year, Upload PDF
**Files:**
- `src/features/library/routes.py`
- `src/features/library/service.py`
- `src/features/research/upload/validator.py` → `validate_year()` and `validate_pdf()`

Library service — implement:
- `get_all_research()` → return all approved research
- `search_research(filters)` → filter by year, category, author

Library routes — implement:
- `GET /api/library/` → load all research
- `GET /api/library/search` → search with filters
- `GET /api/library/<id>/view` → view PDF inline
- `GET /api/library/<id>/download` → download PDF

Year validation:
- If empty → `"year is required"`
- If has letters → `"letters not accepted"`
- If not 4 digits → `"year must 4 digit format"`
- If less than 1990 → `"research at least year 1990 and above"`
- If greater than current year → `"invalid year"`

PDF validation:
- If empty → `"pdf is required"`
- If not a PDF file → `"file must be pdf"`
- If more than 10MB → `"file must be less than 10 mb"`

---

### Kurt Chan — Homepage
**Files:**
- `src/features/homepage/routes.py`
- `src/features/homepage/service.py`

Homepage service — implement:
- `get_homepage_data()` → return featured research and recent uploads

Homepage route — implement:
- `GET /api/homepage/` → load homepage data

---

### Meneses — Published Section
**Files:**
- `src/features/research/published/routes.py`
- `src/features/research/published/service.py`

Service — implement:
- `get_user_research(user_id)` → return all research by the logged-in user
- `delete_research(research_id, user_id)` → delete a research record
- `edit_research(research_id, user_id, data)` → update a research record

Routes — implement:
- `GET /api/research/published` → list user's research
- `GET /api/research/published/<id>/view` → view PDF
- `GET /api/research/published/<id>/download` → download PDF
- `PUT /api/research/published/<id>` → edit research
- `DELETE /api/research/published/<id>` → delete research

---

### De Guzman — Upload Research
**Files:**
- `src/features/research/upload/routes.py`
- `src/features/research/upload/service.py`
- `src/features/research/upload/validator.py` → `validate_title()`

Title validation:
- If empty → `"title is required"`
- If less than 5 characters → `"title must greater than 5 char"`
- If more than 150 characters → `"title must less than 150 char"`

Upload service — implement:
- `upload_research(data, file, user_id, upload_folder)` → save PDF and create research record in DB

Upload route — implement:
- `POST /api/research/upload` → protected route, accepts form data + PDF file

---

## How Responses Work

Every route returns JSON in this format:

```json
# Success
{ "success": true, "message": "...", "data": { ... } }

# Error
{ "success": false, "message": "...", "errors": [ "..." ] }
```

Use the helpers from `src/core/response.py`:
```python
from src.core.response import success_response, error_response

return success_response(data, "message")
return error_response("message", 400, errors)
```

---

## How to Protect a Route (JWT)

Add `@jwt_required()` to any route that needs login:

```python
from flask_jwt_extended import jwt_required, get_jwt_identity

@bp.route('/example', methods=['GET'])
@jwt_required()
def example():
    user_id = get_jwt_identity()
    ...
```

---

## API Endpoints Reference

| Method | Endpoint | Protected | Description |
|--------|----------|-----------|-------------|
| POST | `/api/auth/login` | No | Login |
| POST | `/api/auth/signup` | No | Sign up |
| GET | `/api/homepage/` | No | Homepage data |
| GET | `/api/library/` | No | All research |
| GET | `/api/library/search` | No | Search research |
| GET | `/api/library/<id>/view` | No | View PDF |
| GET | `/api/library/<id>/download` | No | Download PDF |
| POST | `/api/research/upload` | Yes | Upload research |
| GET | `/api/research/published` | Yes | My research |
| PUT | `/api/research/published/<id>` | Yes | Edit research |
| DELETE | `/api/research/published/<id>` | Yes | Delete research |
| GET | `/api/research/published/<id>/view` | Yes | View my PDF |
| GET | `/api/research/published/<id>/download` | Yes | Download my PDF |

---

## Git Workflow

```bash
# Before starting work
git pull https://github.com/arkeos-kzenon/online-archive.git

# Create your own branch
git checkout -b feature/your-name

# After finishing
git add .
git commit -m "your-name: done with validator"
git push origin feature/your-name
```

> Only merge to `main` when your feature is tested and working.
