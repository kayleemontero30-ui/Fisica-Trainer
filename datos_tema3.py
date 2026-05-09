# -*- coding: utf-8 -*-

TEMA3 = {
    "nombre": "Tema 3 - Corriente, circuitos, capacitores e inducción",

    "resumen": """
TEMA 3 - CORRIENTE, CIRCUITOS, CAPACITORES E INDUCCIÓN

Este tema conecta la electrostática con circuitos reales: ya no miramos solo cargas
quietas, sino cargas moviéndose por conductores. Aparecen corriente, resistencia,
potencia, leyes de Kirchhoff, capacitores, circuitos RC y finalmente la idea de
inducción electromagnética.

================================================================================
1. CORRIENTE ELÉCTRICA
================================================================================

La corriente eléctrica mide cuánta carga atraviesa una sección por unidad de tiempo:

I = Δq/Δt

Si la corriente cambia con el tiempo:

I = dq/dt

Unidad:
- Ampere, A.
- 1 A = 1 C/s.

La corriente convencional se define como el movimiento de carga positiva. En metales,
los electrones se mueven en sentido contrario a la corriente convencional.

Ideas importantes:
- Corriente grande significa que pasa mucha carga por segundo.
- La corriente no se "gasta" al pasar por una resistencia.
- En un circuito en serie, la misma corriente atraviesa todos los elementos.
- En un nodo, la carga no se acumula normalmente; por eso entra la misma corriente
  total que sale.

================================================================================
2. DENSIDAD DE CORRIENTE Y VELOCIDAD DE DERIVA
================================================================================

La densidad de corriente J mide corriente por unidad de área:

J = I/A

También se relaciona con la velocidad de deriva de los portadores:

J = n q v_d

y por tanto:

I = n q A v_d

donde:
- n es el número de portadores por unidad de volumen.
- q es la carga de cada portador.
- v_d es la velocidad de deriva.
- A es el área transversal.

Aunque la señal eléctrica se propaga muy rápido, la velocidad de deriva de los
electrones en un conductor suele ser muy pequeña.

================================================================================
3. LEY DE OHM MICROSCÓPICA Y MACROSCÓPICA
================================================================================

Forma microscópica:

J = sigma E

donde sigma es la conductividad.

También se usa:

E = rho J

donde rho es la resistividad.

Forma macroscópica:

V = I R

La conexión entre ambas sale al considerar un conductor uniforme de longitud L y área A:

E = V/L
J = I/A
E = rho J

Entonces:

V/L = rho I/A

y por tanto:

V = I (rho L/A)

Así se obtiene:

R = rho L/A

================================================================================
4. RESISTENCIA Y RESISTIVIDAD
================================================================================

La resistencia mide oposición al paso de corriente:

R = V/I

Para un conductor uniforme:

R = rho L/A

donde:
- rho es la resistividad.
- L es la longitud del conductor.
- A es el área transversal.

Consecuencias:
- Si aumenta L, aumenta R.
- Si aumenta A, disminuye R.
- Un material con mayor rho tiene mayor resistencia para la misma geometría.

La resistividad puede depender de la temperatura:

rho = rho_0 [1 + alpha (T - T_0)]

En metales, normalmente la resistividad aumenta con la temperatura.

================================================================================
5. LEY DE OHM
================================================================================

Para un material óhmico:

V = I R

Esto significa que V e I son proporcionales y R es constante.

Cuidado:
No todos los dispositivos son óhmicos. Pero en muchos ejercicios básicos se asume
que las resistencias cumplen la Ley de Ohm.

Despejes básicos:
- I = V/R
- R = V/I

================================================================================
6. POTENCIA ELÉCTRICA Y EFECTO JOULE
================================================================================

La potencia eléctrica es energía por unidad de tiempo.

Fórmula base:

P = I V

Usando Ohm:

P = I² R
P = V²/R

Estas tres formas son equivalentes si el elemento es resistivo y cumple Ohm.

Uso:
- P=IV es la más general en circuitos DC simples.
- P=I²R conviene si sabes corriente y resistencia.
- P=V²/R conviene si sabes voltaje y resistencia.

Energía consumida:

E = P t

En unidades domésticas también aparece kWh.

================================================================================
7. RESISTENCIAS EN SERIE
================================================================================

Resistencias en serie están una detrás de otra, sin ramificaciones entre ellas.

Propiedad clave:
- La corriente es la misma en todas.

Resistencia equivalente:

R_eq = R1 + R2 + R3 + ...

El voltaje total se reparte:

V_total = V1 + V2 + V3 + ...

donde:

V_i = I R_i

Consejo:
Serie = misma corriente.

================================================================================
8. RESISTENCIAS EN PARALELO
================================================================================

Resistencias en paralelo están conectadas entre los mismos dos nodos.

Propiedad clave:
- Todas tienen el mismo voltaje.

Resistencia equivalente:

1/R_eq = 1/R1 + 1/R2 + 1/R3 + ...

Para dos resistencias:

R_eq = R1 R2/(R1 + R2)

La corriente total se reparte:

I_total = I1 + I2 + I3 + ...

donde:

I_i = V/R_i

Consejo:
Paralelo = mismo voltaje.

La resistencia equivalente en paralelo siempre es menor que la menor resistencia
individual.

================================================================================
9. LEYES DE KIRCHHOFF
================================================================================

Kirchhoff sirve para circuitos que no se pueden reducir directamente por serie/paralelo.

LEY DE NODOS:
La suma de corrientes que entran a un nodo es igual a la suma de corrientes que salen.

ΣI_entrantes = ΣI_salientes

También puede escribirse:

ΣI = 0

Es conservación de carga.

LEY DE MALLAS:
La suma de cambios de potencial alrededor de una malla cerrada es cero.

ΣΔV = 0

Es conservación de energía.

Reglas de signos habituales:
- Al atravesar una batería de - a +: +epsilon.
- Al atravesar una batería de + a -: -epsilon.
- Al atravesar una resistencia en el sentido de la corriente: -IR.
- Al atravesar una resistencia en contra de la corriente: +IR.

================================================================================
10. CAPACITORES
================================================================================

Un capacitor almacena carga y energía en un campo eléctrico.

Definición:

C = Q/V

donde:
- C es capacitancia.
- Q es carga.
- V es diferencia de potencial.

Unidad:
- Faradio, F.

Capacitor de placas paralelas ideal:

C = epsilon A/d

En vacío:

C = epsilon_0 A/d

Con dieléctrico:

C = kappa epsilon_0 A/d

o

C = kappa C_0

donde kappa es la constante dieléctrica.

Ideas:
- Mayor área A → mayor capacitancia.
- Mayor separación d → menor capacitancia.
- Dieléctrico aumenta la capacitancia.

================================================================================
11. CAPACITORES EN SERIE Y PARALELO
================================================================================

CAPACITORES EN PARALELO:
- Mismo voltaje.
- Cargas se suman.
- Capacitancia equivalente:

C_eq = C1 + C2 + C3 + ...

CAPACITORES EN SERIE:
- Misma carga.
- Voltajes se suman.
- Capacitancia equivalente:

1/C_eq = 1/C1 + 1/C2 + 1/C3 + ...

Para dos capacitores en serie:

C_eq = C1 C2/(C1 + C2)

Cuidado:
Las reglas son al revés que en resistencias:
- Resistencias serie se suman.
- Capacitores paralelo se suman.
- Resistencias paralelo usan inversos.
- Capacitores serie usan inversos.

================================================================================
12. ENERGÍA ALMACENADA EN UN CAPACITOR
================================================================================

La energía almacenada es:

U = 1/2 Q V

Usando C=Q/V, también:

U = 1/2 C V²

y:

U = Q²/(2C)

Densidad de energía en un campo eléctrico:

u = 1/2 epsilon E²

================================================================================
13. CIRCUITO RC: CARGA DE UN CAPACITOR
================================================================================

Un circuito RC tiene una resistencia R y un capacitor C.

Durante la carga con una batería de voltaje V:

q(t) = C V (1 - e^{-t/RC})

Voltaje del capacitor:

V_C(t) = V (1 - e^{-t/RC})

Corriente:

i(t) = (V/R) e^{-t/RC}

Constante de tiempo:

tau = RC

Interpretación:
- En t=tau, el capacitor alcanza aproximadamente 63% de la carga final.
- Después de unas 5 tau, se considera casi completamente cargado.
- Al inicio, el capacitor descargado se comporta como un cable ideal.
- Al final, cuando está cargado, se comporta como circuito abierto para DC.

================================================================================
14. CIRCUITO RC: DESCARGA DE UN CAPACITOR
================================================================================

Durante la descarga:

q(t) = Q_0 e^{-t/RC}

Voltaje:

V_C(t) = V_0 e^{-t/RC}

Corriente:

i(t) = -(V_0/R) e^{-t/RC}

El signo negativo indica que la corriente va en sentido contrario al de carga.

Interpretación:
- En t=tau queda aproximadamente 37% de la carga inicial.
- Después de unas 5 tau, se considera prácticamente descargado.

================================================================================
15. FLUJO MAGNÉTICO Y FARADAY
================================================================================

El flujo magnético es:

Phi_B = B A cos(theta)

La Ley de Faraday dice:

epsilon = -N dPhi_B/dt

donde:
- epsilon es la fem inducida.
- N es el número de espiras.
- Phi_B es el flujo magnético a través de una espira.

El signo negativo es la Ley de Lenz:
La corriente inducida se opone al cambio de flujo que la produce.

Puede cambiar el flujo si cambia:
- B,
- A,
- theta,
- o la orientación/posición de la espira.

================================================================================
16. LEY DE LENZ
================================================================================

Lenz te da el sentido de la corriente inducida.

Idea:
La corriente inducida crea un campo magnético que se opone al cambio de flujo.

Ejemplos:
- Si el flujo hacia dentro de la pantalla aumenta, la corriente inducida crea campo
  hacia fuera.
- Si el flujo hacia dentro disminuye, la corriente inducida crea campo hacia dentro.
- Si no cambia el flujo, no hay fem inducida.

================================================================================
17. INDUCTANCIA Y CIRCUITO RL
================================================================================

Si tu curso incluye inductores, la idea es que una bobina se opone a cambios de corriente.

Fem autoinducida:

epsilon_L = -L dI/dt

Energía en un inductor:

U = 1/2 L I²

Circuito RL al conectar batería:

I(t) = (V/R)(1 - e^{-tR/L})

Constante de tiempo:

tau = L/R

Al desconectar:

I(t) = I_0 e^{-tR/L}

Comparación con RC:
- RC tiene tau=RC.
- RL tiene tau=L/R.
- Capacitor se opone a cambios bruscos de voltaje.
- Inductor se opone a cambios bruscos de corriente.

================================================================================
18. CÓMO RECONOCER QUÉ HACER EN UN EJERCICIO
================================================================================

Si dice:
"carga que pasa en cierto tiempo"
→ corriente I=Δq/Δt.

Si dice:
"cable con longitud, área y resistividad"
→ R=rho L/A.

Si dice:
"voltaje, corriente y resistencia"
→ Ley de Ohm V=IR.

Si dice:
"potencia disipada"
→ P=IV, P=I²R o P=V²/R.

Si dice:
"resistencias una detrás de otra"
→ serie, misma corriente.

Si dice:
"resistencias conectadas a los mismos dos nodos"
→ paralelo, mismo voltaje.

Si dice:
"nodo"
→ Kirchhoff de corrientes.

Si dice:
"malla"
→ Kirchhoff de voltajes.

Si dice:
"capacitor"
→ C=Q/V; si hay placas, C=epsilon A/d.

Si dice:
"capacitor cargándose/descargándose en el tiempo"
→ circuito RC y exponenciales.

Si dice:
"flujo magnético cambiante"
→ Faraday-Lenz.

Si dice:
"bobina/inductor y cambio de corriente"
→ autoinducción, RL.

================================================================================
19. ERRORES TÍPICOS
================================================================================

- Confundir serie y paralelo.
- Pensar que en paralelo la corriente es igual en todas las ramas.
- Pensar que en serie el voltaje es igual en todos los elementos.
- Olvidar que la resistencia equivalente en paralelo es menor que la menor resistencia.
- Aplicar Kirchhoff sin elegir signos de forma consistente.
- Olvidar que capacitores tienen reglas opuestas a resistencias para serie/paralelo.
- Usar tau=RC para un circuito RL o tau=L/R para un RC.
- Olvidar el signo conceptual de Lenz.
- Usar el ángulo con la superficie en vez de con la normal para el flujo.
- No convertir unidades: mA a A, μF a F, cm² a m².
""",

    "formulas": [
        {
            "nombre": "Corriente eléctrica",
            "idea_clave": "La corriente mide cuánta carga pasa por una sección por unidad de tiempo.",
            "formula_base": "I = Δq/Δt",
            "formula_principal": "I = dq/dt",
            "sale_de": [
                "La corriente se define como tasa de flujo de carga.",
                "Si la carga pasa de forma aproximadamente constante, se usa I=Δq/Δt.",
                "Si cambia instantáneamente, se usa la derivada I=dq/dt."
            ],
            "despejes": [
                "Δq = I Δt",
                "Δt = Δq/I",
                "q(t) = ∫ I(t) dt"
            ],
            "formulas_relacionadas": [
                "J=I/A",
                "I=nqAv_d",
                "P=IV",
                "V=IR"
            ],
            "uso": "Calcular corriente, carga transferida o tiempo.",
            "cuando_usarla": [
                "Cuando el enunciado habla de carga que atraviesa una sección.",
                "Cuando dan tiempo y carga.",
                "Cuando piden cuántos electrones pasan por segundo."
            ],
            "procedimiento": [
                "Convierte carga a C y tiempo a s.",
                "Usa I=Δq/Δt.",
                "Si preguntan número de electrones, divide carga total entre e."
            ],
            "errores_tipicos": [
                "No convertir mA a A.",
                "Confundir corriente convencional con movimiento de electrones.",
                "Olvidar que 1 A = 1 C/s."
            ]
        },
        {
            "nombre": "Densidad de corriente",
            "idea_clave": "La densidad de corriente mide corriente por área.",
            "formula_base": "J = I/A",
            "formula_principal": "I = J A",
            "sale_de": [
                "Si una corriente I se reparte uniformemente por un área A, la corriente por unidad de área es J.",
                "Por tanto J=I/A.",
                "Si J no es uniforme, la corriente se obtiene integrando J·dA."
            ],
            "despejes": [
                "I = J A",
                "A = I/J"
            ],
            "formulas_relacionadas": [
                "J = nqv_d",
                "J = sigma E",
                "E = rho J"
            ],
            "uso": "Relacionar corriente con área transversal de un conductor.",
            "cuando_usarla": [
                "Cuando aparece área de un cable.",
                "Cuando te piden densidad de corriente.",
                "Cuando se conecta con resistividad o velocidad de deriva."
            ],
            "procedimiento": [
                "Calcula el área transversal.",
                "Usa J=I/A.",
                "Mantén unidades en m²."
            ],
            "errores_tipicos": [
                "Usar diámetro en vez de área.",
                "No convertir mm² o cm² a m².",
                "Olvidar que J es vector en general."
            ]
        },
        {
            "nombre": "Velocidad de deriva",
            "idea_clave": "Relaciona la corriente con el movimiento medio de los portadores de carga.",
            "formula_base": "I = n q A v_d",
            "formula_principal": "v_d = I/(n q A)",
            "sale_de": [
                "En un volumen A v_d Δt hay nA v_d Δt portadores.",
                "La carga que cruza la sección es Δq=nqA v_d Δt.",
                "Dividiendo por Δt se obtiene I=nqA v_d."
            ],
            "despejes": [
                "n = I/(qAv_d)",
                "q = I/(nAv_d)",
                "A = I/(nqv_d)"
            ],
            "formulas_relacionadas": [
                "J=I/A",
                "J=nqv_d",
                "I=Δq/Δt"
            ],
            "uso": "Calcular velocidad de deriva o densidad de portadores.",
            "cuando_usarla": [
                "Cuando el enunciado menciona portadores por volumen.",
                "Cuando preguntan velocidad media de electrones.",
                "Cuando se conecta corriente con movimiento microscópico."
            ],
            "procedimiento": [
                "Identifica n, q, A e I.",
                "Usa v_d=I/(nqA).",
                "Usa el valor absoluto de la carga para el módulo; el signo indica dirección."
            ],
            "errores_tipicos": [
                "Pensar que v_d es la velocidad de propagación de la señal.",
                "No convertir área a m².",
                "Confundir electrones con corriente convencional."
            ]
        },
        {
            "nombre": "Ley de Ohm microscópica",
            "idea_clave": "Relaciona densidad de corriente y campo eléctrico dentro del material.",
            "formula_base": "J = sigma E",
            "formula_principal": "E = rho J",
            "sale_de": [
                "En materiales óhmicos, la densidad de corriente es proporcional al campo aplicado.",
                "La constante de proporcionalidad es la conductividad sigma.",
                "La resistividad es rho=1/sigma, por eso E=rho J."
            ],
            "despejes": [
                "sigma = J/E",
                "E = J/sigma",
                "rho = E/J",
                "J = E/rho"
            ],
            "formulas_relacionadas": [
                "R=rho L/A",
                "V=IR",
                "J=I/A",
                "E=V/L"
            ],
            "uso": "Conectar la física microscópica del material con la resistencia macroscópica.",
            "cuando_usarla": [
                "Cuando aparecen conductividad o resistividad.",
                "Cuando se habla de campo eléctrico dentro de un conductor.",
                "Cuando se deriva R=rho L/A."
            ],
            "procedimiento": [
                "Identifica si te dan sigma o rho.",
                "Usa J=sigma E o E=rho J.",
                "Conecta con I/A y V/L si hay geometría."
            ],
            "errores_tipicos": [
                "Confundir conductividad sigma con densidad superficial de carga.",
                "Confundir rho resistividad con densidad de carga.",
                "Usar V=IR sin revisar si el problema pide forma microscópica."
            ]
        },
        {
            "nombre": "Resistencia de un conductor",
            "idea_clave": "La resistencia depende del material y de la geometría.",
            "formula_base": "R = rho L/A",
            "formula_principal": "R = rho L/A",
            "sale_de": [
                "De la ley microscópica E=rho J.",
                "Para conductor uniforme, E=V/L y J=I/A.",
                "Sustituyendo: V/L=rho I/A.",
                "Entonces V=I(rho L/A), y comparando con V=IR: R=rho L/A."
            ],
            "despejes": [
                "rho = RA/L",
                "L = RA/rho",
                "A = rho L/R"
            ],
            "formulas_relacionadas": [
                "V=IR",
                "J=I/A",
                "E=V/L",
                "rho(T)=rho_0[1+alpha(T-T_0)]"
            ],
            "uso": "Calcular resistencia de cables o conductores uniformes.",
            "cuando_usarla": [
                "Cuando dan longitud, área y resistividad.",
                "Cuando comparas cables de distinto grosor.",
                "Cuando te piden efecto de cambiar L o A."
            ],
            "procedimiento": [
                "Convierte L a m y A a m².",
                "Usa R=rho L/A.",
                "Si el área viene por radio, calcula A=πr²."
            ],
            "errores_tipicos": [
                "Usar diámetro como radio.",
                "No convertir mm² a m².",
                "Pensar que aumentar área aumenta resistencia."
            ]
        },
        {
            "nombre": "Dependencia de resistividad con temperatura",
            "idea_clave": "En metales, la resistividad suele aumentar con la temperatura.",
            "formula_base": "rho = rho_0[1 + alpha(T - T_0)]",
            "formula_principal": "R = R_0[1 + alpha(T - T_0)]",
            "sale_de": [
                "La resistividad del material cambia con temperatura.",
                "Si la geometría del conductor no cambia mucho, R es proporcional a rho.",
                "Por eso la misma relación lineal aproximada se aplica a R."
            ],
            "despejes": [
                "alpha = (R/R_0 - 1)/(T-T_0)",
                "T = T_0 + (R/R_0 - 1)/alpha",
                "R_0 = R/[1+alpha(T-T_0)]"
            ],
            "formulas_relacionadas": [
                "R=rho L/A",
                "V=IR",
                "P=I²R"
            ],
            "uso": "Problemas donde cambia la temperatura de un conductor.",
            "cuando_usarla": [
                "Cuando aparece coeficiente de temperatura alpha.",
                "Cuando piden resistencia a otra temperatura.",
                "Cuando comparas resistencia caliente/fría."
            ],
            "procedimiento": [
                "Identifica T0 y T.",
                "Calcula Delta T=T-T0.",
                "Sustituye en R=R0[1+alpha Delta T]."
            ],
            "errores_tipicos": [
                "Usar Celsius y Kelvin de forma inconsistente en diferencias; para Delta T son equivalentes.",
                "Olvidar que alpha puede ser negativo en algunos materiales.",
                "Aplicar la aproximación lineal fuera de rango sin cuidado."
            ]
        },
        {
            "nombre": "Ley de Ohm macroscópica",
            "idea_clave": "Relaciona voltaje, corriente y resistencia en un elemento óhmico.",
            "formula_base": "V = I R",
            "formula_principal": "V = I R",
            "sale_de": [
                "Para materiales óhmicos, J es proporcional a E.",
                "En un conductor uniforme eso lleva a V proporcional a I.",
                "La constante de proporcionalidad es R."
            ],
            "despejes": [
                "I = V/R",
                "R = V/I"
            ],
            "formulas_relacionadas": [
                "P=IV",
                "P=I²R",
                "P=V²/R",
                "R=rho L/A"
            ],
            "uso": "Resolver circuitos con resistencias óhmicas.",
            "cuando_usarla": [
                "Cuando conoces dos de V, I y R.",
                "Cuando calculas corriente en una resistencia.",
                "Cuando combinas con Kirchhoff."
            ],
            "procedimiento": [
                "Identifica el voltaje sobre esa resistencia.",
                "Identifica la resistencia.",
                "Usa I=V/R o V=IR según lo pedido."
            ],
            "errores_tipicos": [
                "Usar voltaje total en una resistencia que no está sola.",
                "Aplicar Ohm a elementos no óhmicos sin que el problema lo permita.",
                "Confundir resistencia equivalente con resistencia individual."
            ]
        },
        {
            "nombre": "Potencia eléctrica",
            "idea_clave": "La potencia mide energía transferida por unidad de tiempo.",
            "formula_base": "P = I V",
            "formula_principal": "P = I V = I²R = V²/R",
            "sale_de": [
                "La energía por carga es voltaje: V=E/q.",
                "La corriente es carga por tiempo: I=q/t.",
                "Potencia es energía por tiempo, por eso P=IV.",
                "Usando V=IR se obtienen P=I²R y P=V²/R."
            ],
            "despejes": [
                "I = P/V",
                "V = P/I",
                "R = P/I²",
                "R = V²/P",
                "E = Pt"
            ],
            "formulas_relacionadas": [
                "V=IR",
                "E=Pt",
                "R=rho L/A"
            ],
            "uso": "Calcular disipación en resistencias o consumo eléctrico.",
            "cuando_usarla": [
                "Cuando piden potencia disipada.",
                "Cuando aparece energía consumida en cierto tiempo.",
                "Cuando se habla de efecto Joule."
            ],
            "procedimiento": [
                "Escoge la forma según los datos disponibles.",
                "Para una resistencia, puedes usar P=I²R o P=V²/R.",
                "Para energía, multiplica por tiempo."
            ],
            "errores_tipicos": [
                "Usar V total para potencia de una resistencia individual sin verificar.",
                "Confundir W de watt con W de trabajo.",
                "No convertir horas a segundos si necesitas joules."
            ]
        },
        {
            "nombre": "Resistencias en serie",
            "idea_clave": "En serie, la corriente es la misma y las resistencias se suman.",
            "formula_base": "R_eq = R1 + R2 + ...",
            "formula_principal": "R_eq = ΣR_i",
            "sale_de": [
                "En serie, la misma corriente I atraviesa cada resistencia.",
                "El voltaje total es suma de caídas: V=V1+V2+...",
                "Como V_i=IR_i, entonces V=I(R1+R2+...).",
                "Comparando con V=IR_eq, se obtiene R_eq=R1+R2+..."
            ],
            "despejes": [
                "R_n = R_eq - ΣR_otros",
                "I = V_total/R_eq",
                "V_i = I R_i"
            ],
            "formulas_relacionadas": [
                "V=IR",
                "P=I²R",
                "Kirchhoff de mallas"
            ],
            "uso": "Reducir resistencias conectadas una detrás de otra.",
            "cuando_usarla": [
                "Cuando no hay nodos intermedios que dividan corriente.",
                "Cuando todos los elementos llevan la misma corriente.",
                "Cuando el circuito es una sola rama."
            ],
            "procedimiento": [
                "Identifica resistencias en una misma rama.",
                "Súmalas.",
                "Calcula corriente total si hay fuente.",
                "Calcula caídas de voltaje si se piden."
            ],
            "detalles": [
                "La resistencia equivalente es mayor que cada resistencia individual.",
                "El voltaje se reparte proporcionalmente a R."
            ],
            "errores_tipicos": [
                "Pensar que el voltaje es igual en todas en serie.",
                "No reconocer una bifurcación.",
                "Sumar resistencias que en realidad están en paralelo."
            ]
        },
        {
            "nombre": "Resistencias en paralelo",
            "idea_clave": "En paralelo, el voltaje es el mismo y las corrientes se suman.",
            "formula_base": "1/R_eq = 1/R1 + 1/R2 + ...",
            "formula_principal": "R_eq = R1R2/(R1+R2) para dos resistencias",
            "sale_de": [
                "En paralelo, cada rama tiene el mismo voltaje V.",
                "La corriente total es I=I1+I2+...",
                "Como I_i=V/R_i, entonces I=V(1/R1+1/R2+...).",
                "Comparando con I=V/R_eq, se obtiene 1/R_eq=Σ1/R_i."
            ],
            "despejes": [
                "Para dos: R_eq = R1R2/(R1+R2)",
                "I_total = V/R_eq",
                "I_i = V/R_i",
                "V = I_total R_eq"
            ],
            "formulas_relacionadas": [
                "Kirchhoff de nodos",
                "V=IR",
                "P=V²/R"
            ],
            "uso": "Reducir resistencias conectadas entre los mismos dos nodos.",
            "cuando_usarla": [
                "Cuando las resistencias comparten los dos nodos.",
                "Cuando todas tienen el mismo voltaje.",
                "Cuando la corriente se divide en ramas."
            ],
            "procedimiento": [
                "Identifica los nodos comunes.",
                "Aplica inversos para obtener R_eq.",
                "Usa el mismo V en cada rama.",
                "Calcula corrientes de rama con I_i=V/R_i."
            ],
            "detalles": [
                "La R_eq en paralelo es menor que la menor resistencia.",
                "La rama con menor R lleva mayor corriente."
            ],
            "errores_tipicos": [
                "Sumar directamente resistencias en paralelo.",
                "Pensar que la corriente es la misma en todas las ramas.",
                "Olvidar invertir al final."
            ]
        },
        {
            "nombre": "Kirchhoff de nodos",
            "idea_clave": "La corriente no se acumula en un nodo ideal.",
            "formula_base": "ΣI_entrantes = ΣI_salientes",
            "formula_principal": "ΣI = 0",
            "sale_de": [
                "La carga eléctrica se conserva.",
                "En un nodo ideal no se acumula carga con el tiempo.",
                "Por eso la corriente total que entra debe ser igual a la que sale."
            ],
            "despejes": [
                "I_desconocida = suma de corrientes opuestas según signos",
                "Si I1 entra e I2,I3 salen: I1=I2+I3"
            ],
            "formulas_relacionadas": [
                "I=Δq/Δt",
                "Resistencias en paralelo",
                "V=IR"
            ],
            "uso": "Resolver corrientes en circuitos con ramas.",
            "cuando_usarla": [
                "Cuando hay un nodo o unión.",
                "Cuando corrientes se dividen.",
                "Cuando no basta con serie/paralelo."
            ],
            "procedimiento": [
                "Elige signo para corrientes entrantes/salientes.",
                "Escribe la ecuación de conservación.",
                "Combina con Ohm si las corrientes dependen de voltajes."
            ],
            "errores_tipicos": [
                "No ser consistente con signos.",
                "Olvidar una rama.",
                "Pensar que una corriente desaparece en una resistencia."
            ]
        },
        {
            "nombre": "Kirchhoff de mallas",
            "idea_clave": "Al recorrer una malla cerrada, la suma de cambios de potencial es cero.",
            "formula_base": "ΣΔV = 0",
            "formula_principal": "Σepsilon - ΣIR = 0 en una malla simple",
            "sale_de": [
                "La energía se conserva.",
                "Al volver al punto de partida en una malla cerrada, el potencial final debe ser igual al inicial.",
                "Por eso la suma de subidas y caídas de potencial es cero."
            ],
            "despejes": [
                "I = Σepsilon/ΣR en una sola malla simple",
                "epsilon = ΣIR",
                "R_total = Σepsilon/I"
            ],
            "formulas_relacionadas": [
                "V=IR",
                "Potencia P=IV",
                "Reglas de signos de baterías y resistencias"
            ],
            "uso": "Resolver circuitos con una o varias mallas.",
            "cuando_usarla": [
                "Cuando hay circuitos cerrados.",
                "Cuando hay varias baterías.",
                "Cuando no puedes reducir por serie/paralelo.",
                "Cuando piden ecuaciones de malla."
            ],
            "procedimiento": [
                "Elige sentido de recorrido.",
                "Asigna sentidos de corriente.",
                "Suma subidas y caídas.",
                "En resistencia: -IR si recorres en sentido de la corriente.",
                "En batería: +epsilon si vas de - a +."
            ],
            "errores_tipicos": [
                "Cambiar signos sin consistencia.",
                "Olvidar que una corriente asumida negativa solo indica sentido contrario.",
                "No incluir todas las resistencias de la malla."
            ]
        },
        {
            "nombre": "Capacitancia",
            "idea_clave": "La capacitancia mide cuánta carga almacena un capacitor por voltaje aplicado.",
            "formula_base": "C = Q/V",
            "formula_principal": "Q = C V",
            "sale_de": [
                "Experimentalmente, en un capacitor ideal la carga almacenada es proporcional a la diferencia de potencial.",
                "La constante de proporcionalidad es C.",
                "Por definición C=Q/V."
            ],
            "despejes": [
                "Q = C V",
                "V = Q/C"
            ],
            "formulas_relacionadas": [
                "U=1/2 QV",
                "C=epsilon A/d",
                "Capacitores en serie/paralelo"
            ],
            "uso": "Relacionar carga, voltaje y capacitancia.",
            "cuando_usarla": [
                "Cuando aparece un capacitor.",
                "Cuando piden carga almacenada.",
                "Cuando se da voltaje entre placas."
            ],
            "procedimiento": [
                "Convierte capacitancia a F.",
                "Usa Q=CV o V=Q/C.",
                "Cuida unidades como μF = 10^-6 F."
            ],
            "errores_tipicos": [
                "Confundir C de capacitancia con C de Coulomb.",
                "No convertir μF a F.",
                "Olvidar que Q en un capacitor representa magnitud de carga en cada placa."
            ]
        },
        {
            "nombre": "Capacitor de placas paralelas",
            "idea_clave": "La geometría y el dieléctrico determinan la capacitancia.",
            "formula_base": "C = epsilon A/d",
            "formula_principal": "C = kappa epsilon_0 A/d",
            "sale_de": [
                "Entre placas paralelas, el campo aproximado es E=sigma/epsilon.",
                "La diferencia de potencial es V=Ed.",
                "Como sigma=Q/A, entonces V=Qd/(epsilon A).",
                "Usando C=Q/V, resulta C=epsilon A/d."
            ],
            "despejes": [
                "A = Cd/epsilon",
                "d = epsilon A/C",
                "epsilon = Cd/A",
                "kappa = C/C0"
            ],
            "formulas_relacionadas": [
                "C=Q/V",
                "E=V/d",
                "U=1/2 CV²",
                "u=1/2 epsilon E²"
            ],
            "uso": "Calcular capacitancia de placas planas.",
            "cuando_usarla": [
                "Cuando hay dos placas paralelas.",
                "Cuando dan área, separación y dieléctrico.",
                "Cuando piden efecto de introducir un dieléctrico."
            ],
            "procedimiento": [
                "Convierte A y d a SI.",
                "Identifica epsilon=epsilon0 o kappa epsilon0.",
                "Usa C=epsilon A/d."
            ],
            "errores_tipicos": [
                "Usar cm² sin convertir a m².",
                "Confundir d con grosor de placa.",
                "Olvidar multiplicar por kappa si hay dieléctrico."
            ]
        },
        {
            "nombre": "Capacitores en paralelo",
            "idea_clave": "En paralelo, todos los capacitores tienen el mismo voltaje.",
            "formula_base": "C_eq = C1 + C2 + ...",
            "formula_principal": "C_eq = ΣC_i",
            "sale_de": [
                "En paralelo, cada capacitor tiene el mismo voltaje V.",
                "La carga total es Q=Q1+Q2+...",
                "Como Q_i=C_iV, entonces Q=V(C1+C2+...).",
                "Comparando con Q=C_eqV, se obtiene C_eq=ΣC_i."
            ],
            "despejes": [
                "C_n = C_eq - ΣC_otros",
                "Q_total = C_eq V",
                "Q_i = C_i V"
            ],
            "formulas_relacionadas": [
                "C=Q/V",
                "Energía U=1/2CV²",
                "Resistencias en serie/paralelo para comparar"
            ],
            "uso": "Reducir capacitores conectados entre los mismos dos nodos.",
            "cuando_usarla": [
                "Cuando los capacitores comparten voltaje.",
                "Cuando están conectados a los mismos dos nodos.",
                "Cuando se suman cargas."
            ],
            "procedimiento": [
                "Identifica los nodos comunes.",
                "Suma capacitancias.",
                "Usa mismo V para cada capacitor.",
                "Calcula cargas individuales si se pide."
            ],
            "errores_tipicos": [
                "Aplicar la regla de resistencias en paralelo.",
                "Pensar que la carga es igual en todos.",
                "No identificar correctamente los nodos."
            ]
        },
        {
            "nombre": "Capacitores en serie",
            "idea_clave": "En serie, todos los capacitores tienen la misma carga.",
            "formula_base": "1/C_eq = 1/C1 + 1/C2 + ...",
            "formula_principal": "C_eq = C1C2/(C1+C2) para dos capacitores",
            "sale_de": [
                "En serie, la misma magnitud de carga aparece en cada capacitor.",
                "El voltaje total es V=V1+V2+...",
                "Como V_i=Q/C_i, entonces V=Q(1/C1+1/C2+...).",
                "Comparando con V=Q/C_eq, resulta 1/C_eq=Σ1/C_i."
            ],
            "despejes": [
                "Para dos: C_eq=C1C2/(C1+C2)",
                "Q = C_eq V_total",
                "V_i = Q/C_i"
            ],
            "formulas_relacionadas": [
                "C=Q/V",
                "Energía en capacitores",
                "Kirchhoff de mallas"
            ],
            "uso": "Reducir capacitores conectados uno tras otro.",
            "cuando_usarla": [
                "Cuando la carga en cada capacitor es la misma.",
                "Cuando los voltajes se reparten.",
                "Cuando no hay ramificación entre capacitores."
            ],
            "procedimiento": [
                "Calcula C_eq con inversos.",
                "Calcula Q=C_eqV_total.",
                "Usa la misma Q para cada capacitor.",
                "Calcula V_i=Q/C_i."
            ],
            "errores_tipicos": [
                "Sumar capacitancias en serie directamente.",
                "Pensar que el voltaje es igual en todos.",
                "Olvidar invertir al final."
            ]
        },
        {
            "nombre": "Energía almacenada en un capacitor",
            "idea_clave": "Un capacitor almacena energía en su campo eléctrico.",
            "formula_base": "U = 1/2 Q V",
            "formula_principal": "U = 1/2 C V² = Q²/(2C)",
            "sale_de": [
                "Al cargar un capacitor, el voltaje aumenta desde 0 hasta V.",
                "El voltaje medio durante la carga es V/2.",
                "El trabajo para llevar carga Q es U=Q(V/2)=1/2QV.",
                "Usando Q=CV se obtienen las otras formas."
            ],
            "despejes": [
                "C = 2U/V²",
                "V = sqrt(2U/C)",
                "Q = sqrt(2CU)",
                "Q = 2U/V"
            ],
            "formulas_relacionadas": [
                "C=Q/V",
                "C=epsilon A/d",
                "u=1/2epsilon E²"
            ],
            "uso": "Calcular energía almacenada o liberada por capacitores.",
            "cuando_usarla": [
                "Cuando piden energía en un capacitor.",
                "Cuando comparas antes/después de conectar capacitores.",
                "Cuando aparece potencia o descarga."
            ],
            "procedimiento": [
                "Elige la forma según datos: Q,V,C.",
                "Sustituye unidades SI.",
                "Si hay varios capacitores, decide si piden energía total o individual."
            ],
            "errores_tipicos": [
                "Olvidar el factor 1/2.",
                "Usar C en microfaradios sin convertir.",
                "Confundir energía con carga."
            ]
        },
        {
            "nombre": "Circuito RC cargándose",
            "idea_clave": "Un capacitor no se carga instantáneamente; sigue una exponencial.",
            "formula_base": "tau = RC",
            "formula_principal": "q(t)=CV(1-e^{-t/RC})",
            "sale_de": [
                "Kirchhoff en la malla da V - iR - q/C = 0.",
                "Como i=dq/dt, queda una ecuación diferencial: R dq/dt + q/C = V.",
                "La solución con q(0)=0 es q(t)=CV(1-e^{-t/RC})."
            ],
            "despejes": [
                "V_C(t)=V(1-e^{-t/RC})",
                "i(t)=(V/R)e^{-t/RC}",
                "t = -RC ln(1 - q/(CV))",
                "tau=RC"
            ],
            "formulas_relacionadas": [
                "C=Q/V",
                "V=IR",
                "Kirchhoff de mallas",
                "Energía U=1/2CV²"
            ],
            "uso": "Resolver carga temporal de capacitores en circuitos RC.",
            "cuando_usarla": [
                "Cuando hay resistencia, capacitor y batería.",
                "Cuando el capacitor empieza descargado y se carga.",
                "Cuando aparece tiempo t y exponencial."
            ],
            "procedimiento": [
                "Calcula tau=RC.",
                "Identifica valor final Q_f=CV.",
                "Usa q(t)=Q_f(1-e^{-t/tau}).",
                "Para corriente usa i(t)=i0e^{-t/tau}."
            ],
            "detalles": [
                "En t=tau, q≈0.632Q_f.",
                "La corriente empieza máxima y decae.",
                "A largo tiempo, el capacitor se comporta como circuito abierto en DC."
            ],
            "errores_tipicos": [
                "Usar fórmula de descarga para carga.",
                "Olvidar que la corriente decrece durante la carga.",
                "Usar tau=R/C en vez de RC."
            ]
        },
        {
            "nombre": "Circuito RC descargándose",
            "idea_clave": "La carga de un capacitor descargándose decae exponencialmente.",
            "formula_base": "tau = RC",
            "formula_principal": "q(t)=Q0 e^{-t/RC}",
            "sale_de": [
                "Sin batería, Kirchhoff da iR + q/C = 0.",
                "Como i=dq/dt con signo según convención, se obtiene dq/dt=-q/(RC).",
                "La solución es q(t)=Q0e^{-t/RC}."
            ],
            "despejes": [
                "V_C(t)=V0e^{-t/RC}",
                "i(t)=-(V0/R)e^{-t/RC}",
                "t = -RC ln(q/Q0)",
                "tau=RC"
            ],
            "formulas_relacionadas": [
                "C=Q/V",
                "Energía U=1/2CV²",
                "Potencia en resistencia P=i²R"
            ],
            "uso": "Resolver descarga temporal de capacitores.",
            "cuando_usarla": [
                "Cuando el capacitor ya está cargado y se conecta a una resistencia.",
                "Cuando no hay batería durante la descarga.",
                "Cuando aparece decaimiento exponencial."
            ],
            "procedimiento": [
                "Identifica Q0 o V0.",
                "Calcula tau=RC.",
                "Usa q(t)=Q0e^{-t/tau}.",
                "Si piden corriente, considera el signo según sentido elegido."
            ],
            "detalles": [
                "En t=tau queda aproximadamente 37% de la carga inicial.",
                "Después de 5tau queda casi descargado.",
                "La energía termina disipándose en la resistencia."
            ],
            "errores_tipicos": [
                "Usar 1-e^{-t/RC} en una descarga.",
                "Ignorar el sentido de la corriente.",
                "Pensar que se descarga completamente en un tiempo finito."
            ]
        },
        {
            "nombre": "Flujo magnético",
            "idea_clave": "Mide cuánto campo magnético atraviesa una superficie.",
            "formula_base": "Phi_B = B A cos(theta)",
            "formula_principal": "Phi_B = ∫B·dA",
            "sale_de": [
                "El flujo cuenta la componente de B perpendicular al área.",
                "El vector área apunta normal a la superficie.",
                "Para B uniforme y área plana, Phi=BAcos(theta)."
            ],
            "despejes": [
                "B = Phi_B/(Acos(theta))",
                "A = Phi_B/(Bcos(theta))",
                "theta = arccos(Phi_B/(BA))"
            ],
            "formulas_relacionadas": [
                "Faraday: epsilon=-N dPhi_B/dt",
                "Lenz",
                "Phi_B=NBAcos(theta) si hay N espiras"
            ],
            "uso": "Calcular flujo a través de espiras o superficies.",
            "cuando_usarla": [
                "Cuando aparece campo magnético y área.",
                "Cuando hay bobinas/espiras.",
                "Cuando después se pide fem inducida."
            ],
            "procedimiento": [
                "Identifica la normal del área.",
                "Calcula el ángulo con B.",
                "Usa Phi=BAcos(theta).",
                "Si hay N espiras, el enlace de flujo es NPhi."
            ],
            "errores_tipicos": [
                "Usar el ángulo con la superficie en vez de la normal.",
                "Olvidar N en Faraday.",
                "Confundir flujo con campo."
            ]
        },
        {
            "nombre": "Ley de Faraday",
            "idea_clave": "Un flujo magnético cambiante induce una fem.",
            "formula_base": "epsilon = -N dPhi_B/dt",
            "formula_principal": "|epsilon| = N |ΔPhi_B/Δt| si el cambio es uniforme",
            "sale_de": [
                "Experimentalmente, una variación de flujo magnético a través de una espira induce corriente.",
                "La fem inducida es proporcional a la rapidez de cambio del flujo.",
                "El signo negativo representa la Ley de Lenz."
            ],
            "despejes": [
                "ΔPhi_B = -epsilon Δt/N si epsilon es constante",
                "N = |epsilon|/|dPhi_B/dt|",
                "Si B cambia: epsilon = -N A cos(theta) dB/dt",
                "Si A cambia: epsilon = -N B cos(theta) dA/dt"
            ],
            "formulas_relacionadas": [
                "Phi_B=BAcos(theta)",
                "Ley de Lenz",
                "epsilon_L=-L dI/dt"
            ],
            "uso": "Calcular fem inducida por cambios de flujo magnético.",
            "cuando_usarla": [
                "Cuando cambia B, A o theta.",
                "Cuando un imán se mueve cerca de una bobina.",
                "Cuando una espira rota en un campo magnético.",
                "Cuando se pregunta corriente inducida."
            ],
            "procedimiento": [
                "Escribe Phi_B=BAcos(theta).",
                "Identifica qué variable cambia con el tiempo.",
                "Calcula dPhi/dt o ΔPhi/Δt.",
                "Multiplica por N.",
                "Usa Lenz para determinar el sentido."
            ],
            "errores_tipicos": [
                "Pensar que un flujo grande siempre induce fem; debe cambiar.",
                "Olvidar el signo conceptual de Lenz.",
                "No multiplicar por el número de espiras.",
                "Usar grados/radianes incorrectamente si theta cambia."
            ]
        },
        {
            "nombre": "Ley de Lenz",
            "idea_clave": "La corriente inducida se opone al cambio de flujo.",
            "formula_base": "epsilon = -N dPhi_B/dt",
            "formula_principal": "La corriente inducida crea un B que se opone al cambio de Phi_B",
            "sale_de": [
                "El signo menos en Faraday representa conservación de energía.",
                "Si la corriente inducida reforzara el cambio, el sistema ganaría energía sin fuente.",
                "Por eso la respuesta inducida se opone a la variación."
            ],
            "despejes": [
                "No es tanto una fórmula de despeje como una regla de sentido.",
                "Si Phi aumenta hacia dentro, B_inducido apunta hacia fuera.",
                "Si Phi disminuye hacia dentro, B_inducido apunta hacia dentro."
            ],
            "formulas_relacionadas": [
                "Faraday",
                "Regla de la mano derecha para corriente en una espira",
                "Phi_B=BAcos(theta)"
            ],
            "uso": "Determinar el sentido de la corriente inducida.",
            "cuando_usarla": [
                "Cuando piden sentido horario/antihorario.",
                "Cuando un imán entra o sale de una bobina.",
                "Cuando cambia el campo a través de una espira."
            ],
            "procedimiento": [
                "Determina el sentido del flujo externo.",
                "Decide si ese flujo aumenta o disminuye.",
                "El campo inducido se opone al cambio.",
                "Usa mano derecha para encontrar corriente que crea ese campo inducido."
            ],
            "errores_tipicos": [
                "Oponerse al campo en vez de oponerse al cambio de flujo.",
                "Confundir horario/antihorario al mirar desde lados distintos.",
                "Ignorar si el flujo aumenta o disminuye."
            ]
        },
        {
            "nombre": "Autoinducción",
            "idea_clave": "Un inductor se opone a cambios de corriente.",
            "formula_base": "epsilon_L = -L dI/dt",
            "formula_principal": "epsilon_L = -L dI/dt",
            "sale_de": [
                "Una corriente en una bobina crea un campo magnético.",
                "Si la corriente cambia, cambia el flujo magnético creado por la propia bobina.",
                "Por Faraday, ese cambio induce una fem que se opone al cambio."
            ],
            "despejes": [
                "L = -epsilon_L/(dI/dt)",
                "dI/dt = -epsilon_L/L",
                "epsilon_L ≈ -L ΔI/Δt"
            ],
            "formulas_relacionadas": [
                "Faraday",
                "Energía inductor U=1/2LI²",
                "Circuito RL tau=L/R"
            ],
            "uso": "Problemas de bobinas e inductores con corriente variable.",
            "cuando_usarla": [
                "Cuando aparece un inductor L.",
                "Cuando la corriente cambia con el tiempo.",
                "Cuando se habla de fem autoinducida."
            ],
            "procedimiento": [
                "Identifica L y la rapidez de cambio de corriente.",
                "Usa epsilon_L=-L dI/dt.",
                "Interpreta el signo con Lenz."
            ],
            "errores_tipicos": [
                "Pensar que un inductor se opone a la corriente, no al cambio de corriente.",
                "Olvidar el signo de Lenz.",
                "Usar tau=RC para un circuito RL."
            ]
        },
        {
            "nombre": "Energía almacenada en un inductor",
            "idea_clave": "Un inductor almacena energía en su campo magnético.",
            "formula_base": "U = 1/2 L I²",
            "formula_principal": "U = 1/2 L I²",
            "sale_de": [
                "Para establecer corriente en un inductor, la fuente debe trabajar contra la fem autoinducida.",
                "Integrando la potencia asociada a la construcción de la corriente se obtiene U=1/2LI²."
            ],
            "despejes": [
                "L = 2U/I²",
                "I = sqrt(2U/L)"
            ],
            "formulas_relacionadas": [
                "epsilon_L=-L dI/dt",
                "Circuito RL",
                "Energía capacitor U=1/2CV²"
            ],
            "uso": "Calcular energía en bobinas o inductores.",
            "cuando_usarla": [
                "Cuando aparece inductancia L y corriente I.",
                "Cuando piden energía magnética almacenada.",
                "Cuando comparas capacitor vs inductor."
            ],
            "procedimiento": [
                "Convierte L a henrios.",
                "Usa U=1/2LI².",
                "Si piden corriente, despeja I."
            ],
            "errores_tipicos": [
                "Usar voltaje en vez de corriente.",
                "Olvidar el factor 1/2.",
                "Confundir L de inductancia con longitud."
            ]
        },
        {
            "nombre": "Circuito RL conectándose",
            "idea_clave": "La corriente en un circuito RL no alcanza su valor final instantáneamente.",
            "formula_base": "tau = L/R",
            "formula_principal": "I(t) = (V/R)(1-e^{-tR/L})",
            "sale_de": [
                "Kirchhoff da V - IR - L dI/dt = 0.",
                "La solución de esa ecuación diferencial con I(0)=0 es I(t)=(V/R)(1-e^{-tR/L}).",
                "La constante de tiempo es tau=L/R."
            ],
            "despejes": [
                "I_final = V/R",
                "tau = L/R",
                "t = -tau ln(1-I/I_final)"
            ],
            "formulas_relacionadas": [
                "epsilon_L=-L dI/dt",
                "V=IR",
                "U=1/2LI²"
            ],
            "uso": "Resolver crecimiento de corriente en circuitos RL.",
            "cuando_usarla": [
                "Cuando hay resistencia e inductor con batería.",
                "Cuando la corriente está aumentando desde cero.",
                "Cuando aparece tau=L/R."
            ],
            "procedimiento": [
                "Calcula I_final=V/R.",
                "Calcula tau=L/R.",
                "Usa I(t)=I_final(1-e^{-t/tau})."
            ],
            "errores_tipicos": [
                "Usar tau=RC.",
                "Pensar que la corriente salta inmediatamente a V/R.",
                "Confundir el papel de capacitor e inductor."
            ]
        },
        {
            "nombre": "Circuito RL desconectándose",
            "idea_clave": "La corriente de un inductor decae exponencialmente cuando se descarga.",
            "formula_base": "tau = L/R",
            "formula_principal": "I(t)=I0 e^{-tR/L}",
            "sale_de": [
                "Sin fuente, la ecuación de malla contiene la resistencia y la fem del inductor.",
                "La solución indica que la corriente decae exponencialmente.",
                "La escala temporal es tau=L/R."
            ],
            "despejes": [
                "t = -tau ln(I/I0)",
                "tau=L/R",
                "R=L/tau",
                "L=Rtau"
            ],
            "formulas_relacionadas": [
                "epsilon_L=-L dI/dt",
                "U=1/2LI²",
                "Potencia disipada P=I²R"
            ],
            "uso": "Corriente decreciente en circuitos RL.",
            "cuando_usarla": [
                "Cuando se desconecta la batería.",
                "Cuando una corriente inicial I0 decae.",
                "Cuando aparece inductor y resistencia."
            ],
            "procedimiento": [
                "Identifica I0.",
                "Calcula tau=L/R.",
                "Usa I(t)=I0e^{-t/tau}."
            ],
            "errores_tipicos": [
                "Usar fórmula de crecimiento para descarga.",
                "Usar RC en vez de L/R.",
                "Ignorar que el inductor intenta mantener la corriente."
            ]
        }
    ],

    "interpretacion_enunciados": [
        {
            "palabra_clave": "carga que pasa en un tiempo",
            "que_significa": "El problema pide corriente o carga transferida.",
            "que_suele_pedir": [
                "Corriente media.",
                "Carga total.",
                "Número de electrones.",
                "Tiempo necesario."
            ],
            "operaciones_recomendadas": [
                "Usa I=Δq/Δt.",
                "Despeja Δq=IΔt si piden carga.",
                "Para número de electrones, usa N=Q/e.",
                "Convierte mA a A y minutos a segundos."
            ],
            "pista_examen": "Corriente es carga por segundo."
        },
        {
            "palabra_clave": "longitud, área, resistividad",
            "que_significa": "Debes calcular resistencia del conductor.",
            "que_suele_pedir": [
                "Resistencia de un cable.",
                "Resistividad del material.",
                "Efecto de cambiar longitud o grosor."
            ],
            "operaciones_recomendadas": [
                "Usa R=rho L/A.",
                "Si dan radio, calcula A=πr².",
                "Convierte cm² o mm² a m².",
                "Si cambia temperatura, usa R=R0[1+alphaΔT]."
            ],
            "pista_examen": "Más largo = más resistencia; más grueso = menos resistencia."
        },
        {
            "palabra_clave": "voltaje, corriente y resistencia",
            "que_significa": "El ejercicio probablemente usa Ley de Ohm.",
            "que_suele_pedir": [
                "Corriente.",
                "Voltaje.",
                "Resistencia.",
                "Potencia."
            ],
            "operaciones_recomendadas": [
                "Usa V=IR.",
                "Elige el voltaje correcto sobre la resistencia correcta.",
                "Si piden potencia, combina con P=IV."
            ],
            "pista_examen": "No uses voltaje total en una resistencia individual si hay varias."
        },
        {
            "palabra_clave": "potencia disipada",
            "que_significa": "Se busca energía por unidad de tiempo.",
            "que_suele_pedir": [
                "Potencia en una resistencia.",
                "Energía consumida.",
                "Calor disipado.",
                "Coste eléctrico."
            ],
            "operaciones_recomendadas": [
                "Usa P=IV.",
                "Si sabes I y R, usa P=I²R.",
                "Si sabes V y R, usa P=V²/R.",
                "Para energía, E=Pt."
            ],
            "pista_examen": "Elige la fórmula de potencia según los datos disponibles."
        },
        {
            "palabra_clave": "resistencias en serie",
            "que_significa": "La misma corriente pasa por todas.",
            "que_suele_pedir": [
                "Resistencia equivalente.",
                "Corriente total.",
                "Caída de voltaje en cada resistencia.",
                "Potencia en cada resistencia."
            ],
            "operaciones_recomendadas": [
                "Suma resistencias.",
                "Calcula I=V/R_eq.",
                "Calcula V_i=IR_i.",
                "Calcula potencia si se pide."
            ],
            "pista_examen": "Serie = misma corriente."
        },
        {
            "palabra_clave": "resistencias en paralelo",
            "que_significa": "Comparten los mismos dos nodos y tienen el mismo voltaje.",
            "que_suele_pedir": [
                "Resistencia equivalente.",
                "Corriente por cada rama.",
                "Corriente total.",
                "Potencia por rama."
            ],
            "operaciones_recomendadas": [
                "Usa 1/R_eq=Σ1/R_i.",
                "Usa el mismo V en cada rama.",
                "Calcula I_i=V/R_i.",
                "Suma corrientes."
            ],
            "pista_examen": "Paralelo = mismo voltaje."
        },
        {
            "palabra_clave": "nodo / unión",
            "que_significa": "Debes aplicar Kirchhoff de corrientes.",
            "que_suele_pedir": [
                "Corriente desconocida.",
                "Relación entre corrientes de ramas.",
                "Sistema de ecuaciones."
            ],
            "operaciones_recomendadas": [
                "Define qué corrientes entran y cuáles salen.",
                "Escribe ΣI_entrantes=ΣI_salientes.",
                "Combina con Ohm si hace falta."
            ],
            "pista_examen": "Nodo = conservación de carga."
        },
        {
            "palabra_clave": "malla / circuito cerrado",
            "que_significa": "Debes aplicar Kirchhoff de voltajes.",
            "que_suele_pedir": [
                "Corrientes de malla.",
                "Voltajes en resistencias.",
                "Ecuaciones de circuito.",
                "Corriente con varias baterías."
            ],
            "operaciones_recomendadas": [
                "Elige sentido de recorrido.",
                "Anota subidas y caídas de potencial.",
                "Resistencia en sentido de corriente: -IR.",
                "Batería de - a +: +epsilon.",
                "Resuelve el sistema."
            ],
            "pista_examen": "Malla = conservación de energía."
        },
        {
            "palabra_clave": "capacitor / capacitancia",
            "que_significa": "Se trabaja con carga almacenada y diferencia de potencial.",
            "que_suele_pedir": [
                "Carga en el capacitor.",
                "Voltaje entre placas.",
                "Capacitancia.",
                "Energía almacenada."
            ],
            "operaciones_recomendadas": [
                "Usa C=Q/V.",
                "Si es placas paralelas, usa C=epsilon A/d.",
                "Si hay energía, usa U=1/2CV² o U=1/2QV."
            ],
            "pista_examen": "Convierte μF a F antes de calcular."
        },
        {
            "palabra_clave": "capacitores en serie",
            "que_significa": "Misma carga en cada capacitor.",
            "que_suele_pedir": [
                "Capacitancia equivalente.",
                "Carga de cada capacitor.",
                "Voltaje en cada capacitor."
            ],
            "operaciones_recomendadas": [
                "Usa 1/C_eq=Σ1/C_i.",
                "Calcula Q=C_eqV_total.",
                "Usa la misma Q en cada capacitor.",
                "Calcula V_i=Q/C_i."
            ],
            "pista_examen": "Capacitores en serie usan inversos, como resistencias en paralelo."
        },
        {
            "palabra_clave": "capacitores en paralelo",
            "que_significa": "Mismo voltaje en cada capacitor.",
            "que_suele_pedir": [
                "Capacitancia equivalente.",
                "Carga total.",
                "Carga en cada capacitor."
            ],
            "operaciones_recomendadas": [
                "Suma capacitancias.",
                "Usa mismo V para cada capacitor.",
                "Calcula Q_i=C_iV.",
                "Suma cargas."
            ],
            "pista_examen": "Capacitores en paralelo se suman directamente."
        },
        {
            "palabra_clave": "capacitor cargándose",
            "que_significa": "Es un circuito RC de carga.",
            "que_suele_pedir": [
                "q(t).",
                "V_C(t).",
                "i(t).",
                "Constante de tiempo.",
                "Tiempo para cierto porcentaje."
            ],
            "operaciones_recomendadas": [
                "Calcula tau=RC.",
                "Usa q(t)=CV(1-e^{-t/RC}).",
                "Usa i(t)=(V/R)e^{-t/RC}.",
                "Recuerda que la corriente empieza máxima y decae."
            ],
            "pista_examen": "Carga RC = 1 - exponencial."
        },
        {
            "palabra_clave": "capacitor descargándose",
            "que_significa": "Es un circuito RC de descarga.",
            "que_suele_pedir": [
                "Carga restante.",
                "Voltaje restante.",
                "Corriente de descarga.",
                "Tiempo para caer a cierto porcentaje."
            ],
            "operaciones_recomendadas": [
                "Calcula tau=RC.",
                "Usa q(t)=Q0e^{-t/RC}.",
                "Usa V(t)=V0e^{-t/RC}.",
                "Para tiempo, despeja con logaritmos."
            ],
            "pista_examen": "Descarga RC = exponencial pura."
        },
        {
            "palabra_clave": "flujo magnético cambiante",
            "que_significa": "El problema quiere Faraday-Lenz.",
            "que_suele_pedir": [
                "Fem inducida.",
                "Corriente inducida.",
                "Sentido horario/antihorario.",
                "Cambio de flujo."
            ],
            "operaciones_recomendadas": [
                "Escribe Phi_B=BAcos(theta).",
                "Identifica qué cambia: B, A o theta.",
                "Usa epsilon=-N dPhi/dt.",
                "Usa Lenz para el sentido."
            ],
            "pista_examen": "Sin cambio de flujo, no hay fem inducida."
        },
        {
            "palabra_clave": "inductor / bobina con corriente variable",
            "que_significa": "El problema trata autoinducción o circuito RL.",
            "que_suele_pedir": [
                "Fem autoinducida.",
                "Corriente en función del tiempo.",
                "Energía almacenada.",
                "Constante de tiempo."
            ],
            "operaciones_recomendadas": [
                "Usa epsilon_L=-L dI/dt.",
                "Energía: U=1/2LI².",
                "Para RL, tau=L/R.",
                "Crecimiento: I=(V/R)(1-e^{-tR/L}).",
                "Descarga: I=I0e^{-tR/L}."
            ],
            "pista_examen": "Inductor se opone a cambios de corriente; capacitor se opone a cambios de voltaje."
        }
    ],

    "flashcards": [
        {"id": "fis3_fc_001", "frente": "¿Definición de corriente?", "reverso": "I=Δq/Δt o I=dq/dt.", "categoria": "Corriente"},
        {"id": "fis3_fc_002", "frente": "¿Unidad de corriente?", "reverso": "Ampere, A = C/s.", "categoria": "Corriente"},
        {"id": "fis3_fc_003", "frente": "¿Densidad de corriente?", "reverso": "J=I/A.", "categoria": "Corriente"},
        {"id": "fis3_fc_004", "frente": "¿Corriente con velocidad de deriva?", "reverso": "I=nqAv_d.", "categoria": "Corriente"},
        {"id": "fis3_fc_005", "frente": "¿Ley de Ohm microscópica?", "reverso": "J=sigma E o E=rho J.", "categoria": "Ohm"},
        {"id": "fis3_fc_006", "frente": "¿Ley de Ohm macroscópica?", "reverso": "V=IR.", "categoria": "Ohm"},
        {"id": "fis3_fc_007", "frente": "¿Resistencia de un conductor?", "reverso": "R=rho L/A.", "categoria": "Resistencia"},
        {"id": "fis3_fc_008", "frente": "Si aumenta el área del cable, ¿qué pasa con R?", "reverso": "Disminuye.", "categoria": "Resistencia"},
        {"id": "fis3_fc_009", "frente": "Si aumenta la longitud del cable, ¿qué pasa con R?", "reverso": "Aumenta.", "categoria": "Resistencia"},
        {"id": "fis3_fc_010", "frente": "¿Potencia eléctrica base?", "reverso": "P=IV.", "categoria": "Potencia"},
        {"id": "fis3_fc_011", "frente": "¿Potencia en resistencia usando I y R?", "reverso": "P=I²R.", "categoria": "Potencia"},
        {"id": "fis3_fc_012", "frente": "¿Potencia en resistencia usando V y R?", "reverso": "P=V²/R.", "categoria": "Potencia"},
        {"id": "fis3_fc_013", "frente": "En resistencias en serie, ¿qué es igual?", "reverso": "La corriente.", "categoria": "Serie"},
        {"id": "fis3_fc_014", "frente": "Resistencias en serie equivalente:", "reverso": "R_eq=R1+R2+...", "categoria": "Serie"},
        {"id": "fis3_fc_015", "frente": "En resistencias en paralelo, ¿qué es igual?", "reverso": "El voltaje.", "categoria": "Paralelo"},
        {"id": "fis3_fc_016", "frente": "Resistencias en paralelo equivalente:", "reverso": "1/R_eq=1/R1+1/R2+...", "categoria": "Paralelo"},
        {"id": "fis3_fc_017", "frente": "¿Ley de Kirchhoff de nodos?", "reverso": "ΣI_entrantes=ΣI_salientes.", "categoria": "Kirchhoff"},
        {"id": "fis3_fc_018", "frente": "¿Ley de Kirchhoff de mallas?", "reverso": "ΣΔV=0.", "categoria": "Kirchhoff"},
        {"id": "fis3_fc_019", "frente": "¿Definición de capacitancia?", "reverso": "C=Q/V.", "categoria": "Capacitores"},
        {"id": "fis3_fc_020", "frente": "Capacitor de placas paralelas:", "reverso": "C=epsilon A/d.", "categoria": "Capacitores"},
        {"id": "fis3_fc_021", "frente": "Capacitores en paralelo:", "reverso": "C_eq=C1+C2+...", "categoria": "Capacitores"},
        {"id": "fis3_fc_022", "frente": "Capacitores en serie:", "reverso": "1/C_eq=1/C1+1/C2+...", "categoria": "Capacitores"},
        {"id": "fis3_fc_023", "frente": "Energía en capacitor:", "reverso": "U=1/2QV=1/2CV²=Q²/(2C).", "categoria": "Capacitores"},
        {"id": "fis3_fc_024", "frente": "Constante de tiempo RC:", "reverso": "tau=RC.", "categoria": "RC"},
        {"id": "fis3_fc_025", "frente": "Carga de capacitor en RC:", "reverso": "q(t)=CV(1-e^{-t/RC}).", "categoria": "RC"},
        {"id": "fis3_fc_026", "frente": "Descarga de capacitor en RC:", "reverso": "q(t)=Q0e^{-t/RC}.", "categoria": "RC"},
        {"id": "fis3_fc_027", "frente": "En t=tau durante carga RC, ¿qué porcentaje aproximado se alcanza?", "reverso": "Aproximadamente 63%.", "categoria": "RC"},
        {"id": "fis3_fc_028", "frente": "En t=tau durante descarga RC, ¿qué porcentaje queda?", "reverso": "Aproximadamente 37%.", "categoria": "RC"},
        {"id": "fis3_fc_029", "frente": "Flujo magnético:", "reverso": "Phi_B=BAcos(theta).", "categoria": "Faraday"},
        {"id": "fis3_fc_030", "frente": "Ley de Faraday:", "reverso": "epsilon=-N dPhi_B/dt.", "categoria": "Faraday"},
        {"id": "fis3_fc_031", "frente": "¿Qué dice Lenz?", "reverso": "La corriente inducida se opone al cambio de flujo.", "categoria": "Lenz"},
        {"id": "fis3_fc_032", "frente": "Autoinducción:", "reverso": "epsilon_L=-L dI/dt.", "categoria": "Inductores"},
        {"id": "fis3_fc_033", "frente": "Energía en inductor:", "reverso": "U=1/2LI².", "categoria": "Inductores"},
        {"id": "fis3_fc_034", "frente": "Constante de tiempo RL:", "reverso": "tau=L/R.", "categoria": "RL"},
        {"id": "fis3_fc_035", "frente": "¿Qué se opone a cambios bruscos de corriente?", "reverso": "El inductor.", "categoria": "Inductores"}
    ],

    "preguntas_vf": [
        {"id": "fis3_vf_001", "pregunta": "La corriente eléctrica es carga por unidad de tiempo.", "respuesta": True, "explicacion": "I=Δq/Δt.", "categoria": "Corriente", "dificultad": "facil"},
        {"id": "fis3_vf_002", "pregunta": "1 ampere equivale a 1 coulomb por segundo.", "respuesta": True, "explicacion": "1 A=1 C/s.", "categoria": "Corriente", "dificultad": "facil"},
        {"id": "fis3_vf_003", "pregunta": "La corriente convencional va en el mismo sentido que el movimiento de electrones en metales.", "respuesta": False, "explicacion": "Los electrones se mueven en sentido contrario a la corriente convencional.", "categoria": "Corriente", "dificultad": "media"},
        {"id": "fis3_vf_004", "pregunta": "La densidad de corriente es J=I/A.", "respuesta": True, "explicacion": "Es corriente por área transversal.", "categoria": "Corriente", "dificultad": "facil"},
        {"id": "fis3_vf_005", "pregunta": "Si aumenta el área de un cable, su resistencia aumenta.", "respuesta": False, "explicacion": "R=rho L/A, al aumentar A disminuye R.", "categoria": "Resistencia", "dificultad": "facil"},
        {"id": "fis3_vf_006", "pregunta": "Si aumenta la longitud de un cable, su resistencia aumenta.", "respuesta": True, "explicacion": "R es proporcional a L.", "categoria": "Resistencia", "dificultad": "facil"},
        {"id": "fis3_vf_007", "pregunta": "La ley de Ohm macroscópica es V=IR.", "respuesta": True, "explicacion": "Para elementos óhmicos.", "categoria": "Ohm", "dificultad": "facil"},
        {"id": "fis3_vf_008", "pregunta": "Todos los dispositivos cumplen la Ley de Ohm linealmente.", "respuesta": False, "explicacion": "Muchos problemas lo asumen, pero no todos los dispositivos son óhmicos.", "categoria": "Ohm", "dificultad": "media"},
        {"id": "fis3_vf_009", "pregunta": "La potencia eléctrica puede calcularse como P=IV.", "respuesta": True, "explicacion": "Es la relación base de potencia eléctrica.", "categoria": "Potencia", "dificultad": "facil"},
        {"id": "fis3_vf_010", "pregunta": "En una resistencia, P=I²R.", "respuesta": True, "explicacion": "Sale de P=IV y V=IR.", "categoria": "Potencia", "dificultad": "facil"},
        {"id": "fis3_vf_011", "pregunta": "En resistencias en serie pasa la misma corriente por todas.", "respuesta": True, "explicacion": "No hay ramificaciones.", "categoria": "Serie", "dificultad": "facil"},
        {"id": "fis3_vf_012", "pregunta": "En resistencias en serie todas tienen el mismo voltaje.", "respuesta": False, "explicacion": "En serie tienen la misma corriente; el voltaje se reparte.", "categoria": "Serie", "dificultad": "facil"},
        {"id": "fis3_vf_013", "pregunta": "En resistencias en paralelo todas tienen el mismo voltaje.", "respuesta": True, "explicacion": "Comparten los mismos dos nodos.", "categoria": "Paralelo", "dificultad": "facil"},
        {"id": "fis3_vf_014", "pregunta": "En resistencias en paralelo todas tienen la misma corriente.", "respuesta": False, "explicacion": "La corriente se divide según la resistencia de cada rama.", "categoria": "Paralelo", "dificultad": "facil"},
        {"id": "fis3_vf_015", "pregunta": "La resistencia equivalente en paralelo es menor que la menor resistencia individual.", "respuesta": True, "explicacion": "Esa es una propiedad importante del paralelo.", "categoria": "Paralelo", "dificultad": "media"},
        {"id": "fis3_vf_016", "pregunta": "Kirchhoff de nodos expresa conservación de carga.", "respuesta": True, "explicacion": "La corriente que entra debe igualar la que sale.", "categoria": "Kirchhoff", "dificultad": "facil"},
        {"id": "fis3_vf_017", "pregunta": "Kirchhoff de mallas expresa conservación de energía.", "respuesta": True, "explicacion": "La suma de cambios de potencial en una malla cerrada es cero.", "categoria": "Kirchhoff", "dificultad": "facil"},
        {"id": "fis3_vf_018", "pregunta": "La capacitancia se define como C=Q/V.", "respuesta": True, "explicacion": "Carga almacenada por voltaje.", "categoria": "Capacitores", "dificultad": "facil"},
        {"id": "fis3_vf_019", "pregunta": "En un capacitor de placas paralelas, aumentar la distancia aumenta la capacitancia.", "respuesta": False, "explicacion": "C=epsilon A/d, al aumentar d disminuye C.", "categoria": "Capacitores", "dificultad": "facil"},
        {"id": "fis3_vf_020", "pregunta": "Introducir un dieléctrico aumenta la capacitancia.", "respuesta": True, "explicacion": "C=kappa C0 si kappa>1.", "categoria": "Capacitores", "dificultad": "facil"},
        {"id": "fis3_vf_021", "pregunta": "Capacitores en paralelo se suman directamente.", "respuesta": True, "explicacion": "C_eq=C1+C2+...", "categoria": "Capacitores", "dificultad": "facil"},
        {"id": "fis3_vf_022", "pregunta": "Capacitores en serie tienen el mismo voltaje.", "respuesta": False, "explicacion": "En serie tienen la misma carga; el voltaje se reparte.", "categoria": "Capacitores", "dificultad": "media"},
        {"id": "fis3_vf_023", "pregunta": "La energía de un capacitor es U=1/2CV².", "respuesta": True, "explicacion": "También U=1/2QV=Q²/(2C).", "categoria": "Capacitores", "dificultad": "facil"},
        {"id": "fis3_vf_024", "pregunta": "La constante de tiempo de un circuito RC es tau=RC.", "respuesta": True, "explicacion": "tau=RC.", "categoria": "RC", "dificultad": "facil"},
        {"id": "fis3_vf_025", "pregunta": "Durante la carga RC, q(t)=Q0e^{-t/RC}.", "respuesta": False, "explicacion": "Esa es la forma de descarga; en carga q(t)=CV(1-e^{-t/RC}).", "categoria": "RC", "dificultad": "media"},
        {"id": "fis3_vf_026", "pregunta": "Durante la descarga RC, la carga decae exponencialmente.", "respuesta": True, "explicacion": "q(t)=Q0e^{-t/RC}.", "categoria": "RC", "dificultad": "facil"},
        {"id": "fis3_vf_027", "pregunta": "En t=tau, un capacitor cargándose alcanza aproximadamente 63% de la carga final.", "respuesta": True, "explicacion": "1-e^{-1}≈0.632.", "categoria": "RC", "dificultad": "media"},
        {"id": "fis3_vf_028", "pregunta": "La Ley de Faraday requiere cambio de flujo magnético.", "respuesta": True, "explicacion": "epsilon=-N dPhi/dt.", "categoria": "Faraday", "dificultad": "facil"},
        {"id": "fis3_vf_029", "pregunta": "Si el flujo magnético es grande pero constante, hay fem inducida.", "respuesta": False, "explicacion": "Debe cambiar el flujo; si dPhi/dt=0, epsilon=0.", "categoria": "Faraday", "dificultad": "media"},
        {"id": "fis3_vf_030", "pregunta": "La Ley de Lenz dice que la corriente inducida se opone al cambio de flujo.", "respuesta": True, "explicacion": "No se opone necesariamente al campo, sino al cambio de flujo.", "categoria": "Lenz", "dificultad": "media"},
        {"id": "fis3_vf_031", "pregunta": "Un inductor se opone a cambios bruscos de corriente.", "respuesta": True, "explicacion": "Por autoinducción epsilon_L=-L dI/dt.", "categoria": "Inductores", "dificultad": "media"},
        {"id": "fis3_vf_032", "pregunta": "La constante de tiempo de un circuito RL es tau=RC.", "respuesta": False, "explicacion": "Para RL, tau=L/R.", "categoria": "RL", "dificultad": "media"},
        {"id": "fis3_vf_033", "pregunta": "La energía almacenada en un inductor es U=1/2LI².", "respuesta": True, "explicacion": "Se almacena en el campo magnético.", "categoria": "Inductores", "dificultad": "media"},
        {"id": "fis3_vf_034", "pregunta": "Un capacitor ideal cargado se comporta como circuito abierto en DC a largo tiempo.", "respuesta": True, "explicacion": "Cuando está cargado, no pasa corriente DC idealmente.", "categoria": "RC", "dificultad": "media"},
        {"id": "fis3_vf_035", "pregunta": "Un capacitor inicialmente descargado se comporta como circuito abierto justo al conectarlo.", "respuesta": False, "explicacion": "Justo al inicio se comporta como un cable ideal; después se va cargando.", "categoria": "RC", "dificultad": "dificil"}
    ],

    "preguntas_mc": [
        {
            "id": "fis3_mc_001",
            "pregunta": "¿Qué fórmula define corriente eléctrica media?",
            "opciones": ["I=Δq/Δt", "V=IR", "P=IV", "C=Q/V"],
            "respuesta": 1,
            "explicacion": "La corriente mide carga por unidad de tiempo.",
            "categoria": "Corriente",
            "dificultad": "facil"
        },
        {
            "id": "fis3_mc_002",
            "pregunta": "¿Cuál es la unidad de corriente?",
            "opciones": ["Volt", "Ohm", "Ampere", "Faradio"],
            "respuesta": 3,
            "explicacion": "El ampere equivale a C/s.",
            "categoria": "Corriente",
            "dificultad": "facil"
        },
        {
            "id": "fis3_mc_003",
            "pregunta": "La resistencia de un conductor uniforme es:",
            "opciones": ["R=rho L/A", "R=A/(rho L)", "R=V/I²", "R=CV"],
            "respuesta": 1,
            "explicacion": "Depende de resistividad, longitud y área.",
            "categoria": "Resistencia",
            "dificultad": "facil"
        },
        {
            "id": "fis3_mc_004",
            "pregunta": "Si duplicas la longitud de un cable manteniendo todo lo demás, R:",
            "opciones": ["Se duplica", "Se divide entre 2", "No cambia", "Se hace cero"],
            "respuesta": 1,
            "explicacion": "R es proporcional a L.",
            "categoria": "Resistencia",
            "dificultad": "facil"
        },
        {
            "id": "fis3_mc_005",
            "pregunta": "Si duplicas el área transversal de un cable, R:",
            "opciones": ["Se duplica", "Se divide entre 2", "No cambia", "Se cuadruplica"],
            "respuesta": 2,
            "explicacion": "R es inversamente proporcional a A.",
            "categoria": "Resistencia",
            "dificultad": "facil"
        },
        {
            "id": "fis3_mc_006",
            "pregunta": "La Ley de Ohm es:",
            "opciones": ["V=IR", "F=qE", "Phi=BAcosθ", "q=CV²"],
            "respuesta": 1,
            "explicacion": "Relaciona voltaje, corriente y resistencia.",
            "categoria": "Ohm",
            "dificultad": "facil"
        },
        {
            "id": "fis3_mc_007",
            "pregunta": "¿Cuál fórmula de potencia usarías si conoces I y R?",
            "opciones": ["P=I²R", "P=V²/R sin V", "P=Q/V", "P=RC"],
            "respuesta": 1,
            "explicacion": "P=I²R sale de P=IV y V=IR.",
            "categoria": "Potencia",
            "dificultad": "facil"
        },
        {
            "id": "fis3_mc_008",
            "pregunta": "En resistencias en serie:",
            "opciones": ["El voltaje es igual en todas", "La corriente es igual en todas", "La resistencia equivalente es menor que todas", "No hay caída de voltaje"],
            "respuesta": 2,
            "explicacion": "Serie = misma corriente.",
            "categoria": "Serie",
            "dificultad": "facil"
        },
        {
            "id": "fis3_mc_009",
            "pregunta": "En resistencias en paralelo:",
            "opciones": ["La corriente es igual en todas", "El voltaje es igual en todas", "Las resistencias se suman directamente", "La corriente total es cero"],
            "respuesta": 2,
            "explicacion": "Paralelo = mismo voltaje.",
            "categoria": "Paralelo",
            "dificultad": "facil"
        },
        {
            "id": "fis3_mc_010",
            "pregunta": "Para dos resistencias en paralelo, R_eq es:",
            "opciones": ["R1+R2", "R1R2/(R1+R2)", "(R1+R2)/(R1R2)", "R1-R2"],
            "respuesta": 2,
            "explicacion": "Es la fórmula simplificada para dos resistencias en paralelo.",
            "categoria": "Paralelo",
            "dificultad": "facil"
        },
        {
            "id": "fis3_mc_011",
            "pregunta": "La Ley de Kirchhoff de nodos expresa:",
            "opciones": ["Conservación de carga", "Conservación de masa mecánica", "Ley de Coulomb", "Inducción magnética"],
            "respuesta": 1,
            "explicacion": "La corriente que entra al nodo iguala la que sale.",
            "categoria": "Kirchhoff",
            "dificultad": "facil"
        },
        {
            "id": "fis3_mc_012",
            "pregunta": "La Ley de Kirchhoff de mallas dice:",
            "opciones": ["ΣΔV=0", "ΣI=∞", "C=Q/V", "F=qvB"],
            "respuesta": 1,
            "explicacion": "La suma de subidas y caídas de potencial en una malla cerrada es cero.",
            "categoria": "Kirchhoff",
            "dificultad": "facil"
        },
        {
            "id": "fis3_mc_013",
            "pregunta": "La capacitancia se define como:",
            "opciones": ["C=Q/V", "C=V/Q", "C=IR", "C=BA"],
            "respuesta": 1,
            "explicacion": "Carga almacenada por voltaje aplicado.",
            "categoria": "Capacitores",
            "dificultad": "facil"
        },
        {
            "id": "fis3_mc_014",
            "pregunta": "Para placas paralelas:",
            "opciones": ["C=epsilon A/d", "C=epsilon d/A", "C=Q²/V", "C=IR"],
            "respuesta": 1,
            "explicacion": "Mayor área aumenta C; mayor separación disminuye C.",
            "categoria": "Capacitores",
            "dificultad": "facil"
        },
        {
            "id": "fis3_mc_015",
            "pregunta": "Capacitores en paralelo:",
            "opciones": ["Se suman directamente", "Usan inversos", "Tienen la misma carga siempre", "No almacenan energía"],
            "respuesta": 1,
            "explicacion": "C_eq=C1+C2+...",
            "categoria": "Capacitores",
            "dificultad": "facil"
        },
        {
            "id": "fis3_mc_016",
            "pregunta": "Capacitores en serie:",
            "opciones": ["Se suman directamente", "Usan inversos", "Tienen el mismo voltaje siempre", "No tienen carga"],
            "respuesta": 2,
            "explicacion": "1/C_eq=Σ1/C_i.",
            "categoria": "Capacitores",
            "dificultad": "facil"
        },
        {
            "id": "fis3_mc_017",
            "pregunta": "La energía almacenada en un capacitor puede ser:",
            "opciones": ["U=1/2CV²", "U=CV²", "U=IR", "U=mv/r"],
            "respuesta": 1,
            "explicacion": "También U=1/2QV.",
            "categoria": "Capacitores",
            "dificultad": "facil"
        },
        {
            "id": "fis3_mc_018",
            "pregunta": "La constante de tiempo de un RC es:",
            "opciones": ["RC", "R/C", "C/R", "L/R"],
            "respuesta": 1,
            "explicacion": "tau=RC.",
            "categoria": "RC",
            "dificultad": "facil"
        },
        {
            "id": "fis3_mc_019",
            "pregunta": "Durante la carga RC, la carga es:",
            "opciones": ["q=CV(1-e^{-t/RC})", "q=Q0e^{-t/RC}", "q=IR", "q=BAcosθ"],
            "respuesta": 1,
            "explicacion": "Carga desde cero hasta CV.",
            "categoria": "RC",
            "dificultad": "facil"
        },
        {
            "id": "fis3_mc_020",
            "pregunta": "Durante la descarga RC, la carga es:",
            "opciones": ["q=Q0e^{-t/RC}", "q=CV(1-e^{-t/RC})", "q=IR", "q=epsilon A/d"],
            "respuesta": 1,
            "explicacion": "Decae exponencialmente.",
            "categoria": "RC",
            "dificultad": "facil"
        },
        {
            "id": "fis3_mc_021",
            "pregunta": "Si aparece flujo magnético cambiante, usas:",
            "opciones": ["Faraday-Lenz", "Ohm solamente", "Coulomb", "R=rho L/A"],
            "respuesta": 1,
            "explicacion": "epsilon=-N dPhi_B/dt.",
            "categoria": "Faraday",
            "dificultad": "facil"
        },
        {
            "id": "fis3_mc_022",
            "pregunta": "La Ley de Faraday es:",
            "opciones": ["epsilon=-N dPhi_B/dt", "V=IR", "C=Q/V", "F=qE"],
            "respuesta": 1,
            "explicacion": "El signo negativo representa Lenz.",
            "categoria": "Faraday",
            "dificultad": "facil"
        },
        {
            "id": "fis3_mc_023",
            "pregunta": "La Ley de Lenz dice que la corriente inducida:",
            "opciones": ["Se opone al cambio de flujo", "Siempre aumenta el flujo", "Siempre es horaria", "No depende del flujo"],
            "respuesta": 1,
            "explicacion": "Se opone al cambio que la produce.",
            "categoria": "Lenz",
            "dificultad": "media"
        },
        {
            "id": "fis3_mc_024",
            "pregunta": "Un inductor se opone a cambios de:",
            "opciones": ["Corriente", "Capacitancia", "Resistencia geométrica", "Área"],
            "respuesta": 1,
            "explicacion": "epsilon_L=-L dI/dt.",
            "categoria": "Inductores",
            "dificultad": "media"
        },
        {
            "id": "fis3_mc_025",
            "pregunta": "La constante de tiempo de un circuito RL es:",
            "opciones": ["L/R", "RC", "R/L", "LC"],
            "respuesta": 1,
            "explicacion": "tau=L/R.",
            "categoria": "RL",
            "dificultad": "media"
        },
        {
            "id": "fis3_mc_026",
            "pregunta": "Energía almacenada en un inductor:",
            "opciones": ["U=1/2LI²", "U=1/2CV²", "U=qV", "U=IR"],
            "respuesta": 1,
            "explicacion": "El inductor almacena energía en el campo magnético.",
            "categoria": "Inductores",
            "dificultad": "media"
        },
        {
            "id": "fis3_mc_027",
            "pregunta": "En carga RC, la corriente:",
            "opciones": ["Empieza máxima y decae", "Empieza cero y aumenta para siempre", "Es constante", "No existe"],
            "respuesta": 1,
            "explicacion": "i(t)=(V/R)e^{-t/RC}.",
            "categoria": "RC",
            "dificultad": "media"
        },
        {
            "id": "fis3_mc_028",
            "pregunta": "En un capacitor cargado a largo tiempo en DC:",
            "opciones": ["Se comporta como circuito abierto", "Se comporta como resistencia cero", "Desaparece", "Tiene corriente infinita"],
            "respuesta": 1,
            "explicacion": "Cuando ya no cambia la carga, la corriente ideal es cero.",
            "categoria": "RC",
            "dificultad": "media"
        },
        {
            "id": "fis3_mc_029",
            "pregunta": "En un capacitor inicialmente descargado justo al conectar una batería mediante R:",
            "opciones": ["Se comporta inicialmente como cable ideal", "Se comporta como circuito abierto inmediatamente", "Tiene voltaje máximo", "No circula corriente inicial"],
            "respuesta": 1,
            "explicacion": "Al inicio V_C=0, por eso la corriente inicial es V/R.",
            "categoria": "RC",
            "dificultad": "dificil"
        },
        {
            "id": "fis3_mc_030",
            "pregunta": "Si el flujo magnético es constante en el tiempo, la fem inducida es:",
            "opciones": ["Cero", "Máxima", "Negativa infinita", "Igual a NPhi"],
            "respuesta": 1,
            "explicacion": "Si dPhi/dt=0, epsilon=0.",
            "categoria": "Faraday",
            "dificultad": "facil"
        }
    ]
}
