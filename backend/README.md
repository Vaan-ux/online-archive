backend/
├── src/
│   ├── app.py
│   ├── config.py
│   ├── extensions.py
│   │
│   ├── features/
│   │   ├── auth/
│   │   │   ├── login/                  # Dustine / Salangad
│   │   │   │   ├── routes.py
│   │   │   │   ├── service.py
│   │   │   │   └── validator.py
│   │   │   └── signup/
│   │   │       ├── username/           # Soliveres
│   │   │       │   └── validator.py
│   │   │       ├── password/           # Luminarias
│   │   │       │   └── validator.py
│   │   │       ├── phone/              # Nodesca
│   │   │       │   └── validator.py
│   │   │       ├── email/              # Lagdamen
│   │   │       │   └── validator.py
│   │   │       ├── routes.py
│   │   │       └── service.py
│   │   │
│   │   ├── library/                    # Ruenz
│   │   │   ├── routes.py
│   │   │   ├── service.py
│   │   │   └── validator.py
│   │   │
│   │   ├── homepage/                   # Kurt Chan
│   │   │   ├── routes.py
│   │   │   └── service.py
│   │   │
│   │   ├── research/
│   │   │   ├── upload/                 # De Guzman
│   │   │   │   ├── routes.py
│   │   │   │   ├── service.py
│   │   │   │   └── validator.py        # title, authors (Nodesca) || year, pdf (Ruenz)
│   │   │   └── published/              # Meneses
│   │   │       ├── routes.py
│   │   │       └── service.py
│   │
│   ├── models/                         # Shared — 1 person manages this
│   │   ├── user_model.py
│   │   └── research_model.py
│   │
│   ├── core/                           # Shared utilities — 1 person manages this
│   │   ├── auth_handler.py
│   │   ├── response.py
│   │   └── helpers.py
│
├── uploads/
│   └── research/
├── .env
├── requirements.txt
└── main.py