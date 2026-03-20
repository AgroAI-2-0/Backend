from app.models.optimization.formulas import (
    calcular_costo_total,
    estimar_rendimiento,
    optimizar_recursos
)

def procesar_cultivo(data):
    recursos = data["recursos"]
    costos = data["costos"]
    params = data["parametros"]

    costo_total = calcular_costo_total(recursos, costos)

    rendimiento = estimar_rendimiento(
        recursos["agua"],
        recursos["fertilizante"],
        params["eficiencia_agua"],
        params["factor_suelo"]
    )

    optimizacion = optimizar_recursos(
        recursos["agua"],
        recursos["fertilizante"]
    )

    return {
        "costo_total": costo_total,
        "rendimiento_estimado": rendimiento,
        "optimizacion": optimizacion
    }
