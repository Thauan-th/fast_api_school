def student_list():
    return {"message": "All students"}


def student_search(id):
    return {"message": "user where id == path(id)"}


def student_create(student):
    return student


def student_update(id, student):
    return student


def student_delete(id):
    return {"message": f"student with id:{id} was deleted"}


resources = {
    "index": student_list,
    "show": student_search,
    "create": student_create,
    "update": student_update,
    "delete": student_delete
}
