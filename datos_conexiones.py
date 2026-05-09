# -*- coding: utf-8 -*-

CONEXIONES = [
    {
        "titulo": "Coulomb → Campo eléctrico",
        "temas": ["Tema 1"],
        "idea": "El campo eléctrico de una carga puntual sale directamente de la fuerza de Coulomb.",
        "cadena": [
            "F = k|q q0|/r²",
            "E = F/q0",
            "E = k|q|/r²"
        ],
        "para_que_sirve": [
            "Para no memorizar E como una fórmula aislada.",
            "Para entender que E describe la fuerza por unidad de carga de prueba.",
            "Para pasar de fuerza entre cargas a campo creado por una carga."
        ]
    },
    {
        "titulo": "Campo eléctrico → Fuerza eléctrica",
        "temas": ["Tema 1"],
        "idea": "Cuando ya tienes el campo eléctrico, la fuerza sobre cualquier carga se obtiene con F=qE.",
        "cadena": [
            "E = F/q",
            "F = qE"
        ],
        "para_que_sirve": [
            "Para resolver fuerza sobre una carga sin recalcular Coulomb desde cero.",
            "Para recordar que si q es negativa, la fuerza va en sentido contrario a E."
        ]
    },
    {
        "titulo": "Potencial → Energía → Trabajo",
        "temas": ["Tema 1"],
        "idea": "El potencial conecta electrostática con energía y trabajo.",
        "cadena": [
            "V = U/q",
            "U = qV",
            "Delta U = q Delta V",
            "W_campo = -Delta U"
        ],
        "para_que_sirve": [
            "Para ejercicios de trabajo para mover cargas.",
            "Para conectar potencial con conservación de energía.",
            "Para no confundir campo vectorial con potencial escalar."
        ]
    },
    {
        "titulo": "Gauss → Campos con simetría",
        "temas": ["Tema 1"],
        "idea": "Gauss permite obtener campos sin integrar Coulomb si hay simetría.",
        "cadena": [
            "Phi_E = ∮E·dA",
            "Phi_E = Q_enc/epsilon_0",
            "Si E es constante: E A = Q_enc/epsilon_0"
        ],
        "para_que_sirve": [
            "Esfera: usa superficie esférica.",
            "Línea infinita: usa cilindro.",
            "Plano infinito: usa caja gaussiana."
        ]
    },
    {
        "titulo": "Fuerza magnética → Movimiento circular",
        "temas": ["Tema 2"],
        "idea": "Si una carga entra perpendicularmente a B, la fuerza magnética hace de centrípeta.",
        "cadena": [
            "F = |q|vB",
            "F_c = mv²/r",
            "|q|vB = mv²/r",
            "r = mv/(|q|B)"
        ],
        "para_que_sirve": [
            "Para problemas de radio de trayectoria.",
            "Para entender que B cambia dirección de v, no su módulo.",
            "Para ejercicios de espectrómetros de masas o partículas cargadas."
        ]
    },
    {
        "titulo": "Biot-Savart → Hilo, espira y arco",
        "temas": ["Tema 2"],
        "idea": "Biot-Savart es la fórmula general; las fórmulas de hilo/espira son casos derivados.",
        "cadena": [
            "dB = (mu0/4pi) I dl×r_hat/r²",
            "Hilo largo: B=mu0I/(2pi r)",
            "Espira centro: B=mu0I/(2R)",
            "Arco centro: B=mu0I phi/(4pi R)"
        ],
        "para_que_sirve": [
            "Para no memorizar resultados sin saber de dónde vienen.",
            "Para reconocer cuándo usar fórmulas estándar y cuándo integrar."
        ]
    },
    {
        "titulo": "Ampère ↔ Gauss",
        "temas": ["Tema 1", "Tema 2"],
        "idea": "Ampère en magnetismo se usa de forma parecida a Gauss en electrostática: ambas simplifican con simetría.",
        "cadena": [
            "Gauss: ∮E·dA = Q_enc/epsilon0",
            "Ampère: ∮B·dl = mu0 I_enc",
            "Ambas requieren elegir una superficie/curva adecuada"
        ],
        "para_que_sirve": [
            "Gauss: carga encerrada y flujo eléctrico.",
            "Ampère: corriente encerrada y circulación magnética.",
            "No basta con que la ley sea cierta: necesitas simetría para despejar fácilmente."
        ]
    },
    {
        "titulo": "Ohm microscópico → Resistencia",
        "temas": ["Tema 3"],
        "idea": "La fórmula R=rho L/A sale de la ley microscópica E=rho J.",
        "cadena": [
            "E = rho J",
            "E = V/L",
            "J = I/A",
            "V/L = rho I/A",
            "V = I(rho L/A)",
            "R = rho L/A"
        ],
        "para_que_sirve": [
            "Para entender por qué un cable largo tiene más resistencia.",
            "Para recordar por qué aumentar el área baja la resistencia."
        ]
    },
    {
        "titulo": "Ohm → Potencia",
        "temas": ["Tema 3"],
        "idea": "Todas las fórmulas de potencia en resistencias salen de P=IV y V=IR.",
        "cadena": [
            "P = IV",
            "V = IR",
            "P = I(IR) = I²R",
            "I = V/R",
            "P = (V/R)V = V²/R"
        ],
        "para_que_sirve": [
            "Para elegir la fórmula según datos disponibles.",
            "Para no memorizar P=I²R y P=V²/R como fórmulas separadas."
        ]
    },
    {
        "titulo": "Serie y paralelo: resistencias vs capacitores",
        "temas": ["Tema 3"],
        "idea": "Las reglas de capacitores son opuestas a las de resistencias.",
        "cadena": [
            "Resistencias serie: misma I → R_eq = ΣR",
            "Resistencias paralelo: mismo V → 1/R_eq = Σ1/R",
            "Capacitores paralelo: mismo V → C_eq = ΣC",
            "Capacitores serie: misma Q → 1/C_eq = Σ1/C"
        ],
        "para_que_sirve": [
            "Para no mezclar reglas.",
            "Para identificar qué magnitud es igual en cada conexión."
        ]
    },
    {
        "titulo": "Kirchhoff → RC",
        "temas": ["Tema 3"],
        "idea": "Las ecuaciones exponenciales del circuito RC salen de aplicar Kirchhoff a la malla.",
        "cadena": [
            "Carga: V - iR - q/C = 0",
            "i = dq/dt",
            "R dq/dt + q/C = V",
            "q(t)=CV(1-e^{-t/RC})"
        ],
        "para_que_sirve": [
            "Para entender de dónde sale la exponencial.",
            "Para recordar que tau=RC."
        ]
    },
    {
        "titulo": "Flujo magnético → Faraday → Lenz",
        "temas": ["Tema 2", "Tema 3"],
        "idea": "La inducción depende del cambio de flujo magnético, no solo de que exista campo magnético.",
        "cadena": [
            "Phi_B = BAcos(theta)",
            "epsilon = -N dPhi_B/dt",
            "El signo negativo es Lenz"
        ],
        "para_que_sirve": [
            "Para ejercicios de bobinas, imanes y espiras.",
            "Para determinar el sentido de la corriente inducida.",
            "Para recordar que si Phi_B no cambia, no hay fem inducida."
        ]
    },
    {
        "titulo": "Capacitor vs inductor",
        "temas": ["Tema 3"],
        "idea": "Capacitores e inductores tienen roles análogos pero opuestos en transitorios.",
        "cadena": [
            "Capacitor: q=CV, se opone a cambios bruscos de V",
            "Inductor: epsilon=-L dI/dt, se opone a cambios bruscos de I",
            "RC: tau=RC",
            "RL: tau=L/R"
        ],
        "para_que_sirve": [
            "Para distinguir circuitos RC y RL.",
            "Para entender por qué ambos tienen exponenciales.",
            "Para recordar qué magnitud no cambia instantáneamente."
        ]
    }
]
