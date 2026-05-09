# -*- coding: utf-8 -*-

TEMA2 = {
    "nombre": "Tema 2 - Campo magnetostático",

    "resumen": """
Este tema estudia campos magnéticos producidos por corrientes y fuerzas magnéticas.

Ideas clave:
- Una carga en movimiento en un campo magnético puede sentir fuerza.
- La fuerza magnética depende de q, v, B y del ángulo entre v y B.
- Una corriente eléctrica crea campo magnético.
- Para un hilo recto largo, las líneas de B son circunferencias alrededor del hilo.
- La dirección se obtiene con la regla de la mano derecha.
- Biot-Savart se usa para calcular B por elementos de corriente.
- Ampère se usa cuando hay simetría suficiente.
- El flujo magnético mide cuánto campo B atraviesa una superficie.

Lo más importante para ejercicios:
1. Si hay q moviéndose en B, usa F=q v x B.
2. Si hay un hilo largo con corriente, piensa en B=mu0 I/(2 pi r).
3. Si hay simetría circular, piensa en Ampère.
4. Si hay espira o segmento de corriente, piensa en Biot-Savart.
5. Si hay superficie y B, piensa en flujo magnético.
""",

    "formulas": [
        {
            "nombre": "Fuerza magnética sobre carga",
            "formula": "F = q v × B",
            "uso": "Calcular fuerza sobre una carga en movimiento dentro de un campo magnético.",
            "cuando_usarla": [
                "Cuando aparece una partícula cargada con velocidad v en un campo B.",
                "Cuando te preguntan dirección usando regla de la mano derecha."
            ],
            "detalles": [
                "Módulo: F=|q|vB sin(theta).",
                "Si q es negativa, la dirección se invierte.",
                "Si v es paralela a B, la fuerza es cero."
            ]
        },
        {
            "nombre": "Fuerza magnética sobre conductor",
            "formula": "F = I L × B",
            "uso": "Fuerza sobre un tramo de conductor con corriente en un campo magnético.",
            "cuando_usarla": [
                "Cuando hay un alambre con corriente dentro de un campo B.",
                "Cuando te dan longitud L, corriente I y campo B."
            ],
            "detalles": [
                "Módulo: F=ILB sin(theta)."
            ]
        },
        {
            "nombre": "Campo de hilo recto largo",
            "formula": "B = mu0 I / (2 pi r)",
            "uso": "Campo magnético alrededor de un hilo largo.",
            "cuando_usarla": [
                "Cuando el conductor es recto, largo y con corriente.",
                "Cuando hay simetría circular alrededor del hilo."
            ],
            "detalles": [
                "La dirección se obtiene con la regla de la mano derecha.",
                "Las líneas de B son circunferencias alrededor del hilo."
            ]
        },
        {
            "nombre": "Ley de Ampère",
            "formula": "∮ B·dl = mu0 I_enc",
            "uso": "Calcular B usando simetría.",
            "cuando_usarla": [
                "Hilo largo.",
                "Solenoide ideal.",
                "Toroide.",
                "Situaciones con simetría fuerte."
            ],
            "detalles": [
                "Solo simplifica si B es constante o fácil en la trayectoria amperiana."
            ]
        },
        {
            "nombre": "Biot-Savart",
            "formula": "dB = (mu0/4pi) I dl × r_hat / r^2",
            "uso": "Calcular el campo magnético creado por elementos pequeños de corriente.",
            "cuando_usarla": [
                "Espiras.",
                "Segmentos de corriente.",
                "Cuando no puedes usar Ampère fácilmente."
            ],
            "detalles": [
                "Es una integral vectorial.",
                "La dirección viene del producto vectorial dl × r_hat."
            ]
        },
        {
            "nombre": "Flujo magnético",
            "formula": "Phi_B = B A cos(theta)",
            "uso": "Campo magnético atravesando una superficie plana.",
            "cuando_usarla": [
                "Cuando aparece una superficie, bobina o espira.",
                "Cuando luego se usa Faraday."
            ],
            "detalles": [
                "theta es el ángulo entre B y la normal al área.",
                "Unidad: weber (Wb)."
            ]
        }
    ],

    "interpretacion_enunciados": [
        {
            "palabra_clave": "carga moviéndose en B",
            "que_significa": "Probablemente piden fuerza magnética.",
            "que_suele_pedir": [
                "Módulo de F.",
                "Dirección de F.",
                "Trayectoria circular."
            ],
            "operaciones_recomendadas": [
                "Identifica q, v y B.",
                "Calcula F=|q|vBsin(theta).",
                "Usa regla de la mano derecha para q positiva.",
                "Si q es negativa, invierte el sentido."
            ],
            "pista_examen": "Si v es paralela a B, no hay fuerza magnética."
        },
        {
            "palabra_clave": "hilo recto con corriente",
            "que_significa": "Probablemente piden campo magnético circular alrededor del hilo.",
            "que_suele_pedir": [
                "Campo B a distancia r.",
                "Dirección de B.",
                "Fuerza entre hilos paralelos."
            ],
            "operaciones_recomendadas": [
                "Usa B=mu0 I/(2 pi r).",
                "Aplica regla de la mano derecha.",
                "Para dos hilos: mismo sentido se atraen, sentidos opuestos se repelen."
            ],
            "pista_examen": "El campo no apunta hacia afuera del hilo; rodea al hilo en circunferencias."
        },
        {
            "palabra_clave": "trayectoria amperiana",
            "que_significa": "El ejercicio quiere Ley de Ampère.",
            "que_suele_pedir": [
                "Campo de hilo largo.",
                "Campo de solenoide.",
                "Campo de toroide."
            ],
            "operaciones_recomendadas": [
                "Elige una curva cerrada con la simetría del problema.",
                "Calcula corriente encerrada.",
                "Usa ∮B·dl=mu0 I_enc."
            ],
            "pista_examen": "Ampère se parece a Gauss: solo simplifica con simetría."
        },
        {
            "palabra_clave": "espira / segmento de corriente",
            "que_significa": "Probablemente necesitas Biot-Savart.",
            "que_suele_pedir": [
                "Campo en el centro de una espira.",
                "Campo en el eje de una espira.",
                "Dirección del campo creado por corriente."
            ],
            "operaciones_recomendadas": [
                "Divide en elementos dl.",
                "Analiza la dirección con dl × r_hat.",
                "Usa simetría para cancelar componentes."
            ],
            "pista_examen": "En espiras, muchas componentes se cancelan por simetría."
        }
    ],

    "flashcards": [
        {"id": "fis2_fc_01", "frente": "¿Fórmula de fuerza magnética sobre una carga?", "reverso": "F = q v × B.", "categoria": "Fuerza magnética"},
        {"id": "fis2_fc_02", "frente": "¿Cuándo es cero la fuerza magnética?", "reverso": "Cuando v es paralela o antiparalela a B, o si q=0.", "categoria": "Fuerza magnética"},
        {"id": "fis2_fc_03", "frente": "¿Qué forma tienen las líneas de B alrededor de un hilo recto?", "reverso": "Circunferencias alrededor del hilo.", "categoria": "Hilo recto"},
        {"id": "fis2_fc_04", "frente": "¿Qué pasa con dos hilos con corriente en el mismo sentido?", "reverso": "Se atraen.", "categoria": "Hilos paralelos"},
        {"id": "fis2_fc_05", "frente": "¿Cuándo conviene usar Ampère?", "reverso": "Cuando hay simetría fuerte.", "categoria": "Ampère"},
        {"id": "fis2_fc_06", "frente": "¿Qué mide el flujo magnético?", "reverso": "Cuánto campo B atraviesa una superficie.", "categoria": "Flujo magnético"}
    ],

    "preguntas_vf": [
        {"id": "fis2_vf_01", "pregunta": "Si v es paralela a B, la fuerza magnética es máxima.", "respuesta": False, "explicacion": "Si v es paralela a B, sin(theta)=0 y la fuerza es cero.", "categoria": "Fuerza magnética", "dificultad": "facil"},
        {"id": "fis2_vf_02", "pregunta": "El campo magnético alrededor de un hilo recto largo forma circunferencias.", "respuesta": True, "explicacion": "La dirección se obtiene con la regla de la mano derecha.", "categoria": "Hilo recto", "dificultad": "facil"},
        {"id": "fis2_vf_03", "pregunta": "Dos hilos paralelos con corrientes en el mismo sentido se repelen.", "respuesta": False, "explicacion": "Corrientes en el mismo sentido se atraen; sentidos opuestos se repelen.", "categoria": "Hilos paralelos", "dificultad": "media"},
        {"id": "fis2_vf_04", "pregunta": "Ampère siempre es más fácil que Biot-Savart.", "respuesta": False, "explicacion": "Ampère solo simplifica con simetría adecuada.", "categoria": "Ampère", "dificultad": "media"}
    ],

    "preguntas_mc": [
        {
            "id": "fis2_mc_01",
            "pregunta": "¿Qué fórmula usarías para el campo alrededor de un hilo recto largo?",
            "opciones": ["B=mu0 I/(2πr)", "E=kq/r²", "V=IR", "ε=-dΦ/dt"],
            "respuesta": 1,
            "explicacion": "El hilo recto largo tiene simetría circular.",
            "categoria": "Hilo recto",
            "dificultad": "facil"
        },
        {
            "id": "fis2_mc_02",
            "pregunta": "Para una carga negativa en un campo B, la dirección de F respecto a v×B es:",
            "opciones": ["La misma", "La opuesta", "Siempre cero", "Siempre vertical"],
            "respuesta": 2,
            "explicacion": "F=q(v×B), si q<0 se invierte la dirección.",
            "categoria": "Fuerza magnética",
            "dificultad": "facil"
        },
        {
            "id": "fis2_mc_03",
            "pregunta": "¿Qué ley usa una integral cerrada ∮B·dl?",
            "opciones": ["Gauss eléctrica", "Ampère", "Coulomb", "Ohm"],
            "respuesta": 2,
            "explicacion": "La ley de Ampère usa ∮B·dl=mu0 I_enc.",
            "categoria": "Ampère",
            "dificultad": "facil"
        }
    ]
}
