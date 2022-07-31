from Resources.Student import student_search, student_create, student_update, student_delete, student_list

from Models.Student import Student

from fastapi import FastAPI
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
        return student_list()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Bad Request")


@app.get('/users/{id}', status_code=status.HTTP_200_OK)
def find_user(id: int):
    try:
        return student_search(id)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Bad Request")


@app.post('/users', status_code=status.HTTP_201_CREATED)
def new_user(student: Student):
    try:
        return student_create(student)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Bad Request")


@app.put('/users/{id}', status_code=status.HTTP_200_OK)
def update_user(id: int, student: Student):
    try:
        return student_update(id, student)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Bad Request")


@app.delete('/users/{id}', status_code=status.HTTP_200_OK)
def delete_user(id):
    try:
        return student_delete(id)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Bad Request")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', host='localhost', port=8000,
                log_level='info', reload=True)
