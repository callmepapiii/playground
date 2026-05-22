from fastapi import APIRouter
from model.explorer import Explorer
import fake.explorer as service

router = APIRouter(prefix = "/explorer")

@router.get("/")
def get_all() -> list[Explorer]:
    return service.return_all()

@router.get("/{name}")
def get_one(name) -> Explorer | None:
    return service.get_one(name)

@router.post("/")
def  create(explore: Explorer) -> Explorer:
    return service.create(explorer)

@router.delete("/{name}")
def delete(name):
    return service.delete(name)

@router.put("/")
def replace(explorer: Explorer) -> Explorer:
    return service.replace(explorer)

@router.patch("/")
def modify(explorer: Explorer) -> Explorer:
    return service.modify(explorer)