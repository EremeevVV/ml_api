import uvicorn
from ml_api.run_api import create_app

app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info", host="0.0.0.0")
