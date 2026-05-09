# -*- coding: utf-8 -*-

TEMA3 = {
    "nombre": "Tema 3 - Generacion de corriente y circuitos",

    "resumen": """
Este tema estudia como se genera y circula la corriente electrica, y como se analizan
circuitos de corriente continua y alterna con resistencias, capacitores e inductores.

1. Corriente electrica
La corriente electrica mide la cantidad de carga que atraviesa una seccion por unidad
de tiempo:

I = dq/dt

Si la corriente es constante, se puede usar:

I = Q/t

Si la corriente cambia con el tiempo, la carga total se calcula integrando:

Q = integral I(t) dt

2. Densidad de corriente
La densidad de corriente J mide cuanta corriente atraviesa una unidad de area:

J = I/A

Si la corriente no atraviesa perpendicularmente la superficie, se usa:

I = J*A*cos(theta)

Tambien puede relacionarse con la velocidad de arrastre de los electrones:

J = n*e*v_d

donde n es la densidad de electrones libres, e es la carga elemental y v_d es la velocidad
de arrastre.

3. Resistividad, conductividad y Ley de Ohm
La resistencia de un conductor depende del material y de su geometria:

R = rho*L/A

donde rho es la resistividad, L la longitud y A el area transversal.

La conductividad sigma es la inversa de la resistividad:

rho = 1/sigma

La Ley de Ohm relaciona voltaje, corriente y resistencia:

V = I*R

4. Resistencias en serie y paralelo
En serie:
- La corriente es la misma en todas las resistencias.
- El voltaje se reparte.
- La resistencia equivalente es la suma:

R_eq = R1 + R2 + ...

En paralelo:
- El voltaje es el mismo en todas las ramas.
- La corriente se divide.
- La resistencia equivalente cumple:

1/R_eq = 1/R1 + 1/R2 + ...

5. Potencia electrica
La potencia indica la energia transferida por unidad de tiempo:

P = I*V

Para una resistencia:

P = I^2*R
P = V^2/R

Esto es importante para saber si una resistencia se quema o no.

6. Leyes de Kirchhoff
La ley de nodos dice que la suma de corrientes que entran a un nodo es igual a la suma
de corrientes que salen.

La ley de mallas dice que la suma algebraica de voltajes alrededor de una malla cerrada
es cero.

Estas leyes son fundamentales para circuitos con varias baterias y resistencias.

7. Capacitores
Un capacitor almacena carga electrica. Su capacitancia es:

C = Q/V

Para placas paralelas:

C = epsilon_0*A/d

Con dielectrico:

C = K*C0

La energia almacenada es:

U = 1/2*C*V^2

En capacitores en serie:
- La carga es la misma.
- El voltaje se reparte.
- 1/C_eq = 1/C1 + 1/C2 + ...

En capacitores en paralelo:
- El voltaje es el mismo.
- La carga se reparte.
- C_eq = C1 + C2 + ...

8. Circuitos RC
Un circuito RC tiene una resistencia y un capacitor. Su constante de tiempo es:

tau = R*C

Durante la carga:
q(t) = C*E*(1 - e^(-t/(RC)))
i(t) = (E/R)*e^(-t/(RC))

Durante la descarga:
q(t) = Q0*e^(-t/(RC))
i(t) = -(Q0/(RC))*e^(-t/(RC))

La resistencia no cambia la carga final del capacitor, pero si determina que tan rapido se carga.

9. Induccion electromagnetica y Faraday
Si cambia el flujo magnetico a traves de una espira, aparece una fem inducida:

epsilon = -N*dPhi_B/dt

El signo negativo representa la Ley de Lenz: la fem inducida se opone al cambio de flujo
que la produce.

10. Inductores
Un inductor se opone a cambios en la corriente. Su fem autoinducida es:

epsilon = -L*di/dt

La energia almacenada en un inductor es:

U = 1/2*L*I^2

11. Circuitos RL
En un circuito RL, la constante de tiempo es:

tau = L/R

Durante el crecimiento de corriente:

i(t) = (E/R)*(1 - e^(-Rt/L))

Durante la descarga:

i(t) = I0*e^(-Rt/L)

12. Circuitos LC
Un circuito LC ideal oscila intercambiando energia entre el campo electrico del capacitor
y el campo magnetico del inductor.

omega = 1/sqrt(L*C)

f = 1/(2*pi*sqrt(L*C))

13. Circuitos RLC
En corriente alterna, la impedancia total de un circuito RLC serie es:

Z = sqrt(R^2 + (omega*L - 1/(omega*C))^2)

La corriente maxima es:

Imax = Vmax/Z

En resonancia:

omega0 = 1/sqrt(L*C)

En resonancia, la impedancia es minima y la corriente es maxima.
""",

    "formulas": [
        {
            "nombre": "Corriente electrica",
            "formula": "I = dq/dt",
            "uso": "Calcular la corriente como variacion de carga por unidad de tiempo.",
            "cuando_usarla": [
                "Cuando la carga cambia con el tiempo.",
                "Cuando te dan una funcion q(t).",
                "Cuando quieres relacionar corriente y carga."
            ],
            "despejes": [
                {
                    "nombre": "Carga con corriente constante",
                    "formula": "Q = I*t",
                    "explicacion": "Se usa si la corriente es constante."
                },
                {
                    "nombre": "Carga con corriente variable",
                    "formula": "Q = integral I(t) dt",
                    "explicacion": "Se usa si I depende del tiempo."
                }
            ]
        },
        {
            "nombre": "Densidad de corriente",
            "formula": "J = I/A",
            "uso": "Relacionar la corriente con el area de la seccion transversal.",
            "cuando_usarla": [
                "Cuando la corriente atraviesa una superficie.",
                "Cuando te dan el radio o area del conductor.",
                "Cuando preguntan corriente por unidad de area."
            ],
            "despejes": [
                {
                    "nombre": "Corriente desde densidad",
                    "formula": "I = J*A",
                    "explicacion": "Se usa si J es uniforme y perpendicular al area."
                },
                {
                    "nombre": "Corriente con angulo",
                    "formula": "I = J*A*cos(theta)",
                    "explicacion": "Se usa si J forma un angulo con la normal de la superficie."
                }
            ]
        },
        {
            "nombre": "Velocidad de arrastre",
            "formula": "J = n*e*v_d",
            "uso": "Relacionar densidad de corriente con movimiento medio de electrones.",
            "cuando_usarla": [
                "Cuando te dan densidad electronica n.",
                "Cuando te piden velocidad de arrastre.",
                "Cuando aparece cobre u otro conductor con electrones libres."
            ],
            "despejes": [
                {
                    "nombre": "Despeje de velocidad de arrastre",
                    "formula": "v_d = J/(n*e)",
                    "explicacion": "Se usa cuando conoces J, n y e."
                }
            ]
        },
        {
            "nombre": "Resistencia de un conductor",
            "formula": "R = rho*L/A",
            "uso": "Calcular la resistencia a partir del material y la geometria.",
            "cuando_usarla": [
                "Cuando te dan longitud y area.",
                "Cuando te dan resistividad o conductividad.",
                "Cuando el conductor se corta en partes."
            ],
            "despejes": [
                {
                    "nombre": "Resistividad desde conductividad",
                    "formula": "rho = 1/sigma",
                    "explicacion": "Se usa cuando te dan la conductividad."
                },
                {
                    "nombre": "Area circular",
                    "formula": "A = pi*r^2",
                    "explicacion": "Se usa para conductores cilindricos."
                }
            ]
        },
        {
            "nombre": "Ley de Ohm",
            "formula": "V = I*R",
            "uso": "Relacionar voltaje, corriente y resistencia.",
            "cuando_usarla": [
                "Cuando tienes un resistor ohmico.",
                "Cuando te piden I, V o R.",
                "Cuando analizas circuitos DC."
            ],
            "despejes": [
                {
                    "nombre": "Despeje de corriente",
                    "formula": "I = V/R",
                    "explicacion": "Se usa si conoces voltaje y resistencia."
                },
                {
                    "nombre": "Despeje de resistencia",
                    "formula": "R = V/I",
                    "explicacion": "Se usa si conoces voltaje y corriente."
                }
            ]
        },
        {
            "nombre": "Resistencias en serie",
            "formula": "R_eq = R1 + R2 + R3 + ...",
            "uso": "Calcular resistencia equivalente de resistores conectados uno tras otro.",
            "cuando_usarla": [
                "Cuando los resistores forman un solo camino.",
                "Cuando la misma corriente pasa por todos.",
                "Cuando el voltaje se reparte."
            ],
            "despejes": [
                {
                    "nombre": "Corriente en serie",
                    "formula": "I1 = I2 = I3 = I",
                    "explicacion": "La corriente es la misma en serie."
                }
            ]
        },
        {
            "nombre": "Resistencias en paralelo",
            "formula": "1/R_eq = 1/R1 + 1/R2 + 1/R3 + ...",
            "uso": "Calcular resistencia equivalente de ramas en paralelo.",
            "cuando_usarla": [
                "Cuando los resistores estan en ramas separadas.",
                "Cuando el voltaje es igual en cada rama.",
                "Cuando la corriente se divide."
            ],
            "despejes": [
                {
                    "nombre": "Dos resistencias en paralelo",
                    "formula": "R_eq = R1*R2/(R1 + R2)",
                    "explicacion": "Atajo para solo dos resistencias en paralelo."
                }
            ]
        },
        {
            "nombre": "Potencia electrica",
            "formula": "P = I*V",
            "uso": "Calcular energia por unidad de tiempo.",
            "cuando_usarla": [
                "Cuando preguntan potencia suministrada o consumida.",
                "Cuando quieres saber si una resistencia se quema.",
                "Cuando se analiza energia en circuitos."
            ],
            "despejes": [
                {
                    "nombre": "Potencia en resistencia con corriente",
                    "formula": "P = I^2*R",
                    "explicacion": "Se usa si conoces I y R."
                },
                {
                    "nombre": "Potencia en resistencia con voltaje",
                    "formula": "P = V^2/R",
                    "explicacion": "Se usa si conoces V y R."
                }
            ]
        },
        {
            "nombre": "Ley de nodos de Kirchhoff",
            "formula": "sum(I_entrantes) = sum(I_salientes)",
            "uso": "Relacionar corrientes en un nodo.",
            "cuando_usarla": [
                "Cuando un circuito tiene ramas.",
                "Cuando una corriente se divide.",
                "Cuando haces analisis por nodos."
            ],
            "despejes": [
                {
                    "nombre": "Conservacion de corriente",
                    "formula": "sum(I) = 0",
                    "explicacion": "Forma algebraica de la ley de nodos."
                }
            ]
        },
        {
            "nombre": "Ley de mallas de Kirchhoff",
            "formula": "sum(Delta V) = 0",
            "uso": "Analizar voltajes alrededor de una malla cerrada.",
            "cuando_usarla": [
                "Cuando hay varias baterias y resistencias.",
                "Cuando el circuito no se reduce facilmente por serie/paralelo.",
                "Cuando usas corrientes de malla."
            ],
            "despejes": [
                {
                    "nombre": "Caida en resistencia",
                    "formula": "Delta V_R = I*R",
                    "explicacion": "Al atravesar una resistencia en el sentido de la corriente hay caida de potencial."
                }
            ]
        },
        {
            "nombre": "Capacitancia",
            "formula": "C = Q/V",
            "uso": "Relacionar carga almacenada y voltaje en un capacitor.",
            "cuando_usarla": [
                "Cuando te dan carga y voltaje.",
                "Cuando te piden carga almacenada.",
                "Cuando analizas redes de capacitores."
            ],
            "despejes": [
                {
                    "nombre": "Carga del capacitor",
                    "formula": "Q = C*V",
                    "explicacion": "Se usa para calcular carga almacenada."
                },
                {
                    "nombre": "Voltaje del capacitor",
                    "formula": "V = Q/C",
                    "explicacion": "Se usa para calcular voltaje en un capacitor."
                }
            ]
        },
        {
            "nombre": "Capacitor de placas paralelas",
            "formula": "C = epsilon_0*A/d",
            "uso": "Calcular la capacitancia de un capacitor plano-paralelo.",
            "cuando_usarla": [
                "Cuando te dan area de placas y distancia entre placas.",
                "Cuando el capacitor tiene aire o vacio.",
                "Cuando aparece un dielectrico."
            ],
            "despejes": [
                {
                    "nombre": "Con dielectrico",
                    "formula": "C = K*epsilon_0*A/d",
                    "explicacion": "El dielectrico aumenta la capacitancia por un factor K."
                },
                {
                    "nombre": "Despeje de distancia",
                    "formula": "d = epsilon_0*A/C",
                    "explicacion": "Se usa si conoces C y A."
                }
            ]
        },
        {
            "nombre": "Capacitores en serie",
            "formula": "1/C_eq = 1/C1 + 1/C2 + ...",
            "uso": "Calcular capacitancia equivalente en serie.",
            "cuando_usarla": [
                "Cuando los capacitores estan uno detras de otro.",
                "Cuando todos tienen la misma carga.",
                "Cuando el voltaje se reparte."
            ],
            "despejes": [
                {
                    "nombre": "Carga en serie",
                    "formula": "Q1 = Q2 = Q3 = Q",
                    "explicacion": "En serie, la carga es la misma."
                }
            ]
        },
        {
            "nombre": "Capacitores en paralelo",
            "formula": "C_eq = C1 + C2 + ...",
            "uso": "Calcular capacitancia equivalente en paralelo.",
            "cuando_usarla": [
                "Cuando los capacitores estan conectados a los mismos dos nodos.",
                "Cuando todos tienen el mismo voltaje.",
                "Cuando la carga total se reparte."
            ],
            "despejes": [
                {
                    "nombre": "Voltaje en paralelo",
                    "formula": "V1 = V2 = V3 = V",
                    "explicacion": "En paralelo, el voltaje es el mismo."
                }
            ]
        },
        {
            "nombre": "Energia en capacitor",
            "formula": "U = 1/2*C*V^2",
            "uso": "Calcular energia electrostatica almacenada.",
            "cuando_usarla": [
                "Cuando te piden energia almacenada en un capacitor.",
                "Cuando el capacitor esta cargado por completo.",
                "Cuando te dan C y V."
            ],
            "despejes": [
                {
                    "nombre": "Energia usando carga",
                    "formula": "U = Q^2/(2*C)",
                    "explicacion": "Se usa si conoces Q y C."
                },
                {
                    "nombre": "Energia usando Q y V",
                    "formula": "U = 1/2*Q*V",
                    "explicacion": "Se usa si conoces carga y voltaje."
                }
            ]
        },
        {
            "nombre": "Constante de tiempo RC",
            "formula": "tau = R*C",
            "uso": "Medir que tan rapido carga o descarga un capacitor.",
            "cuando_usarla": [
                "Cuando hay un circuito con resistencia y capacitor.",
                "Cuando se pregunta por carga o descarga temporal.",
                "Cuando aparece una exponencial."
            ],
            "despejes": [
                {
                    "nombre": "Tiempo caracteristico",
                    "formula": "t = tau",
                    "explicacion": "A un tiempo tau, el capacitor se ha cargado aproximadamente al 63%."
                }
            ]
        },
        {
            "nombre": "Carga de capacitor en RC",
            "formula": "q(t) = C*E*(1 - e^(-t/(R*C)))",
            "uso": "Calcular la carga durante el proceso de carga de un capacitor.",
            "cuando_usarla": [
                "Cuando el capacitor empieza descargado.",
                "Cuando se conecta a una fuente DC mediante una resistencia.",
                "Cuando se pregunta carga en funcion del tiempo."
            ],
            "despejes": [
                {
                    "nombre": "Carga maxima",
                    "formula": "Qmax = C*E",
                    "explicacion": "La carga final no depende de R."
                },
                {
                    "nombre": "Corriente de carga",
                    "formula": "i(t) = (E/R)*e^(-t/(R*C))",
                    "explicacion": "La corriente empieza maxima y luego baja a cero."
                }
            ]
        },
        {
            "nombre": "Descarga de capacitor en RC",
            "formula": "q(t) = Q0*e^(-t/(R*C))",
            "uso": "Calcular la carga durante la descarga de un capacitor.",
            "cuando_usarla": [
                "Cuando no hay fuente externa.",
                "Cuando el capacitor inicialmente tiene carga Q0.",
                "Cuando la carga disminuye exponencialmente."
            ],
            "despejes": [
                {
                    "nombre": "Corriente de descarga",
                    "formula": "i(t) = -(Q0/(R*C))*e^(-t/(R*C))",
                    "explicacion": "El signo indica sentido contrario al elegido positivo."
                }
            ]
        },
        {
            "nombre": "Ley de Faraday",
            "formula": "epsilon = -N*dPhi_B/dt",
            "uso": "Calcular fem inducida por cambio de flujo magnetico.",
            "cuando_usarla": [
                "Cuando cambia el flujo magnetico.",
                "Cuando cambia B, area o angulo.",
                "Cuando hay una espira o bobina."
            ],
            "despejes": [
                {
                    "nombre": "Modulo de fem media",
                    "formula": "|epsilon| = N*|Delta Phi_B|/Delta t",
                    "explicacion": "Se usa con cambios finitos de flujo."
                }
            ]
        },
        {
            "nombre": "Fem de movimiento",
            "formula": "epsilon = B*L*v",
            "uso": "Calcular fem inducida en una barra que se mueve en un campo magnetico.",
            "cuando_usarla": [
                "Cuando una barra conductora se mueve cortando lineas de campo.",
                "Cuando te dan B, L y v.",
                "Cuando el movimiento es perpendicular al campo."
            ],
            "despejes": [
                {
                    "nombre": "Despeje de velocidad",
                    "formula": "v = epsilon/(B*L)",
                    "explicacion": "Se usa si no conoces la velocidad."
                }
            ]
        },
        {
            "nombre": "Autoinductancia",
            "formula": "L = N*Phi_B/i",
            "uso": "Relacionar flujo magnetico y corriente en una bobina.",
            "cuando_usarla": [
                "Cuando una bobina produce flujo por su propia corriente.",
                "Cuando te piden inductancia.",
                "Cuando aparece autoinduccion."
            ],
            "despejes": [
                {
                    "nombre": "Flujo por espira",
                    "formula": "Phi_B = L*i/N",
                    "explicacion": "Se usa cuando conoces L, i y N."
                }
            ]
        },
        {
            "nombre": "Fem autoinducida",
            "formula": "epsilon = -L*di/dt",
            "uso": "Calcular fem inducida por cambio de corriente en un inductor.",
            "cuando_usarla": [
                "Cuando la corriente en una bobina cambia.",
                "Cuando aparece un inductor.",
                "Cuando preguntan oposicion al cambio de corriente."
            ],
            "despejes": [
                {
                    "nombre": "Modulo de fem autoinducida",
                    "formula": "|epsilon| = L*|di/dt|",
                    "explicacion": "Se usa para calcular la magnitud de la fem."
                }
            ]
        },
        {
            "nombre": "Energia en inductor",
            "formula": "U = 1/2*L*I^2",
            "uso": "Calcular energia almacenada en el campo magnetico de un inductor.",
            "cuando_usarla": [
                "Cuando aparece un inductor con corriente.",
                "Cuando preguntan energia almacenada.",
                "Cuando se analiza un circuito RL o LC."
            ],
            "despejes": [
                {
                    "nombre": "Corriente desde energia",
                    "formula": "I = sqrt(2*U/L)",
                    "explicacion": "Se usa cuando conoces U y L."
                }
            ]
        },
        {
            "nombre": "Constante de tiempo RL",
            "formula": "tau = L/R",
            "uso": "Medir que tan rapido cambia la corriente en un circuito RL.",
            "cuando_usarla": [
                "Cuando hay resistor e inductor.",
                "Cuando se cierra o abre un interruptor.",
                "Cuando la corriente cambia exponencialmente."
            ],
            "despejes": [
                {
                    "nombre": "Crecimiento de corriente RL",
                    "formula": "i(t) = (E/R)*(1 - e^(-R*t/L))",
                    "explicacion": "Se usa al conectar la fuente."
                },
                {
                    "nombre": "Descarga RL",
                    "formula": "i(t) = I0*e^(-R*t/L)",
                    "explicacion": "Se usa al desconectar la fuente."
                }
            ]
        },
        {
            "nombre": "Oscilacion LC",
            "formula": "omega = 1/sqrt(L*C)",
            "uso": "Calcular frecuencia angular natural de un circuito LC.",
            "cuando_usarla": [
                "Cuando hay un capacitor descargandose a traves de un inductor.",
                "Cuando no hay resistencia idealmente.",
                "Cuando se habla de oscilaciones."
            ],
            "despejes": [
                {
                    "nombre": "Frecuencia",
                    "formula": "f = 1/(2*pi*sqrt(L*C))",
                    "explicacion": "Se usa para obtener ciclos por segundo."
                },
                {
                    "nombre": "Corriente maxima",
                    "formula": "Imax = omega*Qmax",
                    "explicacion": "Se usa en oscilaciones LC."
                }
            ]
        },
        {
            "nombre": "Impedancia RLC serie",
            "formula": "Z = sqrt(R^2 + (omega*L - 1/(omega*C))^2)",
            "uso": "Calcular oposicion total en un circuito RLC de corriente alterna.",
            "cuando_usarla": [
                "Cuando hay resistencia, inductor y capacitor en AC.",
                "Cuando te dan frecuencia.",
                "Cuando preguntan corriente maxima o eficaz."
            ],
            "despejes": [
                {
                    "nombre": "Corriente maxima",
                    "formula": "Imax = Vmax/Z",
                    "explicacion": "Se usa para calcular la intensidad maxima en AC."
                },
                {
                    "nombre": "Resonancia",
                    "formula": "omega0 = 1/sqrt(L*C)",
                    "explicacion": "En resonancia, la corriente es maxima."
                }
            ]
        }
    ],

    "flashcards": [
        {
            "id": "t3_fc_01",
            "frente": "¿Que significa corriente electrica?",
            "reverso": "Cantidad de carga que atraviesa una seccion por unidad de tiempo: I = dq/dt.",
            "categoria": "Corriente"
        },
        {
            "id": "t3_fc_02",
            "frente": "¿Que formula relaciona corriente, voltaje y resistencia?",
            "reverso": "Ley de Ohm: V = I*R.",
            "categoria": "Ley de Ohm"
        },
        {
            "id": "t3_fc_03",
            "frente": "¿Como se suman resistencias en serie?",
            "reverso": "R_eq = R1 + R2 + ...",
            "categoria": "Resistencias"
        },
        {
            "id": "t3_fc_04",
            "frente": "¿Que magnitud es igual en resistencias en paralelo?",
            "reverso": "El voltaje es el mismo en cada rama.",
            "categoria": "Resistencias"
        },
        {
            "id": "t3_fc_05",
            "frente": "¿Que dice la ley de nodos de Kirchhoff?",
            "reverso": "La corriente que entra a un nodo es igual a la que sale.",
            "categoria": "Kirchhoff"
        },
        {
            "id": "t3_fc_06",
            "frente": "¿Que dice la ley de mallas de Kirchhoff?",
            "reverso": "La suma algebraica de voltajes en una malla cerrada es cero.",
            "categoria": "Kirchhoff"
        },
        {
            "id": "t3_fc_07",
            "frente": "¿Que es la capacitancia?",
            "reverso": "La capacidad de almacenar carga: C = Q/V.",
            "categoria": "Capacitores"
        },
        {
            "id": "t3_fc_08",
            "frente": "¿Que ocurre con la corriente durante la carga de un capacitor RC?",
            "reverso": "Empieza maxima y disminuye exponencialmente hasta cero.",
            "categoria": "Circuitos RC"
        },
        {
            "id": "t3_fc_09",
            "frente": "¿Que representa tau = RC?",
            "reverso": "La constante de tiempo de un circuito RC.",
            "categoria": "Circuitos RC"
        },
        {
            "id": "t3_fc_10",
            "frente": "¿Que dice la Ley de Faraday?",
            "reverso": "Un cambio de flujo magnetico induce una fem: epsilon = -N*dPhi/dt.",
            "categoria": "Faraday"
        },
        {
            "id": "t3_fc_11",
            "frente": "¿Que hace un inductor?",
            "reverso": "Se opone a cambios en la corriente.",
            "categoria": "Inductores"
        },
        {
            "id": "t3_fc_12",
            "frente": "¿Que representa tau = L/R?",
            "reverso": "La constante de tiempo de un circuito RL.",
            "categoria": "Circuitos RL"
        },
        {
            "id": "t3_fc_13",
            "frente": "¿Que ocurre en un circuito LC ideal?",
            "reverso": "La energia oscila entre el capacitor y el inductor.",
            "categoria": "Circuitos LC"
        },
        {
            "id": "t3_fc_14",
            "frente": "¿Cuando hay resonancia en un RLC?",
            "reverso": "Cuando omega*L = 1/(omega*C), y la corriente es maxima.",
            "categoria": "Circuitos RLC"
        }
    ],

    "preguntas_vf": [
        {
            "id": "t3_vf_01",
            "pregunta": "Si la corriente es constante, la carga que pasa es Q = I*t.",
            "respuesta": True,
            "explicacion": "Para corriente constante, I = Q/t.",
            "categoria": "Corriente",
            "dificultad": "facil"
        },
        {
            "id": "t3_vf_02",
            "pregunta": "En resistencias en serie, la corriente es la misma en todas.",
            "respuesta": True,
            "explicacion": "En serie solo hay un camino para la corriente.",
            "categoria": "Resistencias",
            "dificultad": "facil"
        },
        {
            "id": "t3_vf_03",
            "pregunta": "En resistencias en paralelo, el voltaje es el mismo en cada rama.",
            "respuesta": True,
            "explicacion": "Todas las ramas conectan los mismos dos nodos.",
            "categoria": "Resistencias",
            "dificultad": "facil"
        },
        {
            "id": "t3_vf_04",
            "pregunta": "Agregar resistencias en paralelo aumenta siempre la resistencia equivalente.",
            "respuesta": False,
            "explicacion": "En paralelo, la resistencia equivalente disminuye.",
            "categoria": "Resistencias",
            "dificultad": "media"
        },
        {
            "id": "t3_vf_05",
            "pregunta": "La potencia en una resistencia puede calcularse como P = I^2*R.",
            "respuesta": True,
            "explicacion": "Sale de combinar P=IV con V=IR.",
            "categoria": "Potencia",
            "dificultad": "facil"
        },
        {
            "id": "t3_vf_06",
            "pregunta": "En capacitores en serie, la carga es la misma.",
            "respuesta": True,
            "explicacion": "En serie, los capacitores almacenan la misma carga.",
            "categoria": "Capacitores",
            "dificultad": "media"
        },
        {
            "id": "t3_vf_07",
            "pregunta": "En capacitores en paralelo, la capacitancia equivalente es la suma.",
            "respuesta": True,
            "explicacion": "C_eq = C1 + C2 + ...",
            "categoria": "Capacitores",
            "dificultad": "facil"
        },
        {
            "id": "t3_vf_08",
            "pregunta": "Durante la carga de un capacitor RC, la corriente aumenta con el tiempo.",
            "respuesta": False,
            "explicacion": "Durante la carga, la corriente disminuye exponencialmente.",
            "categoria": "Circuitos RC",
            "dificultad": "media"
        },
        {
            "id": "t3_vf_09",
            "pregunta": "La carga final de un capacitor en un RC conectado a una fuente es Qmax = C*E.",
            "respuesta": True,
            "explicacion": "La carga final no depende de R, solo de C y E.",
            "categoria": "Circuitos RC",
            "dificultad": "media"
        },
        {
            "id": "t3_vf_10",
            "pregunta": "Si el flujo magnetico no cambia, no hay fem inducida.",
            "respuesta": True,
            "explicacion": "Faraday depende de dPhi/dt.",
            "categoria": "Faraday",
            "dificultad": "facil"
        },
        {
            "id": "t3_vf_11",
            "pregunta": "Un inductor se opone a cambios bruscos de corriente.",
            "respuesta": True,
            "explicacion": "La fem autoinducida se opone al cambio de corriente.",
            "categoria": "Inductores",
            "dificultad": "facil"
        },
        {
            "id": "t3_vf_12",
            "pregunta": "Si la corriente en un inductor es constante, la fem autoinducida es cero.",
            "respuesta": True,
            "explicacion": "epsilon = -L*di/dt, y si di/dt = 0, epsilon = 0.",
            "categoria": "Inductores",
            "dificultad": "media"
        },
        {
            "id": "t3_vf_13",
            "pregunta": "En un circuito RL, la constante de tiempo es tau = R/L.",
            "respuesta": False,
            "explicacion": "En RL, tau = L/R.",
            "categoria": "Circuitos RL",
            "dificultad": "media"
        },
        {
            "id": "t3_vf_14",
            "pregunta": "En un circuito LC ideal, la energia total se conserva.",
            "respuesta": True,
            "explicacion": "Sin resistencia, la energia oscila entre C y L sin disiparse.",
            "categoria": "Circuitos LC",
            "dificultad": "media"
        },
        {
            "id": "t3_vf_15",
            "pregunta": "En resonancia RLC serie, la corriente es maxima.",
            "respuesta": True,
            "explicacion": "En resonancia, la impedancia se minimiza.",
            "categoria": "Circuitos RLC",
            "dificultad": "dificil"
        }
    ],

    "preguntas_mc": [
        {
            "id": "t3_mc_01",
            "pregunta": "Si una corriente es I(t), ¿como calculas la carga entre t1 y t2?",
            "opciones": [
                "Q = I*R",
                "Q = integral I(t) dt",
                "Q = V/R",
                "Q = C/V"
            ],
            "respuesta": 2,
            "explicacion": "La carga total es la integral temporal de la corriente.",
            "categoria": "Corriente",
            "dificultad": "media"
        },
        {
            "id": "t3_mc_02",
            "pregunta": "¿Que formula usas para la resistencia de un cilindro conductor?",
            "opciones": [
                "R = rho*L/A",
                "R = C*V",
                "R = L/R",
                "R = I/V"
            ],
            "respuesta": 1,
            "explicacion": "La resistencia depende de resistividad, longitud y area.",
            "categoria": "Resistividad",
            "dificultad": "facil"
        },
        {
            "id": "t3_mc_03",
            "pregunta": "En resistencias en serie, ¿que magnitud es igual?",
            "opciones": [
                "Voltaje",
                "Corriente",
                "Potencia",
                "Capacitancia"
            ],
            "respuesta": 2,
            "explicacion": "En serie, la corriente es la misma.",
            "categoria": "Resistencias",
            "dificultad": "facil"
        },
        {
            "id": "t3_mc_04",
            "pregunta": "En resistencias en paralelo, ¿que magnitud es igual?",
            "opciones": [
                "Corriente",
                "Voltaje",
                "Resistencia",
                "Potencia"
            ],
            "respuesta": 2,
            "explicacion": "En paralelo, el voltaje es el mismo.",
            "categoria": "Resistencias",
            "dificultad": "facil"
        },
        {
            "id": "t3_mc_05",
            "pregunta": "¿Que ley de Kirchhoff se usa en un nodo?",
            "opciones": [
                "Ley de mallas",
                "Ley de nodos",
                "Ley de Faraday",
                "Ley de Coulomb"
            ],
            "respuesta": 2,
            "explicacion": "En nodos se aplica conservacion de corriente.",
            "categoria": "Kirchhoff",
            "dificultad": "facil"
        },
        {
            "id": "t3_mc_06",
            "pregunta": "¿Que formula da la energia almacenada en un capacitor?",
            "opciones": [
                "U = 1/2*C*V^2",
                "U = I*R",
                "U = L/R",
                "U = V/R"
            ],
            "respuesta": 1,
            "explicacion": "La energia electrostatica almacenada es U = 1/2 C V^2.",
            "categoria": "Capacitores",
            "dificultad": "facil"
        },
        {
            "id": "t3_mc_07",
            "pregunta": "¿Que pasa con la corriente durante la carga de un capacitor RC?",
            "opciones": [
                "Aumenta hasta infinito",
                "Permanece constante",
                "Disminuye exponencialmente",
                "Siempre es cero"
            ],
            "respuesta": 3,
            "explicacion": "i(t) = (E/R)*e^(-t/RC).",
            "categoria": "Circuitos RC",
            "dificultad": "media"
        },
        {
            "id": "t3_mc_08",
            "pregunta": "¿Que formula representa la Ley de Faraday?",
            "opciones": [
                "epsilon = -N*dPhi_B/dt",
                "V = IR",
                "F = ma",
                "C = Q/V"
            ],
            "respuesta": 1,
            "explicacion": "Faraday relaciona fem inducida con cambio de flujo.",
            "categoria": "Faraday",
            "dificultad": "facil"
        },
        {
            "id": "t3_mc_09",
            "pregunta": "¿Que formula da la fem autoinducida en un inductor?",
            "opciones": [
                "epsilon = -L*di/dt",
                "epsilon = IR",
                "epsilon = C/V",
                "epsilon = rho L/A"
            ],
            "respuesta": 1,
            "explicacion": "La fem autoinducida se opone al cambio de corriente.",
            "categoria": "Inductores",
            "dificultad": "media"
        },
        {
            "id": "t3_mc_10",
            "pregunta": "¿Cual es la constante de tiempo de un circuito RL?",
            "opciones": [
                "tau = RC",
                "tau = L/R",
                "tau = R/L",
                "tau = LC"
            ],
            "respuesta": 2,
            "explicacion": "En RL, tau = L/R.",
            "categoria": "Circuitos RL",
            "dificultad": "media"
        },
        {
            "id": "t3_mc_11",
            "pregunta": "¿Cual es la frecuencia angular natural de un LC ideal?",
            "opciones": [
                "omega = 1/sqrt(LC)",
                "omega = RC",
                "omega = L/R",
                "omega = R/L"
            ],
            "respuesta": 1,
            "explicacion": "En LC ideal, omega = 1/sqrt(LC).",
            "categoria": "Circuitos LC",
            "dificultad": "media"
        },
        {
            "id": "t3_mc_12",
            "pregunta": "En un RLC serie, ¿cuando ocurre resonancia?",
            "opciones": [
                "Cuando R = 0 siempre",
                "Cuando omega*L = 1/(omega*C)",
                "Cuando C = 0",
                "Cuando la corriente es cero"
            ],
            "respuesta": 2,
            "explicacion": "En resonancia, reactancia inductiva y capacitiva se cancelan.",
            "categoria": "Circuitos RLC",
            "dificultad": "dificil"
        }
    ],

    "ejercicios_numericos": [
        {
            "id": "t3_num_01",
            "enunciado": "Por un hilo circula I(t)=t*e^(-t) A. Calcula la carga entre t=0 s y t=5 s.",
            "respuesta": 0.9596,
            "unidad": "C",
            "tolerancia_relativa": 0.03,
            "explicacion": "Q = integral_0^5 t e^(-t) dt = 1 - 6e^(-5) = 0.9596 C.",
            "categoria": "Corriente",
            "dificultad": "media"
        },
        {
            "id": "t3_num_02",
            "enunciado": "Si circularon 0.9596 C con una corriente constante de 0.5 A, ¿cuanto tiempo fue necesario?",
            "respuesta": 1.9192,
            "unidad": "s",
            "tolerancia_relativa": 0.03,
            "explicacion": "t = Q/I = 0.9596/0.5 = 1.9192 s.",
            "categoria": "Corriente",
            "dificultad": "facil"
        },
        {
            "id": "t3_num_03",
            "enunciado": "Un cilindro de grafito del ejercicio tiene resistencia equivalente final de 67.65 ohm y se conecta a 12 V. Calcula la corriente.",
            "respuesta": 0.177,
            "unidad": "A",
            "tolerancia_relativa": 0.05,
            "explicacion": "I = V/R = 12/67.65 = 0.177 A.",
            "categoria": "Ley de Ohm",
            "dificultad": "media"
        },
        {
            "id": "t3_num_04",
            "enunciado": "Dos resistencias de 4 ohm y 6 ohm estan en serie. Calcula R_eq.",
            "respuesta": 10.0,
            "unidad": "ohm",
            "tolerancia_relativa": 0.01,
            "explicacion": "En serie se suman: R_eq = 4 + 6 = 10 ohm.",
            "categoria": "Resistencias",
            "dificultad": "facil"
        },
        {
            "id": "t3_num_05",
            "enunciado": "Dos resistencias de 4 ohm y 6 ohm estan en paralelo. Calcula R_eq.",
            "respuesta": 2.4,
            "unidad": "ohm",
            "tolerancia_relativa": 0.02,
            "explicacion": "R_eq = R1*R2/(R1+R2) = 24/10 = 2.4 ohm.",
            "categoria": "Resistencias",
            "dificultad": "facil"
        },
        {
            "id": "t3_num_06",
            "enunciado": "Una resistencia consume I = 2 A y tiene R = 5 ohm. Calcula la potencia.",
            "respuesta": 20.0,
            "unidad": "W",
            "tolerancia_relativa": 0.01,
            "explicacion": "P = I^2*R = 2^2*5 = 20 W.",
            "categoria": "Potencia",
            "dificultad": "facil"
        },
        {
            "id": "t3_num_07",
            "enunciado": "Un capacitor de 100 microF se carga con una fuente de 12 V. Calcula la carga maxima.",
            "respuesta": 0.0012,
            "unidad": "C",
            "tolerancia_relativa": 0.03,
            "explicacion": "Qmax = C*V = 100e-6*12 = 0.0012 C.",
            "categoria": "Capacitores",
            "dificultad": "facil"
        },
        {
            "id": "t3_num_08",
            "enunciado": "Un capacitor de 100 microF se carga a 12 V. Calcula la energia almacenada.",
            "respuesta": 0.0072,
            "unidad": "J",
            "tolerancia_relativa": 0.03,
            "explicacion": "U = 1/2*C*V^2 = 0.5*100e-6*12^2 = 0.0072 J.",
            "categoria": "Capacitores",
            "dificultad": "media"
        },
        {
            "id": "t3_num_09",
            "enunciado": "Un capacitor de 100 microF se carga a traves de R = 50 ohm. Calcula tau.",
            "respuesta": 0.005,
            "unidad": "s",
            "tolerancia_relativa": 0.03,
            "explicacion": "tau = R*C = 50*100e-6 = 0.005 s.",
            "categoria": "Circuitos RC",
            "dificultad": "facil"
        },
        {
            "id": "t3_num_10",
            "enunciado": "En el circuito anterior, ¿cuanto tiempo tarda en alcanzar el 90 por ciento de la carga maxima?",
            "respuesta": 0.0115,
            "unidad": "s",
            "tolerancia_relativa": 0.05,
            "explicacion": "0.9 = 1 - e^(-t/tau), entonces t = -tau*ln(0.1) = 2.303*tau = 0.0115 s.",
            "categoria": "Circuitos RC",
            "dificultad": "media"
        },
        {
            "id": "t3_num_11",
            "enunciado": "Una fuente de 12 V esta conectada a C = 2 mF. Calcula la energia final almacenada.",
            "respuesta": 0.144,
            "unidad": "J",
            "tolerancia_relativa": 0.03,
            "explicacion": "U = 1/2*C*V^2 = 0.5*0.002*12^2 = 0.144 J.",
            "categoria": "Capacitores",
            "dificultad": "media"
        },
        {
            "id": "t3_num_12",
            "enunciado": "Una espira tiene area 0.012 m2. El campo cambia de 0 a 0.45 T en 0.09 s con theta=0. Calcula la fem inducida media.",
            "respuesta": 0.06,
            "unidad": "V",
            "tolerancia_relativa": 0.05,
            "explicacion": "DeltaPhi = A*DeltaB = 0.012*0.45 = 0.0054 Wb. epsilon = DeltaPhi/Delta t = 0.06 V.",
            "categoria": "Faraday",
            "dificultad": "media"
        },
        {
            "id": "t3_num_13",
            "enunciado": "Una barra de longitud 0.30 m se mueve a 4 m/s perpendicularmente a B=0.50 T. Calcula la fem.",
            "respuesta": 0.6,
            "unidad": "V",
            "tolerancia_relativa": 0.03,
            "explicacion": "epsilon = B*L*v = 0.50*0.30*4 = 0.6 V.",
            "categoria": "Faraday",
            "dificultad": "media"
        },
        {
            "id": "t3_num_14",
            "enunciado": "Un inductor de L = 1 H tiene una corriente que aumenta de 0 a 2 A en 0.5 s. Calcula la fem autoinducida en modulo.",
            "respuesta": 4.0,
            "unidad": "V",
            "tolerancia_relativa": 0.03,
            "explicacion": "|epsilon| = L*|di/dt| = 1*(2/0.5) = 4 V.",
            "categoria": "Inductores",
            "dificultad": "media"
        },
        {
            "id": "t3_num_15",
            "enunciado": "Un inductor de L = 0.115 H almacena U = 0.260 J. Calcula la corriente.",
            "respuesta": 2.13,
            "unidad": "A",
            "tolerancia_relativa": 0.05,
            "explicacion": "I = sqrt(2U/L) = sqrt(0.520/0.115) = 2.13 A.",
            "categoria": "Inductores",
            "dificultad": "media"
        },
        {
            "id": "t3_num_16",
            "enunciado": "Un circuito RL tiene R = 120 ohm, L = 3 H y V = 40 V. Calcula la corriente final.",
            "respuesta": 0.333,
            "unidad": "A",
            "tolerancia_relativa": 0.05,
            "explicacion": "Tras mucho tiempo, el inductor actua como conductor: I = V/R = 40/120 = 0.333 A.",
            "categoria": "Circuitos RL",
            "dificultad": "facil"
        },
        {
            "id": "t3_num_17",
            "enunciado": "En el RL anterior, calcula el tiempo para alcanzar I = 0.300 A.",
            "respuesta": 0.0576,
            "unidad": "s",
            "tolerancia_relativa": 0.05,
            "explicacion": "I/Imax=0.9. t = -tau*ln(0.1), tau=L/R=3/120=0.025 s. t=0.0576 s.",
            "categoria": "Circuitos RL",
            "dificultad": "media"
        },
        {
            "id": "t3_num_18",
            "enunciado": "Un capacitor de 2 microF se carga a 12 V y luego se descarga por L = 0.25 H. Calcula Imax en el LC.",
            "respuesta": 0.0339,
            "unidad": "A",
            "tolerancia_relativa": 0.05,
            "explicacion": "Qmax=CV=24e-6 C. omega=1/sqrt(LC)=1414 rad/s. Imax=omega*Qmax=0.0339 A.",
            "categoria": "Circuitos LC",
            "dificultad": "dificil"
        },
        {
            "id": "t3_num_19",
            "enunciado": "Para L=0.25 H y C=2 microF, calcula la frecuencia de oscilacion LC.",
            "respuesta": 225.1,
            "unidad": "Hz",
            "tolerancia_relativa": 0.05,
            "explicacion": "f = 1/(2*pi*sqrt(LC)) = 225 Hz.",
            "categoria": "Circuitos LC",
            "dificultad": "dificil"
        },
        {
            "id": "t3_num_20",
            "enunciado": "En un RLC serie con R=100 ohm, L=10 mH, C=100 microF y Vmax=10 V, calcula la corriente maxima en resonancia.",
            "respuesta": 0.1,
            "unidad": "A",
            "tolerancia_relativa": 0.03,
            "explicacion": "En resonancia Z=R, asi que Imax=Vmax/R=10/100=0.1 A.",
            "categoria": "Circuitos RLC",
            "dificultad": "media"
        }
    ]
}