from fastapi import APIRouter
from app.models.controllers.cultivo_controller import procesar_cultivo
from app.models.models.schemas import CultivoRequest

router = APIRouter()

@router.post("/procesar-cultivo")
def procesar(data: CultivoRequest):
    return procesar_cultivo(data.dict())