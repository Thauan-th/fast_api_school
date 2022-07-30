from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi import Path

app = FastAPI()


@app.get('/')
def root():
    return {"message": "Running"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', host='localhost', port=8000,
                log_level='info', reload=True)
