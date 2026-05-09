
TEMA1 = {
    "nombre": "Tema 1 - Campos electricos y electrostatica",

    "resumen": """
La electrostatica estudia las cargas electricas en reposo y los efectos que producen.

En este tema hay varias ideas fundamentales:

1. Carga electrica
La carga electrica puede ser positiva o negativa. Las cargas del mismo signo se repelen,
mientras que las cargas de signo contrario se atraen. La carga se conserva, es decir, no
aparece ni desaparece sin mas: se transfiere de un cuerpo a otro. Tambien esta cuantizada,
lo que significa que aparece en multiplos de la carga elemental.

2. Ley de Coulomb
La Ley de Coulomb calcula la fuerza electrica entre dos cargas puntuales. La fuerza depende
directamente del producto de las cargas e inversamente del cuadrado de la distancia. Por eso,
si la distancia aumenta, la fuerza disminuye mucho; y si la distancia se reduce, la fuerza aumenta.

3. Direccion de la fuerza electrica
No basta con calcular el modulo de la fuerza. Tambien hay que saber si es de atraccion o de
repulsion. Si las cargas tienen el mismo signo, se repelen. Si tienen signos opuestos, se atraen.

4. Campo electrico
El campo electrico indica que fuerza recibiria una carga positiva de prueba colocada en un punto.
Es una magnitud vectorial, por lo que tiene modulo, direccion y sentido. Si hay varias cargas, el campo
total se calcula sumando vectorialmente los campos producidos por cada carga.

5. Superposicion
Cuando hay varias cargas, no se inventa una formula nueva. Se calcula la contribucion de cada carga
por separado y luego se suman las fuerzas o campos. Si estan en linea recta, se suman o restan con signos.
Si estan en dos dimensiones, normalmente se descompone en componentes x e y.

6. Potencial electrico
El potencial electrico es una magnitud escalar. Esto significa que no tiene direccion. Por eso, cuando
hay varias cargas, el potencial total se obtiene sumando directamente los potenciales de cada carga,
teniendo en cuenta el signo de cada carga.

7. Energia potencial electrica
La energia potencial electrica relaciona la carga con el potencial. Si una carga se mueve entre puntos
con distinto potencial, puede haber trabajo electrico o cambio de energia.

8. Flujo electrico y Ley de Gauss
El flujo electrico mide cuanto campo atraviesa una superficie. La Ley de Gauss dice que el flujo total
a traves de una superficie cerrada depende de la carga encerrada. Es especialmente util cuando hay mucha
simetria: esferica, cilindrica o plana.

Idea clave para examenes:
- Si hay dos cargas puntuales y te piden fuerza: Coulomb.
- Si te piden campo por una carga: E = kq/r^2.
- Si hay varias cargas: superposicion vectorial.
- Si te piden potencial: suma escalar de potenciales.
- Si hay superficie cerrada y simetria: Gauss.
""",

    "formulas": [
        {
            "nombre": "Ley de Coulomb",
            "formula": "F = k * |q1*q2| / r^2",
            "uso": "Calcular la fuerza electrica entre dos cargas puntuales.",
            "cuando_usarla": [
                "Cuando hay dos cargas puntuales.",
                "Cuando te dan q1, q2 y la distancia r.",
                "Cuando preguntan fuerza de atraccion o repulsion.",
                "Cuando preguntan como cambia la fuerza si cambia la distancia."
            ],
            "despejes": [
                {
                    "nombre": "Despeje de q1",
                    "formula": "q1 = F*r^2/(k*|q2|)",
                    "explicacion": "Se usa cuando conoces F, r y q2, pero no conoces q1."
                },
                {
                    "nombre": "Despeje de q2",
                    "formula": "q2 = F*r^2/(k*|q1|)",
                    "explicacion": "Se usa cuando conoces F, r y q1, pero no conoces q2."
                },
                {
                    "nombre": "Despeje de r",
                    "formula": "r = sqrt(k*|q1*q2|/F)",
                    "explicacion": "Se usa cuando conoces la fuerza y las dos cargas, pero no la distancia."
                }
            ]
        },
        {
            "nombre": "Campo electrico",
            "formula": "E = F / q",
            "uso": "Relacionar la fuerza electrica con la carga de prueba.",
            "cuando_usarla": [
                "Cuando te dan la fuerza que actua sobre una carga.",
                "Cuando te piden el campo electrico en un punto.",
                "Cuando aparece una carga de prueba q."
            ],
            "despejes": [
                {
                    "nombre": "Despeje de fuerza",
                    "formula": "F = E*q",
                    "explicacion": "Se usa cuando conoces el campo y la carga."
                },
                {
                    "nombre": "Despeje de carga",
                    "formula": "q = F/E",
                    "explicacion": "Se usa cuando conoces la fuerza y el campo."
                }
            ]
        },
        {
            "nombre": "Campo electrico de una carga puntual",
            "formula": "E = k * |q| / r^2",
            "uso": "Calcular el campo creado por una carga puntual a una distancia r.",
            "cuando_usarla": [
                "Cuando hay una carga puntual que crea campo.",
                "Cuando te dan q y r.",
                "Cuando te piden el campo en un punto debido a una carga."
            ],
            "despejes": [
                {
                    "nombre": "Despeje de q",
                    "formula": "q = E*r^2/k",
                    "explicacion": "Se usa cuando conoces E y r, pero no la carga que crea el campo."
                },
                {
                    "nombre": "Despeje de r",
                    "formula": "r = sqrt(k*|q|/E)",
                    "explicacion": "Se usa cuando conoces E y q, pero no la distancia."
                }
            ]
        },
        {
            "nombre": "Principio de superposicion",
            "formula": "E_total = E1 + E2 + E3 + ...",
            "uso": "Calcular el campo total producido por varias cargas.",
            "cuando_usarla": [
                "Cuando hay mas de una carga.",
                "Cuando las fuerzas o campos tienen diferentes direcciones.",
                "Cuando necesitas descomponer en componentes x e y."
            ],
            "despejes": [
                {
                    "nombre": "Componente x total",
                    "formula": "Ex_total = Ex1 + Ex2 + Ex3 + ...",
                    "explicacion": "Se usa cuando los campos no estan todos en la misma direccion."
                },
                {
                    "nombre": "Componente y total",
                    "formula": "Ey_total = Ey1 + Ey2 + Ey3 + ...",
                    "explicacion": "Se usa junto con la componente x para obtener el campo resultante."
                },
                {
                    "nombre": "Modulo del campo resultante",
                    "formula": "E_total = sqrt(Ex_total^2 + Ey_total^2)",
                    "explicacion": "Se usa cuando ya tienes las componentes x e y."
                }
            ]
        },
        {
            "nombre": "Potencial electrico de una carga puntual",
            "formula": "V = k*q/r",
            "uso": "Calcular el potencial electrico creado por una carga puntual.",
            "cuando_usarla": [
                "Cuando te piden potencial electrico.",
                "Cuando te dan una carga q y una distancia r.",
                "Cuando no hace falta direccion porque el potencial es escalar."
            ],
            "despejes": [
                {
                    "nombre": "Despeje de q",
                    "formula": "q = V*r/k",
                    "explicacion": "Se usa cuando conoces el potencial y la distancia."
                },
                {
                    "nombre": "Despeje de r",
                    "formula": "r = k*q/V",
                    "explicacion": "Se usa cuando conoces el potencial y la carga."
                }
            ]
        },
        {
            "nombre": "Energia potencial electrica",
            "formula": "U = q*V",
            "uso": "Relacionar energia potencial electrica con carga y potencial.",
            "cuando_usarla": [
                "Cuando te dan una carga dentro de un potencial.",
                "Cuando te piden energia potencial.",
                "Cuando aparece trabajo electrico o energia."
            ],
            "despejes": [
                {
                    "nombre": "Despeje de q",
                    "formula": "q = U/V",
                    "explicacion": "Se usa cuando conoces energia y potencial."
                },
                {
                    "nombre": "Despeje de V",
                    "formula": "V = U/q",
                    "explicacion": "Se usa cuando conoces energia y carga."
                }
            ]
        },
        {
            "nombre": "Campo uniforme entre placas",
            "formula": "E = ΔV / d",
            "uso": "Calcular el campo entre placas paralelas si el campo es uniforme.",
            "cuando_usarla": [
                "Cuando hay placas paralelas.",
                "Cuando te dan diferencia de potencial y distancia.",
                "Cuando el campo se considera uniforme."
            ],
            "despejes": [
                {
                    "nombre": "Despeje de diferencia de potencial",
                    "formula": "ΔV = E*d",
                    "explicacion": "Se usa cuando conoces el campo y la separacion."
                },
                {
                    "nombre": "Despeje de distancia",
                    "formula": "d = ΔV/E",
                    "explicacion": "Se usa cuando conoces el campo y la diferencia de potencial."
                }
            ]
        },
        {
            "nombre": "Flujo electrico",
            "formula": "Φ = E*A*cos(theta)",
            "uso": "Calcular cuanto campo atraviesa una superficie.",
            "cuando_usarla": [
                "Cuando aparece una superficie con area A.",
                "Cuando preguntan flujo electrico.",
                "Cuando el campo forma un angulo con la normal de la superficie."
            ],
            "despejes": [
                {
                    "nombre": "Despeje de E",
                    "formula": "E = Φ/(A*cos(theta))",
                    "explicacion": "Se usa cuando conoces el flujo, el area y el angulo."
                },
                {
                    "nombre": "Despeje de A",
                    "formula": "A = Φ/(E*cos(theta))",
                    "explicacion": "Se usa cuando conoces el flujo, el campo y el angulo."
                }
            ]
        },
        {
            "nombre": "Ley de Gauss",
            "formula": "Φ = Q_encerrada / epsilon_0",
            "uso": "Relacionar el flujo total a traves de una superficie cerrada con la carga encerrada.",
            "cuando_usarla": [
                "Cuando hay una superficie cerrada.",
                "Cuando te dan o piden carga encerrada.",
                "Cuando hay simetria esferica, cilindrica o plana.",
                "Cuando quieres evitar integrar directamente con Coulomb."
            ],
            "despejes": [
                {
                    "nombre": "Despeje de carga encerrada",
                    "formula": "Q_encerrada = Φ*epsilon_0",
                    "explicacion": "Se usa cuando conoces el flujo total y quieres la carga encerrada."
                }
            ]
        }
    ],

    "flashcards": [
        {
            "id": "fc_carga_01",
            "frente": "¿Que ocurre entre dos cargas del mismo signo?",
            "reverso": "Se repelen.",
            "categoria": "Carga electrica"
        },
        {
            "id": "fc_carga_02",
            "frente": "¿Que ocurre entre dos cargas de signo contrario?",
            "reverso": "Se atraen.",
            "categoria": "Carga electrica"
        },
        {
            "id": "fc_carga_03",
            "frente": "¿Que significa que la carga esta cuantizada?",
            "reverso": "Que aparece en multiplos de una carga elemental.",
            "categoria": "Carga electrica"
        },
        {
            "id": "fc_coulomb_01",
            "frente": "¿Para que sirve la Ley de Coulomb?",
            "reverso": "Para calcular la fuerza electrica entre dos cargas puntuales.",
            "categoria": "Ley de Coulomb"
        },
        {
            "id": "fc_campo_01",
            "frente": "¿El campo electrico es escalar o vectorial?",
            "reverso": "Es vectorial: tiene modulo, direccion y sentido.",
            "categoria": "Campo electrico"
        },
        {
            "id": "fc_potencial_01",
            "frente": "¿El potencial electrico es escalar o vectorial?",
            "reverso": "Es escalar.",
            "categoria": "Potencial electrico"
        },
        {
            "id": "fc_gauss_01",
            "frente": "¿Cuando conviene usar la Ley de Gauss?",
            "reverso": "Cuando hay mucha simetria: esferica, cilindrica o plana.",
            "categoria": "Ley de Gauss"
        }
    ],

    "preguntas_vf": [
        {
            "id": "vf_carga_01",
            "pregunta": "Las cargas del mismo signo se atraen.",
            "respuesta": False,
            "explicacion": "Las cargas del mismo signo se repelen.",
            "categoria": "Carga electrica",
            "dificultad": "facil"
        },
        {
            "id": "vf_carga_02",
            "pregunta": "Las cargas de signo contrario se atraen.",
            "respuesta": True,
            "explicacion": "Una carga positiva y una negativa se atraen.",
            "categoria": "Carga electrica",
            "dificultad": "facil"
        },
        {
            "id": "vf_carga_03",
            "pregunta": "La carga electrica se conserva.",
            "respuesta": True,
            "explicacion": "La carga neta de un sistema cerrado permanece constante.",
            "categoria": "Carga electrica",
            "dificultad": "facil"
        },
        {
            "id": "vf_coulomb_01",
            "pregunta": "La fuerza de Coulomb aumenta si aumenta la distancia.",
            "respuesta": False,
            "explicacion": "Disminuye, porque la distancia aparece como r^2 en el denominador.",
            "categoria": "Ley de Coulomb",
            "dificultad": "facil"
        },
        {
            "id": "vf_coulomb_02",
            "pregunta": "Si la distancia entre dos cargas se reduce a la mitad, la fuerza se multiplica por 4.",
            "respuesta": True,
            "explicacion": "F es inversamente proporcional a r^2.",
            "categoria": "Ley de Coulomb",
            "dificultad": "media"
        },
        {
            "id": "vf_coulomb_03",
            "pregunta": "Si la distancia entre dos cargas se reduce a un tercio, la fuerza se multiplica por 9.",
            "respuesta": True,
            "explicacion": "Como F depende de 1/r^2, al hacer r/3 la fuerza se multiplica por 9.",
            "categoria": "Ley de Coulomb",
            "dificultad": "media"
        },
        {
            "id": "vf_campo_01",
            "pregunta": "El campo electrico es una magnitud vectorial.",
            "respuesta": True,
            "explicacion": "El campo electrico tiene modulo, direccion y sentido.",
            "categoria": "Campo electrico",
            "dificultad": "facil"
        },
        {
            "id": "vf_potencial_01",
            "pregunta": "El potencial electrico es una magnitud vectorial.",
            "respuesta": False,
            "explicacion": "El potencial electrico es escalar.",
            "categoria": "Potencial electrico",
            "dificultad": "facil"
        },
        {
            "id": "vf_superposicion_01",
            "pregunta": "El principio de superposicion permite sumar campos electricos producidos por varias cargas.",
            "respuesta": True,
            "explicacion": "El campo total es la suma vectorial de los campos individuales.",
            "categoria": "Campo electrico",
            "dificultad": "media"
        },
        {
            "id": "vf_gauss_01",
            "pregunta": "La Ley de Gauss solo se puede usar si hay exactamente dos cargas.",
            "respuesta": False,
            "explicacion": "Gauss se usa con superficies cerradas y es especialmente util con simetria.",
            "categoria": "Ley de Gauss",
            "dificultad": "media"
        },
        {
            "id": "vf_potencial_02",
            "pregunta": "En una superficie equipotencial, el potencial es constante.",
            "respuesta": True,
            "explicacion": "Todos los puntos de una superficie equipotencial tienen el mismo potencial.",
            "categoria": "Potencial electrico",
            "dificultad": "media"
        },
        {
            "id": "vf_gauss_02",
            "pregunta": "El flujo neto a traves de una superficie cerrada depende solo de la carga encerrada.",
            "respuesta": True,
            "explicacion": "Esto es justamente la idea central de la Ley de Gauss.",
            "categoria": "Ley de Gauss",
            "dificultad": "dificil"
        }
    ],

    "preguntas_mc": [
        {
            "id": "mc_coulomb_01",
            "pregunta": "Te dan q1, q2 y r. Te piden la fuerza electrica. ¿Que formula usas?",
            "opciones": [
                "E = F/q",
                "F = k*|q1*q2|/r^2",
                "V = k*q/r",
                "Φ = E*A*cos(theta)"
            ],
            "respuesta": 2,
            "explicacion": "Se usa la Ley de Coulomb porque hay dos cargas puntuales.",
            "categoria": "Ley de Coulomb",
            "dificultad": "facil"
        },
        {
            "id": "mc_campo_01",
            "pregunta": "Te dan F y q. Te piden el campo electrico E. ¿Que formula usas?",
            "opciones": [
                "E = F/q",
                "F = k*|q1*q2|/r^2",
                "V = k*q/r",
                "U = q*V"
            ],
            "respuesta": 1,
            "explicacion": "El campo electrico se define como fuerza por unidad de carga.",
            "categoria": "Campo electrico",
            "dificultad": "facil"
        },
        {
            "id": "mc_potencial_01",
            "pregunta": "Te dan una carga q y una distancia r. Te piden el potencial electrico. ¿Que formula usas?",
            "opciones": [
                "V = k*q/r",
                "E = k*q/r^2",
                "F = m*a",
                "Φ = Q/epsilon_0"
            ],
            "respuesta": 1,
            "explicacion": "El potencial de una carga puntual es V = k*q/r.",
            "categoria": "Potencial electrico",
            "dificultad": "facil"
        },
        {
            "id": "mc_gauss_01",
            "pregunta": "¿Cuando conviene usar la Ley de Gauss?",
            "opciones": [
                "Cuando hay cualquier distribucion sin simetria.",
                "Cuando hay simetria esferica, cilindrica o plana.",
                "Solo cuando hay una carga negativa.",
                "Solo para calcular energia cinetica."
            ],
            "respuesta": 2,
            "explicacion": "Gauss es especialmente util cuando la simetria permite simplificar el flujo.",
            "categoria": "Ley de Gauss",
            "dificultad": "media"
        },
        {
            "id": "mc_superposicion_01",
            "pregunta": "Si hay varias cargas y te piden el campo total en un punto, ¿que haces?",
            "opciones": [
                "Multiplicar todos los campos.",
                "Sumar vectorialmente los campos individuales.",
                "Restar siempre los modulos.",
                "Usar solo la carga mas grande."
            ],
            "respuesta": 2,
            "explicacion": "Se aplica el principio de superposicion.",
            "categoria": "Campo electrico",
            "dificultad": "media"
        },
        {
            "id": "mc_flujo_01",
            "pregunta": "¿Cual de estas formulas representa flujo electrico con campo uniforme?",
            "opciones": [
                "Φ = E*A*cos(theta)",
                "F = k*q1*q2/r^2",
                "V = k*q/r",
                "E = F/q"
            ],
            "respuesta": 1,
            "explicacion": "El flujo depende del campo, el area y el angulo con la normal.",
            "categoria": "Flujo electrico",
            "dificultad": "media"
        },
        {
            "id": "mc_placas_01",
            "pregunta": "Entre placas paralelas con campo uniforme, si te dan ΔV y d, ¿que formula usas?",
            "opciones": [
                "E = ΔV/d",
                "F = k*q1*q2/r^2",
                "q = Ne",
                "U = mgh"
            ],
            "respuesta": 1,
            "explicacion": "Para un campo uniforme entre placas se usa E = ΔV/d.",
            "categoria": "Potencial electrico",
            "dificultad": "media"
        },
        {
            "id": "mc_potencial_02",
            "pregunta": "¿Que magnitud es escalar?",
            "opciones": [
                "Campo electrico",
                "Fuerza electrica",
                "Potencial electrico",
                "Aceleracion"
            ],
            "respuesta": 3,
            "explicacion": "El potencial electrico no tiene direccion, solo valor.",
            "categoria": "Potencial electrico",
            "dificultad": "facil"
        }
    ],

    "ejercicios_numericos": [
        {
            "id": "num_coulomb_01",
            "enunciado": "Dos cargas q1 = 1.0e-6 C y q2 = 2.5e-6 C estan separadas 5 cm en el vacio. Calcula el modulo de la fuerza electrica en N.",
            "respuesta": 9.0,
            "unidad": "N",
            "tolerancia_relativa": 0.03,
            "explicacion": "Usa F = k*|q1*q2|/r^2, con r = 0.05 m. Resultado: F = 9 N.",
            "categoria": "Ley de Coulomb",
            "dificultad": "facil"
        },
        {
            "id": "num_coulomb_02",
            "enunciado": "Dos cargas q1 = -1.25e-9 C y q2 = 2.0e-5 C estan separadas 10 cm en el vacio. Calcula el modulo de la fuerza en N.",
            "respuesta": 0.0225,
            "unidad": "N",
            "tolerancia_relativa": 0.05,
            "explicacion": "Usa Coulomb con r = 0.1 m. Como tienen signos opuestos, se atraen. Modulo: 0.0225 N.",
            "categoria": "Ley de Coulomb",
            "dificultad": "media"
        },
        {
            "id": "num_coulomb_03",
            "enunciado": "Dos cargas se atraen con una fuerza inicial de 600 N. Si la distancia se reduce a un tercio, ¿cual es la nueva fuerza en N?",
            "respuesta": 5400.0,
            "unidad": "N",
            "tolerancia_relativa": 0.03,
            "explicacion": "Al reducir r a r/3, la fuerza se multiplica por 9. Entonces F = 600*9 = 5400 N.",
            "categoria": "Ley de Coulomb",
            "dificultad": "media"
        },
        {
            "id": "num_potencial_01",
            "enunciado": "Una carga de 4 nC es transportada con un trabajo de 7e-5 J. Calcula el potencial electrico en V.",
            "respuesta": 17500.0,
            "unidad": "V",
            "tolerancia_relativa": 0.03,
            "explicacion": "Usa W = q*V, por tanto V = W/q = 7e-5 / 4e-9 = 1.75e4 V.",
            "categoria": "Potencial electrico",
            "dificultad": "media"
        },
        {
            "id": "num_potencial_02",
            "enunciado": "Un conductor esferico tiene carga Q = 5 nC y radio R = 0.15 m. Calcula el potencial en su superficie en V.",
            "respuesta": 300.0,
            "unidad": "V",
            "tolerancia_relativa": 0.03,
            "explicacion": "Usa V = kQ/R = 9e9*5e-9/0.15 = 300 V.",
            "categoria": "Potencial electrico",
            "dificultad": "media"
        },
        {
            "id": "num_gauss_01",
            "enunciado": "Una superficie gaussiana encierra una carga q = 1.0e-6 C. Calcula el flujo electrico total aproximado en N*m^2/C. Usa epsilon0 = 8.85e-12.",
            "respuesta": 1.13e5,
            "unidad": "N*m^2/C",
            "tolerancia_relativa": 0.05,
            "explicacion": "Usa Φ = q/epsilon0 = 1e-6 / 8.85e-12 ≈ 1.13e5 N*m^2/C.",
            "categoria": "Ley de Gauss",
            "dificultad": "dificil"
        }
    ]
}# -*- coding: utf-8 -*-

