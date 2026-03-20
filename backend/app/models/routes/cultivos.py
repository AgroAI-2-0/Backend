from fastapi import APIRouter
from app.services.cultivo_service import procesar_cultivo
from app.models.schemas import CultivoRequest

router = APIRouter()

@router.post("/procesar-cultivo")
def procesar(data: CultivoRequest):
    return procesar_cultivo(data.dict())