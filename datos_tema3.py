# -*- coding: utf-8 -*-

TEMA3 = {
    "nombre": "Tema 3 - Corriente, circuitos e inducción",

    "resumen": """
Este tema trata de circuitos eléctricos, resistencias, capacitores, corriente continua e inducción.

Ideas clave:
- La corriente I mide carga por unidad de tiempo.
- La ley de Ohm relaciona voltaje, corriente y resistencia: V=IR.
- En serie, la misma corriente pasa por todos los elementos.
- En paralelo, todos los elementos tienen la misma diferencia de potencial.
- Kirchhoff permite resolver circuitos más complejos.
- Un capacitor almacena carga y energía.
- En un circuito RC, la carga y descarga no son instantáneas: siguen curvas exponenciales.
- Faraday dice que un flujo magnético cambiante induce fem.
- Lenz dice que la corriente inducida se opone al cambio de flujo.

Lo más importante para ejercicios:
1. Si es una resistencia simple, usa Ohm.
2. Si son resistencias en serie/paralelo, reduce el circuito.
3. Si hay nodos y mallas, usa Kirchhoff.
4. Si aparece un capacitor con tiempo, piensa en RC.
5. Si aparece flujo magnético cambiante, piensa en Faraday-Lenz.
""",

    "formulas": [
        {
            "nombre": "Corriente eléctrica",
            "formula": "I = Δq / Δt",
            "uso": "Relacionar corriente con carga que atraviesa una sección.",
            "cuando_usarla": [
                "Cuando te dan carga y tiempo.",
                "Cuando preguntan cuántos coulombs pasan."
            ],
            "detalles": [
                "Unidad: ampere = C/s."
            ]
        },
        {
            "nombre": "Ley de Ohm",
            "formula": "V = I R",
            "uso": "Relacionar voltaje, corriente y resistencia.",
            "cuando_usarla": [
                "Circuitos con resistencias óhmicas.",
                "Cuando conoces dos de V, I, R."
            ],
            "detalles": [
                "No todos los materiales cumplen Ohm linealmente, pero en problemas básicos se asume."
            ]
        },
        {
            "nombre": "Resistencia de un conductor",
            "formula": "R = rho L / A",
            "uso": "Calcular resistencia por geometría y material.",
            "cuando_usarla": [
                "Cuando te dan resistividad, longitud y área.",
                "Cuando comparas cables."
            ],
            "detalles": [
                "Más longitud: más resistencia.",
                "Más área: menos resistencia."
            ]
        },
        {
            "nombre": "Potencia eléctrica",
            "formula": "P = I V = I^2 R = V^2/R",
            "uso": "Calcular energía por unidad de tiempo en circuitos.",
            "cuando_usarla": [
                "Cuando te piden potencia disipada.",
                "Cuando aparece efecto Joule."
            ],
            "detalles": [
                "Elige la forma según datos disponibles."
            ]
        },
        {
            "nombre": "Resistencias en serie",
            "formula": "R_eq = R1 + R2 + ...",
            "uso": "Reducir resistencias conectadas una tras otra.",
            "cuando_usarla": [
                "Cuando la misma corriente pasa por todas.",
                "Cuando no hay bifurcaciones entre resistencias."
            ],
            "detalles": [
                "En serie se suma la resistencia."
            ]
        },
        {
            "nombre": "Resistencias en paralelo",
            "formula": "1/R_eq = 1/R1 + 1/R2 + ...",
            "uso": "Reducir resistencias conectadas entre los mismos dos nodos.",
            "cuando_usarla": [
                "Cuando tienen el mismo voltaje.",
                "Cuando hay ramas."
            ],
            "detalles": [
                "La equivalente en paralelo es menor que la menor resistencia individual."
            ]
        },
        {
            "nombre": "Kirchhoff nodos",
            "formula": "Σ I_entrantes = Σ I_salientes",
            "uso": "Conservación de carga en un nodo.",
            "cuando_usarla": [
                "Cuando hay ramas en un circuito.",
                "Cuando te piden corrientes desconocidas."
            ],
            "detalles": [
                "También se escribe ΣI=0 con signos."
            ]
        },
        {
            "nombre": "Kirchhoff mallas",
            "formula": "Σ ΔV = 0",
            "uso": "Conservación de energía alrededor de una malla cerrada.",
            "cuando_usarla": [
                "Cuando hay varias baterías o resistencias.",
                "Cuando no puedes reducir todo por serie/paralelo."
            ],
            "detalles": [
                "Al atravesar una resistencia en sentido de la corriente: caída -IR."
            ]
        },
        {
            "nombre": "Capacitancia",
            "formula": "C = Q / V",
            "uso": "Relacionar carga, voltaje y capacitancia.",
            "cuando_usarla": [
                "Cuando hay capacitores.",
                "Cuando te dan carga y diferencia de potencial."
            ],
            "detalles": [
                "Unidad: faradio (F)."
            ]
        },
        {
            "nombre": "Carga de capacitor en RC",
            "formula": "q(t)=CV(1-e^{-t/RC})",
            "uso": "Carga de un capacitor con batería y resistencia.",
            "cuando_usarla": [
                "Cuando aparece carga de capacitor en función del tiempo.",
                "Cuando el circuito está cargándose."
            ],
            "detalles": [
                "La constante de tiempo es tau=RC."
            ]
        },
        {
            "nombre": "Descarga de capacitor en RC",
            "formula": "q(t)=Q0 e^{-t/RC}",
            "uso": "Descarga de un capacitor a través de una resistencia.",
            "cuando_usarla": [
                "Cuando se desconecta la batería y el capacitor se descarga.",
                "Cuando aparece decaimiento exponencial."
            ],
            "detalles": [
                "La corriente también decae exponencialmente."
            ]
        },
        {
            "nombre": "Ley de Faraday",
            "formula": "epsilon = -N dPhi_B/dt",
            "uso": "Fem inducida por flujo magnético cambiante.",
            "cuando_usarla": [
                "Cuando hay bobina, imán o campo magnético variable.",
                "Cuando el flujo cambia con el tiempo."
            ],
            "detalles": [
                "El signo menos representa la ley de Lenz."
            ]
        }
    ],

    "interpretacion_enunciados": [
        {
            "palabra_clave": "resistencias en serie",
            "que_significa": "La misma corriente atraviesa cada resistencia.",
            "que_suele_pedir": [
                "Resistencia equivalente.",
                "Corriente total.",
                "Caída de voltaje en cada resistencia."
            ],
            "operaciones_recomendadas": [
                "Suma resistencias.",
                "Calcula I=V/R_eq.",
                "Calcula V_i=I R_i."
            ],
            "pista_examen": "Serie = misma corriente."
        },
        {
            "palabra_clave": "resistencias en paralelo",
            "que_significa": "Las resistencias comparten los mismos dos nodos.",
            "que_suele_pedir": [
                "Resistencia equivalente.",
                "Corriente por rama.",
                "Corriente total."
            ],
            "operaciones_recomendadas": [
                "Usa 1/R_eq=sum(1/R_i).",
                "El voltaje es el mismo en cada rama.",
                "Calcula I_i=V/R_i.",
                "Suma corrientes de ramas."
            ],
            "pista_examen": "Paralelo = mismo voltaje."
        },
        {
            "palabra_clave": "nodo / unión",
            "que_significa": "El ejercicio quiere Kirchhoff de corrientes.",
            "que_suele_pedir": [
                "Corrientes desconocidas.",
                "Relación entre ramas."
            ],
            "operaciones_recomendadas": [
                "Elige signos para corrientes entrantes y salientes.",
                "Aplica ΣI=0.",
                "Combina con Ohm o mallas si hace falta."
            ],
            "pista_examen": "Nodo = conservación de carga."
        },
        {
            "palabra_clave": "malla / circuito cerrado",
            "que_significa": "El ejercicio quiere Kirchhoff de voltajes.",
            "que_suele_pedir": [
                "Corrientes en mallas.",
                "Voltajes en resistencias.",
                "Ecuaciones de circuito."
            ],
            "operaciones_recomendadas": [
                "Elige sentido de recorrido.",
                "Suma subidas y caídas de potencial.",
                "En resistencia: caída -IR si vas con la corriente.",
                "En batería: +epsilon si vas de - a +."
            ],
            "pista_examen": "Malla = conservación de energía."
        },
        {
            "palabra_clave": "capacitor con tiempo",
            "que_significa": "Probablemente es circuito RC.",
            "que_suele_pedir": [
                "Carga q(t).",
                "Corriente i(t).",
                "Voltaje del capacitor.",
                "Constante de tiempo."
            ],
            "operaciones_recomendadas": [
                "Identifica si carga o descarga.",
                "Calcula tau=RC.",
                "Usa exponencial adecuada.",
                "Recuerda que en t=tau ya hay ~63% de carga final al cargar."
            ],
            "pista_examen": "Si ves e^{-t/RC}, estás en RC."
        },
        {
            "palabra_clave": "flujo magnético cambiante",
            "que_significa": "El ejercicio quiere Faraday-Lenz.",
            "que_suele_pedir": [
                "Fem inducida.",
                "Sentido de corriente inducida.",
                "Cambio de flujo."
            ],
            "operaciones_recomendadas": [
                "Calcula Phi_B=BAcos(theta).",
                "Mira qué cambia: B, A o theta.",
                "Usa epsilon=-N dPhi/dt.",
                "Usa Lenz para el sentido."
            ],
            "pista_examen": "Si el flujo no cambia, no hay fem inducida."
        }
    ],

    "flashcards": [
        {"id": "fis3_fc_01", "frente": "¿Ley de Ohm?", "reverso": "V=IR.", "categoria": "Ohm"},
        {"id": "fis3_fc_02", "frente": "En serie, ¿qué magnitud es igual?", "reverso": "La corriente.", "categoria": "Serie"},
        {"id": "fis3_fc_03", "frente": "En paralelo, ¿qué magnitud es igual?", "reverso": "El voltaje.", "categoria": "Paralelo"},
        {"id": "fis3_fc_04", "frente": "¿Qué dice Kirchhoff en nodos?", "reverso": "La suma de corrientes entrantes iguala la suma de salientes.", "categoria": "Kirchhoff"},
        {"id": "fis3_fc_05", "frente": "¿Constante de tiempo en RC?", "reverso": "tau=RC.", "categoria": "RC"},
        {"id": "fis3_fc_06", "frente": "¿Qué requiere Faraday para inducir fem?", "reverso": "Flujo magnético cambiante.", "categoria": "Faraday"}
    ],

    "preguntas_vf": [
        {"id": "fis3_vf_01", "pregunta": "En resistencias en serie pasa la misma corriente por todas.", "respuesta": True, "explicacion": "En serie no hay bifurcaciones.", "categoria": "Serie", "dificultad": "facil"},
        {"id": "fis3_vf_02", "pregunta": "En resistencias en paralelo todas tienen el mismo voltaje.", "respuesta": True, "explicacion": "Están conectadas entre los mismos dos nodos.", "categoria": "Paralelo", "dificultad": "facil"},
        {"id": "fis3_vf_03", "pregunta": "La resistencia equivalente en paralelo siempre es mayor que todas las resistencias individuales.", "respuesta": False, "explicacion": "En paralelo la equivalente es menor que la menor resistencia individual.", "categoria": "Paralelo", "dificultad": "media"},
        {"id": "fis3_vf_04", "pregunta": "Si el flujo magnético es constante, no hay fem inducida.", "respuesta": True, "explicacion": "Faraday depende de dPhi/dt.", "categoria": "Faraday", "dificultad": "facil"},
        {"id": "fis3_vf_05", "pregunta": "En un circuito RC la constante de tiempo es tau=R/C.", "respuesta": False, "explicacion": "La constante de tiempo es tau=RC.", "categoria": "RC", "dificultad": "facil"}
    ],

    "preguntas_mc": [
        {
            "id": "fis3_mc_01",
            "pregunta": "¿Qué fórmula representa la ley de Ohm?",
            "opciones": ["V=IR", "F=qvB", "E=kq/r²", "Phi=BAcosθ"],
            "respuesta": 1,
            "explicacion": "Ohm relaciona voltaje, corriente y resistencia.",
            "categoria": "Ohm",
            "dificultad": "facil"
        },
        {
            "id": "fis3_mc_02",
            "pregunta": "En paralelo:",
            "opciones": ["La corriente es igual en todas", "El voltaje es igual en todas", "Las resistencias se suman directamente", "No hay corriente"],
            "respuesta": 2,
            "explicacion": "Las ramas en paralelo comparten los mismos dos nodos.",
            "categoria": "Paralelo",
            "dificultad": "facil"
        },
        {
            "id": "fis3_mc_03",
            "pregunta": "¿Qué ley usas si aparece una malla cerrada?",
            "opciones": ["Kirchhoff de voltajes", "Coulomb", "Gauss", "Biot-Savart"],
            "respuesta": 1,
            "explicacion": "En una malla se usa ΣΔV=0.",
            "categoria": "Kirchhoff",
            "dificultad": "facil"
        },
        {
            "id": "fis3_mc_04",
            "pregunta": "Si aparece una bobina y flujo magnético cambiante, piensas en:",
            "opciones": ["Faraday-Lenz", "Ohm únicamente", "Coulomb", "Serie-paralelo"],
            "respuesta": 1,
            "explicacion": "La fem inducida aparece por cambio de flujo magnético.",
            "categoria": "Faraday",
            "dificultad": "media"
        }
    ]
}
