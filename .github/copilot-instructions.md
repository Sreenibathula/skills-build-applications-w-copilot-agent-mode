# OctoFit Tracker Copilot Instructions

## Project Overview
OctoFit Tracker is a fitness app for high school students, featuring user authentication, activity logging, team management, leaderboards, and personalized workout suggestions. Built with React frontend, Django REST backend, and MongoDB database.

## Architecture
- **Frontend**: React app in `octofit-tracker/frontend/`, using Bootstrap for styling and React Router for navigation.
- **Backend**: Django project in `octofit-tracker/backend/octofit_tracker/`, with Djongo for MongoDB integration.
- **Database**: MongoDB, accessed via Django ORM only (no direct MongoDB scripts).
- **Communication**: REST API between frontend and backend.

## Key Patterns
- **Directory Structure**: Always work from root; prefix commands with `octofit-tracker/backend/` or `octofit-tracker/frontend/` instead of changing directories.
- **Backend Serializers**: Convert MongoDB ObjectId fields to strings in serializers.py.
- **URLs**: Include codespace-aware base URLs in urls.py (e.g., `https://{codespace_name}-8000.app.github.dev`).
- **Settings**: Add codespace ALLOWED_HOSTS in settings.py.
- **Frontend**: Use `--prefix octofit-tracker/frontend` for npm installs; import Bootstrap CSS in src/index.js.
- **Testing**: Use curl to test REST endpoints.

## Development Workflows
- **Setup**: Create venv with `python3 -m venv octofit-tracker/backend/venv`; activate and install from `octofit-tracker/backend/requirements.txt`.
- **Django Project**: Run `django-admin startproject octofit_tracker octofit-tracker/backend` from root.
- **Migrations**: `python manage.py migrate` in backend dir.
- **Running**: Use VS Code launch configs for backend (port 8000) and frontend (port 3000).
- **MongoDB**: Check with `ps aux | grep mongod`; use Django ORM for data operations.

## Conventions
- **Ports**: Backend on 8000 (public), frontend on 3000 (public), MongoDB on 27017 (private).
- **Environment**: Use `CODESPACE_NAME` env var for dynamic URLs and hosts.
- **Images**: App logo at `docs/octofitapp-small.png`.
- **Packages**: Specific versions in requirements.txt; install with pip in activated venv.

Reference: `.github/instructions/` for detailed guidelines per component.</content>
<parameter name="filePath">/workspaces/skills-build-applications-w-copilot-agent-mode/.github/copilot-instructions.md