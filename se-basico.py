# Base de conocimiento
base_de_conocimiento = {
    "Ingresos Altos": "Apto para solicitar tarjeta de crédito",
    "Buen Historial de Crédito": "Apto para solicitar tarjeta de crédito",
    "Deudas Bajas": "Apto para solicitar tarjeta de crédito",
    "Antigüedad Laboral Alta": "Apto para solicitar tarjeta de crédito",
    "Antigüedad en el Domicilio Alta": "Apto para solicitar tarjeta de crédito"
}

# Motor de inferencia
def evaluar_aprobacion_tarjeta(hechos):
    for hecho in hechos:
        if hecho not in base_de_conocimiento:
            return "No apto para solicitar tarjeta de crédito"
    
    return "Apto para solicitar tarjeta de crédito"

if __name__ == "__main__":
    hechos = []

    print("Por favor, responda algunas preguntas para determinar su elegibilidad para una tarjeta de crédito.")
    
    ingresos = input("¿Tiene ingresos altos? (Sí/No): ")
    historial_credito = input("¿Tiene un buen historial de crédito? (Sí/No): ")
    deudas = input("¿Tiene deudas bajas? (Sí/No): ")
    antiguedad_laboral = input("¿Tiene antigüedad laboral alta? (Sí/No): ")
    antiguedad_domicilio = input("¿Tiene antigüedad en el domicilio alta? (Sí/No): ")

    if ingresos.lower() == "sí":
        hechos.append("Ingresos Altos")
    if historial_credito.lower() == "sí":
        hechos.append("Buen Historial de Crédito")
    if deudas.lower() == "sí":
        hechos.append("Deudas Bajas")
    if antiguedad_laboral.lower() == "sí":
        hechos.append("Antigüedad Laboral Alta")
    if antiguedad_domicilio.lower() == "sí":
        hechos.append("Antigüedad en el Domicilio Alta")

    resultado = evaluar_aprobacion_tarjeta(hechos)
    print("Resultado:", resultado)
