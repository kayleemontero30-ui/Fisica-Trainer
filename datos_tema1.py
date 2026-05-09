# -*- coding: utf-8 -*-

TEMA1 = {
    "nombre": "Tema 1 - Campo eléctrico y electrostática",

    "resumen": """
Este tema trata de cargas eléctricas en reposo y de cómo producen fuerzas, campos y potenciales.

Ideas clave:
- La carga puede ser positiva o negativa.
- Cargas del mismo signo se repelen.
- Cargas de signo opuesto se atraen.
- La fuerza eléctrica entre dos cargas se calcula con la ley de Coulomb.
- El campo eléctrico E indica qué fuerza sentiría una carga de prueba positiva.
- Si hay varias cargas, se usa superposición: sumas vectorialmente los campos o fuerzas.
- El potencial eléctrico V es energía potencial por unidad de carga.
- La ley de Gauss permite calcular E fácilmente cuando hay mucha simetría.

Lo más importante para ejercicios:
1. Si te piden fuerza entre cargas, usa Coulomb.
2. Si te piden campo en un punto, calcula E de cada carga y suma vectores.
3. Si te piden potencial, suma escalares, no vectores.
4. Si aparece esfera, cilindro o plano infinito con simetría, piensa en Gauss.
5. Si aparece “trabajo” o “energía”, piensa en potencial eléctrico.
""",

    "formulas": [
        {
            "nombre": "Ley de Coulomb",
            "formula": "F = k |q1 q2| / r^2",
            "uso": "Calcular la fuerza eléctrica entre dos cargas puntuales.",
            "cuando_usarla": [
                "Cuando el enunciado habla de dos cargas separadas una distancia.",
                "Cuando te piden fuerza de atracción o repulsión.",
                "Cuando te dan q1, q2 y r."
            ],
            "detalles": [
                "La dirección va sobre la línea que une las cargas.",
                "Mismo signo: repulsión.",
                "Signo opuesto: atracción.",
                "k ≈ 8.99e9 N·m²/C²."
            ]
        },
        {
            "nombre": "Campo eléctrico de una carga puntual",
            "formula": "E = k |q| / r^2",
            "uso": "Calcular el campo creado por una carga en un punto.",
            "cuando_usarla": [
                "Cuando te piden el campo en un punto debido a una carga.",
                "Cuando luego tienes que calcular F=qE."
            ],
            "detalles": [
                "Sale de cargas positivas.",
                "Entra hacia cargas negativas.",
                "E es vector."
            ]
        },
        {
            "nombre": "Fuerza sobre una carga en un campo",
            "formula": "F = q E",
            "uso": "Calcular la fuerza que siente una carga dentro de un campo eléctrico.",
            "cuando_usarla": [
                "Cuando ya tienes E y te dan una carga de prueba.",
                "Cuando el enunciado dice 'fuerza sobre la carga'."
            ],
            "detalles": [
                "Si q es positiva, F tiene el mismo sentido que E.",
                "Si q es negativa, F tiene sentido contrario a E."
            ]
        },
        {
            "nombre": "Superposición de campos",
            "formula": "E_total = E1 + E2 + ...",
            "uso": "Sumar campos de varias cargas.",
            "cuando_usarla": [
                "Cuando hay más de una carga.",
                "Cuando el punto donde calculas el campo recibe contribuciones de varias fuentes."
            ],
            "detalles": [
                "Se suma vectorialmente.",
                "Primero calcula dirección y componentes de cada campo."
            ]
        },
        {
            "nombre": "Potencial eléctrico de una carga puntual",
            "formula": "V = k q / r",
            "uso": "Calcular potencial eléctrico en un punto.",
            "cuando_usarla": [
                "Cuando te piden potencial y no campo.",
                "Cuando hay varias cargas y puedes sumar escalares."
            ],
            "detalles": [
                "V puede ser positivo o negativo.",
                "El potencial se suma como escalar: V_total=V1+V2+..."
            ]
        },
        {
            "nombre": "Energía potencial eléctrica",
            "formula": "U = q V",
            "uso": "Relacionar potencial con energía de una carga.",
            "cuando_usarla": [
                "Cuando te piden energía potencial.",
                "Cuando te piden trabajo entre dos puntos."
            ],
            "detalles": [
                "También puede usarse ΔU=qΔV."
            ]
        },
        {
            "nombre": "Flujo eléctrico",
            "formula": "Phi_E = E A cos(theta)",
            "uso": "Calcular flujo de campo eléctrico a través de una superficie plana.",
            "cuando_usarla": [
                "Cuando aparece una superficie y un campo uniforme.",
                "Cuando te piden líneas de campo atravesando un área."
            ],
            "detalles": [
                "theta es el ángulo entre E y la normal de la superficie.",
                "Si E es perpendicular a la superficie, theta=0 y Phi=EA."
            ]
        },
        {
            "nombre": "Ley de Gauss",
            "formula": "Phi_E = Q_enc / epsilon_0",
            "uso": "Calcular campo eléctrico con simetría.",
            "cuando_usarla": [
                "Distribución esférica, cilíndrica o plano infinito.",
                "Cuando E tiene magnitud constante sobre una superficie gaussiana."
            ],
            "detalles": [
                "No es que Gauss no sirva siempre; es que solo simplifica cuando hay simetría suficiente.",
                "epsilon_0 ≈ 8.85e-12 C²/(N·m²)."
            ]
        }
    ],

    "interpretacion_enunciados": [
        {
            "palabra_clave": "dos cargas separadas",
            "que_significa": "Normalmente piden fuerza eléctrica con ley de Coulomb.",
            "que_suele_pedir": [
                "Fuerza de atracción o repulsión.",
                "Distancia necesaria para cierta fuerza.",
                "Carga desconocida."
            ],
            "operaciones_recomendadas": [
                "Convierte microCoulomb, nanoCoulomb, cm, etc. a SI.",
                "Usa F=k|q1q2|/r^2.",
                "Determina si la fuerza es atractiva o repulsiva por los signos.",
                "Dibuja la línea que une las cargas."
            ],
            "pista_examen": "Si solo hay dos cargas y una distancia, casi siempre es Coulomb."
        },
        {
            "palabra_clave": "campo en un punto",
            "que_significa": "Te piden el vector E producido por una o varias cargas.",
            "que_suele_pedir": [
                "Módulo y dirección del campo.",
                "Punto donde el campo se anula.",
                "Campo total por superposición."
            ],
            "operaciones_recomendadas": [
                "Calcula E de cada carga.",
                "Decide dirección: sale de +, entra en -.",
                "Descompón en componentes si no están en línea.",
                "Suma vectorialmente."
            ],
            "pista_examen": "Campo E es vector. No sumes solo módulos si hay geometría en 2D."
        },
        {
            "palabra_clave": "potencial",
            "que_significa": "Te piden una magnitud escalar relacionada con energía.",
            "que_suele_pedir": [
                "Potencial en un punto.",
                "Trabajo para mover una carga.",
                "Energía potencial."
            ],
            "operaciones_recomendadas": [
                "Usa V=kq/r.",
                "Suma potenciales como escalares.",
                "Luego si hace falta usa U=qV o W=-ΔU."
            ],
            "pista_examen": "Potencial V no tiene dirección: es mucho más fácil de sumar que E."
        },
        {
            "palabra_clave": "superficie cerrada / gaussiana",
            "que_significa": "El ejercicio probablemente quiere Ley de Gauss.",
            "que_suele_pedir": [
                "Flujo eléctrico.",
                "Campo eléctrico con simetría.",
                "Carga encerrada."
            ],
            "operaciones_recomendadas": [
                "Identifica la simetría: esfera, cilindro, plano.",
                "Elige superficie gaussiana adecuada.",
                "Calcula Q_enc.",
                "Usa Phi_E=Q_enc/epsilon_0 y despeja E si hay simetría."
            ],
            "pista_examen": "Gauss ayuda cuando E es constante en partes de la superficie o el flujo se simplifica."
        }
    ],

    "flashcards": [
        {"id": "fis1_fc_01", "frente": "¿Qué pasa con dos cargas del mismo signo?", "reverso": "Se repelen.", "categoria": "Coulomb"},
        {"id": "fis1_fc_02", "frente": "¿Qué pasa con dos cargas de signo opuesto?", "reverso": "Se atraen.", "categoria": "Coulomb"},
        {"id": "fis1_fc_03", "frente": "¿La fuerza eléctrica es vector o escalar?", "reverso": "Vector.", "categoria": "Fuerza eléctrica"},
        {"id": "fis1_fc_04", "frente": "¿El potencial eléctrico es vector o escalar?", "reverso": "Escalar.", "categoria": "Potencial"},
        {"id": "fis1_fc_05", "frente": "¿De dónde salen las líneas de campo eléctrico?", "reverso": "Salen de cargas positivas y entran en cargas negativas.", "categoria": "Campo eléctrico"},
        {"id": "fis1_fc_06", "frente": "¿Cuándo conviene usar Gauss?", "reverso": "Cuando hay simetría: esfera, cilindro o plano infinito.", "categoria": "Gauss"}
    ],

    "preguntas_vf": [
        {"id": "fis1_vf_01", "pregunta": "Cargas del mismo signo se atraen.", "respuesta": False, "explicacion": "Cargas del mismo signo se repelen.", "categoria": "Coulomb", "dificultad": "facil"},
        {"id": "fis1_vf_02", "pregunta": "El campo eléctrico de una carga positiva apunta hacia afuera.", "respuesta": True, "explicacion": "Por convenio, E apunta en la dirección de la fuerza sobre una carga positiva.", "categoria": "Campo eléctrico", "dificultad": "facil"},
        {"id": "fis1_vf_03", "pregunta": "El potencial eléctrico se suma vectorialmente.", "respuesta": False, "explicacion": "El potencial es escalar, se suma algebraicamente.", "categoria": "Potencial", "dificultad": "media"},
        {"id": "fis1_vf_04", "pregunta": "La ley de Gauss siempre simplifica cualquier problema de campo eléctrico.", "respuesta": False, "explicacion": "Solo simplifica mucho cuando hay simetría suficiente.", "categoria": "Gauss", "dificultad": "media"},
        {"id": "fis1_vf_05", "pregunta": "Si q es negativa, la fuerza F=qE tiene sentido contrario a E.", "respuesta": True, "explicacion": "El signo negativo invierte la dirección.", "categoria": "Fuerza eléctrica", "dificultad": "facil"}
    ],

    "preguntas_mc": [
        {
            "id": "fis1_mc_01",
            "pregunta": "¿Qué fórmula usarías para la fuerza entre dos cargas puntuales?",
            "opciones": ["F=k|q1q2|/r²", "V=IR", "B=μ0I/2πr", "ε=-dΦ/dt"],
            "respuesta": 1,
            "explicacion": "La fuerza entre cargas puntuales se calcula con la ley de Coulomb.",
            "categoria": "Coulomb",
            "dificultad": "facil"
        },
        {
            "id": "fis1_mc_02",
            "pregunta": "Si hay varias cargas y quieres el campo total, debes:",
            "opciones": ["Sumar potenciales", "Sumar campos vectorialmente", "Multiplicar cargas", "Usar siempre Kirchhoff"],
            "respuesta": 2,
            "explicacion": "El campo eléctrico es vector, así que se suman componentes.",
            "categoria": "Superposición",
            "dificultad": "facil"
        },
        {
            "id": "fis1_mc_03",
            "pregunta": "¿Cuál es la mejor pista para usar Ley de Gauss?",
            "opciones": ["Circuito con resistencias", "Simetría esférica/cilíndrica/plana", "Carga moviéndose en B", "Una bobina girando"],
            "respuesta": 2,
            "explicacion": "Gauss es muy útil con simetría alta.",
            "categoria": "Gauss",
            "dificultad": "media"
        }
    ]
}
