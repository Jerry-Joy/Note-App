# Note App

A full-stack note-taking application built with Django REST Framework and React.

## Features

- ✅ User authentication (JWT)
- ✅ Create, read, update, delete notes
- ✅ Responsive design (mobile-friendly)
- ✅ Modern UI with Tailwind CSS
- ✅ Secure API endpoints

## Tech Stack

### Backend
- Django 5.2.8
- Django REST Framework 3.16.1
- Simple JWT for authentication
- SQLite database (can be changed to PostgreSQL)

### Frontend
- React 19.2.0
- Vite 7.2.4
- React Router DOM 7.10.1
- Tailwind CSS 3.x
- Axios for API requests

## Installation

### Prerequisites
- Python 3.8+
- Node.js 16+
- Git

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create and activate virtual environment:
```bash
# Windows
python -m venv env
env\Scripts\activate

# macOS/Linux
python3 -m venv env
source env/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

The backend will run on `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The frontend will run on `http://localhost:5173`

## Usage

1. Register a new account at `/register`
2. Login with your credentials at `/login`
3. Create, edit, and delete notes from the home page
4. Logout when finished

## API Endpoints

- `POST /api/user/register/` - Register new user
- `POST /api/token/` - Login and get JWT tokens
- `POST /api/token/refresh/` - Refresh access token
- `GET /api/notes/` - Get all user's notes
- `POST /api/notes/` - Create a new note
- `GET /api/notes/<id>/` - Get a specific note
- `PUT /api/notes/<id>/` - Update a note
- `DELETE /api/notes/<id>/` - Delete a note

## Project Structure

```
Note App/
├── backend/
│   ├── api/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── urls.py
│   ├── backend/
│   │   ├── settings.py
│   │   └── urls.py
│   └── manage.py
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Forms.jsx
│   │   │   └── ProtectedRoute.jsx
│   │   ├── pages/
│   │   │   ├── Home.jsx
│   │   │   ├── Login.jsx
│   │   │   ├── Register.jsx
│   │   │   ├── NotFound.jsx
│   │   │   └── Logout.jsx
│   │   ├── api.js
│   │   ├── constants.js
│   │   └── App.jsx
│   ├── index.html
│   └── package.json
└── requirements.txt
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

Built with ❤️ by Jerry

## Screenshots

_(Add screenshots of your app here)_

## Future Features

- [ ] AI note summarization
- [ ] Tags and categories
- [ ] Dark mode
- [ ] Search functionality
- [ ] Export notes to PDF
- [ ] Note sharing
