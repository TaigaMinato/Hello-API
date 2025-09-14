# Hello API
This is a practice project to learn modern development flow (GitHub Flow, CI/CD, and deployment) with FastAPI.  
The main goal is **to experience the end-to-end workflow** rather than building a complex application.

---

## Features
- Simple FastAPI application with `/hello` endpoint
- GitHub Flow: branch → pull request → review → merge
- CI with GitHub Actions (Ruff for linting, pytest for testing)
- CD with Render (auto deploy on push to `main`)

---

## How to run locally
```bash
# Create & activate virtual environment
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Run API
uvicorn main:app --reload
```
Then open: https://hello-api-jnl4.onrender.com/hello

## Endpoints
```bash
GET /hello
# Response
{
  "message": "Hello, World!"
}
```
You can also pass a query parameter:
```bash
GET /hello?name=Minato
# Response
{
  "message": "Hello, Minato!"
}
```

## Development Flow
1. Branching
- Create a feature branch (feature/add-ci, test/add-pytest, etc.)
- Push changes and open a Pull Request
- Run CI automatically
2. CI (Continuous Integration)
- Ruff: lint check
- pytest: unit tests
3. CD (Continuous Deployment)
- Render is connected to GitHub
- On merge into main, a new deployment is triggered automatically

## Project Structure
```bash
Hello-API/
 ├── .github/workflows/ci.yml   # CI pipeline (lint + test)
 ├── main.py                    # FastAPI application
 ├── requirements.txt           # Dependencies
 ├── tests/                     # Pytest test cases
 └── README.md                  # Project documentation
 ```

## Deployment
The service is deployed automatically on Render:
-> https://hello-api-jnl4.onrender.com/hello

## Purpose
This project is not about writing advanced code, but about experiencing real-world development practices in small-scale projects:
- GitHub Flow (branch -> PR -> merge)
- CI/CD pipeline
- Dependency & environment management
- Deploying to a live environment