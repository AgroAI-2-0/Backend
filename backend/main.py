from fastapi import FastAPI
from app.models.routes import cultivos
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Agro Platform API",
    description="Plataforma para optimización de recursos agrícolas",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
# Registrar rutas
app.include_router(cultivos.router, prefix="/api")

# Endpoint base
@app.get("/")
def root():
    return {"message": "API Agro Platform funcionando correctamente"}