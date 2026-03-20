def calcular_costo_total(recursos, costos):
    total = 0
    for key in recursos:
        total += recursos[key] * costos.get(key, 0)
    return total


def estimar_rendimiento(agua, fertilizante, eficiencia, factor_suelo):
    return (agua * eficiencia) + (fertilizante * factor_suelo)


def optimizar_recursos(agua, fertilizante):
    return {
        "agua_recomendada": agua * 0.9,
        "fertilizante_recomendado": fertilizante * 0.9
    }