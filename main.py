from Resources.Student import resources

from Models.Student import Student

from fastapi import FastAPI
from fastapi import Body
from fastapi import HTTPException
from fastapi import status
from fastapi import Path

app = FastAPI()


@app.get('/', status_code=status.HTTP_200_OK)
def root():
    return {"message": "Running"}


@app.get('/users', status_code=status.HTTP_200_OK)
def all_users():
    try:
        return resources["index"]()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Bad Request")


@app.get('/users/{id}', status_code=status.HTTP_200_OK)
def find_user(id: int = Path(default=None, title="Student ID", description="ID to find a studant")):
    try:
        return resources["show"](id)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Bad Request")


@app.post('/users', status_code=status.HTTP_201_CREATED)
def new_user(student: Student = Body(default=None, title="Studant Informations", description="Studant registration information")):
    try:
        return resources["create"](student)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Bad Request")


@app.put('/users/{id}', status_code=status.HTTP_200_OK)
def update_user(id: int = Path(default='None', title="Student ID", description="ID to find the user to be updated"),
                student: Student = Body(default=None, title="Student Informations", description="Studant registration Informations")):
    try:
        return resources["update"](id, student)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Bad Request")


@app.delete('/users/{id}', status_code=status.HTTP_200_OK)
def delete_user(id: int = Path(default=None, title="Student ID", description="Student to be deleted")):
    try:
        return resources["delete"](id)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Bad Request")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', host='localhost', port=8000,
                log_level='info', reload=True)
