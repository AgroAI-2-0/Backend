from pydantic import BaseModel, Field
from typing import Dict
from datetime import date

# -------------------------
# Cultivo
# -------------------------
class Cultivo(BaseModel):
    tipo_cultivo: str = Field(..., example="maiz")
    hectareas: float = Field(..., gt=0)
    fecha_siembra: date
    ubicacion: str


# -------------------------
# Recursos
# -------------------------
class Recursos(BaseModel):
    agua: float = Field(..., ge=0)           # litros
    fertilizante: float = Field(..., ge=0)   # kg
    insecticida: float = Field(..., ge=0)    # litros
    semillas: float = Field(..., ge=0)       # kg/unidades


# -------------------------
# Costos
# -------------------------
class Costos(BaseModel):
    agua: float = Field(..., ge=0)
    fertilizante: float = Field(..., ge=0)
    insecticida: float = Field(..., ge=0)
    semillas: float = Field(..., ge=0)


# -------------------------
# Parámetros agrícolas
# -------------------------
class Parametros(BaseModel):
    eficiencia_agua: float = Field(..., gt=0)
    factor_suelo: float = Field(..., gt=0)
    rendimiento_base: float = Field(..., gt=0)


# -------------------------
# Clima
# -------------------------
class Clima(BaseModel):
    temperatura: float
    humedad: float
    lluvia: float


# -------------------------
# Request completo
# -------------------------
class CultivoRequest(BaseModel):
    cultivo: Cultivo
    recursos: Recursos
    costos: Costos
    parametros: Parametros
    clima: Clima