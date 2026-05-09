# -*- coding: utf-8 -*-

TEMA1 = {
    "nombre": "Tema 1 - Campo eléctrico y electrostática",

    "resumen": """
TEMA 1 - CAMPO ELÉCTRICO Y ELECTROSTÁTICA

Este tema estudia cargas eléctricas en reposo. La idea central es entender cómo las
cargas producen fuerzas, campos eléctricos, potencial eléctrico, energía potencial y
flujo eléctrico. También se introduce la Ley de Gauss, que sirve para calcular campos
eléctricos cuando hay simetría.

================================================================================
1. CARGA ELÉCTRICA
================================================================================

La carga eléctrica es una propiedad de la materia. Hay dos tipos de carga:

- Carga positiva.
- Carga negativa.

Reglas básicas:

- Cargas del mismo signo se repelen.
- Cargas de signo opuesto se atraen.
- La carga se conserva.
- La carga está cuantizada: aparece en múltiplos de la carga elemental e.

En problemas básicos normalmente trabajamos con cargas puntuales, es decir, cargas
con tamaño despreciable comparado con las distancias del problema.

Unidades importantes:

- Coulomb: C.
- microCoulomb: 1 μC = 10^-6 C.
- nanoCoulomb: 1 nC = 10^-9 C.
- picoCoulomb: 1 pC = 10^-12 C.

Consejo de examen:
Antes de usar cualquier fórmula, convierte todas las cargas y distancias al Sistema
Internacional.

================================================================================
2. LEY DE COULOMB
================================================================================

La Ley de Coulomb da la fuerza eléctrica entre dos cargas puntuales:

F = k |q1 q2| / r^2

donde:
- F es el módulo de la fuerza.
- q1 y q2 son las cargas.
- r es la distancia entre ellas.
- k es la constante de Coulomb.

En el vacío:

k = 1/(4π epsilon_0) ≈ 8.99 x 10^9 N m^2/C^2

Si el problema está en un medio con permitividad relativa epsilon_r, la fuerza se
reduce:

F = (k/epsilon_r) |q1 q2| / r^2

Dirección de la fuerza:

- Si q1 y q2 tienen el mismo signo, se repelen.
- Si q1 y q2 tienen signo contrario, se atraen.
- La fuerza actúa sobre la línea que une las cargas.

Importante:
La fórmula con valor absoluto da el módulo. La dirección se decide con un dibujo.

================================================================================
3. PRINCIPIO DE SUPERPOSICIÓN
================================================================================

Si una carga recibe fuerzas de varias cargas, la fuerza total no se calcula con una
fórmula nueva. Se suman vectorialmente todas las fuerzas:

F_total = F1 + F2 + F3 + ...

Esto también se aplica al campo eléctrico:

E_total = E1 + E2 + E3 + ...

En ejercicios con varias cargas:
1. Dibuja cada fuerza o campo por separado.
2. Calcula su módulo.
3. Descompón en componentes x, y, z si hace falta.
4. Suma componentes.
5. Calcula módulo y dirección del resultado si lo piden.

Consejo:
Si hay simetría, muchas componentes se cancelan. No empieces calculando a ciegas:
mira primero el dibujo.

================================================================================
4. CAMPO ELÉCTRICO
================================================================================

El campo eléctrico se define como la fuerza eléctrica por unidad de carga de prueba
positiva:

E = F / q0

Esto significa:
- El campo no es la fuerza.
- El campo te dice qué fuerza sentiría una carga positiva colocada ahí.
- Si después pones una carga q en ese campo, la fuerza será F = qE.

Campo creado por una carga puntual:

E = k |q| / r^2

Dirección:
- Si la carga fuente q es positiva, el campo sale de ella.
- Si la carga fuente q es negativa, el campo entra hacia ella.

Relación con Coulomb:
Si una carga q crea un campo en el punto donde colocas q0:

F = k |q q0| / r^2

y como E = F/q0:

E = k |q| / r^2

Por eso el campo de una carga puntual sale directamente de Coulomb.

================================================================================
5. LÍNEAS DE CAMPO ELÉCTRICO
================================================================================

Las líneas de campo son una forma visual de representar el campo eléctrico.

Reglas:
- Salen de cargas positivas.
- Entran en cargas negativas.
- Cuanto más juntas están, más intenso es el campo.
- El vector E en un punto es tangente a la línea de campo.
- Las líneas de campo no se cruzan.

Consejo:
Si te piden dirección cualitativa del campo, dibujar líneas de campo ayuda muchísimo.

================================================================================
6. POTENCIAL ELÉCTRICO
================================================================================

El potencial eléctrico V es energía potencial por unidad de carga:

V = U / q

Para una carga puntual:

V = k q / r

Diferencia clave con el campo:
- E es vector.
- V es escalar.

Por eso, si hay varias cargas:

V_total = V1 + V2 + V3 + ...

Aquí no se descompone en componentes. Solo se suman signos y valores.

Relación con energía:

U = q V
Delta U = q Delta V

Relación con trabajo:
El trabajo del campo eléctrico está relacionado con el cambio de energía potencial:

W_campo = - Delta U

Si mueves una carga lentamente con un agente externo, el trabajo externo puede ser:

W_ext = Delta U

Consejo:
Si el problema te pide trabajo, energía, velocidad o diferencia de potencial, piensa
en potencial eléctrico, no solo en fuerza.

================================================================================
7. SUPERFICIES EQUIPOTENCIALES
================================================================================

Una superficie equipotencial es una superficie donde el potencial tiene el mismo valor.

Características:
- Mover una carga sobre una equipotencial no requiere trabajo del campo.
- El campo eléctrico es perpendicular a las superficies equipotenciales.
- Para una carga puntual, las equipotenciales son esferas centradas en la carga.
- Cerca de una carga positiva, V es positivo; cerca de una carga negativa, V es negativo.

Relación importante:
El campo eléctrico apunta hacia donde el potencial disminuye más rápidamente.

================================================================================
8. FLUJO ELÉCTRICO
================================================================================

El flujo eléctrico mide cuántas líneas de campo atraviesan una superficie.

Para campo uniforme y superficie plana:

Phi_E = E A cos(theta)

donde:
- E es el campo.
- A es el área.
- theta es el ángulo entre E y el vector normal de la superficie.

Casos típicos:
- Si E es perpendicular a la superficie: theta = 0, Phi = EA.
- Si E es paralelo a la superficie: theta = 90°, Phi = 0.
- Si el campo entra en una superficie cerrada puede contarse negativo según la
  orientación del vector área.

Consejo:
El ángulo se toma con la normal de la superficie, no con la superficie misma.

================================================================================
9. LEY DE GAUSS
================================================================================

La Ley de Gauss dice:

Phi_E = Q_enc / epsilon_0

En forma integral:

∮ E · dA = Q_enc / epsilon_0

Esta ley siempre es cierta, pero solo es fácil de usar para calcular E cuando hay
simetría.

Cuándo usar Gauss:
- Simetría esférica.
- Simetría cilíndrica.
- Plano infinito.
- Conductores en equilibrio electrostático.
- Cuando puedes elegir una superficie gaussiana donde E sea constante o donde
  partes del flujo sean cero.

No conviene usar Gauss para despejar E si:
- Las cargas están distribuidas de forma irregular.
- No hay simetría.
- E no tiene magnitud constante en la superficie elegida.

Superficies gaussianas típicas:
- Esfera para carga puntual o esfera cargada.
- Cilindro para línea infinita de carga.
- Caja/píldora gaussiana para plano infinito.

================================================================================
10. CONDUCTORES EN EQUILIBRIO ELECTROSTÁTICO
================================================================================

En un conductor en equilibrio electrostático:

- El campo eléctrico dentro del material conductor es cero.
- Toda carga neta reside en la superficie.
- La superficie del conductor es equipotencial.
- El campo justo fuera de la superficie es perpendicular a la superficie.
- Si hubiese componente tangencial de E, las cargas se moverían; por eso no puede
  haber componente tangencial en equilibrio.

Consejo:
Si el problema menciona conductor en equilibrio, piensa inmediatamente:
E dentro = 0.

================================================================================
11. CÓMO RECONOCER EL TIPO DE EJERCICIO
================================================================================

Si el enunciado dice:
"dos cargas separadas..."
→ Ley de Coulomb.

Si dice:
"campo eléctrico en un punto..."
→ Campo E, superposición, componentes.

Si dice:
"potencial en un punto..."
→ V = kq/r y suma escalar.

Si dice:
"trabajo para mover una carga..."
→ U=qV, Delta U=q Delta V, W=-Delta U.

Si dice:
"flujo a través de una superficie..."
→ Phi = EA cos(theta).

Si dice:
"superficie cerrada", "carga encerrada", "simetría esférica/cilíndrica/plana..."
→ Ley de Gauss.

Si dice:
"conductor en equilibrio..."
→ E interior cero, carga en superficie, equipotencial.

================================================================================
12. ERRORES TÍPICOS DEL TEMA
================================================================================

- Usar centímetros directamente sin convertir a metros.
- Usar microCoulomb directamente sin convertir a Coulomb.
- Sumar campos como escalares cuando son vectores.
- Sumar potenciales como vectores cuando son escalares.
- Olvidar el signo del potencial.
- Confundir fuerza eléctrica F con campo eléctrico E.
- Confundir el ángulo con la superficie y el ángulo con la normal en flujo.
- Usar Gauss sin simetría y pensar que siempre permite despejar E.
- No dibujar direcciones antes de calcular.
- Olvidar que una carga negativa siente fuerza en sentido contrario al campo.
""",

    "formulas": [
        {
            "nombre": "Ley de Coulomb",
            "idea_clave": "Calcula la fuerza eléctrica entre dos cargas puntuales.",
            "formula_base": "F = k |q1 q2| / r^2",
            "formula_principal": "F = (1/(4π epsilon_0)) |q1 q2| / r^2",
            "sale_de": [
                "Experimentalmente, la fuerza es proporcional al producto de las cargas.",
                "También es inversamente proporcional al cuadrado de la distancia.",
                "La constante de proporcionalidad en el vacío es k = 1/(4π epsilon_0)."
            ],
            "despejes": [
                "q1 = F r^2 / (k |q2|)",
                "q2 = F r^2 / (k |q1|)",
                "r = sqrt(k |q1 q2| / F)",
                "k = F r^2 / |q1 q2|",
                "epsilon_r = k |q1 q2| / (F r^2) si F=(k/epsilon_r)|q1q2|/r^2"
            ],
            "formulas_relacionadas": [
                "E = F/q0",
                "E = k |q|/r^2",
                "F = qE",
                "U = k q1 q2/r"
            ],
            "uso": "Se usa para encontrar la fuerza entre dos cargas puntuales.",
            "cuando_usarla": [
                "Cuando el problema habla de dos cargas separadas una distancia.",
                "Cuando pide atracción o repulsión.",
                "Cuando pide despejar distancia, carga o permitividad relativa.",
                "Cuando después necesitas sumar fuerzas de varias cargas."
            ],
            "procedimiento": [
                "Convierte cargas a C y distancias a m.",
                "Calcula el módulo con F=k|q1q2|/r².",
                "Decide dirección con signos: iguales repelen, opuestos atraen.",
                "Si hay varias cargas, repite para cada interacción y suma vectorialmente."
            ],
            "detalles": [
                "La fuerza sobre q1 y la fuerza sobre q2 tienen el mismo módulo y sentidos opuestos.",
                "La fórmula con valor absoluto da módulo; el signo se usa para dirección.",
                "En un medio material puede aparecer epsilon_r."
            ],
            "errores_tipicos": [
                "No convertir cm a m.",
                "No convertir μC a C.",
                "Usar r en vez de r².",
                "Decir atracción/repulsión sin mirar signos."
            ],
            "mini_ejemplo": {
                "enunciado": "q1=+1 μC, q2=+2.5 μC, r=5 cm. Calcula F.",
                "pasos": [
                    "q1=1e-6 C, q2=2.5e-6 C, r=0.05 m.",
                    "F=9e9(1e-6)(2.5e-6)/(0.05)^2.",
                    "F=9 N.",
                    "Como ambas son positivas, se repelen."
                ],
                "resultado": "F=9 N, repulsiva."
            }
        },
        {
            "nombre": "Fuerza eléctrica resultante por superposición",
            "idea_clave": "Cuando hay más de dos cargas, la fuerza total es suma vectorial.",
            "formula_base": "F_total = F_1 + F_2 + ...",
            "formula_principal": "F_total_x = ΣF_x,  F_total_y = ΣF_y",
            "sale_de": [
                "Cada carga ejerce su propia fuerza sobre la carga estudiada.",
                "La interacción eléctrica cumple superposición.",
                "Como la fuerza es vector, se suman componentes."
            ],
            "despejes": [
                "F_total = sqrt(F_x^2 + F_y^2)",
                "theta = atan(F_y/F_x)",
                "F_x = F cos(theta)",
                "F_y = F sin(theta)"
            ],
            "formulas_relacionadas": [
                "F = k |q1 q2|/r^2",
                "E_total = E_1 + E_2 + ...",
                "E_x = ΣE_x, E_y = ΣE_y"
            ],
            "uso": "Resolver problemas de tres o más cargas donde piden fuerza neta.",
            "cuando_usarla": [
                "Cuando una carga recibe fuerza de varias cargas.",
                "Cuando el enunciado dice fuerza resultante.",
                "Cuando hay triángulos o geometría 2D."
            ],
            "procedimiento": [
                "Elige la carga sobre la que actúan las fuerzas.",
                "Dibuja cada fuerza individual.",
                "Calcula cada módulo con Coulomb.",
                "Descompón en x/y si no están en la misma línea.",
                "Suma componentes y calcula módulo final."
            ],
            "errores_tipicos": [
                "Sumar módulos directamente aunque las fuerzas no estén alineadas.",
                "Olvidar que una fuerza atractiva apunta hacia la otra carga.",
                "Equivocarse con seno/coseno al descomponer."
            ]
        },
        {
            "nombre": "Definición de campo eléctrico",
            "idea_clave": "El campo eléctrico es fuerza por unidad de carga positiva de prueba.",
            "formula_base": "E = F / q0",
            "formula_principal": "F = q E",
            "sale_de": [
                "Se introduce una carga de prueba q0 pequeña y positiva.",
                "Se mide la fuerza F que sentiría.",
                "El campo se define como E=F/q0 para describir el efecto de las cargas fuente sin depender de q0."
            ],
            "despejes": [
                "F = q0 E",
                "q0 = F/E",
                "E = F/q0"
            ],
            "formulas_relacionadas": [
                "E = k |q|/r²",
                "F = k |q q0|/r²",
                "E_total = ΣE_i"
            ],
            "uso": "Relacionar fuerza y campo eléctrico.",
            "cuando_usarla": [
                "Cuando ya conoces E y te piden fuerza sobre una carga.",
                "Cuando conoces F y q y te piden E.",
                "Cuando quieres distinguir campo producido por fuentes y fuerza sobre una carga concreta."
            ],
            "procedimiento": [
                "Identifica si la carga que te dan es fuente o carga de prueba.",
                "Si te piden fuerza sobre q, usa F=qE.",
                "Si q es negativa, la fuerza va en sentido contrario a E."
            ],
            "errores_tipicos": [
                "Confundir E con F.",
                "Olvidar que para q negativa la fuerza invierte dirección.",
                "Usar q fuente en F=qE cuando realmente q debe ser la carga que siente la fuerza."
            ]
        },
        {
            "nombre": "Campo eléctrico de una carga puntual",
            "idea_clave": "Campo creado por una carga fuente q a distancia r.",
            "formula_base": "E = F/q0",
            "formula_principal": "E = k |q| / r²",
            "sale_de": [
                "La fuerza de Coulomb entre q y una carga de prueba q0 es F=k|q q0|/r².",
                "Por definición, E=F/q0.",
                "Al dividir por q0 queda E=k|q|/r²."
            ],
            "despejes": [
                "q = E r²/k",
                "r = sqrt(k |q|/E)",
                "k = E r²/|q|"
            ],
            "formulas_relacionadas": [
                "F = q0 E",
                "F = k |q q0|/r²",
                "V = k q/r"
            ],
            "uso": "Calcular el campo creado por una carga puntual.",
            "cuando_usarla": [
                "Cuando hay una carga fuente y un punto de observación.",
                "Cuando te piden campo debido a una carga.",
                "Cuando luego debes sumar campos de varias cargas."
            ],
            "procedimiento": [
                "Dibuja la carga y el punto.",
                "Calcula r.",
                "Calcula módulo E=k|q|/r².",
                "Decide dirección: sale de +, entra en -."
            ],
            "detalles": [
                "El campo no depende de la carga de prueba.",
                "El signo de q decide la dirección.",
                "El módulo siempre es positivo."
            ],
            "errores_tipicos": [
                "Usar q0 además de q en la fórmula del campo.",
                "Sumar campos sin componentes.",
                "Olvidar que el campo de una carga negativa apunta hacia la carga."
            ]
        },
        {
            "nombre": "Campo eléctrico total por varias cargas",
            "idea_clave": "El campo total se obtiene sumando vectores E.",
            "formula_base": "E_total = E1 + E2 + ...",
            "formula_principal": "E_total = Σ k q_i r_i_hat / r_i²",
            "sale_de": [
                "Cada carga produce un campo en el punto.",
                "Los campos cumplen superposición.",
                "Como E es vector, se suman componentes."
            ],
            "despejes": [
                "E_total_x = ΣE_ix",
                "E_total_y = ΣE_iy",
                "|E_total| = sqrt(E_x² + E_y²)",
                "theta = atan(E_y/E_x)"
            ],
            "formulas_relacionadas": [
                "E = k|q|/r²",
                "F = q0 E_total",
                "V_total = ΣV_i"
            ],
            "uso": "Calcular campo neto en un punto debido a varias cargas.",
            "cuando_usarla": [
                "Cuando hay dos o más cargas.",
                "Cuando el punto P recibe campos de varias fuentes.",
                "Cuando aparece una configuración con simetría."
            ],
            "procedimiento": [
                "Calcula el campo de cada carga en P.",
                "Dibuja la dirección de cada E.",
                "Descompón en componentes.",
                "Suma componentes.",
                "Calcula módulo y dirección final."
            ],
            "errores_tipicos": [
                "Sumar módulos aunque los vectores tengan direcciones distintas.",
                "Confundir campo con potencial.",
                "No aprovechar simetría para cancelar componentes."
            ]
        },
        {
            "nombre": "Campo nulo entre o alrededor de cargas",
            "idea_clave": "Para encontrar dónde E=0, igualas campos opuestos.",
            "formula_base": "E_total = 0",
            "formula_principal": "k |q1|/r1² = k |q2|/r2²",
            "sale_de": [
                "Para que el campo neto sea cero, los campos deben tener igual módulo y sentidos opuestos.",
                "En una línea, se pueden igualar módulos si ya decidiste la región correcta.",
                "La constante k suele cancelarse."
            ],
            "despejes": [
                "|q1|/r1² = |q2|/r2²",
                "sqrt(|q1|)/r1 = sqrt(|q2|)/r2",
                "r1/r2 = sqrt(|q1|/|q2|)"
            ],
            "formulas_relacionadas": [
                "E = k|q|/r²",
                "F_total = 0",
                "Superposición vectorial"
            ],
            "uso": "Encontrar puntos donde el campo eléctrico se anula.",
            "cuando_usarla": [
                "Cuando el enunciado dice punto donde el campo es cero.",
                "Cuando hay dos cargas en un eje.",
                "Cuando se busca equilibrio eléctrico de una carga de prueba."
            ],
            "procedimiento": [
                "Divide el eje en regiones.",
                "Dibuja dirección del campo de cada carga en cada región.",
                "Descarta regiones donde los campos van en el mismo sentido.",
                "En la región posible, iguala módulos.",
                "Resuelve la ecuación."
            ],
            "errores_tipicos": [
                "Igualar módulos sin comprobar direcciones.",
                "Elegir la región incorrecta.",
                "Olvidar que entre cargas iguales del mismo signo sí puede haber cancelación."
            ]
        },
        {
            "nombre": "Potencial eléctrico de una carga puntual",
            "idea_clave": "El potencial es una magnitud escalar asociada a una carga fuente.",
            "formula_base": "V = U/q0",
            "formula_principal": "V = k q / r",
            "sale_de": [
                "El potencial se define como energía potencial por unidad de carga.",
                "La energía potencial de dos cargas puntuales es U=k q q0/r.",
                "Al dividir por q0 queda V=kq/r."
            ],
            "despejes": [
                "q = V r/k",
                "r = k q/V",
                "U = q0 V",
                "Delta U = q0 Delta V"
            ],
            "formulas_relacionadas": [
                "U = qV",
                "E = k|q|/r²",
                "W_campo = -Delta U",
                "V_total = ΣV_i"
            ],
            "uso": "Calcular potencial creado por una carga puntual.",
            "cuando_usarla": [
                "Cuando te piden potencial en un punto.",
                "Cuando hay varias cargas y quieres sumar escalares.",
                "Cuando luego necesitas energía o trabajo."
            ],
            "procedimiento": [
                "Calcula distancia r desde la carga al punto.",
                "Usa V=kq/r con signo de q.",
                "Si hay varias cargas, suma algebraicamente cada V."
            ],
            "detalles": [
                "El potencial puede ser positivo, negativo o cero.",
                "No tiene dirección.",
                "Es más sencillo que el campo porque no requiere componentes."
            ],
            "errores_tipicos": [
                "Usar valor absoluto de q cuando el signo sí importa.",
                "Intentar descomponer potencial en componentes.",
                "Confundir V de potencial con V de voltaje en circuitos; físicamente están conectados, pero el contexto importa."
            ]
        },
        {
            "nombre": "Potencial total por varias cargas",
            "idea_clave": "El potencial total se suma algebraicamente, no vectorialmente.",
            "formula_base": "V_total = V1 + V2 + ...",
            "formula_principal": "V_total = Σ k q_i/r_i",
            "sale_de": [
                "El potencial es escalar.",
                "Cada carga contribuye con V_i=kq_i/r_i.",
                "La superposición escalar permite sumar directamente con signos."
            ],
            "despejes": [
                "V_total = k(q1/r1 + q2/r2 + ...)",
                "Si V_total=0: Σ q_i/r_i = 0",
                "U = q0 V_total"
            ],
            "formulas_relacionadas": [
                "V = kq/r",
                "U = qV",
                "E_total = ΣE_i"
            ],
            "uso": "Calcular potencial neto en un punto por varias cargas.",
            "cuando_usarla": [
                "Cuando hay varias cargas y te piden potencial.",
                "Cuando te piden energía de una carga en ese punto.",
                "Cuando buscas puntos de potencial cero."
            ],
            "procedimiento": [
                "Calcula r_i desde cada carga hasta el punto.",
                "Calcula V_i=kq_i/r_i con su signo.",
                "Suma todos los V_i."
            ],
            "errores_tipicos": [
                "Sumar potencial como vector.",
                "Ignorar signos de cargas negativas.",
                "Confundir punto donde V=0 con punto donde E=0."
            ]
        },
        {
            "nombre": "Energía potencial eléctrica de dos cargas",
            "idea_clave": "Energía asociada a la posición relativa de dos cargas.",
            "formula_base": "U = q V",
            "formula_principal": "U = k q1 q2 / r",
            "sale_de": [
                "El potencial creado por q1 en la posición de q2 es V=kq1/r.",
                "La energía de q2 en ese potencial es U=q2V.",
                "Entonces U=kq1q2/r."
            ],
            "despejes": [
                "q1 = U r/(k q2)",
                "q2 = U r/(k q1)",
                "r = k q1 q2/U",
                "Delta U = q Delta V"
            ],
            "formulas_relacionadas": [
                "V = kq/r",
                "U = qV",
                "W_campo = -Delta U"
            ],
            "uso": "Resolver problemas de energía y trabajo con cargas puntuales.",
            "cuando_usarla": [
                "Cuando te piden trabajo para acercar o separar cargas.",
                "Cuando hay energía potencial eléctrica.",
                "Cuando comparas posiciones inicial y final."
            ],
            "procedimiento": [
                "Calcula U_i y U_f.",
                "Calcula Delta U=U_f-U_i.",
                "Trabajo del campo: W_campo=-Delta U.",
                "Trabajo externo lento: W_ext=Delta U."
            ],
            "errores_tipicos": [
                "Usar valor absoluto cuando el signo de U importa.",
                "Confundir trabajo del campo con trabajo externo.",
                "Olvidar que cargas opuestas tienen U negativa."
            ]
        },
        {
            "nombre": "Trabajo eléctrico y diferencia de potencial",
            "idea_clave": "El trabajo está relacionado con el cambio de potencial y energía.",
            "formula_base": "Delta U = q Delta V",
            "formula_principal": "W_campo = -q Delta V",
            "sale_de": [
                "La energía potencial de una carga en un potencial es U=qV.",
                "El cambio de energía es Delta U=q(V_f-V_i).",
                "El trabajo del campo eléctrico reduce la energía potencial: W_campo=-Delta U."
            ],
            "despejes": [
                "Delta V = Delta U/q",
                "q = Delta U/Delta V",
                "W_ext = q Delta V si el movimiento es lento",
                "V_f = V_i + Delta V"
            ],
            "formulas_relacionadas": [
                "U = qV",
                "V = kq/r",
                "K_i + U_i = K_f + U_f si no hay fuerzas no conservativas"
            ],
            "uso": "Resolver ejercicios de trabajo, energía o movimiento entre potenciales.",
            "cuando_usarla": [
                "Cuando se mueve una carga entre dos puntos.",
                "Cuando preguntan trabajo del campo o de un agente externo.",
                "Cuando aparece diferencia de potencial."
            ],
            "procedimiento": [
                "Identifica punto inicial y final.",
                "Calcula Delta V=V_f-V_i.",
                "Calcula Delta U=qDelta V.",
                "Decide si piden trabajo del campo o trabajo externo."
            ],
            "errores_tipicos": [
                "Cambiar el signo de Delta V.",
                "Confundir W_campo con W_externo.",
                "Olvidar el signo de q."
            ]
        },
        {
            "nombre": "Relación entre campo eléctrico y potencial uniforme",
            "idea_clave": "En un campo uniforme, el campo se relaciona con la caída de potencial.",
            "formula_base": "E = -Delta V / Delta s",
            "formula_principal": "Delta V = - E d si el desplazamiento va en la dirección de E",
            "sale_de": [
                "El campo eléctrico apunta hacia donde el potencial disminuye.",
                "En una dimensión, E_x = -dV/dx.",
                "Si E es uniforme, la derivada se convierte en cociente: E=-Delta V/Delta x."
            ],
            "despejes": [
                "Delta V = -E d",
                "E = |Delta V|/d",
                "d = |Delta V|/E"
            ],
            "formulas_relacionadas": [
                "F=qE",
                "Delta U=qDelta V",
                "Trabajo W_campo=qE d si el desplazamiento va con la fuerza"
            ],
            "uso": "Campos uniformes, placas paralelas y diferencias de potencial.",
            "cuando_usarla": [
                "Cuando el problema menciona placas paralelas.",
                "Cuando el campo es uniforme.",
                "Cuando dan voltaje y separación."
            ],
            "procedimiento": [
                "Identifica la dirección del campo.",
                "Identifica la separación d entre equipotenciales o placas.",
                "Usa E=|Delta V|/d para módulo.",
                "Recuerda que E apunta hacia menor potencial."
            ],
            "errores_tipicos": [
                "Olvidar el signo menos conceptual.",
                "Confundir distancia total con desplazamiento en dirección del campo.",
                "Usar esta fórmula en un campo no uniforme sin cuidado."
            ]
        },
        {
            "nombre": "Flujo eléctrico",
            "idea_clave": "Mide cuánto campo atraviesa una superficie.",
            "formula_base": "Phi_E = E A cos(theta)",
            "formula_principal": "Phi_E = ∫ E · dA",
            "sale_de": [
                "El flujo cuenta la componente del campo perpendicular a la superficie.",
                "Para campo uniforme y área plana, la componente normal es E cos(theta).",
                "Entonces Phi=EAcos(theta)."
            ],
            "despejes": [
                "E = Phi_E/(A cos(theta))",
                "A = Phi_E/(E cos(theta))",
                "cos(theta)=Phi_E/(EA)"
            ],
            "formulas_relacionadas": [
                "Ley de Gauss: Phi_E=Q_enc/epsilon_0",
                "E = kq/r²",
                "Área esfera: A=4πr²"
            ],
            "uso": "Calcular flujo a través de una superficie.",
            "cuando_usarla": [
                "Cuando el enunciado habla de superficie y campo uniforme.",
                "Cuando te piden líneas de campo atravesando un área.",
                "Antes de aplicar Gauss."
            ],
            "procedimiento": [
                "Identifica el vector normal a la superficie.",
                "Determina el ángulo theta entre E y la normal.",
                "Usa Phi=EAcos(theta).",
                "Aplica signo si la orientación importa."
            ],
            "detalles": [
                "Si E es paralelo a la superficie, no atraviesa la superficie: flujo cero.",
                "Si E es perpendicular a la superficie, flujo máximo.",
                "La unidad es N m²/C."
            ],
            "errores_tipicos": [
                "Usar el ángulo con la superficie en vez del ángulo con la normal.",
                "Olvidar que el flujo puede ser negativo.",
                "Confundir área real con área proyectada."
            ]
        },
        {
            "nombre": "Ley de Gauss",
            "idea_clave": "Relaciona flujo eléctrico total con carga encerrada.",
            "formula_base": "Phi_E = Q_enc / epsilon_0",
            "formula_principal": "∮ E · dA = Q_enc / epsilon_0",
            "sale_de": [
                "Para una carga puntual, E=kq/r².",
                "En una esfera centrada en la carga, E es radial y constante en módulo.",
                "El flujo es E(4πr²) = (1/(4πepsilon_0))(q/r²)(4πr²) = q/epsilon_0.",
                "La ley se generaliza a cualquier superficie cerrada."
            ],
            "despejes": [
                "Q_enc = epsilon_0 Phi_E",
                "E = Q_enc/(epsilon_0 A) si E es constante y perpendicular",
                "E = Q_enc/(epsilon_0 4πr²) para simetría esférica",
                "E = lambda/(2πepsilon_0 r) para línea infinita",
                "E = sigma/(2epsilon_0) para plano infinito aislado"
            ],
            "formulas_relacionadas": [
                "Phi_E = EAcos(theta)",
                "Área esfera = 4πr²",
                "Área lateral cilindro = 2πrL",
                "E conductor interior = 0"
            ],
            "uso": "Calcular campo eléctrico cuando hay simetría.",
            "cuando_usarla": [
                "Cuando hay esfera, cilindro o plano infinito.",
                "Cuando se menciona superficie gaussiana.",
                "Cuando piden carga encerrada a partir del flujo.",
                "Cuando hay conductor en equilibrio."
            ],
            "procedimiento": [
                "Identifica la simetría.",
                "Elige superficie gaussiana adecuada.",
                "Determina Q_enc.",
                "Simplifica el flujo: partes con E constante y partes con flujo cero.",
                "Despeja E."
            ],
            "detalles": [
                "Gauss siempre es verdadera, pero no siempre ayuda a calcular E.",
                "Solo la carga encerrada cuenta para el flujo neto.",
                "Cargas fuera de la superficie pueden cambiar E localmente, pero no el flujo neto total."
            ],
            "errores_tipicos": [
                "Usar Q total en vez de Q encerrada.",
                "Elegir una superficie gaussiana sin simetría.",
                "Pensar que flujo cero implica E cero en todos los puntos.",
                "Olvidar que la superficie debe ser cerrada en Ley de Gauss."
            ]
        },
        {
            "nombre": "Campo de una esfera/carga con simetría esférica",
            "idea_clave": "Fuera de una distribución esférica, el campo se comporta como si toda la carga estuviera en el centro.",
            "formula_base": "∮E·dA = Q_enc/epsilon_0",
            "formula_principal": "E = Q_enc/(4πepsilon_0 r²)",
            "sale_de": [
                "Se elige una superficie gaussiana esférica de radio r.",
                "Por simetría, E tiene el mismo módulo en toda la esfera y es radial.",
                "El flujo es E(4πr²).",
                "Igualando a Q_enc/epsilon_0 se obtiene E=Q_enc/(4πepsilon_0 r²)."
            ],
            "despejes": [
                "Q_enc = E 4πepsilon_0 r²",
                "r = sqrt(Q_enc/(4πepsilon_0 E))"
            ],
            "formulas_relacionadas": [
                "E = kQ/r²",
                "k = 1/(4πepsilon_0)",
                "Phi_E = Q_enc/epsilon_0"
            ],
            "uso": "Esferas cargadas, cargas puntuales, cortezas esféricas y conductores esféricos.",
            "cuando_usarla": [
                "Cuando la distribución tiene simetría esférica.",
                "Cuando se pide E a distancia r del centro.",
                "Cuando una esfera conductora se trata desde fuera."
            ],
            "procedimiento": [
                "Distingue si el punto está dentro o fuera.",
                "Calcula Q_enc para ese radio.",
                "Usa E(4πr²)=Q_enc/epsilon_0.",
                "Despeja E."
            ],
            "errores_tipicos": [
                "Usar carga total aunque el punto esté dentro de una distribución volumétrica.",
                "No distinguir conductor de aislante uniformemente cargado.",
                "Olvidar que dentro de un conductor en equilibrio E=0."
            ]
        },
        {
            "nombre": "Campo de línea infinita de carga",
            "idea_clave": "Para una línea infinita, la superficie gaussiana natural es un cilindro.",
            "formula_base": "∮E·dA = Q_enc/epsilon_0",
            "formula_principal": "E = lambda/(2πepsilon_0 r)",
            "sale_de": [
                "La simetría cilíndrica indica que E es radial y depende solo de r.",
                "Se elige un cilindro de radio r y longitud L.",
                "El flujo por las tapas es cero porque E es paralelo a ellas.",
                "El flujo lateral es E(2πrL).",
                "La carga encerrada es lambda L.",
                "Entonces E(2πrL)=lambda L/epsilon_0."
            ],
            "despejes": [
                "lambda = E 2πepsilon_0 r",
                "r = lambda/(2πepsilon_0 E)"
            ],
            "formulas_relacionadas": [
                "Q=lambda L",
                "Área lateral cilindro=2πrL",
                "Ley de Gauss"
            ],
            "uso": "Campo eléctrico de líneas largas de carga.",
            "cuando_usarla": [
                "Cuando el enunciado dice línea infinita o cable largo cargado.",
                "Cuando hay simetría cilíndrica.",
                "Cuando te dan densidad lineal lambda."
            ],
            "procedimiento": [
                "Escoge cilindro coaxial con la línea.",
                "Calcula Q_enc=lambda L.",
                "Usa solo el área lateral para el flujo.",
                "Despeja E."
            ],
            "errores_tipicos": [
                "Usar área de esfera en vez de cilindro.",
                "Incluir flujo por las tapas.",
                "Confundir lambda con densidad superficial sigma."
            ]
        },
        {
            "nombre": "Campo de plano infinito cargado",
            "idea_clave": "Para un plano infinito, el campo es perpendicular al plano y constante.",
            "formula_base": "∮E·dA = Q_enc/epsilon_0",
            "formula_principal": "E = sigma/(2epsilon_0) para una lámina infinita aislada",
            "sale_de": [
                "La simetría indica que E es perpendicular al plano por ambos lados.",
                "Se usa una caja gaussiana tipo píldora que atraviesa el plano.",
                "El flujo lateral es cero.",
                "Hay flujo por dos tapas: 2EA.",
                "La carga encerrada es sigma A.",
                "Entonces 2EA=sigma A/epsilon_0."
            ],
            "despejes": [
                "sigma = 2epsilon_0 E",
                "E = sigma/(2epsilon_0)",
                "Para conductor justo fuera: E=sigma/epsilon_0"
            ],
            "formulas_relacionadas": [
                "Phi_E = Q_enc/epsilon_0",
                "Q=sigma A",
                "Campo entre placas paralelas ideal: E≈sigma/epsilon_0"
            ],
            "uso": "Láminas infinitas, placas grandes y superficies con simetría plana.",
            "cuando_usarla": [
                "Cuando aparece plano infinito.",
                "Cuando una lámina tiene densidad superficial sigma.",
                "Cuando se usa una superficie gaussiana en forma de caja."
            ],
            "procedimiento": [
                "Dibuja el campo perpendicular al plano.",
                "Elige una caja gaussiana cruzando la lámina.",
                "Suma flujo de las dos tapas.",
                "Iguala a sigma A/epsilon_0."
            ],
            "errores_tipicos": [
                "Olvidar el factor 2 para una lámina aislada.",
                "Confundir lámina aislada con conductor.",
                "Usar r aunque el campo de plano infinito no depende de r."
            ]
        },
        {
            "nombre": "Conductor en equilibrio electrostático",
            "idea_clave": "En un conductor en equilibrio, el campo dentro del material conductor es cero.",
            "formula_base": "E_interior = 0",
            "formula_principal": "E_justo_fuera = sigma/epsilon_0",
            "sale_de": [
                "Si hubiera campo dentro del conductor, las cargas libres se moverían.",
                "En equilibrio, las cargas ya no se mueven; por tanto E interior debe ser cero.",
                "Usando Gauss en una caja pequeña que atraviesa la superficie, se obtiene E=sigma/epsilon_0 justo fuera."
            ],
            "despejes": [
                "sigma = epsilon_0 E",
                "Phi_E interior = 0 si no hay carga encerrada en cavidad",
                "V constante en el conductor"
            ],
            "formulas_relacionadas": [
                "Ley de Gauss",
                "E = -dV/ds",
                "Superficie equipotencial"
            ],
            "uso": "Problemas de conductores, esferas conductoras, cavidades y equilibrio electrostático.",
            "cuando_usarla": [
                "Cuando se menciona conductor en equilibrio.",
                "Cuando te preguntan campo dentro de un conductor.",
                "Cuando se pregunta dónde queda la carga neta."
            ],
            "procedimiento": [
                "Escribe E=0 dentro del conductor.",
                "Indica que la carga neta queda en la superficie.",
                "Si se pide campo externo, usa simetría o Gauss.",
                "Recuerda que la superficie es equipotencial."
            ],
            "errores_tipicos": [
                "Pensar que dentro de una esfera conductora cargada hay campo.",
                "Confundir conductor con aislante uniformemente cargado.",
                "Olvidar que el campo externo es perpendicular a la superficie."
            ]
        }
    ],

    "interpretacion_enunciados": [
        {
            "palabra_clave": "dos cargas separadas",
            "que_significa": "Normalmente piden fuerza eléctrica por Ley de Coulomb.",
            "que_suele_pedir": [
                "Módulo de la fuerza.",
                "Si la fuerza es atractiva o repulsiva.",
                "Distancia necesaria para una fuerza dada.",
                "Carga desconocida.",
                "Permitividad relativa del medio."
            ],
            "operaciones_recomendadas": [
                "Convierte todas las unidades a SI.",
                "Usa F=k|q1q2|/r².",
                "Si hay medio, usa F=(k/epsilon_r)|q1q2|/r².",
                "Decide atracción/repulsión con los signos.",
                "Haz un dibujo de la línea que une las cargas."
            ],
            "pista_examen": "Si solo aparecen q1, q2 y r, casi seguro es Coulomb."
        },
        {
            "palabra_clave": "fuerza resultante sobre una carga",
            "que_significa": "Hay varias fuerzas eléctricas actuando sobre una misma carga.",
            "que_suele_pedir": [
                "Fuerza neta.",
                "Componentes de la fuerza.",
                "Módulo y dirección final.",
                "Equilibrio de una carga."
            ],
            "operaciones_recomendadas": [
                "Elige la carga sobre la que actúan las fuerzas.",
                "Dibuja cada fuerza por separado.",
                "Calcula cada módulo con Coulomb.",
                "Descompón en componentes.",
                "Suma vectorialmente."
            ],
            "pista_examen": "La palabra resultante casi siempre significa suma vectorial."
        },
        {
            "palabra_clave": "campo eléctrico en un punto",
            "que_significa": "Te piden E en un punto del espacio, no fuerza sobre una carga necesariamente.",
            "que_suele_pedir": [
                "Campo debido a una carga.",
                "Campo total por varias cargas.",
                "Punto donde el campo se anula.",
                "Dirección del campo."
            ],
            "operaciones_recomendadas": [
                "Calcula E de cada carga.",
                "Dibuja dirección: sale de +, entra en -.",
                "Descompón en componentes.",
                "Suma vectores."
            ],
            "pista_examen": "Campo eléctrico es vector; potencial eléctrico no."
        },
        {
            "palabra_clave": "punto donde el campo es cero",
            "que_significa": "Buscas una posición donde los campos se cancelan.",
            "que_suele_pedir": [
                "Coordenada x del punto.",
                "Región donde se anula E.",
                "Comparación entre cargas de distinto módulo."
            ],
            "operaciones_recomendadas": [
                "Divide el eje en regiones.",
                "Dibuja direcciones de E en cada región.",
                "Descarta regiones donde los campos tienen el mismo sentido.",
                "Iguala módulos donde puedan oponerse.",
                "Resuelve la ecuación."
            ],
            "pista_examen": "No empieces igualando fórmulas sin decidir primero dónde los campos son opuestos."
        },
        {
            "palabra_clave": "potencial eléctrico en un punto",
            "que_significa": "Te piden V, que es una magnitud escalar.",
            "que_suele_pedir": [
                "Potencial debido a una carga.",
                "Potencial total por varias cargas.",
                "Punto donde V=0.",
                "Energía de una carga colocada allí."
            ],
            "operaciones_recomendadas": [
                "Usa V=kq/r con signo.",
                "Suma algebraicamente los potenciales.",
                "No uses componentes.",
                "Si luego piden energía, usa U=qV."
            ],
            "pista_examen": "Potencial se suma mucho más fácil que campo porque no tiene dirección."
        },
        {
            "palabra_clave": "trabajo para mover una carga",
            "que_significa": "El problema va de energía potencial y diferencia de potencial.",
            "que_suele_pedir": [
                "Trabajo del campo.",
                "Trabajo externo.",
                "Cambio de energía potencial.",
                "Velocidad final por conservación de energía."
            ],
            "operaciones_recomendadas": [
                "Calcula V_i y V_f.",
                "Calcula Delta V=V_f-V_i.",
                "Usa Delta U=qDelta V.",
                "Decide si piden W_campo=-Delta U o W_ext=Delta U."
            ],
            "pista_examen": "Cuidado con el signo de q y con si el trabajo lo hace el campo o un agente externo."
        },
        {
            "palabra_clave": "flujo eléctrico",
            "que_significa": "Te piden cuánto campo atraviesa una superficie.",
            "que_suele_pedir": [
                "Phi_E a través de una superficie plana.",
                "Flujo neto en una superficie cerrada.",
                "Ángulo entre campo y superficie/normal."
            ],
            "operaciones_recomendadas": [
                "Identifica la normal de la superficie.",
                "Usa theta entre E y la normal.",
                "Para superficie plana y E uniforme usa Phi=EAcos(theta).",
                "Para superficie cerrada piensa en Gauss."
            ],
            "pista_examen": "El ángulo de la fórmula es con la normal, no con el plano."
        },
        {
            "palabra_clave": "superficie cerrada / carga encerrada",
            "que_significa": "Probablemente debes usar Ley de Gauss.",
            "que_suele_pedir": [
                "Flujo total.",
                "Carga encerrada.",
                "Campo con simetría.",
                "Campo en conductores."
            ],
            "operaciones_recomendadas": [
                "Identifica Q_enc.",
                "Usa Phi=Q_enc/epsilon_0.",
                "Si hay simetría, escribe el flujo como E por área.",
                "Despeja E."
            ],
            "pista_examen": "En Gauss solo cuenta la carga encerrada para el flujo neto."
        },
        {
            "palabra_clave": "esfera / cilindro / plano infinito",
            "que_significa": "El problema tiene simetría y probablemente quiere Gauss.",
            "que_suele_pedir": [
                "Campo eléctrico en función de r.",
                "Campo dentro/fuera.",
                "Carga encerrada.",
                "Densidad de carga."
            ],
            "operaciones_recomendadas": [
                "Esfera: superficie gaussiana esférica.",
                "Cilindro/línea: superficie gaussiana cilíndrica.",
                "Plano: caja gaussiana tipo píldora.",
                "Calcula Q_enc según la región."
            ],
            "pista_examen": "La superficie gaussiana se elige para que el flujo sea fácil, no porque sea una superficie física."
        },
        {
            "palabra_clave": "conductor en equilibrio",
            "que_significa": "Las cargas libres ya se acomodaron y no se mueven.",
            "que_suele_pedir": [
                "Campo dentro del conductor.",
                "Dónde está la carga neta.",
                "Potencial del conductor.",
                "Campo justo fuera de la superficie."
            ],
            "operaciones_recomendadas": [
                "Escribe E=0 dentro del conductor.",
                "Indica que la carga neta queda en la superficie.",
                "La superficie es equipotencial.",
                "El campo externo es perpendicular a la superficie."
            ],
            "pista_examen": "Si el conductor está en equilibrio electrostático, el campo dentro del material conductor es cero."
        }
    ],

    "flashcards": [
        {"id": "fis1_fc_001", "frente": "¿Qué pasa con dos cargas del mismo signo?", "reverso": "Se repelen.", "categoria": "Carga eléctrica"},
        {"id": "fis1_fc_002", "frente": "¿Qué pasa con dos cargas de signo opuesto?", "reverso": "Se atraen.", "categoria": "Carga eléctrica"},
        {"id": "fis1_fc_003", "frente": "¿Cuál es la fórmula de Coulomb?", "reverso": "F=k|q1q2|/r².", "categoria": "Coulomb"},
        {"id": "fis1_fc_004", "frente": "¿Qué significa k en Coulomb?", "reverso": "La constante de Coulomb: k≈8.99e9 N·m²/C².", "categoria": "Coulomb"},
        {"id": "fis1_fc_005", "frente": "¿Qué debes hacer siempre antes de usar Coulomb?", "reverso": "Convertir cargas a C y distancias a m.", "categoria": "Unidades"},
        {"id": "fis1_fc_006", "frente": "¿El campo eléctrico es vector o escalar?", "reverso": "Vector.", "categoria": "Campo eléctrico"},
        {"id": "fis1_fc_007", "frente": "¿El potencial eléctrico es vector o escalar?", "reverso": "Escalar.", "categoria": "Potencial"},
        {"id": "fis1_fc_008", "frente": "¿De dónde salen las líneas de campo eléctrico?", "reverso": "Salen de cargas positivas y entran en cargas negativas.", "categoria": "Campo eléctrico"},
        {"id": "fis1_fc_009", "frente": "¿Definición de campo eléctrico?", "reverso": "E=F/q0.", "categoria": "Campo eléctrico"},
        {"id": "fis1_fc_010", "frente": "¿Fuerza sobre una carga q en un campo E?", "reverso": "F=qE.", "categoria": "Campo eléctrico"},
        {"id": "fis1_fc_011", "frente": "¿Campo creado por una carga puntual?", "reverso": "E=k|q|/r².", "categoria": "Campo eléctrico"},
        {"id": "fis1_fc_012", "frente": "Si q es negativa, ¿F=qE va en el mismo sentido que E?", "reverso": "No, va en sentido contrario.", "categoria": "Campo eléctrico"},
        {"id": "fis1_fc_013", "frente": "¿Cómo se suman campos eléctricos?", "reverso": "Vectorialmente, por componentes.", "categoria": "Superposición"},
        {"id": "fis1_fc_014", "frente": "¿Cómo se suman potenciales eléctricos?", "reverso": "Algebraicamente como escalares.", "categoria": "Potencial"},
        {"id": "fis1_fc_015", "frente": "¿Potencial de una carga puntual?", "reverso": "V=kq/r.", "categoria": "Potencial"},
        {"id": "fis1_fc_016", "frente": "¿Relación entre energía potencial y potencial?", "reverso": "U=qV.", "categoria": "Energía"},
        {"id": "fis1_fc_017", "frente": "¿Trabajo del campo eléctrico?", "reverso": "W_campo=-Delta U=-q Delta V.", "categoria": "Trabajo"},
        {"id": "fis1_fc_018", "frente": "¿Flujo eléctrico en campo uniforme?", "reverso": "Phi_E=EAcos(theta).", "categoria": "Flujo"},
        {"id": "fis1_fc_019", "frente": "En flujo, ¿theta es con la superficie o con la normal?", "reverso": "Con la normal.", "categoria": "Flujo"},
        {"id": "fis1_fc_020", "frente": "¿Ley de Gauss?", "reverso": "Phi_E=Q_enc/epsilon_0.", "categoria": "Gauss"},
        {"id": "fis1_fc_021", "frente": "¿Cuándo conviene usar Gauss?", "reverso": "Con simetría esférica, cilíndrica o plana.", "categoria": "Gauss"},
        {"id": "fis1_fc_022", "frente": "¿Qué carga cuenta en Gauss?", "reverso": "La carga encerrada por la superficie cerrada.", "categoria": "Gauss"},
        {"id": "fis1_fc_023", "frente": "¿Campo dentro de un conductor en equilibrio?", "reverso": "E=0.", "categoria": "Conductores"},
        {"id": "fis1_fc_024", "frente": "¿Dónde está la carga neta de un conductor en equilibrio?", "reverso": "En la superficie.", "categoria": "Conductores"},
        {"id": "fis1_fc_025", "frente": "¿La superficie de un conductor en equilibrio es equipotencial?", "reverso": "Sí.", "categoria": "Conductores"},
        {"id": "fis1_fc_026", "frente": "¿Campo de línea infinita de carga?", "reverso": "E=lambda/(2πepsilon_0 r).", "categoria": "Gauss"},
        {"id": "fis1_fc_027", "frente": "¿Campo de plano infinito aislado?", "reverso": "E=sigma/(2epsilon_0).", "categoria": "Gauss"},
        {"id": "fis1_fc_028", "frente": "¿Qué superficie gaussiana usas para una carga puntual?", "reverso": "Una esfera centrada en la carga.", "categoria": "Gauss"},
        {"id": "fis1_fc_029", "frente": "¿Qué superficie gaussiana usas para una línea infinita?", "reverso": "Un cilindro coaxial.", "categoria": "Gauss"},
        {"id": "fis1_fc_030", "frente": "¿Qué superficie gaussiana usas para un plano infinito?", "reverso": "Una caja/píldora gaussiana.", "categoria": "Gauss"}
    ],

    "preguntas_vf": [
        {"id": "fis1_vf_001", "pregunta": "Cargas del mismo signo se atraen.", "respuesta": False, "explicacion": "Cargas del mismo signo se repelen.", "categoria": "Carga eléctrica", "dificultad": "facil"},
        {"id": "fis1_vf_002", "pregunta": "Cargas de signo opuesto se atraen.", "respuesta": True, "explicacion": "Es la regla básica de interacción eléctrica.", "categoria": "Carga eléctrica", "dificultad": "facil"},
        {"id": "fis1_vf_003", "pregunta": "La fuerza de Coulomb disminuye con r².", "respuesta": True, "explicacion": "F es inversamente proporcional al cuadrado de la distancia.", "categoria": "Coulomb", "dificultad": "facil"},
        {"id": "fis1_vf_004", "pregunta": "Si duplicas la distancia entre dos cargas, la fuerza se duplica.", "respuesta": False, "explicacion": "Si r se duplica, F se divide entre 4.", "categoria": "Coulomb", "dificultad": "facil"},
        {"id": "fis1_vf_005", "pregunta": "La fuerza eléctrica es una magnitud vectorial.", "respuesta": True, "explicacion": "Tiene módulo, dirección y sentido.", "categoria": "Coulomb", "dificultad": "facil"},
        {"id": "fis1_vf_006", "pregunta": "En una fuerza resultante, puedes sumar siempre solo los módulos.", "respuesta": False, "explicacion": "Solo si las fuerzas están en la misma línea y con signos. En general se suman vectores.", "categoria": "Superposición", "dificultad": "media"},
        {"id": "fis1_vf_007", "pregunta": "El campo eléctrico se define como E=F/q0.", "respuesta": True, "explicacion": "Es fuerza por unidad de carga de prueba positiva.", "categoria": "Campo eléctrico", "dificultad": "facil"},
        {"id": "fis1_vf_008", "pregunta": "El campo de una carga positiva apunta hacia la carga.", "respuesta": False, "explicacion": "Sale de la carga positiva.", "categoria": "Campo eléctrico", "dificultad": "facil"},
        {"id": "fis1_vf_009", "pregunta": "El campo de una carga negativa apunta hacia la carga.", "respuesta": True, "explicacion": "Las líneas de campo entran en cargas negativas.", "categoria": "Campo eléctrico", "dificultad": "facil"},
        {"id": "fis1_vf_010", "pregunta": "Si una carga q negativa está en un campo E, la fuerza va en sentido contrario a E.", "respuesta": True, "explicacion": "F=qE; si q<0, invierte dirección.", "categoria": "Campo eléctrico", "dificultad": "facil"},
        {"id": "fis1_vf_011", "pregunta": "El potencial eléctrico es una magnitud vectorial.", "respuesta": False, "explicacion": "El potencial es escalar.", "categoria": "Potencial", "dificultad": "facil"},
        {"id": "fis1_vf_012", "pregunta": "Los potenciales de varias cargas se suman algebraicamente.", "respuesta": True, "explicacion": "V es escalar, por eso se suman con signo.", "categoria": "Potencial", "dificultad": "facil"},
        {"id": "fis1_vf_013", "pregunta": "El campo eléctrico y el potencial eléctrico se suman de la misma manera.", "respuesta": False, "explicacion": "E se suma vectorialmente; V se suma escalarmente.", "categoria": "Potencial", "dificultad": "media"},
        {"id": "fis1_vf_014", "pregunta": "Un punto donde V=0 necesariamente tiene E=0.", "respuesta": False, "explicacion": "Potencial cero y campo cero no son lo mismo.", "categoria": "Potencial", "dificultad": "media"},
        {"id": "fis1_vf_015", "pregunta": "La energía potencial eléctrica cumple U=qV.", "respuesta": True, "explicacion": "Es la relación entre energía potencial y potencial.", "categoria": "Energía", "dificultad": "facil"},
        {"id": "fis1_vf_016", "pregunta": "El trabajo del campo eléctrico es W_campo=-Delta U.", "respuesta": True, "explicacion": "Para fuerzas conservativas, el trabajo del campo reduce la energía potencial.", "categoria": "Trabajo", "dificultad": "media"},
        {"id": "fis1_vf_017", "pregunta": "El flujo eléctrico usa el ángulo entre E y la superficie.", "respuesta": False, "explicacion": "La fórmula usa el ángulo entre E y la normal a la superficie.", "categoria": "Flujo", "dificultad": "media"},
        {"id": "fis1_vf_018", "pregunta": "Si E es paralelo a una superficie plana, el flujo a través de ella es cero.", "respuesta": True, "explicacion": "No atraviesa la superficie; theta con la normal es 90°.", "categoria": "Flujo", "dificultad": "facil"},
        {"id": "fis1_vf_019", "pregunta": "La Ley de Gauss dice que el flujo neto depende de la carga encerrada.", "respuesta": True, "explicacion": "Phi_E=Q_enc/epsilon_0.", "categoria": "Gauss", "dificultad": "facil"},
        {"id": "fis1_vf_020", "pregunta": "Gauss solo es verdadera para esferas.", "respuesta": False, "explicacion": "La ley es general; lo que cambia es si ayuda a despejar E fácilmente.", "categoria": "Gauss", "dificultad": "media"},
        {"id": "fis1_vf_021", "pregunta": "Para una línea infinita de carga conviene usar una superficie gaussiana cilíndrica.", "respuesta": True, "explicacion": "La simetría es cilíndrica.", "categoria": "Gauss", "dificultad": "facil"},
        {"id": "fis1_vf_022", "pregunta": "Para un plano infinito cargado, el campo depende de la distancia al plano.", "respuesta": False, "explicacion": "Idealmente el campo de un plano infinito no depende de la distancia.", "categoria": "Gauss", "dificultad": "media"},
        {"id": "fis1_vf_023", "pregunta": "Dentro de un conductor en equilibrio electrostático, E=0.", "respuesta": True, "explicacion": "Si hubiera campo, las cargas libres se moverían.", "categoria": "Conductores", "dificultad": "facil"},
        {"id": "fis1_vf_024", "pregunta": "La carga neta de un conductor en equilibrio se queda en el volumen interior.", "respuesta": False, "explicacion": "Se distribuye en la superficie.", "categoria": "Conductores", "dificultad": "media"},
        {"id": "fis1_vf_025", "pregunta": "La superficie de un conductor en equilibrio es equipotencial.", "respuesta": True, "explicacion": "Si no lo fuera, habría campo tangencial y las cargas se moverían.", "categoria": "Conductores", "dificultad": "media"},
        {"id": "fis1_vf_026", "pregunta": "Si una superficie cerrada encierra carga neta cero, el flujo neto es cero.", "respuesta": True, "explicacion": "Por Gauss, Phi=Q_enc/epsilon_0.", "categoria": "Gauss", "dificultad": "media"},
        {"id": "fis1_vf_027", "pregunta": "Flujo neto cero siempre significa campo eléctrico cero en toda la superficie.", "respuesta": False, "explicacion": "Puede haber campo entrando y saliendo con flujo neto cero.", "categoria": "Gauss", "dificultad": "dificil"},
        {"id": "fis1_vf_028", "pregunta": "La fuerza eléctrica entre dos cargas cumple acción-reacción: mismos módulos y sentidos opuestos.", "respuesta": True, "explicacion": "Son fuerzas de interacción entre dos cuerpos.", "categoria": "Coulomb", "dificultad": "facil"},
        {"id": "fis1_vf_029", "pregunta": "En el vacío, k≈9e9 N m²/C².", "respuesta": True, "explicacion": "Es el valor aproximado habitual.", "categoria": "Coulomb", "dificultad": "facil"},
        {"id": "fis1_vf_030", "pregunta": "Si el medio tiene epsilon_r mayor que 1, la fuerza eléctrica disminuye respecto al vacío.", "respuesta": True, "explicacion": "En el modelo simple, F=(k/epsilon_r)|q1q2|/r².", "categoria": "Coulomb", "dificultad": "media"}
    ],

    "preguntas_mc": [
        {
            "id": "fis1_mc_001",
            "pregunta": "¿Qué fórmula usas para la fuerza entre dos cargas puntuales?",
            "opciones": ["F=k|q1q2|/r²", "E=V/d", "Phi=EAcos(theta)", "U=qV"],
            "respuesta": 1,
            "explicacion": "La interacción entre dos cargas puntuales se calcula con Coulomb.",
            "categoria": "Coulomb",
            "dificultad": "facil"
        },
        {
            "id": "fis1_mc_002",
            "pregunta": "Dos cargas positivas se:",
            "opciones": ["Atraen", "Repelen", "Anulan", "No interactúan"],
            "respuesta": 2,
            "explicacion": "Cargas del mismo signo se repelen.",
            "categoria": "Carga eléctrica",
            "dificultad": "facil"
        },
        {
            "id": "fis1_mc_003",
            "pregunta": "Si r se duplica, la fuerza de Coulomb:",
            "opciones": ["Se duplica", "Se divide entre 2", "Se divide entre 4", "No cambia"],
            "respuesta": 3,
            "explicacion": "F es proporcional a 1/r².",
            "categoria": "Coulomb",
            "dificultad": "facil"
        },
        {
            "id": "fis1_mc_004",
            "pregunta": "¿Qué unidad debes usar para μC antes de sustituir en Coulomb?",
            "opciones": ["Dejar μC igual", "Convertir a C", "Convertir a N", "Convertir a V"],
            "respuesta": 2,
            "explicacion": "El Sistema Internacional usa Coulomb.",
            "categoria": "Unidades",
            "dificultad": "facil"
        },
        {
            "id": "fis1_mc_005",
            "pregunta": "¿Cuál es la definición de campo eléctrico?",
            "opciones": ["E=F/q0", "E=qV", "E=IR", "E=Phi/A"],
            "respuesta": 1,
            "explicacion": "El campo es fuerza por unidad de carga de prueba.",
            "categoria": "Campo eléctrico",
            "dificultad": "facil"
        },
        {
            "id": "fis1_mc_006",
            "pregunta": "El campo eléctrico creado por una carga positiva:",
            "opciones": ["Entra hacia la carga", "Sale de la carga", "Siempre es cero", "Gira alrededor de la carga"],
            "respuesta": 2,
            "explicacion": "Las líneas de campo salen de cargas positivas.",
            "categoria": "Campo eléctrico",
            "dificultad": "facil"
        },
        {
            "id": "fis1_mc_007",
            "pregunta": "Si una carga negativa se coloca en un campo E, la fuerza sobre ella:",
            "opciones": ["Va en el mismo sentido que E", "Va en sentido contrario a E", "Siempre es cero", "No depende de E"],
            "respuesta": 2,
            "explicacion": "F=qE y q es negativa.",
            "categoria": "Campo eléctrico",
            "dificultad": "facil"
        },
        {
            "id": "fis1_mc_008",
            "pregunta": "Si hay varias cargas y piden campo total, debes:",
            "opciones": ["Sumar módulos siempre", "Sumar vectorialmente", "Sumar potenciales", "Usar solo la carga más grande"],
            "respuesta": 2,
            "explicacion": "El campo eléctrico es vector.",
            "categoria": "Superposición",
            "dificultad": "facil"
        },
        {
            "id": "fis1_mc_009",
            "pregunta": "El potencial eléctrico de una carga puntual es:",
            "opciones": ["V=kq/r", "V=kq/r²", "V=F/q", "V=IR"],
            "respuesta": 1,
            "explicacion": "El potencial de una carga puntual decae como 1/r.",
            "categoria": "Potencial",
            "dificultad": "facil"
        },
        {
            "id": "fis1_mc_010",
            "pregunta": "Los potenciales de varias cargas se suman:",
            "opciones": ["Vectorialmente", "Algebraicamente", "Solo si son positivos", "Con producto vectorial"],
            "respuesta": 2,
            "explicacion": "El potencial es escalar.",
            "categoria": "Potencial",
            "dificultad": "facil"
        },
        {
            "id": "fis1_mc_011",
            "pregunta": "Si te piden energía potencial de una carga q en un potencial V, usas:",
            "opciones": ["U=qV", "U=IR", "U=EA", "U=q/E"],
            "respuesta": 1,
            "explicacion": "La energía potencial eléctrica cumple U=qV.",
            "categoria": "Energía",
            "dificultad": "facil"
        },
        {
            "id": "fis1_mc_012",
            "pregunta": "El flujo eléctrico para campo uniforme y área plana es:",
            "opciones": ["Phi=EAcos(theta)", "Phi=E/A", "Phi=qV", "Phi=kq/r"],
            "respuesta": 1,
            "explicacion": "Solo cuenta la componente normal del campo.",
            "categoria": "Flujo",
            "dificultad": "facil"
        },
        {
            "id": "fis1_mc_013",
            "pregunta": "En Phi=EAcos(theta), theta es el ángulo entre:",
            "opciones": ["E y la superficie", "E y la normal a la superficie", "q y E", "V y E"],
            "respuesta": 2,
            "explicacion": "El área vectorial es perpendicular a la superficie.",
            "categoria": "Flujo",
            "dificultad": "media"
        },
        {
            "id": "fis1_mc_014",
            "pregunta": "La Ley de Gauss es:",
            "opciones": ["Phi_E=Q_enc/epsilon_0", "F=qvB", "V=IR", "B=mu0I/2πr"],
            "respuesta": 1,
            "explicacion": "Relaciona flujo neto con carga encerrada.",
            "categoria": "Gauss",
            "dificultad": "facil"
        },
        {
            "id": "fis1_mc_015",
            "pregunta": "¿Cuál es la mejor pista para usar Gauss para despejar E?",
            "opciones": ["No hay simetría", "Hay simetría esférica/cilíndrica/plana", "Hay una batería", "Hay una resistencia"],
            "respuesta": 2,
            "explicacion": "Gauss simplifica cuando el flujo se puede expresar fácilmente.",
            "categoria": "Gauss",
            "dificultad": "facil"
        },
        {
            "id": "fis1_mc_016",
            "pregunta": "Para una carga puntual, la superficie gaussiana más útil es:",
            "opciones": ["Cubo cualquiera", "Esfera centrada en la carga", "Cilindro desplazado", "Plano abierto"],
            "respuesta": 2,
            "explicacion": "La simetría de una carga puntual es esférica.",
            "categoria": "Gauss",
            "dificultad": "facil"
        },
        {
            "id": "fis1_mc_017",
            "pregunta": "Para una línea infinita de carga, la superficie gaussiana natural es:",
            "opciones": ["Esfera", "Cilindro coaxial", "Triángulo", "Disco abierto"],
            "respuesta": 2,
            "explicacion": "La simetría es cilíndrica.",
            "categoria": "Gauss",
            "dificultad": "facil"
        },
        {
            "id": "fis1_mc_018",
            "pregunta": "Dentro de un conductor en equilibrio electrostático:",
            "opciones": ["E=0", "E es máximo", "V=0 siempre", "La carga está en el centro"],
            "respuesta": 1,
            "explicacion": "Si E no fuera cero, las cargas libres se moverían.",
            "categoria": "Conductores",
            "dificultad": "facil"
        },
        {
            "id": "fis1_mc_019",
            "pregunta": "La carga neta de un conductor en equilibrio se localiza en:",
            "opciones": ["El centro", "La superficie", "Todo el volumen uniformemente", "Ningún sitio"],
            "respuesta": 2,
            "explicacion": "En equilibrio electrostático, la carga neta reside en la superficie.",
            "categoria": "Conductores",
            "dificultad": "media"
        },
        {
            "id": "fis1_mc_020",
            "pregunta": "Si una superficie cerrada no encierra carga neta, su flujo neto es:",
            "opciones": ["Siempre positivo", "Siempre negativo", "Cero", "Infinito"],
            "respuesta": 3,
            "explicacion": "Por Gauss, Phi=Q_enc/epsilon_0=0.",
            "categoria": "Gauss",
            "dificultad": "media"
        },
        {
            "id": "fis1_mc_021",
            "pregunta": "La fórmula E=lambda/(2πepsilon_0 r) corresponde a:",
            "opciones": ["Carga puntual", "Línea infinita de carga", "Plano infinito", "Conductor sin carga"],
            "respuesta": 2,
            "explicacion": "Es el campo de una línea infinita con densidad lineal lambda.",
            "categoria": "Gauss",
            "dificultad": "media"
        },
        {
            "id": "fis1_mc_022",
            "pregunta": "La fórmula E=sigma/(2epsilon_0) corresponde idealmente a:",
            "opciones": ["Plano infinito aislado", "Carga puntual", "Hilo recto", "Circuito RC"],
            "respuesta": 1,
            "explicacion": "Se obtiene con una caja gaussiana atravesando la lámina.",
            "categoria": "Gauss",
            "dificultad": "media"
        },
        {
            "id": "fis1_mc_023",
            "pregunta": "Si un problema dice 'trabajo para llevar una carga de A a B', conviene pensar en:",
            "opciones": ["Diferencia de potencial", "Solo en Coulomb", "Ley de Ampère", "Resistencia equivalente"],
            "respuesta": 1,
            "explicacion": "Trabajo y energía se relacionan con Delta U=qDelta V.",
            "categoria": "Trabajo",
            "dificultad": "media"
        },
        {
            "id": "fis1_mc_024",
            "pregunta": "¿Qué afirmación es correcta?",
            "opciones": ["E y V siempre son cero en el mismo punto", "E es vector y V es escalar", "V se suma por componentes", "E no tiene dirección"],
            "respuesta": 2,
            "explicacion": "Esta diferencia es esencial en electrostática.",
            "categoria": "Conceptos",
            "dificultad": "facil"
        },
        {
            "id": "fis1_mc_025",
            "pregunta": "Si el campo eléctrico es perpendicular a una superficie plana y sale en la dirección de la normal, el flujo es:",
            "opciones": ["EA", "0", "-EA", "E/A"],
            "respuesta": 1,
            "explicacion": "theta=0, por tanto cos(theta)=1.",
            "categoria": "Flujo",
            "dificultad": "facil"
        }
    ]
}
