# -*- coding: utf-8 -*-

CONEXIONES = [
    {
        "titulo": "Campo electrico vs campo magnetico",
        "tema_origen": "Tema 1 - Campo electrico",
        "tema_destino": "Tema 2 - Campo magnetostatico",
        "explicacion": """
En el Tema 1, una carga electrica crea un campo electrico E y otra carga siente una fuerza F = qE.

En el Tema 2, una carga en movimiento o una corriente crea un campo magnetico B, y una carga
en movimiento puede sentir una fuerza magnetica F = q(v x B).

Conexion clave:
- Campo electrico: puede actuar sobre cargas en reposo o en movimiento.
- Campo magnetico: actua sobre cargas en movimiento.
"""
    },
    {
        "titulo": "Coulomb vs Biot-Savart",
        "tema_origen": "Tema 1 - Campo electrico",
        "tema_destino": "Tema 2 - Campo magnetostatico",
        "explicacion": """
La Ley de Coulomb permite calcular campos o fuerzas electricas creadas por cargas.

La Ley de Biot-Savart permite calcular el campo magnetico creado por elementos de corriente.

Conexion clave:
- Coulomb: cargas electricas producen campo electrico.
- Biot-Savart: corrientes electricas producen campo magnetico.
- En ambos casos se calcula una contribucion elemental y luego se suma o integra.
"""
    },
    {
        "titulo": "Gauss vs Ampere",
        "tema_origen": "Tema 1 - Campo electrico",
        "tema_destino": "Tema 2 - Campo magnetostatico",
        "explicacion": """
La Ley de Gauss usa una superficie cerrada para relacionar el flujo electrico con la carga encerrada.

La Ley de Ampere usa una trayectoria cerrada para relacionar la circulacion del campo magnetico
con la corriente encerrada.

Conexion clave:
- Gauss: superficie cerrada + carga encerrada.
- Ampere: camino cerrado + corriente encerrada.
- Ambas leyes son especialmente utiles cuando hay simetria.
"""
    },
    {
        "titulo": "Superposicion electrica y magnetica",
        "tema_origen": "Tema 1 - Campo electrico",
        "tema_destino": "Tema 2 - Campo magnetostatico",
        "explicacion": """
En el campo electrico, si varias cargas producen campo en un punto, el campo total se obtiene
sumando vectorialmente las contribuciones.

En el campo magnetico ocurre algo parecido: si varias corrientes o segmentos de corriente producen
campo, el campo total tambien se obtiene por superposicion.

Conexion clave:
- En ambos temas hay que sumar vectores.
- Si todo esta en una linea, puede bastar con signos.
- Si esta en dos dimensiones, conviene usar componentes x e y.
"""
    },
    {
        "titulo": "Flujo electrico vs flujo magnetico",
        "tema_origen": "Tema 1 - Campo electrico",
        "tema_destino": "Tema 2 - Campo magnetostatico",
        "explicacion": """
En electrostatica aparece el flujo electrico para entender la Ley de Gauss.

En magnetostatica tambien aparece el flujo magnetico, pero con una diferencia importante:
no existen monopolos magneticos aislados. Por eso, las lineas de campo magnetico son cerradas.

Conexion clave:
- Flujo electrico: se relaciona con carga encerrada.
- Flujo magnetico: a traves de una superficie cerrada idealmente es cero.
"""
    }
]