# Task Manager

A full-stack task management application built with FastAPI (Python) and React (TypeScript). Manage your tasks efficiently with a modern, responsive interface.

![Task Manager](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)

## Features

✅ **Full CRUD Operations** - Create, Read, Update, Delete tasks  
✅ **Task Priorities** - Low, Medium, High priority levels  
✅ **Task Status** - Mark tasks as complete/incomplete  
✅ **Filtering** - View all, active, or completed tasks  
✅ **Statistics Dashboard** - Real-time task statistics  
✅ **Responsive Design** - Works on desktop and mobile  
✅ **Type Safety** - Full TypeScript support  
✅ **REST API** - Well-documented FastAPI backend  

## Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - SQL toolkit and ORM
- **SQLite** - Lightweight database
- **Pydantic** - Data validation using Python type hints
- **Uvicorn** - ASGI server

### Frontend
- **React 19** - UI library
- **TypeScript** - Type-safe JavaScript
- **Vite** - Next-generation frontend tooling
- **Tailwind CSS 4** - Utility-first CSS framework

## Project Structure

```
task-manager/
├── backend/
│   ├── main.py           # FastAPI application and routes
│   ├── models.py         # SQLAlchemy database models
│   ├── schemas.py        # Pydantic schemas
│   ├── database.py       # Database configuration
│   └── requirements.txt  # Python dependencies
│
└── frontend/
    ├── src/
    │   ├── components/   # React components
    │   │   ├── TaskForm.tsx
    │   │   └── TaskItem.tsx
    │   ├── services/     # API service layer
    │   │   └── api.ts
    │   ├── types/        # TypeScript type definitions
    │   │   └── task.ts
    │   ├── App.tsx       # Main application component
    │   ├── main.tsx      # Application entry point
    │   └── index.css     # Global styles
    └── package.json      # Node dependencies
```

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js 18+
- npm or yarn

### Backend Setup

1. **Navigate to the backend directory:**
   ```bash
   cd backend
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the backend server:**
   ```bash
   python3 -m uvicorn main:app --reload
   ```

   The API will be available at `http://localhost:8000`

5. **View API documentation:**
   - Swagger UI: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

### Frontend Setup

1. **Navigate to the frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm run dev
   ```

   The application will be available at `http://localhost:5173`

## API Documentation

### Base URL
```
http://localhost:8000
```

### Endpoints

#### Health Check
```http
GET /health
```
Returns the health status and version of the API.

**Response:**
```json
{
  "status": "healthy",
  "version": "1.0.0"
}
```

---

#### Get All Tasks
```http
GET /tasks
```
Retrieve all tasks from the database.

**Response:**
```json
[
  {
    "id": 1,
    "title": "Complete project",
    "description": "Finish the task manager project",
    "priority": "high",
    "completed": false,
    "created_at": "2025-11-15T10:30:00"
  }
]
```

---

#### Create Task
```http
POST /tasks
```
Create a new task.

**Request Body:**
```json
{
  "title": "New task",
  "description": "Task description (optional)",
  "priority": "medium"
}
```

**Fields:**
- `title` (string, required): Task title
- `description` (string, optional): Task description
- `priority` (string, required): One of `"low"`, `"medium"`, or `"high"`

**Response:**
```json
{
  "id": 2,
  "title": "New task",
  "description": "Task description",
  "priority": "medium",
  "completed": false,
  "created_at": "2025-11-15T10:35:00"
}
```

---

#### Update Task
```http
PUT /task/{task_id}
```
Update an existing task.

**Path Parameters:**
- `task_id` (integer): The ID of the task to update

**Request Body:**
```json
{
  "title": "Updated task",
  "description": "Updated description",
  "priority": "high"
}
```

**Response:**
```json
{
  "id": 2,
  "title": "Updated task",
  "description": "Updated description",
  "priority": "high",
  "completed": false,
  "created_at": "2025-11-15T10:35:00"
}
```

---

#### Toggle Task Completion
```http
PATCH /tasks/{task_id}/complete
```
Toggle the completion status of a task.

**Path Parameters:**
- `task_id` (integer): The ID of the task to toggle

**Response:**
```json
{
  "id": 2,
  "title": "Updated task",
  "description": "Updated description",
  "priority": "high",
  "completed": true,
  "created_at": "2025-11-15T10:35:00"
}
```

---

#### Delete Task
```http
DELETE /tasks/{task_id}
```
Delete a task from the database.

**Path Parameters:**
- `task_id` (integer): The ID of the task to delete

**Response:**
```json
{
  "message": "Task deleted successfully"
}
```

---

### Error Responses

All endpoints may return the following error responses:

**404 Not Found:**
```json
{
  "detail": "Task not found"
}
```

**422 Validation Error:**
```json
{
  "detail": [
    {
      "loc": ["body", "title"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

## Data Models

### Task Schema

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| id | integer | Auto | - | Unique task identifier |
| title | string | Yes | - | Task title |
| description | string | No | null | Task description |
| priority | string | Yes | "medium" | Priority level: "low", "medium", or "high" |
| completed | boolean | No | false | Task completion status |
| created_at | datetime | Auto | now() | Task creation timestamp |

## Development

### Running Tests

Backend:
```bash
cd backend
pytest
```

Frontend:
```bash
cd frontend
npm test
```

### Building for Production

Backend:
```bash
# The FastAPI app can be deployed using any ASGI server
uvicorn main:app --host 0.0.0.0 --port 8000
```

Frontend:
```bash
cd frontend
npm run build
npm run preview  # Preview the production build
```

## Environment Variables

### Backend
Create a `.env` file in the backend directory:

```env
DATABASE_URL=sqlite:///./tasks.db
CORS_ORIGINS=http://localhost:5173,http://localhost:3000
```

### Frontend
Create a `.env` file in the frontend directory:

```env
VITE_API_BASE_URL=http://localhost:8000
```

## CORS Configuration

The backend is configured to allow requests from:
- `http://localhost:5173` (Vite dev server)

To add more origins, update the `allow_origins` list in `backend/main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173', 'https://yourdomain.com'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes using conventional commits (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Commit Convention

We follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` - New features
- `fix:` - Bug fixes
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, etc.)
- `refactor:` - Code refactoring
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks

## License

This project is open source and available under the [MIT License](LICENSE).

## Troubleshooting

### Backend Issues

**Port already in use:**
```bash
# Kill the process using port 8000
lsof -ti:8000 | xargs kill -9
```

**Database locked:**
```bash
# Remove the database file and restart
rm tasks.db
```

### Frontend Issues

**Port already in use:**
```bash
# Kill the process using port 5173
lsof -ti:5173 | xargs kill -9
```

**Module not found:**
```bash
# Clear node_modules and reinstall
rm -rf node_modules package-lock.json
npm install
```

## Contact

- Repository: [https://github.com/AlbertNewton254/task-manager](https://github.com/AlbertNewton254/task-manager)
- Issues: [https://github.com/AlbertNewton254/task-manager/issues](https://github.com/AlbertNewton254/task-manager/issues)

---

Built with ❤️ using FastAPI and React
