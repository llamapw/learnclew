from fastapi import FastAPI

# Import all models to register them with SQLAlchemy
from app.models import user, auth_identity, project, source, job, asset, workspace, course, progress, stored_object

app = FastAPI()


@app.get('/api/health')
def healthcheck() -> dict[str, str]:
    return {'status': 'ok'}
