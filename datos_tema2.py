# -*- coding: utf-8 -*-

TEMA2 = {
    "nombre": "Tema 2 - Campo magnetostatico",

    "resumen": """
El campo magnetostatico estudia los campos magneticos producidos por cargas en movimiento
y corrientes electricas estacionarias.

1. Campo magnetico
El campo magnetico B es una magnitud vectorial. Su unidad en el Sistema Internacional es
el tesla, T. Igual que el campo electrico, tiene modulo, direccion y sentido. Sin embargo,
su origen fisico es diferente: el campo electrico puede ser producido por cargas en reposo,
mientras que el campo magnetico esta asociado a cargas en movimiento o corrientes.

2. Polos magneticos
En electricidad existen cargas positivas y negativas aisladas. En magnetismo, en cambio, no
se observan polos magneticos aislados. Si se parte un iman, no se obtiene un polo norte solo
y un polo sur solo, sino dos imanes mas pequenos, cada uno con su norte y su sur.

3. Fuerza magnetica sobre una carga
Una carga q que se mueve con velocidad v dentro de un campo magnetico B puede experimentar
una fuerza magnetica. Su modulo es:

F = |q|*v*B*sen(theta)

donde theta es el angulo entre la velocidad y el campo magnetico.

Ideas importantes:
- Si la carga esta en reposo, no hay fuerza magnetica.
- Si v es paralela o antiparalela a B, la fuerza es cero.
- Si v es perpendicular a B, la fuerza es maxima.
- La fuerza magnetica siempre es perpendicular a v y a B.
- Para una carga positiva, el sentido se obtiene con la regla de la mano derecha.
- Para una carga negativa, el sentido es el contrario.

4. Fuerza magnetica sobre un conductor
Un conductor con corriente dentro de un campo magnetico tambien puede experimentar una fuerza.
Esto ocurre porque la corriente esta formada por cargas en movimiento. Para un tramo recto
de conductor:

F = I*L*B*sen(theta)

donde I es la corriente, L la longitud del conductor dentro del campo y theta el angulo entre
el conductor/corriente y el campo magnetico.

5. Flujo magnetico
El flujo magnetico mide cuanto campo magnetico atraviesa una superficie:

Phi_B = B*A*cos(theta)

donde theta es el angulo entre B y la normal de la superficie. Si B es paralelo a la normal,
el flujo es maximo. Si B es perpendicular a la normal, el flujo es cero.

6. Ley de Biot-Savart
La Ley de Biot-Savart permite calcular el campo magnetico creado por un elemento pequeno
de corriente. Es parecida al metodo usado en electrostatica con distribuciones de carga:
se toma una contribucion elemental y luego se integra o suma sobre todo el conductor.

Para un elemento de corriente:

dB = (mu0/(4*pi)) * (I*dl*sen(theta)/r^2)

donde:
- I es la corriente.
- dl es el elemento de longitud.
- r es la distancia desde el elemento al punto donde se calcula el campo.
- theta es el angulo entre dl y el vector hacia el punto.

7. Campo de un hilo recto largo
Para un conductor recto muy largo con corriente I, el campo magnetico a una distancia r es:

B = mu0*I/(2*pi*r)

Las lineas de campo son circunferencias alrededor del hilo. El sentido se obtiene con la
regla de la mano derecha: el pulgar apunta en la direccion de la corriente y los dedos indican
el sentido de B.

8. Ley de Ampere
La Ley de Ampere relaciona la circulacion del campo magnetico alrededor de una trayectoria
cerrada con la corriente encerrada por esa trayectoria:

integral(B·dl) = mu0*I_encerrada

Es especialmente util cuando hay simetria, por ejemplo:
- hilo recto largo
- conductor cilindrico largo
- solenoide largo
- toroide

9. Conductor cilindrico largo
Para un conductor cilindrico largo de radio R con corriente uniformemente distribuida:

Dentro del conductor, si r < R:
B = mu0*I*r/(2*pi*R^2)

Fuera del conductor, si r > R:
B = mu0*I/(2*pi*r)

Dentro el campo crece linealmente con r. Fuera se comporta como si toda la corriente estuviera
concentrada en el eje.

10. Solenoide largo
Un solenoide largo produce en su interior un campo magnetico aproximadamente uniforme:

B = mu0*n*I

donde n es el numero de espiras por unidad de longitud. Fuera de un solenoide largo ideal,
el campo es aproximadamente cero.

11. Toroide
Un toroide produce un campo magnetico que queda practicamente confinado dentro del devanado.
Dentro del toroide:

B = mu0*N*I/(2*pi*r)

En el hueco interior y fuera del toroide ideal, el campo es aproximadamente cero.

Idea clave para examenes:
- Si aparece una carga moviendose en un campo B, piensa en F = |q|vBsen(theta).
- Si aparece un conductor con corriente en un campo B, piensa en F = ILBsen(theta).
- Si aparece un elemento de corriente, piensa en Biot-Savart.
- Si aparece un hilo recto largo, puedes usar B = mu0I/(2*pi*r).
- Si hay simetria circular/cilindrica, piensa en Ley de Ampere.
- Si aparece un solenoide largo, usa B = mu0nI.
- Si aparece un toroide, usa B = mu0NI/(2*pi*r).
""",

    "formulas": [
        {
            "nombre": "Fuerza magnetica sobre una carga",
            "formula": "F = |q|*v*B*sen(theta)",
            "uso": "Calcular el modulo de la fuerza magnetica sobre una carga en movimiento.",
            "cuando_usarla": [
                "Cuando una carga q se mueve dentro de un campo magnetico B.",
                "Cuando te dan velocidad v, campo B y angulo theta.",
                "Cuando preguntan si la fuerza es maxima, cero o intermedia.",
                "Cuando aparece una particula cargada en movimiento."
            ],
            "despejes": [
                {
                    "nombre": "Despeje de carga",
                    "formula": "|q| = F/(v*B*sen(theta))",
                    "explicacion": "Se usa cuando conoces F, v, B y theta, pero no la carga."
                },
                {
                    "nombre": "Despeje de velocidad",
                    "formula": "v = F/(|q|*B*sen(theta))",
                    "explicacion": "Se usa cuando conoces F, q, B y theta, pero no v."
                },
                {
                    "nombre": "Despeje de campo magnetico",
                    "formula": "B = F/(|q|*v*sen(theta))",
                    "explicacion": "Se usa cuando conoces F, q, v y theta, pero no B."
                }
            ]
        },
        {
            "nombre": "Fuerza magnetica vectorial sobre una carga",
            "formula": "F = q*(v x B)",
            "uso": "Determinar la direccion y el sentido de la fuerza magnetica.",
            "cuando_usarla": [
                "Cuando te piden direccion o sentido de la fuerza.",
                "Cuando hay que aplicar la regla de la mano derecha.",
                "Cuando debes distinguir entre carga positiva y negativa."
            ],
            "despejes": [
                {
                    "nombre": "Modulo del producto vectorial",
                    "formula": "|v x B| = v*B*sen(theta)",
                    "explicacion": "Permite pasar de la forma vectorial a la formula de modulos."
                },
                {
                    "nombre": "Fuerza para carga positiva",
                    "formula": "F apunta en la direccion de v x B",
                    "explicacion": "Se usa la regla de la mano derecha."
                },
                {
                    "nombre": "Fuerza para carga negativa",
                    "formula": "F apunta en sentido contrario a v x B",
                    "explicacion": "Para cargas negativas se invierte el sentido."
                }
            ]
        },
        {
            "nombre": "Fuerza magnetica sobre un conductor",
            "formula": "F = I*L*B*sen(theta)",
            "uso": "Calcular la fuerza magnetica sobre un conductor recto con corriente dentro de un campo B.",
            "cuando_usarla": [
                "Cuando hay un cable o barra conductora con corriente.",
                "Cuando el conductor esta dentro de un campo magnetico.",
                "Cuando te dan I, L, B y theta."
            ],
            "despejes": [
                {
                    "nombre": "Despeje de corriente",
                    "formula": "I = F/(L*B*sen(theta))",
                    "explicacion": "Se usa cuando conoces F, L, B y theta, pero no I."
                },
                {
                    "nombre": "Despeje de longitud",
                    "formula": "L = F/(I*B*sen(theta))",
                    "explicacion": "Se usa cuando conoces F, I, B y theta, pero no L."
                },
                {
                    "nombre": "Despeje de campo magnetico",
                    "formula": "B = F/(I*L*sen(theta))",
                    "explicacion": "Se usa cuando conoces F, I, L y theta, pero no B."
                }
            ]
        },
        {
            "nombre": "Flujo magnetico",
            "formula": "Phi_B = B*A*cos(theta)",
            "uso": "Calcular el flujo magnetico a traves de una superficie plana.",
            "cuando_usarla": [
                "Cuando aparece un campo magnetico atravesando una superficie.",
                "Cuando te dan B, A y el angulo con la normal.",
                "Cuando preguntan cuanto campo atraviesa una superficie."
            ],
            "despejes": [
                {
                    "nombre": "Despeje de B",
                    "formula": "B = Phi_B/(A*cos(theta))",
                    "explicacion": "Se usa cuando conoces el flujo, el area y el angulo."
                },
                {
                    "nombre": "Despeje de area",
                    "formula": "A = Phi_B/(B*cos(theta))",
                    "explicacion": "Se usa cuando conoces el flujo, B y theta, pero no A."
                },
                {
                    "nombre": "Flujo maximo",
                    "formula": "Phi_B = B*A",
                    "explicacion": "Ocurre cuando theta = 0 grados, es decir, B es paralelo a la normal."
                },
                {
                    "nombre": "Flujo cero",
                    "formula": "Phi_B = 0",
                    "explicacion": "Ocurre cuando theta = 90 grados."
                }
            ]
        },
        {
            "nombre": "Ley de Biot-Savart para elemento de corriente",
            "formula": "dB = (mu0/(4*pi))*(I*dl*sen(theta)/r^2)",
            "uso": "Calcular la contribucion de campo magnetico de un pequeno elemento de corriente.",
            "cuando_usarla": [
                "Cuando aparece un elemento de corriente dl.",
                "Cuando el conductor no se puede tratar directamente con Ampere.",
                "Cuando hay que integrar contribuciones de corriente."
            ],
            "despejes": [
                {
                    "nombre": "Despeje de corriente",
                    "formula": "I = dB*4*pi*r^2/(mu0*dl*sen(theta))",
                    "explicacion": "Se usa cuando conoces dB, r, dl y theta, pero no I."
                },
                {
                    "nombre": "Despeje de distancia",
                    "formula": "r = sqrt((mu0*I*dl*sen(theta))/(4*pi*dB))",
                    "explicacion": "Se usa cuando conoces dB, I, dl y theta, pero no r."
                },
                {
                    "nombre": "Caso theta = 90 grados",
                    "formula": "dB = (mu0/(4*pi))*(I*dl/r^2)",
                    "explicacion": "Se usa cuando dl es perpendicular al vector hacia el punto."
                }
            ]
        },
        {
            "nombre": "Campo de un hilo recto largo",
            "formula": "B = mu0*I/(2*pi*r)",
            "uso": "Calcular el campo magnetico alrededor de un conductor recto largo.",
            "cuando_usarla": [
                "Cuando hay un hilo recto muy largo.",
                "Cuando te piden B a una distancia r del hilo.",
                "Cuando las lineas de campo son circunferencias alrededor del conductor.",
                "Cuando puedes aplicar Ampere con una circunferencia amperiana."
            ],
            "despejes": [
                {
                    "nombre": "Despeje de corriente",
                    "formula": "I = B*2*pi*r/mu0",
                    "explicacion": "Se usa cuando conoces B y r, pero no I."
                },
                {
                    "nombre": "Despeje de distancia",
                    "formula": "r = mu0*I/(2*pi*B)",
                    "explicacion": "Se usa cuando conoces B e I, pero no r."
                }
            ]
        },
        {
            "nombre": "Ley de Ampere",
            "formula": "integral(B·dl) = mu0*I_encerrada",
            "uso": "Relacionar la circulacion del campo magnetico con la corriente encerrada.",
            "cuando_usarla": [
                "Cuando hay una trayectoria cerrada.",
                "Cuando se puede elegir un bucle amperiano sencillo.",
                "Cuando el campo es paralelo a dl y constante en la trayectoria.",
                "Cuando hay simetria circular, cilindrica o toroidal."
            ],
            "despejes": [
                {
                    "nombre": "Ampere con trayectoria circular",
                    "formula": "B*(2*pi*r) = mu0*I_encerrada",
                    "explicacion": "Se usa cuando el campo es constante sobre una circunferencia."
                },
                {
                    "nombre": "Campo desde Ampere",
                    "formula": "B = mu0*I_encerrada/(2*pi*r)",
                    "explicacion": "Se usa para un hilo largo o simetrias circulares."
                },
                {
                    "nombre": "Corriente encerrada",
                    "formula": "I_encerrada = integral(B·dl)/mu0",
                    "explicacion": "Se usa cuando conoces la circulacion del campo magnetico."
                }
            ]
        },
        {
            "nombre": "Campo dentro de un conductor cilindrico",
            "formula": "B = mu0*I*r/(2*pi*R^2)",
            "uso": "Calcular el campo magnetico dentro de un conductor cilindrico largo con corriente uniforme.",
            "cuando_usarla": [
                "Cuando estas dentro del conductor.",
                "Cuando r < R.",
                "Cuando la corriente esta uniformemente distribuida en la seccion."
            ],
            "despejes": [
                {
                    "nombre": "Campo interior",
                    "formula": "B(r) = mu0*I*r/(2*pi*R^2)",
                    "explicacion": "Dentro del conductor, el campo crece linealmente con r."
                },
                {
                    "nombre": "Corriente encerrada interior",
                    "formula": "I_encerrada = I*r^2/R^2",
                    "explicacion": "Se usa porque el bucle amperiano solo encierra parte de la corriente total."
                }
            ]
        },
        {
            "nombre": "Campo fuera de un conductor cilindrico",
            "formula": "B = mu0*I/(2*pi*r)",
            "uso": "Calcular el campo magnetico fuera de un conductor cilindrico largo.",
            "cuando_usarla": [
                "Cuando estas fuera del conductor.",
                "Cuando r > R.",
                "Cuando toda la corriente queda encerrada por el bucle amperiano."
            ],
            "despejes": [
                {
                    "nombre": "Campo exterior",
                    "formula": "B(r) = mu0*I/(2*pi*r)",
                    "explicacion": "Fuera, el conductor se comporta como si toda la corriente estuviera en el eje."
                }
            ]
        },
        {
            "nombre": "Campo en el centro de una espira circular",
            "formula": "B = mu0*I/(2*a)",
            "uso": "Calcular el campo magnetico en el centro de una espira circular de radio a.",
            "cuando_usarla": [
                "Cuando el punto esta en el centro de la espira.",
                "Cuando te dan el radio a y la corriente I.",
                "Cuando el problema trata de una espira circular."
            ],
            "despejes": [
                {
                    "nombre": "Despeje de corriente",
                    "formula": "I = 2*a*B/mu0",
                    "explicacion": "Se usa cuando conoces B y a, pero no I."
                },
                {
                    "nombre": "Despeje de radio",
                    "formula": "a = mu0*I/(2*B)",
                    "explicacion": "Se usa cuando conoces B e I, pero no a."
                }
            ]
        },
        {
            "nombre": "Campo sobre el eje de una espira circular",
            "formula": "B = mu0*I*a^2/(2*(x^2 + a^2)^(3/2))",
            "uso": "Calcular el campo en un punto sobre el eje de una espira circular.",
            "cuando_usarla": [
                "Cuando el punto no esta en el centro pero esta sobre el eje de la espira.",
                "Cuando te dan el radio a, la corriente I y la distancia axial x.",
                "Cuando las componentes perpendiculares se cancelan por simetria."
            ],
            "despejes": [
                {
                    "nombre": "Caso centro de la espira",
                    "formula": "B(0) = mu0*I/(2*a)",
                    "explicacion": "Sale de poner x = 0."
                },
                {
                    "nombre": "Caso lejano",
                    "formula": "B ≈ mu0*I*a^2/(2*x^3)",
                    "explicacion": "Aproximacion para x mucho mayor que a."
                }
            ]
        },
        {
            "nombre": "Campo en un solenoide largo",
            "formula": "B = mu0*n*I",
            "uso": "Calcular el campo magnetico dentro de un solenoide largo ideal.",
            "cuando_usarla": [
                "Cuando hay un solenoide largo.",
                "Cuando te dan n, el numero de espiras por unidad de longitud.",
                "Cuando el campo es aproximadamente uniforme dentro y cero fuera."
            ],
            "despejes": [
                {
                    "nombre": "Despeje de n",
                    "formula": "n = B/(mu0*I)",
                    "explicacion": "Se usa cuando quieres saber cuantas espiras por metro se necesitan."
                },
                {
                    "nombre": "Despeje de corriente",
                    "formula": "I = B/(mu0*n)",
                    "explicacion": "Se usa cuando conoces B y n, pero no I."
                }
            ]
        },
        {
            "nombre": "Campo en un toroide",
            "formula": "B = mu0*N*I/(2*pi*r)",
            "uso": "Calcular el campo dentro del devanado de un toroide ideal.",
            "cuando_usarla": [
                "Cuando hay un toroide.",
                "Cuando estas dentro del material enrollado.",
                "Cuando la trayectoria amperiana encierra N espiras."
            ],
            "despejes": [
                {
                    "nombre": "Despeje de numero de espiras",
                    "formula": "N = B*2*pi*r/(mu0*I)",
                    "explicacion": "Se usa cuando quieres saber cuantas espiras tiene el toroide."
                },
                {
                    "nombre": "Despeje de corriente",
                    "formula": "I = B*2*pi*r/(mu0*N)",
                    "explicacion": "Se usa cuando conoces B, N y r, pero no I."
                },
                {
                    "nombre": "Campo fuera del toroide ideal",
                    "formula": "B = 0",
                    "explicacion": "Idealmente, el campo magnetico queda confinado dentro del toroide."
                }
            ]
        }
    ],

    "flashcards": [
        {
            "id": "t2_fc_01",
            "frente": "¿El campo magnetico es escalar o vectorial?",
            "reverso": "Es vectorial: tiene modulo, direccion y sentido.",
            "categoria": "Campo magnetico"
        },
        {
            "id": "t2_fc_02",
            "frente": "¿Una carga en reposo dentro de un campo magnetico experimenta fuerza magnetica?",
            "reverso": "No. La fuerza magnetica requiere que la carga se mueva.",
            "categoria": "Fuerza magnetica"
        },
        {
            "id": "t2_fc_03",
            "frente": "¿Cuando es maxima la fuerza magnetica sobre una carga?",
            "reverso": "Cuando la velocidad es perpendicular al campo magnetico.",
            "categoria": "Fuerza magnetica"
        },
        {
            "id": "t2_fc_04",
            "frente": "¿Que pasa si v es paralela a B?",
            "reverso": "La fuerza magnetica es cero porque sen(0) = 0.",
            "categoria": "Fuerza magnetica"
        },
        {
            "id": "t2_fc_05",
            "frente": "¿Que pasa con el sentido de la fuerza si la carga es negativa?",
            "reverso": "El sentido es contrario al que da la regla de la mano derecha para una carga positiva.",
            "categoria": "Fuerza magnetica"
        },
        {
            "id": "t2_fc_06",
            "frente": "¿Que forma tienen las lineas de campo magnetico alrededor de un hilo recto largo?",
            "reverso": "Son circunferencias concentricas alrededor del hilo.",
            "categoria": "Campo de un hilo"
        },
        {
            "id": "t2_fc_07",
            "frente": "¿Cuando conviene usar la Ley de Ampere?",
            "reverso": "Cuando hay simetria y se puede elegir una trayectoria amperiana sencilla.",
            "categoria": "Ley de Ampere"
        },
        {
            "id": "t2_fc_08",
            "frente": "¿Como es el campo dentro de un solenoide largo ideal?",
            "reverso": "Aproximadamente uniforme y paralelo al eje.",
            "categoria": "Solenoide"
        },
        {
            "id": "t2_fc_09",
            "frente": "¿Como es el campo fuera de un solenoide largo ideal?",
            "reverso": "Aproximadamente cero.",
            "categoria": "Solenoide"
        },
        {
            "id": "t2_fc_10",
            "frente": "¿Donde esta confinado el campo magnetico de un toroide ideal?",
            "reverso": "Dentro del devanado del toroide.",
            "categoria": "Toroide"
        }
    ],

    "preguntas_vf": [
        {
            "id": "t2_vf_01",
            "pregunta": "Una carga en reposo puede experimentar fuerza magnetica.",
            "respuesta": False,
            "explicacion": "La fuerza magnetica sobre una carga depende de su velocidad.",
            "categoria": "Fuerza magnetica",
            "dificultad": "facil"
        },
        {
            "id": "t2_vf_02",
            "pregunta": "Si v y B son paralelos, la fuerza magnetica es cero.",
            "respuesta": True,
            "explicacion": "F = |q|vBsen(theta). Si theta = 0 grados, sen(theta)=0.",
            "categoria": "Fuerza magnetica",
            "dificultad": "facil"
        },
        {
            "id": "t2_vf_03",
            "pregunta": "La fuerza magnetica siempre es perpendicular a la velocidad de la carga.",
            "respuesta": True,
            "explicacion": "La fuerza magnetica es perpendicular tanto a v como a B.",
            "categoria": "Fuerza magnetica",
            "dificultad": "facil"
        },
        {
            "id": "t2_vf_04",
            "pregunta": "El campo magnetico es una magnitud escalar.",
            "respuesta": False,
            "explicacion": "El campo magnetico es vectorial.",
            "categoria": "Campo magnetico",
            "dificultad": "facil"
        },
        {
            "id": "t2_vf_05",
            "pregunta": "Al partir un iman, se obtiene un polo norte aislado y un polo sur aislado.",
            "respuesta": False,
            "explicacion": "Cada fragmento sigue teniendo polo norte y polo sur.",
            "categoria": "Magnetismo basico",
            "dificultad": "facil"
        },
        {
            "id": "t2_vf_06",
            "pregunta": "La Ley de Biot-Savart sirve para calcular el campo magnetico creado por corrientes.",
            "respuesta": True,
            "explicacion": "Biot-Savart calcula contribuciones dB de elementos de corriente.",
            "categoria": "Biot-Savart",
            "dificultad": "media"
        },
        {
            "id": "t2_vf_07",
            "pregunta": "La Ley de Ampere utiliza una integral de linea cerrada.",
            "respuesta": True,
            "explicacion": "Ampere relaciona integral(B·dl) con la corriente encerrada.",
            "categoria": "Ley de Ampere",
            "dificultad": "media"
        },
        {
            "id": "t2_vf_08",
            "pregunta": "Si una trayectoria amperiana no encierra corriente neta, necesariamente B es cero en todos los puntos.",
            "respuesta": False,
            "explicacion": "La integral puede ser cero aunque el campo no sea cero en cada punto.",
            "categoria": "Ley de Ampere",
            "dificultad": "dificil"
        },
        {
            "id": "t2_vf_09",
            "pregunta": "Dentro de un conductor cilindrico largo con corriente uniforme, B crece linealmente con r.",
            "respuesta": True,
            "explicacion": "Para r < R, B = mu0*I*r/(2*pi*R^2).",
            "categoria": "Ley de Ampere",
            "dificultad": "dificil"
        },
        {
            "id": "t2_vf_10",
            "pregunta": "Fuera de un conductor cilindrico largo, B disminuye como 1/r.",
            "respuesta": True,
            "explicacion": "Para r > R, B = mu0*I/(2*pi*r).",
            "categoria": "Ley de Ampere",
            "dificultad": "media"
        },
        {
            "id": "t2_vf_11",
            "pregunta": "En un solenoide largo ideal, el campo exterior es aproximadamente cero.",
            "respuesta": True,
            "explicacion": "El modelo ideal de solenoide largo considera B casi nulo fuera.",
            "categoria": "Solenoide",
            "dificultad": "media"
        },
        {
            "id": "t2_vf_12",
            "pregunta": "En un toroide ideal, el campo magnetico es igual en todas partes del espacio.",
            "respuesta": False,
            "explicacion": "El campo queda practicamente confinado dentro del devanado.",
            "categoria": "Toroide",
            "dificultad": "media"
        }
    ],

    "preguntas_mc": [
        {
            "id": "t2_mc_01",
            "pregunta": "Una carga q se mueve con velocidad v perpendicular a un campo B. ¿Que formula da el modulo de la fuerza?",
            "opciones": [
                "F = qE",
                "F = |q|vB",
                "B = mu0I/(2*pi*r)",
                "Phi_B = BAcos(theta)"
            ],
            "respuesta": 2,
            "explicacion": "Si theta = 90 grados, sen(theta)=1 y F = |q|vB.",
            "categoria": "Fuerza magnetica",
            "dificultad": "facil"
        },
        {
            "id": "t2_mc_02",
            "pregunta": "¿Que ocurre si una carga se mueve paralela al campo magnetico?",
            "opciones": [
                "La fuerza es maxima",
                "La fuerza es cero",
                "La fuerza apunta en la direccion de B",
                "La fuerza apunta en la direccion de v"
            ],
            "respuesta": 2,
            "explicacion": "Si v es paralela a B, theta = 0 y sen(theta)=0.",
            "categoria": "Fuerza magnetica",
            "dificultad": "facil"
        },
        {
            "id": "t2_mc_03",
            "pregunta": "¿Que formula usas para el campo magnetico a distancia r de un hilo recto largo?",
            "opciones": [
                "B = mu0*I/(2*pi*r)",
                "F = k*q1*q2/r^2",
                "E = F/q",
                "Phi_E = Q/epsilon0"
            ],
            "respuesta": 1,
            "explicacion": "Es el campo magnetico de un hilo recto largo.",
            "categoria": "Campo de un hilo",
            "dificultad": "facil"
        },
        {
            "id": "t2_mc_04",
            "pregunta": "¿Que ley conviene usar para obtener el campo de un solenoide largo ideal?",
            "opciones": [
                "Ley de Coulomb",
                "Ley de Ampere",
                "Ley de Hooke",
                "Ley de Ohm solamente"
            ],
            "respuesta": 2,
            "explicacion": "Ampere permite obtener B = mu0*n*I para un solenoide largo.",
            "categoria": "Solenoide",
            "dificultad": "media"
        },
        {
            "id": "t2_mc_05",
            "pregunta": "En un toroide ideal, ¿donde es aproximadamente distinto de cero el campo magnetico?",
            "opciones": [
                "Solo en el hueco central",
                "Solo fuera del toroide",
                "Dentro del devanado",
                "En todas partes igual"
            ],
            "respuesta": 3,
            "explicacion": "En el modelo ideal, el campo queda confinado dentro del devanado.",
            "categoria": "Toroide",
            "dificultad": "media"
        },
        {
            "id": "t2_mc_06",
            "pregunta": "¿Que representa I_encerrada en la Ley de Ampere?",
            "opciones": [
                "La corriente total de toda la instalacion",
                "La corriente neta que atraviesa la superficie limitada por la trayectoria",
                "La corriente que circula por el borde de la trayectoria",
                "La corriente inducida por Faraday"
            ],
            "respuesta": 2,
            "explicacion": "I_encerrada es la corriente neta atravesada por la trayectoria amperiana.",
            "categoria": "Ley de Ampere",
            "dificultad": "media"
        },
        {
            "id": "t2_mc_07",
            "pregunta": "Dentro de un conductor cilindrico con corriente uniforme, ¿como depende B de r?",
            "opciones": [
                "B es proporcional a r",
                "B es proporcional a 1/r",
                "B es constante",
                "B siempre es cero"
            ],
            "respuesta": 1,
            "explicacion": "Dentro, B = mu0*I*r/(2*pi*R^2), por tanto crece linealmente con r.",
            "categoria": "Ley de Ampere",
            "dificultad": "dificil"
        },
        {
            "id": "t2_mc_08",
            "pregunta": "Fuera de un conductor cilindrico largo, ¿que corriente encierra el bucle amperiano?",
            "opciones": [
                "Ninguna corriente",
                "Solo una fraccion de la corriente",
                "Toda la corriente I",
                "Una corriente negativa siempre"
            ],
            "respuesta": 3,
            "explicacion": "Si r > R, el bucle encierra toda la corriente del conductor.",
            "categoria": "Ley de Ampere",
            "dificultad": "media"
        },
        {
            "id": "t2_mc_09",
            "pregunta": "¿Que formula corresponde al campo dentro de un solenoide largo?",
            "opciones": [
                "B = mu0*n*I",
                "B = mu0*I/(2*pi*r)",
                "F = |q|vB",
                "Phi_B = BAcos(theta)"
            ],
            "respuesta": 1,
            "explicacion": "Dentro de un solenoide largo ideal, B = mu0*n*I.",
            "categoria": "Solenoide",
            "dificultad": "facil"
        },
        {
            "id": "t2_mc_10",
            "pregunta": "¿Que formula corresponde al campo dentro del devanado de un toroide?",
            "opciones": [
                "B = mu0*N*I/(2*pi*r)",
                "B = mu0*n*I",
                "E = kq/r^2",
                "F = ma"
            ],
            "respuesta": 1,
            "explicacion": "Para un toroide ideal dentro del devanado, B = mu0*N*I/(2*pi*r).",
            "categoria": "Toroide",
            "dificultad": "media"
        }
    ],

    "ejercicios_numericos": [
        {
            "id": "t2_num_01",
            "enunciado": "Un segmento de corriente tiene I = 125 A, dl = 1.0 cm, r = 1.2 m y theta = 90 grados. Calcula dB en teslas usando Biot-Savart.",
            "respuesta": 8.7e-8,
            "unidad": "T",
            "tolerancia_relativa": 0.06,
            "explicacion": "dB = (mu0/4pi)*I*dl*sen(theta)/r^2 = 1e-7*125*0.01/1.2^2 = 8.7e-8 T.",
            "categoria": "Biot-Savart",
            "dificultad": "media"
        },
        {
            "id": "t2_num_02",
            "enunciado": "El mismo segmento tiene I = 125 A, dl = 1.0 cm, r = 1.2 m y theta = 30 grados. Calcula dB en teslas.",
            "respuesta": 4.3e-8,
            "unidad": "T",
            "tolerancia_relativa": 0.06,
            "explicacion": "Es el mismo caso, pero sen(30)=0.5. Por eso el campo es aproximadamente la mitad: 4.3e-8 T.",
            "categoria": "Biot-Savart",
            "dificultad": "media"
        },
        {
            "id": "t2_num_03",
            "enunciado": "Un hilo recto largo conduce I = 10 A. Calcula B a r = 0.05 m del hilo.",
            "respuesta": 4.0e-5,
            "unidad": "T",
            "tolerancia_relativa": 0.05,
            "explicacion": "B = mu0*I/(2*pi*r) = 4pi*1e-7*10/(2pi*0.05) = 4.0e-5 T.",
            "categoria": "Campo de un hilo",
            "dificultad": "facil"
        },
        {
            "id": "t2_num_04",
            "enunciado": "Un hilo recto largo produce B = 2.0e-5 T a una distancia r = 0.10 m. Calcula la corriente I.",
            "respuesta": 10.0,
            "unidad": "A",
            "tolerancia_relativa": 0.05,
            "explicacion": "I = B*2*pi*r/mu0 = 2.0e-5*2pi*0.10/(4pi*1e-7) = 10 A.",
            "categoria": "Campo de un hilo",
            "dificultad": "media"
        },
        {
            "id": "t2_num_05",
            "enunciado": "Un solenoide largo tiene n = 800 espiras/m y corriente I = 2 A. Calcula B dentro del solenoide.",
            "respuesta": 2.01e-3,
            "unidad": "T",
            "tolerancia_relativa": 0.05,
            "explicacion": "B = mu0*n*I = 4pi*1e-7*800*2 = 2.01e-3 T.",
            "categoria": "Solenoide",
            "dificultad": "media"
        },
        {
            "id": "t2_num_06",
            "enunciado": "Un solenoide largo produce B = 1.0e-3 T con I = 2 A. Calcula n en espiras/m.",
            "respuesta": 397.9,
            "unidad": "espiras/m",
            "tolerancia_relativa": 0.05,
            "explicacion": "n = B/(mu0*I) = 1.0e-3/(4pi*1e-7*2) ≈ 398 espiras/m.",
            "categoria": "Solenoide",
            "dificultad": "media"
        },
        {
            "id": "t2_num_07",
            "enunciado": "Un toroide tiene N = 500 espiras, I = 2 A y r = 0.10 m. Calcula B dentro del devanado.",
            "respuesta": 2.0e-3,
            "unidad": "T",
            "tolerancia_relativa": 0.05,
            "explicacion": "B = mu0*N*I/(2*pi*r) = 4pi*1e-7*500*2/(2pi*0.10) = 2.0e-3 T.",
            "categoria": "Toroide",
            "dificultad": "dificil"
        },
        {
            "id": "t2_num_08",
            "enunciado": "Una espira circular de radio a = 0.20 m conduce I = 3 A. Calcula B en el centro de la espira.",
            "respuesta": 9.42e-6,
            "unidad": "T",
            "tolerancia_relativa": 0.05,
            "explicacion": "B = mu0*I/(2*a) = 4pi*1e-7*3/(2*0.20) = 9.42e-6 T.",
            "categoria": "Espira circular",
            "dificultad": "media"
        },
        {
            "id": "t2_num_09",
            "enunciado": "Una carga q = 2.0e-6 C se mueve con v = 3.0e4 m/s perpendicularmente a B = 0.20 T. Calcula la fuerza magnetica.",
            "respuesta": 0.012,
            "unidad": "N",
            "tolerancia_relativa": 0.05,
            "explicacion": "F = |q|vBsen(90) = 2e-6*3e4*0.20 = 0.012 N.",
            "categoria": "Fuerza magnetica",
            "dificultad": "facil"
        },
        {
            "id": "t2_num_10",
            "enunciado": "Un conductor de longitud L = 0.50 m lleva I = 4 A y esta perpendicular a B = 0.30 T. Calcula la fuerza magnetica.",
            "respuesta": 0.60,
            "unidad": "N",
            "tolerancia_relativa": 0.05,
            "explicacion": "F = I*L*B*sen(90) = 4*0.50*0.30 = 0.60 N.",
            "categoria": "Fuerza sobre conductor",
            "dificultad": "facil"
        },
        {
            "id": "t2_num_11",
            "enunciado": "Un conductor cilindrico largo tiene R = 0.04 m, I = 8 A. Calcula B dentro del conductor a r = 0.02 m.",
            "respuesta": 2.0e-5,
            "unidad": "T",
            "tolerancia_relativa": 0.06,
            "explicacion": "Para r<R, B = mu0*I*r/(2*pi*R^2) = 4pi*1e-7*8*0.02/(2pi*0.04^2) = 2.0e-5 T.",
            "categoria": "Ley de Ampere",
            "dificultad": "dificil"
        },
        {
            "id": "t2_num_12",
            "enunciado": "Un conductor cilindrico largo conduce I = 8 A. Calcula B fuera del conductor a r = 0.08 m.",
            "respuesta": 2.0e-5,
            "unidad": "T",
            "tolerancia_relativa": 0.06,
            "explicacion": "Para r>R, B = mu0*I/(2*pi*r) = 4pi*1e-7*8/(2pi*0.08) = 2.0e-5 T.",
            "categoria": "Ley de Ampere",
            "dificultad": "media"
        }
    ]
}