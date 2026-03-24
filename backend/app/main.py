from fastapi import FastAPI

app = FastAPI()


@app.get('/api/health')
def healthcheck() -> dict[str, str]:
    return {'status': 'ok'}
