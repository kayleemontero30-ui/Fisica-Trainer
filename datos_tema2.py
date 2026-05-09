# -*- coding: utf-8 -*-

TEMA2 = {
    "nombre": "Tema 2 - Campo magnetostatico",

    "resumen": """
El campo magnetostatico estudia los campos magneticos producidos por cargas en movimiento
y corrientes electricas estacionarias. En este tema no estudiamos todavia induccion
electromagnetica, porque eso pertenece al tema de Faraday/circuitos.

1. Campo magnetico
El campo magnetico B es una magnitud vectorial. Tiene modulo, direccion y sentido.
Su unidad en el Sistema Internacional es el tesla, T.

Una diferencia importante con el campo electrico es que el campo electrico puede ser producido
por cargas en reposo, mientras que el campo magnetico esta asociado a cargas en movimiento
o corrientes electricas.

2. Polos magneticos
En electricidad existen cargas positivas y negativas aisladas. En magnetismo, en cambio,
no se observan polos magneticos aislados. Si se parte un iman, no se obtiene un polo norte
separado y un polo sur separado. Se obtienen dos imanes mas pequenos, cada uno con polo norte
y polo sur.

3. Lineas de campo magnetico
Las lineas de campo magnetico indican la direccion del campo B. Fuera de un iman, el campo
sale del polo norte y entra por el polo sur. Las lineas de campo magnetico son cerradas.

En dibujos:
- Un punto suele representar un vector que sale del papel.
- Una cruz suele representar un vector que entra en el papel.

Importante:
Las lineas de campo magnetico no son exactamente lineas de fuerza. La fuerza magnetica sobre
una carga no apunta en la direccion de B, sino perpendicular a v y a B.

4. Fuerza magnetica sobre una carga
Una carga q que se mueve con velocidad v dentro de un campo magnetico B puede experimentar
una fuerza magnetica:

F = |q|*v*B*sen(theta)

donde theta es el angulo entre la velocidad y el campo magnetico.

Ideas importantes:
- Si la carga esta en reposo, no hay fuerza magnetica.
- Si v es paralela o antiparalela a B, la fuerza es cero.
- Si v es perpendicular a B, la fuerza es maxima.
- La fuerza magnetica siempre es perpendicular a v y a B.
- Para una carga positiva, el sentido se obtiene con la regla de la mano derecha.
- Para una carga negativa, el sentido es el contrario.

5. Fuerza de Lorentz
Si una carga esta sometida a campo electrico E y campo magnetico B, la fuerza total es:

F = q*(E + v x B)

Esto conecta el Tema 1 con el Tema 2:
- En el Tema 1: F = qE.
- En el Tema 2: F = q*(v x B).
- Juntas forman la fuerza de Lorentz.

6. Fuerza magnetica sobre un conductor
Un conductor con corriente dentro de un campo magnetico tambien puede experimentar una fuerza.
Esto ocurre porque la corriente esta formada por cargas en movimiento.

Para un tramo recto:

F = I*L*B*sen(theta)

donde I es la corriente, L es la longitud del conductor dentro del campo y theta es el angulo
entre el conductor/corriente y el campo magnetico.

7. Flujo magnetico
El flujo magnetico mide cuanto campo magnetico atraviesa una superficie:

Phi_B = B*A*cos(theta)

donde theta es el angulo entre B y la normal de la superficie.

Casos importantes:
- Si theta = 0 grados, el flujo es maximo: Phi_B = B*A.
- Si theta = 90 grados, el flujo es cero.
- En una superficie cerrada, el flujo magnetico neto es cero porque no existen monopolos
  magneticos aislados.

8. Ley de Biot-Savart
La Ley de Biot-Savart permite calcular el campo magnetico producido por un elemento pequeno
de corriente:

dB = (mu0/(4*pi)) * (I*dl*sen(theta)/r^2)

En forma vectorial:

dB = (mu0/(4*pi)) * (I*(dl x r_hat)/r^2)

La idea es parecida a los campos electricos producidos por distribuciones de carga:
se calcula una contribucion pequena y luego se suman o integran todas las contribuciones.

9. Hilo recto finito
Para un hilo recto de longitud 2a y un punto situado a una distancia perpendicular x desde
el centro del hilo:

B = (mu0*I/(4*pi)) * (2*a)/(x*sqrt(x^2 + a^2))

Este resultado aparece al integrar Biot-Savart sobre el hilo.

10. Hilo recto infinito
Si el hilo es muy largo, se puede usar el caso limite:

B = mu0*I/(2*pi*r)

Las lineas de campo son circunferencias alrededor del hilo. El sentido se obtiene con la
regla de la mano derecha: el pulgar apunta en la direccion de la corriente y los dedos indican
el sentido de B.

11. Espira circular
Para una espira circular de radio a con corriente I, el campo en el eje de la espira es:

B = mu0*I*a^2/(2*(x^2 + a^2)^(3/2))

En el centro de la espira, x = 0:

B = mu0*I/(2*a)

Si hay N espiras, el campo se multiplica por N.

12. Ley de Ampere
La Ley de Ampere relaciona la circulacion del campo magnetico alrededor de una trayectoria
cerrada con la corriente neta encerrada:

integral(B·dl) = mu0*I_encerrada

Es especialmente util cuando hay simetria. Por ejemplo:
- hilo recto largo
- conductor cilindrico largo
- solenoide largo
- toroide

Importante:
Si la integral de Ampere da cero, eso no significa necesariamente que B sea cero en todos
los puntos. Puede significar que la corriente neta encerrada es cero o que las contribuciones
se cancelan.

13. Conductor cilindrico largo
Para un conductor cilindrico largo de radio R con corriente uniformemente distribuida:

Dentro del conductor, si r < R:

B = mu0*I*r/(2*pi*R^2)

Fuera del conductor, si r > R:

B = mu0*I/(2*pi*r)

Dentro del conductor, el campo crece linealmente con r. Fuera del conductor, el campo disminuye
como 1/r.

14. Solenoide largo
Un solenoide largo produce un campo magnetico aproximadamente uniforme en su interior:

B = mu0*n*I

donde n es el numero de espiras por unidad de longitud. Fuera de un solenoide largo ideal,
el campo es aproximadamente cero.

15. Toroide
Un toroide produce un campo magnetico practicamente confinado dentro del devanado.

Dentro del devanado:

B = mu0*N*I/(2*pi*r)

En el hueco interior y fuera del toroide ideal, el campo es aproximadamente cero.

Idea clave para examenes:
- Carga moviendose en B: usa F = |q|vBsen(theta).
- Carga con E y B: usa Lorentz, F = q*(E + v x B).
- Conductor con corriente dentro de B: usa F = ILBsen(theta).
- Elemento de corriente: usa Biot-Savart.
- Hilo recto largo: usa B = mu0I/(2*pi*r).
- Espira circular: usa B = mu0Ia^2/(2*(x^2+a^2)^(3/2)).
- Simetria circular/cilindrica: piensa en Ampere.
- Solenoide largo: usa B = mu0nI.
- Toroide: usa B = mu0NI/(2*pi*r).
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
                },
                {
                    "nombre": "Fuerza maxima",
                    "formula": "F_max = |q|*v*B",
                    "explicacion": "Ocurre cuando theta = 90 grados."
                },
                {
                    "nombre": "Fuerza cero",
                    "formula": "F = 0",
                    "explicacion": "Ocurre si theta = 0 o 180 grados, es decir, si v es paralela o antiparalela a B."
                }
            ]
        },
        {
            "nombre": "Fuerza magnetica vectorial sobre una carga",
            "formula": "F = q*(v x B)",
            "uso": "Determinar direccion y sentido de la fuerza magnetica.",
            "cuando_usarla": [
                "Cuando el problema pide direccion o sentido de la fuerza.",
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
            "nombre": "Fuerza de Lorentz",
            "formula": "F = q*(E + v x B)",
            "uso": "Calcular la fuerza total sobre una carga cuando existen campo electrico y campo magnetico.",
            "cuando_usarla": [
                "Cuando aparecen simultaneamente E y B.",
                "Cuando una carga se mueve en una region con campo electrico y magnetico.",
                "Cuando se combinan fuerza electrica y fuerza magnetica."
            ],
            "despejes": [
                {
                    "nombre": "Parte electrica",
                    "formula": "F_electrica = q*E",
                    "explicacion": "Es la contribucion del campo electrico."
                },
                {
                    "nombre": "Parte magnetica",
                    "formula": "F_magnetica = q*(v x B)",
                    "explicacion": "Es la contribucion del campo magnetico."
                },
                {
                    "nombre": "Modulo magnetico",
                    "formula": "F_magnetica = |q|*v*B*sen(theta)",
                    "explicacion": "Se usa para calcular solo el modulo de la parte magnetica."
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
            "nombre": "Fuerza entre dos corrientes paralelas",
            "formula": "F/L = mu0*I1*I2/(2*pi*d)",
            "uso": "Calcular la fuerza por unidad de longitud entre dos conductores rectos paralelos.",
            "cuando_usarla": [
                "Cuando hay dos hilos largos paralelos con corriente.",
                "Cuando te dan I1, I2 y la distancia d.",
                "Cuando preguntan si se atraen o repelen."
            ],
            "despejes": [
                {
                    "nombre": "Corrientes en el mismo sentido",
                    "formula": "Fuerza atractiva",
                    "explicacion": "Dos corrientes paralelas en el mismo sentido se atraen."
                },
                {
                    "nombre": "Corrientes en sentidos opuestos",
                    "formula": "Fuerza repulsiva",
                    "explicacion": "Dos corrientes paralelas en sentidos opuestos se repelen."
                },
                {
                    "nombre": "Despeje de distancia",
                    "formula": "d = mu0*I1*I2/(2*pi*(F/L))",
                    "explicacion": "Se usa cuando conoces la fuerza por unidad de longitud y las corrientes."
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
                    "explicacion": "Ocurre cuando theta = 0 grados."
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
            "nombre": "Biot-Savart vectorial",
            "formula": "dB = (mu0/(4*pi))*(I*(dl x r_hat)/r^2)",
            "uso": "Determinar direccion y sentido del campo magnetico producido por un elemento de corriente.",
            "cuando_usarla": [
                "Cuando el problema pide direccion de dB.",
                "Cuando necesitas usar producto vectorial.",
                "Cuando hay que aplicar la regla de la mano derecha."
            ],
            "despejes": [
                {
                    "nombre": "Direccion de dB",
                    "formula": "dB apunta en la direccion de dl x r_hat",
                    "explicacion": "Se obtiene con la regla de la mano derecha."
                },
                {
                    "nombre": "Vector r_hat",
                    "formula": "r_hat = r/r",
                    "explicacion": "Vector unitario desde el elemento de corriente hasta el punto donde se calcula B."
                }
            ]
        },
        {
            "nombre": "Campo de un hilo recto finito",
            "formula": "B = (mu0*I/(4*pi))*(2*a)/(x*sqrt(x^2 + a^2))",
            "uso": "Calcular el campo de un hilo recto de longitud 2a en un punto sobre su bisectriz perpendicular.",
            "cuando_usarla": [
                "Cuando el hilo tiene longitud finita 2a.",
                "Cuando el punto esta a distancia perpendicular x desde el centro del hilo.",
                "Cuando se ha integrado Biot-Savart sobre un segmento recto."
            ],
            "despejes": [
                {
                    "nombre": "Caso de hilo muy largo",
                    "formula": "B ≈ mu0*I/(2*pi*x)",
                    "explicacion": "Se obtiene cuando a es mucho mayor que x."
                },
                {
                    "nombre": "Dependencia con la corriente",
                    "formula": "B proporcional a I",
                    "explicacion": "Si duplicas I, se duplica B."
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
                },
                {
                    "nombre": "Bobina de N espiras",
                    "formula": "B = mu0*N*I/(2*a)",
                    "explicacion": "Si hay N espiras iguales, el campo se multiplica por N."
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
                },
                {
                    "nombre": "Bobina de N espiras",
                    "formula": "B = mu0*N*I*a^2/(2*(x^2 + a^2)^(3/2))",
                    "explicacion": "Para una bobina de N espiras, se multiplica por N."
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
                    "explicacion": "El bucle amperiano solo encierra parte de la corriente total."
                },
                {
                    "nombre": "Densidad de corriente uniforme",
                    "formula": "J = I/(pi*R^2)",
                    "explicacion": "Se usa para obtener la corriente encerrada dentro de un radio r."
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
                },
                {
                    "nombre": "Corriente encerrada exterior",
                    "formula": "I_encerrada = I",
                    "explicacion": "Para r > R, el bucle amperiano encierra toda la corriente."
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
                },
                {
                    "nombre": "Relacion con N y L",
                    "formula": "n = N/L",
                    "explicacion": "n es el numero de espiras por unidad de longitud."
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
            "frente": "¿Existen polos magneticos aislados?",
            "reverso": "No. Los polos magneticos siempre aparecen en pares norte-sur.",
            "categoria": "Magnetismo basico"
        },
        {
            "id": "t2_fc_03",
            "frente": "¿Una carga en reposo dentro de un campo magnetico experimenta fuerza magnetica?",
            "reverso": "No. La fuerza magnetica requiere que la carga se mueva.",
            "categoria": "Fuerza magnetica"
        },
        {
            "id": "t2_fc_04",
            "frente": "¿Cuando es maxima la fuerza magnetica sobre una carga?",
            "reverso": "Cuando la velocidad es perpendicular al campo magnetico.",
            "categoria": "Fuerza magnetica"
        },
        {
            "id": "t2_fc_05",
            "frente": "¿Que pasa si v es paralela a B?",
            "reverso": "La fuerza magnetica es cero porque sen(0) = 0.",
            "categoria": "Fuerza magnetica"
        },
        {
            "id": "t2_fc_06",
            "frente": "¿Que pasa con el sentido de la fuerza si la carga es negativa?",
            "reverso": "El sentido es contrario al que da la regla de la mano derecha para una carga positiva.",
            "categoria": "Fuerza magnetica"
        },
        {
            "id": "t2_fc_07",
            "frente": "¿Que representa un punto en un dibujo de campo magnetico?",
            "reverso": "Un vector que sale del plano de la pagina.",
            "categoria": "Representacion vectorial"
        },
        {
            "id": "t2_fc_08",
            "frente": "¿Que representa una cruz en un dibujo de campo magnetico?",
            "reverso": "Un vector que entra en el plano de la pagina.",
            "categoria": "Representacion vectorial"
        },
        {
            "id": "t2_fc_09",
            "frente": "¿Que forma tienen las lineas de campo alrededor de un hilo recto largo?",
            "reverso": "Son circunferencias concentricas alrededor del hilo.",
            "categoria": "Campo de un hilo"
        },
        {
            "id": "t2_fc_10",
            "frente": "¿Cuando conviene usar la Ley de Ampere?",
            "reverso": "Cuando hay simetria y se puede elegir una trayectoria amperiana sencilla.",
            "categoria": "Ley de Ampere"
        },
        {
            "id": "t2_fc_11",
            "frente": "¿Como es el campo dentro de un solenoide largo ideal?",
            "reverso": "Aproximadamente uniforme y paralelo al eje.",
            "categoria": "Solenoide"
        },
        {
            "id": "t2_fc_12",
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
            "pregunta": "La fuerza de Lorentz incluye la fuerza electrica y la fuerza magnetica.",
            "respuesta": True,
            "explicacion": "F = q*(E + v x B).",
            "categoria": "Fuerza de Lorentz",
            "dificultad": "media"
        },
        {
            "id": "t2_vf_07",
            "pregunta": "La Ley de Biot-Savart sirve para calcular el campo magnetico creado por corrientes.",
            "respuesta": True,
            "explicacion": "Biot-Savart calcula contribuciones dB de elementos de corriente.",
            "categoria": "Biot-Savart",
            "dificultad": "media"
        },
        {
            "id": "t2_vf_08",
            "pregunta": "La Ley de Ampere utiliza una integral de linea cerrada.",
            "respuesta": True,
            "explicacion": "Ampere relaciona integral(B·dl) con la corriente encerrada.",
            "categoria": "Ley de Ampere",
            "dificultad": "media"
        },
        {
            "id": "t2_vf_09",
            "pregunta": "Si una trayectoria amperiana no encierra corriente neta, necesariamente B es cero en todos los puntos.",
            "respuesta": False,
            "explicacion": "La integral puede ser cero aunque el campo no sea cero en cada punto.",
            "categoria": "Ley de Ampere",
            "dificultad": "dificil"
        },
        {
            "id": "t2_vf_10",
            "pregunta": "Dentro de un conductor cilindrico largo con corriente uniforme, B crece linealmente con r.",
            "respuesta": True,
            "explicacion": "Para r < R, B = mu0*I*r/(2*pi*R^2).",
            "categoria": "Ley de Ampere",
            "dificultad": "dificil"
        },
        {
            "id": "t2_vf_11",
            "pregunta": "Fuera de un conductor cilindrico largo, B disminuye como 1/r.",
            "respuesta": True,
            "explicacion": "Para r > R, B = mu0*I/(2*pi*r).",
            "categoria": "Ley de Ampere",
            "dificultad": "media"
        },
        {
            "id": "t2_vf_12",
            "pregunta": "En un solenoide largo ideal, el campo exterior es aproximadamente cero.",
            "respuesta": True,
            "explicacion": "El modelo ideal de solenoide largo considera B casi nulo fuera.",
            "categoria": "Solenoide",
            "dificultad": "media"
        },
        {
            "id": "t2_vf_13",
            "pregunta": "En un toroide ideal, el campo magnetico es igual en todas partes del espacio.",
            "respuesta": False,
            "explicacion": "El campo queda practicamente confinado dentro del devanado.",
            "categoria": "Toroide",
            "dificultad": "media"
        },
        {
            "id": "t2_vf_14",
            "pregunta": "Dos corrientes paralelas en el mismo sentido se atraen.",
            "respuesta": True,
            "explicacion": "Corrientes paralelas en el mismo sentido se atraen.",
            "categoria": "Fuerza entre corrientes",
            "dificultad": "media"
        },
        {
            "id": "t2_vf_15",
            "pregunta": "Dos corrientes paralelas en sentidos opuestos se atraen.",
            "respuesta": False,
            "explicacion": "Corrientes paralelas en sentidos opuestos se repelen.",
            "categoria": "Fuerza entre corrientes",
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
            "pregunta": "¿Que formula representa la fuerza de Lorentz?",
            "opciones": [
                "F = q*(E + v x B)",
                "F = k*q1*q2/r^2",
                "B = mu0*n*I",
                "Phi_B = B*A*cos(theta)"
            ],
            "respuesta": 1,
            "explicacion": "La fuerza de Lorentz combina fuerza electrica y magnetica.",
            "categoria": "Fuerza de Lorentz",
            "dificultad": "media"
        },
        {
            "id": "t2_mc_04",
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
            "id": "t2_mc_05",
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
            "id": "t2_mc_06",
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
            "id": "t2_mc_07",
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
            "id": "t2_mc_08",
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
            "id": "t2_mc_09",
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
            "id": "t2_mc_10",
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
            "id": "t2_mc_11",
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
        },
        {
            "id": "t2_mc_12",
            "pregunta": "¿Que significa una cruz en un dibujo de campo magnetico?",
            "opciones": [
                "Campo saliendo del papel",
                "Campo entrando en el papel",
                "Campo igual a cero",
                "Campo electrico positivo"
            ],
            "respuesta": 2,
            "explicacion": "La cruz representa un vector que entra en el plano de la pagina.",
            "categoria": "Representacion vectorial",
            "dificultad": "facil"
        },
        {
            "id": "t2_mc_13",
            "pregunta": "¿Que significa un punto en un dibujo de campo magnetico?",
            "opciones": [
                "Campo saliendo del papel",
                "Campo entrando en el papel",
                "Campo igual a cero",
                "Carga negativa"
            ],
            "respuesta": 1,
            "explicacion": "El punto representa un vector que sale del plano de la pagina.",
            "categoria": "Representacion vectorial",
            "dificultad": "facil"
        },
        {
            "id": "t2_mc_14",
            "pregunta": "¿Que se obtiene si se parte un iman por la mitad?",
            "opciones": [
                "Un polo norte aislado y un polo sur aislado",
                "Dos imanes mas pequenos, cada uno con norte y sur",
                "Solo cargas positivas",
                "Un campo electrico uniforme"
            ],
            "respuesta": 2,
            "explicacion": "No se han observado monopolos magneticos aislados.",
            "categoria": "Magnetismo basico",
            "dificultad": "facil"
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
            "enunciado": "Un hilo recto finito tiene I = 5 A y longitud total 2a = 0.80 m. El punto P esta a x = 0.30 m del centro sobre la bisectriz perpendicular. Calcula B.",
            "respuesta": 2.67e-6,
            "unidad": "T",
            "tolerancia_relativa": 0.06,
            "explicacion": "Usa B = (mu0*I/(4*pi))*(2a)/(x*sqrt(x^2+a^2)). Con a=0.40 m, x=0.30 m e I=5 A, B≈2.67e-6 T.",
            "categoria": "Hilo recto finito",
            "dificultad": "dificil"
        },
        {
            "id": "t2_num_04",
            "enunciado": "Un hilo recto largo conduce I = 10 A. Calcula B a r = 0.05 m del hilo.",
            "respuesta": 4.0e-5,
            "unidad": "T",
            "tolerancia_relativa": 0.05,
            "explicacion": "B = mu0*I/(2*pi*r) = 4pi*1e-7*10/(2pi*0.05) = 4.0e-5 T.",
            "categoria": "Campo de un hilo",
            "dificultad": "facil"
        },
        {
            "id": "t2_num_05",
            "enunciado": "Un hilo recto largo produce B = 2.0e-5 T a una distancia r = 0.10 m. Calcula la corriente I.",
            "respuesta": 10.0,
            "unidad": "A",
            "tolerancia_relativa": 0.05,
            "explicacion": "I = B*2*pi*r/mu0 = 2.0e-5*2pi*0.10/(4pi*1e-7) = 10 A.",
            "categoria": "Campo de un hilo",
            "dificultad": "media"
        },
        {
            "id": "t2_num_06",
            "enunciado": "Una espira circular de radio a = 0.20 m conduce I = 3 A. Calcula B en el centro de la espira.",
            "respuesta": 9.42e-6,
            "unidad": "T",
            "tolerancia_relativa": 0.05,
            "explicacion": "B = mu0*I/(2*a) = 4pi*1e-7*3/(2*0.20) = 9.42e-6 T.",
            "categoria": "Espira circular",
            "dificultad": "media"
        },
        {
            "id": "t2_num_07",
            "enunciado": "Una espira circular de radio a = 0.20 m conduce I = 3 A. Calcula B sobre su eje a x = 0.30 m del centro.",
            "respuesta": 1.61e-6,
            "unidad": "T",
            "tolerancia_relativa": 0.06,
            "explicacion": "B = mu0*I*a^2/(2*(x^2+a^2)^(3/2)). Con a=0.20, x=0.30 e I=3, B≈1.61e-6 T.",
            "categoria": "Espira circular",
            "dificultad": "dificil"
        },
        {
            "id": "t2_num_08",
            "enunciado": "Una bobina de N = 100 espiras, radio a = 0.60 m e I = 5.0 A. Calcula B en el centro.",
            "respuesta": 5.24e-4,
            "unidad": "T",
            "tolerancia_relativa": 0.05,
            "explicacion": "En el centro, B = mu0*N*I/(2*a) = 4pi*1e-7*100*5/(2*0.60) ≈ 5.24e-4 T.",
            "categoria": "Bobina circular",
            "dificultad": "media"
        },
        {
            "id": "t2_num_09",
            "enunciado": "Un solenoide largo tiene n = 800 espiras/m y corriente I = 2 A. Calcula B dentro del solenoide.",
            "respuesta": 2.01e-3,
            "unidad": "T",
            "tolerancia_relativa": 0.05,
            "explicacion": "B = mu0*n*I = 4pi*1e-7*800*2 = 2.01e-3 T.",
            "categoria": "Solenoide",
            "dificultad": "media"
        },
        {
            "id": "t2_num_10",
            "enunciado": "Un solenoide largo produce B = 1.0e-3 T con I = 2 A. Calcula n en espiras/m.",
            "respuesta": 397.9,
            "unidad": "espiras/m",
            "tolerancia_relativa": 0.05,
            "explicacion": "n = B/(mu0*I) = 1.0e-3/(4pi*1e-7*2) ≈ 398 espiras/m.",
            "categoria": "Solenoide",
            "dificultad": "media"
        },
        {
            "id": "t2_num_11",
            "enunciado": "Un toroide tiene N = 500 espiras, I = 2 A y r = 0.10 m. Calcula B dentro del devanado.",
            "respuesta": 2.0e-3,
            "unidad": "T",
            "tolerancia_relativa": 0.05,
            "explicacion": "B = mu0*N*I/(2*pi*r) = 4pi*1e-7*500*2/(2pi*0.10) = 2.0e-3 T.",
            "categoria": "Toroide",
            "dificultad": "dificil"
        },
        {
            "id": "t2_num_12",
            "enunciado": "Una carga q = 2.0e-6 C se mueve con v = 3.0e4 m/s perpendicularmente a B = 0.20 T. Calcula la fuerza magnetica.",
            "respuesta": 0.012,
            "unidad": "N",
            "tolerancia_relativa": 0.05,
            "explicacion": "F = |q|vBsen(90) = 2e-6*3e4*0.20 = 0.012 N.",
            "categoria": "Fuerza magnetica",
            "dificultad": "facil"
        },
        {
            "id": "t2_num_13",
            "enunciado": "Un conductor de longitud L = 0.50 m lleva I = 4 A y esta perpendicular a B = 0.30 T. Calcula la fuerza magnetica.",
            "respuesta": 0.60,
            "unidad": "N",
            "tolerancia_relativa": 0.05,
            "explicacion": "F = I*L*B*sen(90) = 4*0.50*0.30 = 0.60 N.",
            "categoria": "Fuerza sobre conductor",
            "dificultad": "facil"
        },
        {
            "id": "t2_num_14",
            "enunciado": "Un conductor cilindrico largo tiene R = 0.04 m, I = 8 A. Calcula B dentro del conductor a r = 0.02 m.",
            "respuesta": 2.0e-5,
            "unidad": "T",
            "tolerancia_relativa": 0.06,
            "explicacion": "Para r<R, B = mu0*I*r/(2*pi*R^2) = 4pi*1e-7*8*0.02/(2pi*0.04^2) = 2.0e-5 T.",
            "categoria": "Ley de Ampere",
            "dificultad": "dificil"
        },
        {
            "id": "t2_num_15",
            "enunciado": "Un conductor cilindrico largo conduce I = 8 A. Calcula B fuera del conductor a r = 0.08 m.",
            "respuesta": 2.0e-5,
            "unidad": "T",
            "tolerancia_relativa": 0.06,
            "explicacion": "Para r>R, B = mu0*I/(2*pi*r) = 4pi*1e-7*8/(2pi*0.08) = 2.0e-5 T.",
            "categoria": "Ley de Ampere",
            "dificultad": "media"
        },
        {
            "id": "t2_num_16",
            "enunciado": "Dos hilos paralelos largos llevan I1 = 10 A e I2 = 5 A en el mismo sentido, separados d = 0.10 m. Calcula F/L.",
            "respuesta": 1.0e-4,
            "unidad": "N/m",
            "tolerancia_relativa": 0.06,
            "explicacion": "F/L = mu0*I1*I2/(2*pi*d) = 4pi*1e-7*10*5/(2pi*0.10) = 1.0e-4 N/m. Como van en el mismo sentido, se atraen.",
            "categoria": "Fuerza entre corrientes",
            "dificultad": "media"
        }
    ]
}