TEMA1 = {
    "nombre": "Tema 1 - Campos electricos y electrostatica",

    "resumen": """
La electrostatica estudia las cargas electricas en reposo y los efectos que producen.

En este tema hay varias ideas fundamentales:

1. Carga electrica
La carga electrica puede ser positiva o negativa. Las cargas del mismo signo se repelen,
mientras que las cargas de signo contrario se atraen. La carga se conserva, es decir, no
aparece ni desaparece sin mas: se transfiere de un cuerpo a otro. Tambien esta cuantizada,
lo que significa que aparece en multiplos de la carga elemental.

2. Ley de Coulomb
La Ley de Coulomb calcula la fuerza electrica entre dos cargas puntuales. La fuerza depende
directamente del producto de las cargas e inversamente del cuadrado de la distancia. Por eso,
si la distancia aumenta, la fuerza disminuye mucho; y si la distancia se reduce, la fuerza aumenta.

3. Direccion de la fuerza electrica
No basta con calcular el modulo de la fuerza. Tambien hay que saber si es de atraccion o de
repulsion. Si las cargas tienen el mismo signo, se repelen. Si tienen signos opuestos, se atraen.

4. Campo electrico
El campo electrico indica que fuerza recibiria una carga positiva de prueba colocada en un punto.
Es una magnitud vectorial, por lo que tiene modulo, direccion y sentido. Si hay varias cargas, el campo
total se calcula sumando vectorialmente los campos producidos por cada carga.

5. Superposicion
Cuando hay varias cargas, no se inventa una formula nueva. Se calcula la contribucion de cada carga
por separado y luego se suman las fuerzas o campos. Si estan en linea recta, se suman o restan con signos.
Si estan en dos dimensiones, normalmente se descompone en componentes x e y.

6. Potencial electrico
El potencial electrico es una magnitud escalar. Esto significa que no tiene direccion. Por eso, cuando
hay varias cargas, el potencial total se obtiene sumando directamente los potenciales de cada carga,
teniendo en cuenta el signo de cada carga.

7. Energia potencial electrica
La energia potencial electrica relaciona la carga con el potencial. Si una carga se mueve entre puntos
con distinto potencial, puede haber trabajo electrico o cambio de energia.

8. Flujo electrico y Ley de Gauss
El flujo electrico mide cuanto campo atraviesa una superficie. La Ley de Gauss dice que el flujo total
a traves de una superficie cerrada depende de la carga encerrada. Es especialmente util cuando hay mucha
simetria: esferica, cilindrica o plana.

Idea clave para examenes:
- Si hay dos cargas puntuales y te piden fuerza: Coulomb.
- Si te piden campo por una carga: E = kq/r^2.
- Si hay varias cargas: superposicion vectorial.
- Si te piden potencial: suma escalar de potenciales.
- Si hay superficie cerrada y simetria: Gauss.
""",

    "formulas": [
        {
            "nombre": "Ley de Coulomb",
            "formula": "F = k * |q1*q2| / r^2",
            "uso": "Calcular la fuerza electrica entre dos cargas puntuales.",
            "cuando_usarla": [
                "Cuando hay dos cargas puntuales.",
                "Cuando te dan q1, q2 y la distancia r.",
                "Cuando preguntan fuerza de atraccion o repulsion.",
                "Cuando preguntan como cambia la fuerza si cambia la distancia."
            ],
            "despejes": [
                {
                    "nombre": "Despeje de q1",
                    "formula": "q1 = F*r^2/(k*|q2|)",
                    "explicacion": "Se usa cuando conoces F, r y q2, pero no conoces q1."
                },
                {
                    "nombre": "Despeje de q2",
                    "formula": "q2 = F*r^2/(k*|q1|)",
                    "explicacion": "Se usa cuando conoces F, r y q1, pero no conoces q2."
                },
                {
                    "nombre": "Despeje de r",
                    "formula": "r = sqrt(k*|q1*q2|/F)",
                    "explicacion": "Se usa cuando conoces la fuerza y las dos cargas, pero no la distancia."
                }
            ]
        },
        {
            "nombre": "Campo electrico",
            "formula": "E = F / q",
            "uso": "Relacionar la fuerza electrica con la carga de prueba.",
            "cuando_usarla": [
                "Cuando te dan la fuerza que actua sobre una carga.",
                "Cuando te piden el campo electrico en un punto.",
                "Cuando aparece una carga de prueba q."
            ],
            "despejes": [
                {
                    "nombre": "Despeje de fuerza",
                    "formula": "F = E*q",
                    "explicacion": "Se usa cuando conoces el campo y la carga."
                },
                {
                    "nombre": "Despeje de carga",
                    "formula": "q = F/E",
                    "explicacion": "Se usa cuando conoces la fuerza y el campo."
                }
            ]
        },
        {
            "nombre": "Campo electrico de una carga puntual",
            "formula": "E = k * |q| / r^2",
            "uso": "Calcular el campo creado por una carga puntual a una distancia r.",
            "cuando_usarla": [
                "Cuando hay una carga puntual que crea campo.",
                "Cuando te dan q y r.",
                "Cuando te piden el campo en un punto debido a una carga."
            ],
            "despejes": [
                {
                    "nombre": "Despeje de q",
                    "formula": "q = E*r^2/k",
                    "explicacion": "Se usa cuando conoces E y r, pero no la carga que crea el campo."
                },
                {
                    "nombre": "Despeje de r",
                    "formula": "r = sqrt(k*|q|/E)",
                    "explicacion": "Se usa cuando conoces E y q, pero no la distancia."
                }
            ]
        },
        {
            "nombre": "Principio de superposicion",
            "formula": "E_total = E1 + E2 + E3 + ...",
            "uso": "Calcular el campo total producido por varias cargas.",
            "cuando_usarla": [
                "Cuando hay mas de una carga.",
                "Cuando las fuerzas o campos tienen diferentes direcciones.",
                "Cuando necesitas descomponer en componentes x e y."
            ],
            "despejes": [
                {
                    "nombre": "Componente x total",
                    "formula": "Ex_total = Ex1 + Ex2 + Ex3 + ...",
                    "explicacion": "Se usa cuando los campos no estan todos en la misma direccion."
                },
                {
                    "nombre": "Componente y total",
                    "formula": "Ey_total = Ey1 + Ey2 + Ey3 + ...",
                    "explicacion": "Se usa junto con la componente x para obtener el campo resultante."
                },
                {
                    "nombre": "Modulo del campo resultante",
                    "formula": "E_total = sqrt(Ex_total^2 + Ey_total^2)",
                    "explicacion": "Se usa cuando ya tienes las componentes x e y."
                }
            ]
        },
        {
            "nombre": "Potencial electrico de una carga puntual",
            "formula": "V = k*q/r",
            "uso": "Calcular el potencial electrico creado por una carga puntual.",
            "cuando_usarla": [
                "Cuando te piden potencial electrico.",
                "Cuando te dan una carga q y una distancia r.",
                "Cuando no hace falta direccion porque el potencial es escalar."
            ],
            "despejes": [
                {
                    "nombre": "Despeje de q",
                    "formula": "q = V*r/k",
                    "explicacion": "Se usa cuando conoces el potencial y la distancia."
                },
                {
                    "nombre": "Despeje de r",
                    "formula": "r = k*q/V",
                    "explicacion": "Se usa cuando conoces el potencial y la carga."
                }
            ]
        },
        {
            "nombre": "Energia potencial electrica",
            "formula": "U = q*V",
            "uso": "Relacionar energia potencial electrica con carga y potencial.",
            "cuando_usarla": [
                "Cuando te dan una carga dentro de un potencial.",
                "Cuando te piden energia potencial.",
                "Cuando aparece trabajo electrico o energia."
            ],
            "despejes": [
                {
                    "nombre": "Despeje de q",
                    "formula": "q = U/V",
                    "explicacion": "Se usa cuando conoces energia y potencial."
                },
                {
                    "nombre": "Despeje de V",
                    "formula": "V = U/q",
                    "explicacion": "Se usa cuando conoces energia y carga."
                }
            ]
        },
        {
            "nombre": "Campo uniforme entre placas",
            "formula": "E = ΔV / d",
            "uso": "Calcular el campo entre placas paralelas si el campo es uniforme.",
            "cuando_usarla": [
                "Cuando hay placas paralelas.",
                "Cuando te dan diferencia de potencial y distancia.",
                "Cuando el campo se considera uniforme."
            ],
            "despejes": [
                {
                    "nombre": "Despeje de diferencia de potencial",
                    "formula": "ΔV = E*d",
                    "explicacion": "Se usa cuando conoces el campo y la separacion."
                },
                {
                    "nombre": "Despeje de distancia",
                    "formula": "d = ΔV/E",
                    "explicacion": "Se usa cuando conoces el campo y la diferencia de potencial."
                }
            ]
        },
        {
            "nombre": "Flujo electrico",
            "formula": "Φ = E*A*cos(theta)",
            "uso": "Calcular cuanto campo atraviesa una superficie.",
            "cuando_usarla": [
                "Cuando aparece una superficie con area A.",
                "Cuando preguntan flujo electrico.",
                "Cuando el campo forma un angulo con la normal de la superficie."
            ],
            "despejes": [
                {
                    "nombre": "Despeje de E",
                    "formula": "E = Φ/(A*cos(theta))",
                    "explicacion": "Se usa cuando conoces el flujo, el area y el angulo."
                },
                {
                    "nombre": "Despeje de A",
                    "formula": "A = Φ/(E*cos(theta))",
                    "explicacion": "Se usa cuando conoces el flujo, el campo y el angulo."
                }
            ]
        },
        {
            "nombre": "Ley de Gauss",
            "formula": "Φ = Q_encerrada / epsilon_0",
            "uso": "Relacionar el flujo total a traves de una superficie cerrada con la carga encerrada.",
            "cuando_usarla": [
                "Cuando hay una superficie cerrada.",
                "Cuando te dan o piden carga encerrada.",
                "Cuando hay simetria esferica, cilindrica o plana.",
                "Cuando quieres evitar integrar directamente con Coulomb."
            ],
            "despejes": [
                {
                    "nombre": "Despeje de carga encerrada",
                    "formula": "Q_encerrada = Φ*epsilon_0",
                    "explicacion": "Se usa cuando conoces el flujo total y quieres la carga encerrada."
                }
            ]
        }
    ],

    "flashcards": [
        {
            "id": "fc_carga_01",
            "frente": "¿Que ocurre entre dos cargas del mismo signo?",
            "reverso": "Se repelen.",
            "categoria": "Carga electrica"
        },
        {
            "id": "fc_carga_02",
            "frente": "¿Que ocurre entre dos cargas de signo contrario?",
            "reverso": "Se atraen.",
            "categoria": "Carga electrica"
        },
        {
            "id": "fc_carga_03",
            "frente": "¿Que significa que la carga esta cuantizada?",
            "reverso": "Que aparece en multiplos de una carga elemental.",
            "categoria": "Carga electrica"
        },
        {
            "id": "fc_coulomb_01",
            "frente": "¿Para que sirve la Ley de Coulomb?",
            "reverso": "Para calcular la fuerza electrica entre dos cargas puntuales.",
            "categoria": "Ley de Coulomb"
        },
        {
            "id": "fc_campo_01",
            "frente": "¿El campo electrico es escalar o vectorial?",
            "reverso": "Es vectorial: tiene modulo, direccion y sentido.",
            "categoria": "Campo electrico"
        },
        {
            "id": "fc_potencial_01",
            "frente": "¿El potencial electrico es escalar o vectorial?",
            "reverso": "Es escalar.",
            "categoria": "Potencial electrico"
        },
        {
            "id": "fc_gauss_01",
            "frente": "¿Cuando conviene usar la Ley de Gauss?",
            "reverso": "Cuando hay mucha simetria: esferica, cilindrica o plana.",
            "categoria": "Ley de Gauss"
        }
    ],

    "preguntas_vf": [
        {
            "id": "vf_carga_01",
            "pregunta": "Las cargas del mismo signo se atraen.",
            "respuesta": False,
            "explicacion": "Las cargas del mismo signo se repelen.",
            "categoria": "Carga electrica",
            "dificultad": "facil"
        },
        {
            "id": "vf_carga_02",
            "pregunta": "Las cargas de signo contrario se atraen.",
            "respuesta": True,
            "explicacion": "Una carga positiva y una negativa se atraen.",
            "categoria": "Carga electrica",
            "dificultad": "facil"
        },
        {
            "id": "vf_carga_03",
            "pregunta": "La carga electrica se conserva.",
            "respuesta": True,
            "explicacion": "La carga neta de un sistema cerrado permanece constante.",
            "categoria": "Carga electrica",
            "dificultad": "facil"
        },
        {
            "id": "vf_coulomb_01",
            "pregunta": "La fuerza de Coulomb aumenta si aumenta la distancia.",
            "respuesta": False,
            "explicacion": "Disminuye, porque la distancia aparece como r^2 en el denominador.",
            "categoria": "Ley de Coulomb",
            "dificultad": "facil"
        },
        {
            "id": "vf_coulomb_02",
            "pregunta": "Si la distancia entre dos cargas se reduce a la mitad, la fuerza se multiplica por 4.",
            "respuesta": True,
            "explicacion": "F es inversamente proporcional a r^2.",
            "categoria": "Ley de Coulomb",
            "dificultad": "media"
        },
        {
            "id": "vf_coulomb_03",
            "pregunta": "Si la distancia entre dos cargas se reduce a un tercio, la fuerza se multiplica por 9.",
            "respuesta": True,
            "explicacion": "Como F depende de 1/r^2, al hacer r/3 la fuerza se multiplica por 9.",
            "categoria": "Ley de Coulomb",
            "dificultad": "media"
        },
        {
            "id": "vf_campo_01",
            "pregunta": "El campo electrico es una magnitud vectorial.",
            "respuesta": True,
            "explicacion": "El campo electrico tiene modulo, direccion y sentido.",
            "categoria": "Campo electrico",
            "dificultad": "facil"
        },
        {
            "id": "vf_potencial_01",
            "pregunta": "El potencial electrico es una magnitud vectorial.",
            "respuesta": False,
            "explicacion": "El potencial electrico es escalar.",
            "categoria": "Potencial electrico",
            "dificultad": "facil"
        },
        {
            "id": "vf_superposicion_01",
            "pregunta": "El principio de superposicion permite sumar campos electricos producidos por varias cargas.",
            "respuesta": True,
            "explicacion": "El campo total es la suma vectorial de los campos individuales.",
            "categoria": "Campo electrico",
            "dificultad": "media"
        },
        {
            "id": "vf_gauss_01",
            "pregunta": "La Ley de Gauss solo se puede usar si hay exactamente dos cargas.",
            "respuesta": False,
            "explicacion": "Gauss se usa con superficies cerradas y es especialmente util con simetria.",
            "categoria": "Ley de Gauss",
            "dificultad": "media"
        },
        {
            "id": "vf_potencial_02",
            "pregunta": "En una superficie equipotencial, el potencial es constante.",
            "respuesta": True,
            "explicacion": "Todos los puntos de una superficie equipotencial tienen el mismo potencial.",
            "categoria": "Potencial electrico",
            "dificultad": "media"
        },
        {
            "id": "vf_gauss_02",
            "pregunta": "El flujo neto a traves de una superficie cerrada depende solo de la carga encerrada.",
            "respuesta": True,
            "explicacion": "Esto es justamente la idea central de la Ley de Gauss.",
            "categoria": "Ley de Gauss",
            "dificultad": "dificil"
        }
    ],

    "preguntas_mc": [
        {
            "id": "mc_coulomb_01",
            "pregunta": "Te dan q1, q2 y r. Te piden la fuerza electrica. ¿Que formula usas?",
            "opciones": [
                "E = F/q",
                "F = k*|q1*q2|/r^2",
                "V = k*q/r",
                "Φ = E*A*cos(theta)"
            ],
            "respuesta": 2,
            "explicacion": "Se usa la Ley de Coulomb porque hay dos cargas puntuales.",
            "categoria": "Ley de Coulomb",
            "dificultad": "facil"
        },
        {
            "id": "mc_campo_01",
            "pregunta": "Te dan F y q. Te piden el campo electrico E. ¿Que formula usas?",
            "opciones": [
                "E = F/q",
                "F = k*|q1*q2|/r^2",
                "V = k*q/r",
                "U = q*V"
            ],
            "respuesta": 1,
            "explicacion": "El campo electrico se define como fuerza por unidad de carga.",
            "categoria": "Campo electrico",
            "dificultad": "facil"
        },
        {
            "id": "mc_potencial_01",
            "pregunta": "Te dan una carga q y una distancia r. Te piden el potencial electrico. ¿Que formula usas?",
            "opciones": [
                "V = k*q/r",
                "E = k*q/r^2",
                "F = m*a",
                "Φ = Q/epsilon_0"
            ],
            "respuesta": 1,
            "explicacion": "El potencial de una carga puntual es V = k*q/r.",
            "categoria": "Potencial electrico",
            "dificultad": "facil"
        },
        {
            "id": "mc_gauss_01",
            "pregunta": "¿Cuando conviene usar la Ley de Gauss?",
            "opciones": [
                "Cuando hay cualquier distribucion sin simetria.",
                "Cuando hay simetria esferica, cilindrica o plana.",
                "Solo cuando hay una carga negativa.",
                "Solo para calcular energia cinetica."
            ],
            "respuesta": 2,
            "explicacion": "Gauss es especialmente util cuando la simetria permite simplificar el flujo.",
            "categoria": "Ley de Gauss",
            "dificultad": "media"
        },
        {
            "id": "mc_superposicion_01",
            "pregunta": "Si hay varias cargas y te piden el campo total en un punto, ¿que haces?",
            "opciones": [
                "Multiplicar todos los campos.",
                "Sumar vectorialmente los campos individuales.",
                "Restar siempre los modulos.",
                "Usar solo la carga mas grande."
            ],
            "respuesta": 2,
            "explicacion": "Se aplica el principio de superposicion.",
            "categoria": "Campo electrico",
            "dificultad": "media"
        },
        {
            "id": "mc_flujo_01",
            "pregunta": "¿Cual de estas formulas representa flujo electrico con campo uniforme?",
            "opciones": [
                "Φ = E*A*cos(theta)",
                "F = k*q1*q2/r^2",
                "V = k*q/r",
                "E = F/q"
            ],
            "respuesta": 1,
            "explicacion": "El flujo depende del campo, el area y el angulo con la normal.",
            "categoria": "Flujo electrico",
            "dificultad": "media"
        },
        {
            "id": "mc_placas_01",
            "pregunta": "Entre placas paralelas con campo uniforme, si te dan ΔV y d, ¿que formula usas?",
            "opciones": [
                "E = ΔV/d",
                "F = k*q1*q2/r^2",
                "q = Ne",
                "U = mgh"
            ],
            "respuesta": 1,
            "explicacion": "Para un campo uniforme entre placas se usa E = ΔV/d.",
            "categoria": "Potencial electrico",
            "dificultad": "media"
        },
        {
            "id": "mc_potencial_02",
            "pregunta": "¿Que magnitud es escalar?",
            "opciones": [
                "Campo electrico",
                "Fuerza electrica",
                "Potencial electrico",
                "Aceleracion"
            ],
            "respuesta": 3,
            "explicacion": "El potencial electrico no tiene direccion, solo valor.",
            "categoria": "Potencial electrico",
            "dificultad": "facil"
        }
    ],

    "ejercicios_numericos": [
        {
            "id": "num_coulomb_01",
            "enunciado": "Dos cargas q1 = 1.0e-6 C y q2 = 2.5e-6 C estan separadas 5 cm en el vacio. Calcula el modulo de la fuerza electrica en N.",
            "respuesta": 9.0,
            "unidad": "N",
            "tolerancia_relativa": 0.03,
            "explicacion": "Usa F = k*|q1*q2|/r^2, con r = 0.05 m. Resultado: F = 9 N.",
            "categoria": "Ley de Coulomb",
            "dificultad": "facil"
        },
        {
            "id": "num_coulomb_02",
            "enunciado": "Dos cargas q1 = -1.25e-9 C y q2 = 2.0e-5 C estan separadas 10 cm en el vacio. Calcula el modulo de la fuerza en N.",
            "respuesta": 0.0225,
            "unidad": "N",
            "tolerancia_relativa": 0.05,
            "explicacion": "Usa Coulomb con r = 0.1 m. Como tienen signos opuestos, se atraen. Modulo: 0.0225 N.",
            "categoria": "Ley de Coulomb",
            "dificultad": "media"
        },
        {
            "id": "num_coulomb_03",
            "enunciado": "Dos cargas se atraen con una fuerza inicial de 600 N. Si la distancia se reduce a un tercio, ¿cual es la nueva fuerza en N?",
            "respuesta": 5400.0,
            "unidad": "N",
            "tolerancia_relativa": 0.03,
            "explicacion": "Al reducir r a r/3, la fuerza se multiplica por 9. Entonces F = 600*9 = 5400 N.",
            "categoria": "Ley de Coulomb",
            "dificultad": "media"
        },
        {
            "id": "num_potencial_01",
            "enunciado": "Una carga de 4 nC es transportada con un trabajo de 7e-5 J. Calcula el potencial electrico en V.",
            "respuesta": 17500.0,
            "unidad": "V",
            "tolerancia_relativa": 0.03,
            "explicacion": "Usa W = q*V, por tanto V = W/q = 7e-5 / 4e-9 = 1.75e4 V.",
            "categoria": "Potencial electrico",
            "dificultad": "media"
        },
        {
            "id": "num_potencial_02",
            "enunciado": "Un conductor esferico tiene carga Q = 5 nC y radio R = 0.15 m. Calcula el potencial en su superficie en V.",
            "respuesta": 300.0,
            "unidad": "V",
            "tolerancia_relativa": 0.03,
            "explicacion": "Usa V = kQ/R = 9e9*5e-9/0.15 = 300 V.",
            "categoria": "Potencial electrico",
            "dificultad": "media"
        },
        {
            "id": "num_gauss_01",
            "enunciado": "Una superficie gaussiana encierra una carga q = 1.0e-6 C. Calcula el flujo electrico total aproximado en N*m^2/C. Usa epsilon0 = 8.85e-12.",
            "respuesta": 1.13e5,
            "unidad": "N*m^2/C",
            "tolerancia_relativa": 0.05,
            "explicacion": "Usa Φ = q/epsilon0 = 1e-6 / 8.85e-12 ≈ 1.13e5 N*m^2/C.",
            "categoria": "Ley de Gauss",
            "dificultad": "dificil"
        }
    ]
}