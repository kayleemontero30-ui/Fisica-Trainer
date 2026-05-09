# -*- coding: utf-8 -*-

TEMA2 = {
    "nombre": "Tema 2 - Campo magnetostático",

    "resumen": """
TEMA 2 - CAMPO MAGNETOSTÁTICO

Este tema estudia campos magnéticos producidos por corrientes estacionarias y las
fuerzas magnéticas que aparecen sobre cargas en movimiento o sobre conductores con
corriente.

La palabra "magnetostático" indica que trabajamos con corrientes constantes en el
tiempo. No estamos todavía en inducción electromagnética, donde el flujo cambia con
el tiempo y aparece una fem inducida. Aquí normalmente el campo magnético B es
producido por corrientes estacionarias.

================================================================================
1. CAMPO MAGNÉTICO B
================================================================================

El campo magnético se representa con el vector B.

Unidad:
- Tesla (T).

El campo magnético puede ser producido por:
- imanes,
- corrientes eléctricas,
- cargas en movimiento.

Diferencia importante con el campo eléctrico:
- Una carga eléctrica en reposo puede sentir fuerza eléctrica si hay E.
- Una carga solo siente fuerza magnética si se mueve respecto a B.
- La fuerza magnética depende de la dirección de la velocidad.

================================================================================
2. FUERZA MAGNÉTICA SOBRE UNA CARGA
================================================================================

La fuerza magnética sobre una carga q que se mueve con velocidad v en un campo B es:

F = q v × B

Módulo:

F = |q| v B sin(theta)

donde theta es el ángulo entre v y B.

Consecuencias:
- Si v es paralela a B, theta=0 y F=0.
- Si v es perpendicular a B, theta=90° y F es máxima.
- La fuerza magnética siempre es perpendicular a v y a B.
- Si q es positiva, el sentido se obtiene con la regla de la mano derecha.
- Si q es negativa, se invierte el sentido.

Regla de la mano derecha:
- Dedos en dirección de v.
- Giras hacia B.
- Pulgar indica v × B para carga positiva.
- Para carga negativa, el sentido real es contrario.

================================================================================
3. MOVIMIENTO CIRCULAR DE UNA CARGA EN UN CAMPO MAGNÉTICO
================================================================================

Si una partícula cargada entra con velocidad perpendicular a un campo magnético uniforme,
la fuerza magnética actúa como fuerza centrípeta.

F_magnética = F_centrípeta

|q|vB = mv²/r

Despejando:

r = mv/(|q|B)

Esto significa:
- Mayor masa → radio mayor.
- Mayor velocidad → radio mayor.
- Mayor carga o campo magnético → radio menor.

La fuerza magnética no realiza trabajo porque es perpendicular al desplazamiento
instantáneo. Por eso cambia la dirección de la velocidad, pero no su módulo.

Si la velocidad tiene componente paralela a B, la partícula sigue una trayectoria helicoidal:
- La componente perpendicular produce giro.
- La componente paralela avanza a lo largo del campo.

================================================================================
4. FUERZA MAGNÉTICA SOBRE UN CONDUCTOR CON CORRIENTE
================================================================================

Un conductor con corriente dentro de un campo magnético puede sentir fuerza:

F = I L × B

Módulo:

F = I L B sin(theta)

donde:
- I es la corriente.
- L es un vector con dirección de la corriente y módulo igual a la longitud del tramo.
- theta es el ángulo entre L y B.

Para un conductor recto:
- Si el conductor es paralelo a B, la fuerza es cero.
- Si es perpendicular a B, la fuerza es máxima.

================================================================================
5. FUERZA ENTRE DOS HILOS PARALELOS
================================================================================

Un hilo con corriente crea un campo magnético alrededor. Ese campo actúa sobre el otro
hilo si también tiene corriente.

Resultado cualitativo:
- Corrientes en el mismo sentido → los hilos se atraen.
- Corrientes en sentidos opuestos → los hilos se repelen.

Fuerza por unidad de longitud:

F/L = μ0 I1 I2 / (2πd)

donde d es la distancia entre los hilos.

================================================================================
6. FLUJO MAGNÉTICO
================================================================================

El flujo magnético mide cuánto campo magnético atraviesa una superficie.

Para campo uniforme y superficie plana:

Phi_B = B A cos(theta)

donde theta es el ángulo entre B y la normal a la superficie.

Unidad:
- Weber (Wb).

Importante:
- El flujo magnético es esencial para la Ley de Faraday, que aparece después.
- En magnetostática puede usarse para practicar área vectorial y orientación.
- El flujo se maximiza si B es perpendicular a la superficie.
- El flujo es cero si B es paralelo a la superficie.

================================================================================
7. BIOT-SAVART
================================================================================

La Ley de Biot-Savart permite calcular el campo magnético creado por un pequeño elemento
de corriente:

dB = (μ0/4π) I (dl × r_hat)/r²

o en módulo:

dB = (μ0/4π) I dl sin(theta)/r²

donde:
- dl es un elemento de longitud en la dirección de la corriente.
- r_hat apunta desde el elemento de corriente hacia el punto donde calculas B.
- r es la distancia desde el elemento hasta el punto.

Biot-Savart se usa cuando:
- El conductor tiene geometría finita o curva.
- Hay una espira.
- Hay un arco de circunferencia.
- No se puede usar Ampère fácilmente.

Consejo:
Biot-Savart suele ser más laborioso porque requiere integrar. Antes de integrar,
mira si la simetría cancela componentes.

================================================================================
8. CAMPO DE UN HILO RECTO LARGO
================================================================================

Para un hilo recto largo con corriente I, el campo magnético a distancia r es:

B = μ0 I / (2πr)

Las líneas de campo son circunferencias alrededor del hilo.

Dirección:
- Se usa la regla de la mano derecha.
- Pulgar en dirección de la corriente.
- Dedos indican el sentido de B alrededor del hilo.

Esto también se puede obtener con la Ley de Ampère usando una circunferencia como
trayectoria amperiana.

================================================================================
9. CAMPO EN EL CENTRO DE UNA ESPIRA CIRCULAR
================================================================================

Para una espira circular de radio R con corriente I, el campo magnético en el centro es:

B = μ0 I / (2R)

Si hay N espiras:

B = μ0 N I / (2R)

Dirección:
- Se usa la regla de la mano derecha.
- Dedos siguen la corriente.
- Pulgar indica el sentido de B en el eje de la espira.

================================================================================
10. LEY DE AMPÈRE
================================================================================

La Ley de Ampère dice:

∮ B · dl = μ0 I_enc

donde I_enc es la corriente encerrada por la trayectoria amperiana.

Ampère se parece a Gauss en estrategia:
- No siempre sirve para calcular B fácilmente.
- Es muy útil cuando hay simetría.
- La trayectoria se elige para que B sea constante o para que B·dl sea fácil.

Casos típicos:
- Hilo recto largo.
- Solenoide ideal.
- Toroide.
- Conductor cilíndrico largo.

================================================================================
11. SOLENOIDE IDEAL
================================================================================

Un solenoide es una bobina larga con muchas espiras.

Dentro de un solenoide ideal:

B = μ0 n I

donde:
- n=N/L es el número de espiras por unidad de longitud.

Características:
- Dentro del solenoide, B es aproximadamente uniforme.
- Fuera, el campo se suele aproximar como casi cero si es ideal y largo.
- La dirección se obtiene con la regla de la mano derecha.

================================================================================
12. TOROIDE
================================================================================

Un toroide es como un solenoide cerrado en forma de donut.

Campo dentro del toroide:

B = μ0 N I / (2πr)

donde r es la distancia al centro del toroide.

Características:
- El campo queda principalmente confinado dentro del toroide.
- La trayectoria amperiana natural es una circunferencia dentro del toroide.

================================================================================
13. MOMENTO MAGNÉTICO Y TORQUE EN UNA ESPIRA
================================================================================

Una espira con corriente se comporta como un dipolo magnético.

Momento magnético:

μ = N I A

Vectorialmente, μ apunta normal al plano de la espira según regla de la mano derecha.

Torque sobre una espira en un campo magnético:

τ = μ × B

Módulo:

τ = μ B sin(theta)

Esto aparece en motores eléctricos, donde una espira con corriente gira dentro de un
campo magnético.

================================================================================
14. CÓMO RECONOCER QUÉ LEY USAR
================================================================================

Si el enunciado dice:
"carga q se mueve con velocidad v en un campo B..."
→ fuerza magnética F=qv×B.

Si dice:
"trayectoria circular", "radio", "partícula en campo uniforme..."
→ combina fuerza magnética con fuerza centrípeta.

Si dice:
"conductor recto con corriente en campo B..."
→ F=IL×B.

Si dice:
"dos hilos paralelos..."
→ campo de un hilo + fuerza sobre el otro, o F/L=μ0I1I2/(2πd).

Si dice:
"hilo recto largo..."
→ B=μ0I/(2πr), normalmente con regla de la mano derecha.

Si dice:
"espira circular" o "centro de la espira..."
→ B=μ0I/(2R).

Si dice:
"trayectoria amperiana", "simetría", "solenoide", "toroide..."
→ Ley de Ampère.

Si dice:
"elemento de corriente", "arco", "segmento", "Biot-Savart..."
→ Ley de Biot-Savart.

Si dice:
"flujo magnético", "área", "normal", "ángulo..."
→ Phi_B=BAcos(theta).

================================================================================
15. ERRORES TÍPICOS DEL TEMA
================================================================================

- Olvidar que la fuerza magnética solo aparece si la carga se mueve.
- Usar F=qvB aunque v y B no sean perpendiculares.
- Olvidar el factor sin(theta).
- No invertir el sentido cuando la carga es negativa.
- Confundir B entrando en la pantalla con B saliendo.
- Pensar que el campo de un hilo apunta radialmente; en realidad rodea al hilo.
- Usar Ampère sin simetría suficiente.
- Confundir corriente encerrada con corriente total disponible.
- En flujo, usar el ángulo con la superficie en vez de con la normal.
- Confundir solenoide con toroide.
- Usar el radio de la espira donde va la distancia al punto, o al revés.
- Olvidar que μ0=4π x 10^-7 T m/A.
""",

    "formulas": [
        {
            "nombre": "Fuerza magnética sobre una carga",
            "idea_clave": "Una carga en movimiento en un campo magnético siente una fuerza perpendicular a v y a B.",
            "formula_base": "F = q v × B",
            "formula_principal": "|F| = |q| v B sin(theta)",
            "sale_de": [
                "Experimentalmente, la fuerza magnética depende de la carga, la velocidad y el campo magnético.",
                "La fuerza es perpendicular tanto a v como a B, por eso se expresa con producto vectorial.",
                "El módulo del producto vectorial v×B es vBsin(theta)."
            ],
            "despejes": [
                "|q| = F/(vBsin(theta))",
                "v = F/(|q|Bsin(theta))",
                "B = F/(|q|v sin(theta))",
                "sin(theta)=F/(|q|vB)"
            ],
            "formulas_relacionadas": [
                "F_c = mv²/r",
                "r = mv/(|q|B)",
                "F = I L × B",
                "Phi_B = BAcos(theta)"
            ],
            "uso": "Calcular fuerza magnética sobre una partícula cargada en movimiento.",
            "cuando_usarla": [
                "Cuando aparece una carga q moviéndose con velocidad v en un campo B.",
                "Cuando piden dirección de la fuerza magnética.",
                "Cuando se habla de trayectoria circular o desviación de partículas."
            ],
            "procedimiento": [
                "Identifica q, v, B y el ángulo entre v y B.",
                "Calcula el módulo con |F|=|q|vBsin(theta).",
                "Usa regla de la mano derecha para q positiva.",
                "Si q es negativa, invierte el sentido.",
                "Recuerda que F es perpendicular a v y a B."
            ],
            "detalles": [
                "Si v es paralela a B, la fuerza es cero.",
                "Si v es perpendicular a B, la fuerza es máxima.",
                "La fuerza magnética no realiza trabajo porque es perpendicular al desplazamiento instantáneo."
            ],
            "errores_tipicos": [
                "Olvidar el sin(theta).",
                "No invertir dirección para carga negativa.",
                "Confundir el sentido de B entrando/saliendo del plano.",
                "Usar esta fórmula para una carga en reposo."
            ],
            "mini_ejemplo": {
                "enunciado": "Una carga positiva se mueve hacia la derecha y B entra en la pantalla.",
                "pasos": [
                    "v apunta hacia +x.",
                    "B entra en la pantalla.",
                    "Para q positiva, v×B apunta hacia arriba.",
                    "Si la carga fuese negativa, la fuerza sería hacia abajo."
                ],
                "resultado": "F perpendicular a v y a B."
            }
        },
        {
            "nombre": "Movimiento circular de una carga en B uniforme",
            "idea_clave": "Si v es perpendicular a B, la fuerza magnética actúa como fuerza centrípeta.",
            "formula_base": "|q|vB = mv²/r",
            "formula_principal": "r = mv/(|q|B)",
            "sale_de": [
                "La fuerza magnética para v perpendicular a B es F=|q|vB.",
                "En movimiento circular uniforme la fuerza centrípeta es F_c=mv²/r.",
                "Igualando |q|vB=mv²/r y simplificando v se obtiene r=mv/(|q|B)."
            ],
            "despejes": [
                "m = r|q|B/v",
                "v = r|q|B/m",
                "|q| = mv/(rB)",
                "B = mv/(r|q|)"
            ],
            "formulas_relacionadas": [
                "F = q v × B",
                "F_c = mv²/r",
                "omega = |q|B/m",
                "T = 2πm/(|q|B)"
            ],
            "uso": "Resolver trayectorias circulares de partículas cargadas en campos magnéticos.",
            "cuando_usarla": [
                "Cuando el enunciado menciona radio de trayectoria.",
                "Cuando una partícula entra perpendicularmente a B.",
                "Cuando piden masa, carga, velocidad o campo a partir de la curvatura."
            ],
            "procedimiento": [
                "Comprueba que v sea perpendicular a B.",
                "Escribe F_magnética=F_centrípeta.",
                "Sustituye |q|vB=mv²/r.",
                "Despeja la magnitud pedida."
            ],
            "detalles": [
                "El campo magnético cambia la dirección de v, no su módulo.",
                "Si hay componente paralela a B, la trayectoria es helicoidal.",
                "El radio aumenta con masa y velocidad."
            ],
            "errores_tipicos": [
                "Usar energía cinética como si el campo hiciera trabajo.",
                "Olvidar simplificar una v.",
                "No usar valor absoluto de la carga para el radio."
            ]
        },
        {
            "nombre": "Frecuencia angular ciclotrón",
            "idea_clave": "La frecuencia de giro de una carga en B uniforme no depende de la velocidad si el modelo es no relativista.",
            "formula_base": "omega = v/r",
            "formula_principal": "omega = |q|B/m",
            "sale_de": [
                "Para movimiento circular, omega=v/r.",
                "Del radio magnético r=mv/(|q|B).",
                "Sustituyendo: omega=v/(mv/(|q|B))=|q|B/m."
            ],
            "despejes": [
                "|q| = omega m/B",
                "B = omega m/|q|",
                "m = |q|B/omega",
                "T = 2π/omega = 2πm/(|q|B)"
            ],
            "formulas_relacionadas": [
                "r = mv/(|q|B)",
                "F = |q|vB",
                "f = omega/(2π)"
            ],
            "uso": "Problemas de partículas cargadas girando en campos magnéticos.",
            "cuando_usarla": [
                "Cuando piden periodo, frecuencia o velocidad angular.",
                "Cuando aparece movimiento circular en B uniforme.",
                "Cuando se comparan partículas por masa/carga."
            ],
            "procedimiento": [
                "Identifica q, m y B.",
                "Usa omega=|q|B/m.",
                "Si piden periodo, usa T=2π/omega.",
                "Si piden frecuencia, usa f=omega/(2π)."
            ],
            "errores_tipicos": [
                "Meter la velocidad en omega cuando no hace falta.",
                "Olvidar el valor absoluto de q.",
                "Confundir frecuencia angular omega con frecuencia f."
            ]
        },
        {
            "nombre": "Fuerza magnética sobre un conductor",
            "idea_clave": "Un conductor con corriente en un campo magnético siente fuerza porque sus cargas se mueven.",
            "formula_base": "F = I L × B",
            "formula_principal": "|F| = I L B sin(theta)",
            "sale_de": [
                "Una corriente es movimiento organizado de cargas.",
                "Cada carga móvil siente fuerza magnética qv×B.",
                "Al sumar el efecto sobre todas las cargas del tramo se obtiene F=IL×B."
            ],
            "despejes": [
                "I = F/(LBsin(theta))",
                "L = F/(IBsin(theta))",
                "B = F/(ILsin(theta))",
                "sin(theta)=F/(ILB)"
            ],
            "formulas_relacionadas": [
                "F = q v × B",
                "Torque en espira: tau=mu×B",
                "F/L = μ0 I1 I2/(2πd)"
            ],
            "uso": "Calcular fuerza sobre un alambre con corriente dentro de un campo magnético.",
            "cuando_usarla": [
                "Cuando hay un conductor recto de longitud L con corriente I.",
                "Cuando el conductor está dentro de un campo magnético B.",
                "Cuando piden dirección de fuerza sobre un cable."
            ],
            "procedimiento": [
                "Identifica la dirección de la corriente.",
                "Toma L en dirección de la corriente.",
                "Calcula módulo con ILBsin(theta).",
                "Usa regla de la mano derecha para L×B."
            ],
            "detalles": [
                "Si el conductor es paralelo a B, no hay fuerza.",
                "Si es perpendicular, la fuerza es máxima.",
                "La dirección del vector L sigue la corriente convencional."
            ],
            "errores_tipicos": [
                "Usar la longitud total aunque solo una parte esté dentro de B.",
                "Usar L como escalar sin dirección al buscar sentido.",
                "Olvidar el ángulo entre corriente y campo."
            ]
        },
        {
            "nombre": "Campo magnético de un hilo recto largo",
            "idea_clave": "Un hilo largo con corriente crea un campo circular alrededor del hilo.",
            "formula_base": "∮B·dl = μ0 I_enc",
            "formula_principal": "B = μ0 I/(2πr)",
            "sale_de": [
                "Se usa una trayectoria amperiana circular de radio r centrada en el hilo.",
                "Por simetría, B tiene el mismo módulo en toda la circunferencia.",
                "B es tangente a la trayectoria, así que ∮B·dl=B(2πr).",
                "Ampère da B(2πr)=μ0I.",
                "Despejando: B=μ0I/(2πr)."
            ],
            "despejes": [
                "I = B(2πr)/μ0",
                "r = μ0I/(2πB)",
                "μ0 = B(2πr)/I"
            ],
            "formulas_relacionadas": [
                "Ley de Ampère: ∮B·dl=μ0I_enc",
                "F = IL×B",
                "F/L = μ0I1I2/(2πd)"
            ],
            "uso": "Calcular el campo alrededor de un hilo recto muy largo.",
            "cuando_usarla": [
                "Cuando el problema dice hilo recto largo o conductor infinito.",
                "Cuando piden B a distancia r del hilo.",
                "Cuando se estudian fuerzas entre hilos paralelos."
            ],
            "procedimiento": [
                "Identifica I y la distancia r.",
                "Calcula B=μ0I/(2πr).",
                "Usa la regla de la mano derecha para el sentido.",
                "Dibuja líneas circulares alrededor del hilo."
            ],
            "detalles": [
                "B disminuye como 1/r.",
                "Las líneas de B no salen radialmente; rodean al hilo.",
                "μ0=4π×10^-7 T·m/A."
            ],
            "errores_tipicos": [
                "Dibujar B saliendo del hilo como si fuera campo eléctrico.",
                "Confundir r con diámetro.",
                "Olvidar el factor 2π."
            ]
        },
        {
            "nombre": "Fuerza entre dos hilos paralelos",
            "idea_clave": "Cada hilo crea un campo que ejerce fuerza sobre el otro.",
            "formula_base": "F = I L B",
            "formula_principal": "F/L = μ0 I1 I2/(2πd)",
            "sale_de": [
                "El campo creado por el hilo 1 a distancia d es B1=μ0I1/(2πd).",
                "El hilo 2 con corriente I2 siente fuerza F=I2 L B1.",
                "Dividiendo entre L: F/L=I2B1=μ0I1I2/(2πd)."
            ],
            "despejes": [
                "I1 = (F/L)(2πd)/(μ0I2)",
                "I2 = (F/L)(2πd)/(μ0I1)",
                "d = μ0I1I2/(2π(F/L))"
            ],
            "formulas_relacionadas": [
                "B = μ0I/(2πr)",
                "F = IL×B",
                "Regla de la mano derecha"
            ],
            "uso": "Calcular atracción o repulsión entre corrientes paralelas.",
            "cuando_usarla": [
                "Cuando hay dos hilos largos paralelos.",
                "Cuando piden fuerza por unidad de longitud.",
                "Cuando preguntan si se atraen o repelen."
            ],
            "procedimiento": [
                "Identifica I1, I2 y distancia d.",
                "Calcula F/L.",
                "Mismo sentido de corriente: atracción.",
                "Sentidos opuestos: repulsión."
            ],
            "detalles": [
                "El resultado se da por unidad de longitud si no se especifica L.",
                "Este fenómeno se usa para definir el ampere en formulaciones clásicas."
            ],
            "errores_tipicos": [
                "Decir que mismo sentido se repelen.",
                "Usar r² en vez de d.",
                "Olvidar que es fuerza por longitud."
            ]
        },
        {
            "nombre": "Flujo magnético",
            "idea_clave": "Mide cuánto campo magnético atraviesa una superficie.",
            "formula_base": "Phi_B = B A cos(theta)",
            "formula_principal": "Phi_B = ∫B·dA",
            "sale_de": [
                "El flujo cuenta la componente de B perpendicular a la superficie.",
                "El vector área apunta normal a la superficie.",
                "Para B uniforme y área plana, la componente normal es Bcos(theta).",
                "Entonces Phi_B=BAcos(theta)."
            ],
            "despejes": [
                "B = Phi_B/(Acos(theta))",
                "A = Phi_B/(Bcos(theta))",
                "cos(theta)=Phi_B/(BA)",
                "theta=arccos(Phi_B/(BA))"
            ],
            "formulas_relacionadas": [
                "Ley de Faraday: epsilon=-N dPhi_B/dt",
                "B de hilo: μ0I/(2πr)",
                "B de solenoide: μ0nI"
            ],
            "uso": "Calcular flujo magnético a través de una superficie.",
            "cuando_usarla": [
                "Cuando aparece una superficie, espira o bobina.",
                "Cuando se habla de flujo magnético.",
                "Cuando después se conecta con inducción."
            ],
            "procedimiento": [
                "Identifica el vector normal del área.",
                "Determina el ángulo theta entre B y la normal.",
                "Usa Phi_B=BAcos(theta).",
                "Cuida el signo si la orientación importa."
            ],
            "detalles": [
                "La unidad es Weber (Wb).",
                "Si B es paralelo a la superficie, el flujo es cero.",
                "Si B es perpendicular a la superficie, el flujo es máximo."
            ],
            "errores_tipicos": [
                "Usar el ángulo con la superficie en vez del ángulo con la normal.",
                "Olvidar multiplicar por N si hay varias espiras en Faraday.",
                "Confundir flujo con campo."
            ]
        },
        {
            "nombre": "Ley de Biot-Savart",
            "idea_clave": "Permite calcular B creado por elementos de corriente.",
            "formula_base": "dB = (μ0/4π) I (dl × r_hat)/r²",
            "formula_principal": "|dB| = (μ0/4π) I dl sin(theta)/r²",
            "sale_de": [
                "Un elemento de corriente I dl produce una pequeña contribución dB.",
                "La dirección viene dada por dl×r_hat.",
                "El módulo decrece como 1/r² y depende del ángulo por sin(theta).",
                "El campo total se obtiene integrando todas las contribuciones."
            ],
            "despejes": [
                "B = ∫dB",
                "dB = (μ0/4π) I dl sin(theta)/r²",
                "Para arco circular: B = μ0 I phi/(4πR) en el centro si phi está en radianes"
            ],
            "formulas_relacionadas": [
                "B centro espira = μ0I/(2R)",
                "B hilo largo = μ0I/(2πr)",
                "Regla de la mano derecha"
            ],
            "uso": "Calcular campos magnéticos cuando Ampère no simplifica directamente.",
            "cuando_usarla": [
                "Cuando hay espiras, arcos o segmentos finitos.",
                "Cuando el problema menciona Biot-Savart.",
                "Cuando se pide campo en el centro de una geometría curva."
            ],
            "procedimiento": [
                "Divide el conductor en elementos dl.",
                "Define r desde dl hasta el punto de observación.",
                "Determina la dirección con dl×r_hat.",
                "Usa simetría para cancelar componentes.",
                "Integra las componentes que sobreviven."
            ],
            "detalles": [
                "Es una ley integral vectorial.",
                "Antes de integrar, conviene analizar dirección y simetría.",
                "Para configuraciones estándar se usan resultados ya derivados."
            ],
            "errores_tipicos": [
                "Confundir r_hat con la dirección de la corriente.",
                "Olvidar el producto vectorial.",
                "No usar radianes en fórmulas de arco.",
                "Integrar módulos aunque las direcciones cambien sin analizar simetría."
            ]
        },
        {
            "nombre": "Campo en el centro de una espira circular",
            "idea_clave": "Una espira circular con corriente produce un campo perpendicular al plano de la espira en su centro.",
            "formula_base": "dB = (μ0/4π) I dl/R²",
            "formula_principal": "B = μ0 I/(2R)",
            "sale_de": [
                "En el centro de la espira, todos los elementos dl están a distancia R.",
                "dl es perpendicular a r_hat, por tanto sin(theta)=1.",
                "Todas las contribuciones dB apuntan en la misma dirección del eje.",
                "Integrando dl alrededor de la espira: ∫dl=2πR.",
                "B=(μ0/4π)I(2πR)/R²=μ0I/(2R)."
            ],
            "despejes": [
                "I = 2RB/μ0",
                "R = μ0I/(2B)",
                "Para N espiras: B = μ0NI/(2R)"
            ],
            "formulas_relacionadas": [
                "Biot-Savart",
                "Momento magnético μ=NIA",
                "Torque τ=μBsin(theta)"
            ],
            "uso": "Calcular campo en el centro de una espira o bobina circular.",
            "cuando_usarla": [
                "Cuando el punto está en el centro de una espira.",
                "Cuando te dan radio R y corriente I.",
                "Cuando hay N vueltas iguales."
            ],
            "procedimiento": [
                "Identifica R, I y número de espiras N.",
                "Usa B=μ0NI/(2R) si hay N espiras.",
                "Determina sentido con regla de la mano derecha."
            ],
            "detalles": [
                "El campo es perpendicular al plano de la espira.",
                "Si la corriente es antihoraria vista desde ti, B sale hacia ti.",
                "Si la corriente es horaria vista desde ti, B entra en la pantalla."
            ],
            "errores_tipicos": [
                "Usar la fórmula del hilo recto.",
                "Olvidar multiplicar por N.",
                "Confundir diámetro con radio."
            ]
        },
        {
            "nombre": "Campo de un arco circular en el centro",
            "idea_clave": "Un arco de corriente produce en el centro una fracción del campo de una espira completa.",
            "formula_base": "B_arco = (phi/(2π)) B_espira",
            "formula_principal": "B = μ0 I phi/(4πR)",
            "sale_de": [
                "El campo de una espira completa en el centro es μ0I/(2R).",
                "Un arco de ángulo phi representa la fracción phi/(2π) de la circunferencia.",
                "Entonces B=(phi/(2π))(μ0I/(2R))=μ0Iphi/(4πR)."
            ],
            "despejes": [
                "I = 4πRB/(μ0phi)",
                "phi = 4πRB/(μ0I)",
                "R = μ0Iphi/(4πB)"
            ],
            "formulas_relacionadas": [
                "Biot-Savart",
                "B espira = μ0I/(2R)",
                "Superposición de campos magnéticos"
            ],
            "uso": "Campos en el centro de arcos de circunferencia.",
            "cuando_usarla": [
                "Cuando hay un arco circular de radio R.",
                "Cuando el punto está en el centro del arco.",
                "Cuando el ángulo del arco está dado."
            ],
            "procedimiento": [
                "Convierte el ángulo a radianes.",
                "Usa B=μ0Iphi/(4πR).",
                "Determina el sentido con regla de la mano derecha.",
                "Suma contribuciones si hay varios arcos."
            ],
            "errores_tipicos": [
                "Usar grados en vez de radianes.",
                "Olvidar que tramos radiales pueden no aportar en el centro si dl es paralelo a r_hat.",
                "No sumar sentidos correctamente."
            ]
        },
        {
            "nombre": "Ley de Ampère",
            "idea_clave": "Relaciona la circulación de B con la corriente encerrada.",
            "formula_base": "∮ B · dl = μ0 I_enc",
            "formula_principal": "∮ B · dl = μ0 I_enc",
            "sale_de": [
                "Para corrientes estacionarias, el campo magnético rodea corrientes.",
                "La integral cerrada de B a lo largo de una curva mide esa circulación.",
                "Ampère dice que esa circulación depende de la corriente neta atravesando la superficie limitada por la curva."
            ],
            "despejes": [
                "I_enc = (1/μ0)∮B·dl",
                "B = μ0I_enc/(longitud de trayectoria) si B es constante y paralelo a dl",
                "Para circunferencia: B = μ0I_enc/(2πr)"
            ],
            "formulas_relacionadas": [
                "B hilo largo = μ0I/(2πr)",
                "B solenoide = μ0nI",
                "B toroide = μ0NI/(2πr)"
            ],
            "uso": "Calcular B cuando hay simetría suficiente.",
            "cuando_usarla": [
                "Hilo recto largo.",
                "Solenoide ideal.",
                "Toroide.",
                "Conductor cilíndrico largo.",
                "Cuando el enunciado menciona trayectoria amperiana."
            ],
            "procedimiento": [
                "Identifica la simetría del problema.",
                "Elige una trayectoria amperiana adecuada.",
                "Determina I_enc.",
                "Simplifica ∮B·dl.",
                "Despeja B."
            ],
            "detalles": [
                "Ampère siempre es válida en magnetostática, pero no siempre permite despejar B fácilmente.",
                "La corriente encerrada puede ser positiva o negativa según orientación.",
                "Se parece a Gauss en el uso de simetría."
            ],
            "errores_tipicos": [
                "Usar Ampère sin simetría.",
                "Confundir corriente encerrada con corriente total de todo el circuito.",
                "Olvidar que B debe ser paralelo o perpendicular a dl según el tramo.",
                "No usar una curva cerrada."
            ]
        },
        {
            "nombre": "Campo dentro de un solenoide ideal",
            "idea_clave": "Un solenoide largo produce un campo casi uniforme en su interior.",
            "formula_base": "∮B·dl = μ0 I_enc",
            "formula_principal": "B = μ0 n I",
            "sale_de": [
                "Se aplica Ampère a una trayectoria rectangular que pasa por dentro y fuera del solenoide.",
                "En un solenoide ideal, el campo exterior se aproxima a cero.",
                "Dentro, B es aproximadamente uniforme y paralelo al eje.",
                "La corriente encerrada es nL veces I, donde n es espiras por longitud.",
                "Ampère da BL=μ0(nL)I, por tanto B=μ0nI."
            ],
            "despejes": [
                "n = B/(μ0I)",
                "I = B/(μ0n)",
                "N = nL",
                "B = μ0(N/L)I"
            ],
            "formulas_relacionadas": [
                "Ley de Ampère",
                "Flujo magnético Phi_B=BA",
                "Inductancia en temas posteriores"
            ],
            "uso": "Calcular campo magnético dentro de solenoides ideales.",
            "cuando_usarla": [
                "Cuando el enunciado dice solenoide largo.",
                "Cuando te dan N, L e I.",
                "Cuando se asume campo uniforme interior."
            ],
            "procedimiento": [
                "Calcula n=N/L.",
                "Usa B=μ0nI.",
                "Determina dirección con la regla de la mano derecha."
            ],
            "detalles": [
                "La aproximación funciona bien para solenoides largos comparados con su radio.",
                "Fuera del solenoide ideal, B se aproxima como cero.",
                "Dentro, B va a lo largo del eje."
            ],
            "errores_tipicos": [
                "Usar N en vez de n=N/L.",
                "Aplicar la fórmula a un solenoide corto sin considerar aproximación.",
                "Confundir sentido del campo con sentido de corriente en las espiras."
            ]
        },
        {
            "nombre": "Campo dentro de un toroide",
            "idea_clave": "Un toroide confina el campo magnético principalmente en su interior.",
            "formula_base": "∮B·dl = μ0 I_enc",
            "formula_principal": "B = μ0 N I/(2πr)",
            "sale_de": [
                "Se usa una trayectoria amperiana circular de radio r dentro del toroide.",
                "Por simetría, B es tangente y casi constante sobre esa circunferencia.",
                "La integral es B(2πr).",
                "La corriente encerrada es NI.",
                "Ampère da B(2πr)=μ0NI."
            ],
            "despejes": [
                "N = B(2πr)/(μ0I)",
                "I = B(2πr)/(μ0N)",
                "r = μ0NI/(2πB)"
            ],
            "formulas_relacionadas": [
                "Ley de Ampère",
                "Solenoide ideal B=μ0nI",
                "Flujo magnético"
            ],
            "uso": "Calcular campo magnético en toroides.",
            "cuando_usarla": [
                "Cuando el enunciado dice toroide.",
                "Cuando hay N vueltas alrededor de un núcleo circular.",
                "Cuando piden B a un radio r dentro del toroide."
            ],
            "procedimiento": [
                "Elige circunferencia amperiana dentro del toroide.",
                "Determina r.",
                "Usa B=μ0NI/(2πr).",
                "Fuera del toroide ideal, el campo se suele aproximar como cero."
            ],
            "errores_tipicos": [
                "Usar n=N/L como en solenoide recto.",
                "Olvidar que B depende de r.",
                "Usar radio exterior/interior equivocado si el problema especifica una posición."
            ]
        },
        {
            "nombre": "Momento magnético de una espira",
            "idea_clave": "Una espira con corriente se comporta como un dipolo magnético.",
            "formula_base": "mu = I A",
            "formula_principal": "mu = N I A",
            "sale_de": [
                "La corriente circulando en un área crea un dipolo magnético.",
                "El módulo del momento magnético es corriente por área.",
                "Si hay N vueltas, cada vuelta aporta y se multiplica por N."
            ],
            "despejes": [
                "I = mu/(NA)",
                "A = mu/(NI)",
                "N = mu/(IA)"
            ],
            "formulas_relacionadas": [
                "Torque: tau=mu×B",
                "tau=muBsin(theta)",
                "Energía: U=-mu·B"
            ],
            "uso": "Describir espiras y bobinas como dipolos magnéticos.",
            "cuando_usarla": [
                "Cuando hay una espira con corriente.",
                "Cuando se pide torque o energía en un campo B.",
                "Cuando el problema menciona momento dipolar magnético."
            ],
            "procedimiento": [
                "Calcula el área de la espira.",
                "Multiplica por I y por N si hay varias vueltas.",
                "Determina dirección de mu con regla de la mano derecha."
            ],
            "detalles": [
                "La dirección de mu es normal al plano de la espira.",
                "Dedos siguen la corriente; pulgar indica mu."
            ],
            "errores_tipicos": [
                "Usar perímetro en vez de área.",
                "Olvidar N.",
                "Confundir dirección de corriente con dirección de mu."
            ]
        },
        {
            "nombre": "Torque sobre una espira en campo magnético",
            "idea_clave": "Un campo magnético tiende a alinear el momento magnético de una espira con B.",
            "formula_base": "tau = mu × B",
            "formula_principal": "|tau| = mu B sin(theta) = N I A B sin(theta)",
            "sale_de": [
                "Los lados opuestos de una espira con corriente pueden sentir fuerzas magnéticas opuestas.",
                "Estas fuerzas forman un par de fuerzas.",
                "Ese par produce un torque que intenta alinear mu con B."
            ],
            "despejes": [
                "mu = tau/(Bsin(theta))",
                "B = tau/(mu sin(theta))",
                "I = tau/(NABsin(theta))",
                "A = tau/(NIBsin(theta))"
            ],
            "formulas_relacionadas": [
                "mu=NIA",
                "F=IL×B",
                "U=-mu·B"
            ],
            "uso": "Resolver espiras, bobinas y motores en campos magnéticos.",
            "cuando_usarla": [
                "Cuando una espira con corriente está en un campo B.",
                "Cuando piden torque máximo.",
                "Cuando se menciona rotación de una bobina."
            ],
            "procedimiento": [
                "Calcula mu=NIA.",
                "Identifica el ángulo entre mu y B.",
                "Usa tau=muBsin(theta).",
                "Dirección con regla de la mano derecha para producto vectorial."
            ],
            "detalles": [
                "Torque máximo si mu es perpendicular a B.",
                "Torque cero si mu es paralelo o antiparalelo a B.",
                "Este principio aparece en motores eléctricos."
            ],
            "errores_tipicos": [
                "Usar ángulo entre el plano de la espira y B en vez de entre mu y B.",
                "Olvidar que mu es normal al plano.",
                "Confundir torque con fuerza neta."
            ]
        },
        {
            "nombre": "Energía de un dipolo magnético",
            "idea_clave": "Un dipolo magnético tiene energía potencial según su orientación respecto a B.",
            "formula_base": "U = -mu · B",
            "formula_principal": "U = -mu B cos(theta)",
            "sale_de": [
                "El campo magnético ejerce un torque que tiende a alinear mu con B.",
                "La energía potencial es mínima cuando mu y B están alineados.",
                "La forma escalar que cumple esto es U=-muBcos(theta)."
            ],
            "despejes": [
                "mu = -U/(Bcos(theta))",
                "B = -U/(mu cos(theta))",
                "cos(theta) = -U/(muB)"
            ],
            "formulas_relacionadas": [
                "tau=mu×B",
                "mu=NIA",
                "Trabajo asociado a rotación"
            ],
            "uso": "Problemas de orientación de espiras o dipolos magnéticos.",
            "cuando_usarla": [
                "Cuando se habla de energía potencial de una espira.",
                "Cuando piden configuración estable.",
                "Cuando se compara orientación paralela y antiparalela."
            ],
            "procedimiento": [
                "Calcula mu.",
                "Identifica theta entre mu y B.",
                "Usa U=-muBcos(theta).",
                "Compara energías si hay varias orientaciones."
            ],
            "detalles": [
                "Mínimo de energía: mu paralelo a B.",
                "Máximo de energía: mu antiparalelo a B."
            ],
            "errores_tipicos": [
                "Usar seno en energía en vez de coseno.",
                "Confundir el ángulo del plano de la espira con el de mu.",
                "Olvidar el signo menos."
            ]
        }
    ],

    "interpretacion_enunciados": [
        {
            "palabra_clave": "carga moviéndose en un campo B",
            "que_significa": "Te piden fuerza magnética sobre una partícula cargada.",
            "que_suele_pedir": [
                "Módulo de la fuerza.",
                "Dirección de la fuerza.",
                "Si la partícula se desvía hacia arriba/abajo/dentro/fuera.",
                "Condición para que no haya fuerza."
            ],
            "operaciones_recomendadas": [
                "Identifica q, v y B.",
                "Calcula |F|=|q|vBsin(theta).",
                "Usa regla de la mano derecha para q positiva.",
                "Invierte el sentido si q es negativa.",
                "Recuerda que F es perpendicular a v y B."
            ],
            "pista_examen": "Si v es paralela a B, la fuerza magnética es cero."
        },
        {
            "palabra_clave": "trayectoria circular / radio de giro",
            "que_significa": "La fuerza magnética actúa como fuerza centrípeta.",
            "que_suele_pedir": [
                "Radio de la trayectoria.",
                "Velocidad de la partícula.",
                "Masa o carga.",
                "Campo magnético necesario.",
                "Periodo o frecuencia."
            ],
            "operaciones_recomendadas": [
                "Comprueba si v es perpendicular a B.",
                "Iguala |q|vB=mv²/r.",
                "Usa r=mv/(|q|B).",
                "Si piden periodo, usa T=2πm/(|q|B)."
            ],
            "pista_examen": "El campo magnético no cambia la rapidez, solo la dirección."
        },
        {
            "palabra_clave": "conductor con corriente dentro de B",
            "que_significa": "Te piden fuerza magnética sobre un cable.",
            "que_suele_pedir": [
                "Fuerza sobre un tramo recto.",
                "Dirección de la fuerza.",
                "Corriente o longitud necesaria.",
                "Equilibrio de un conductor."
            ],
            "operaciones_recomendadas": [
                "Identifica dirección de la corriente.",
                "Usa F=ILBsin(theta).",
                "Para dirección, usa L×B.",
                "Si el cable es paralelo a B, F=0."
            ],
            "pista_examen": "El vector L va en la dirección de la corriente convencional."
        },
        {
            "palabra_clave": "hilo recto largo",
            "que_significa": "Te piden campo magnético circular alrededor del hilo.",
            "que_suele_pedir": [
                "Campo B a distancia r.",
                "Dirección del campo.",
                "Fuerza sobre otra corriente cercana.",
                "Superposición de campos de varios hilos."
            ],
            "operaciones_recomendadas": [
                "Usa B=μ0I/(2πr).",
                "Dibuja circunferencias alrededor del hilo.",
                "Usa regla de la mano derecha.",
                "Si hay varios hilos, suma B vectorialmente."
            ],
            "pista_examen": "El campo de un hilo no apunta radialmente: rodea al hilo."
        },
        {
            "palabra_clave": "dos hilos paralelos",
            "que_significa": "Hay interacción magnética entre corrientes.",
            "que_suele_pedir": [
                "Atracción o repulsión.",
                "Fuerza por unidad de longitud.",
                "Distancia entre hilos.",
                "Corriente desconocida."
            ],
            "operaciones_recomendadas": [
                "Usa F/L=μ0I1I2/(2πd).",
                "Mismo sentido de corriente: atracción.",
                "Sentidos opuestos: repulsión.",
                "Dibuja el campo de un hilo en la posición del otro."
            ],
            "pista_examen": "Mismo sentido atrae; sentido contrario repele."
        },
        {
            "palabra_clave": "flujo magnético",
            "que_significa": "Te piden B atravesando un área.",
            "que_suele_pedir": [
                "Phi_B.",
                "Ángulo de una espira respecto al campo.",
                "Área o campo desconocido.",
                "Preparación para Faraday."
            ],
            "operaciones_recomendadas": [
                "Identifica la normal del área.",
                "Usa theta entre B y la normal.",
                "Aplica Phi_B=BAcos(theta).",
                "Si hay N espiras en Faraday, se multiplicará por N."
            ],
            "pista_examen": "Igual que en flujo eléctrico: el ángulo es con la normal."
        },
        {
            "palabra_clave": "Biot-Savart / elemento de corriente",
            "que_significa": "Probablemente debes integrar contribuciones de corriente.",
            "que_suele_pedir": [
                "Campo de un arco.",
                "Campo de una espira.",
                "Campo de un segmento finito.",
                "Dirección de dB."
            ],
            "operaciones_recomendadas": [
                "Escribe dB=(μ0/4π)I(dl×r_hat)/r².",
                "Analiza dirección con producto vectorial.",
                "Usa simetría para cancelar componentes.",
                "Integra solo lo que sobrevive."
            ],
            "pista_examen": "Antes de integrar, mira la simetría: muchas componentes se cancelan."
        },
        {
            "palabra_clave": "espira circular / centro de la espira",
            "que_significa": "Puedes usar fórmula estándar de Biot-Savart para una espira.",
            "que_suele_pedir": [
                "Campo en el centro.",
                "Sentido del campo.",
                "Efecto de N vueltas.",
                "Corriente necesaria para cierto B."
            ],
            "operaciones_recomendadas": [
                "Usa B=μ0I/(2R).",
                "Si hay N espiras, usa B=μ0NI/(2R).",
                "Dirección con regla de la mano derecha.",
                "No olvides que R es radio."
            ],
            "pista_examen": "Dedos siguen la corriente de la espira; pulgar da dirección de B en el centro."
        },
        {
            "palabra_clave": "trayectoria amperiana / simetría",
            "que_significa": "El ejercicio quiere Ley de Ampère.",
            "que_suele_pedir": [
                "Campo de hilo largo.",
                "Campo de solenoide.",
                "Campo de toroide.",
                "Campo dentro/fuera de un conductor cilíndrico."
            ],
            "operaciones_recomendadas": [
                "Elige una curva cerrada adecuada.",
                "Calcula I_enc.",
                "Simplifica ∮B·dl.",
                "Despeja B si la simetría lo permite."
            ],
            "pista_examen": "Ampère funciona como Gauss: la ley siempre vale, pero solo simplifica con simetría."
        },
        {
            "palabra_clave": "solenoide largo",
            "que_significa": "Campo magnético casi uniforme dentro de una bobina larga.",
            "que_suele_pedir": [
                "Campo dentro del solenoide.",
                "Número de espiras por longitud.",
                "Corriente necesaria.",
                "Sentido del campo."
            ],
            "operaciones_recomendadas": [
                "Calcula n=N/L.",
                "Usa B=μ0nI.",
                "Aproxima B exterior como cero si el solenoide es ideal.",
                "Dirección con regla de la mano derecha."
            ],
            "pista_examen": "No uses N directamente: usa n=N/L."
        },
        {
            "palabra_clave": "toroide",
            "que_significa": "Solenoide cerrado; se usa Ampère con circunferencia interna.",
            "que_suele_pedir": [
                "Campo dentro del toroide.",
                "Campo fuera idealmente.",
                "Dependencia con r.",
                "Corriente o número de vueltas."
            ],
            "operaciones_recomendadas": [
                "Usa B=μ0NI/(2πr) dentro.",
                "Elige una trayectoria circular dentro del toroide.",
                "Aproxima campo exterior como cero si es ideal."
            ],
            "pista_examen": "En el toroide B depende de r; en el solenoide ideal recto B≈μ0nI."
        },
        {
            "palabra_clave": "espira en un campo magnético / torque",
            "que_significa": "La espira tiene momento magnético y puede girar.",
            "que_suele_pedir": [
                "Torque sobre la espira.",
                "Momento magnético.",
                "Orientación estable.",
                "Energía potencial."
            ],
            "operaciones_recomendadas": [
                "Calcula μ=NIA.",
                "Determina dirección de μ con regla de la mano derecha.",
                "Usa τ=μBsin(theta).",
                "Si piden energía, usa U=-μBcos(theta)."
            ],
            "pista_examen": "El ángulo es entre μ y B, no necesariamente entre el plano de la espira y B."
        }
    ],

    "flashcards": [
        {"id": "fis2_fc_001", "frente": "¿Fórmula vectorial de fuerza magnética sobre una carga?", "reverso": "F = q v × B.", "categoria": "Fuerza magnética"},
        {"id": "fis2_fc_002", "frente": "¿Módulo de fuerza magnética sobre una carga?", "reverso": "|F|=|q|vBsin(theta).", "categoria": "Fuerza magnética"},
        {"id": "fis2_fc_003", "frente": "¿Cuándo es cero la fuerza magnética sobre una carga?", "reverso": "Si v es paralela/antiparalela a B, si v=0 o si q=0.", "categoria": "Fuerza magnética"},
        {"id": "fis2_fc_004", "frente": "¿Qué haces si la carga es negativa al usar regla de la mano derecha?", "reverso": "Inviertes el sentido obtenido para v×B.", "categoria": "Fuerza magnética"},
        {"id": "fis2_fc_005", "frente": "¿La fuerza magnética realiza trabajo?", "reverso": "No, porque es perpendicular a la velocidad.", "categoria": "Fuerza magnética"},
        {"id": "fis2_fc_006", "frente": "¿Radio de giro de una carga en B perpendicular?", "reverso": "r=mv/(|q|B).", "categoria": "Movimiento circular"},
        {"id": "fis2_fc_007", "frente": "¿Frecuencia angular ciclotrón?", "reverso": "omega=|q|B/m.", "categoria": "Movimiento circular"},
        {"id": "fis2_fc_008", "frente": "¿Fuerza sobre conductor con corriente?", "reverso": "F=IL×B.", "categoria": "Conductor"},
        {"id": "fis2_fc_009", "frente": "¿Módulo de fuerza sobre conductor recto?", "reverso": "F=ILBsin(theta).", "categoria": "Conductor"},
        {"id": "fis2_fc_010", "frente": "¿Campo alrededor de un hilo recto largo?", "reverso": "B=μ0I/(2πr).", "categoria": "Hilo recto"},
        {"id": "fis2_fc_011", "frente": "¿Forma de las líneas de B alrededor de un hilo recto?", "reverso": "Circunferencias alrededor del hilo.", "categoria": "Hilo recto"},
        {"id": "fis2_fc_012", "frente": "¿Cómo determinas el sentido de B alrededor de un hilo?", "reverso": "Regla de la mano derecha: pulgar corriente, dedos B.", "categoria": "Hilo recto"},
        {"id": "fis2_fc_013", "frente": "¿Qué pasa con dos hilos con corriente en el mismo sentido?", "reverso": "Se atraen.", "categoria": "Hilos paralelos"},
        {"id": "fis2_fc_014", "frente": "¿Qué pasa con dos hilos con corrientes opuestas?", "reverso": "Se repelen.", "categoria": "Hilos paralelos"},
        {"id": "fis2_fc_015", "frente": "¿Fuerza por longitud entre hilos paralelos?", "reverso": "F/L=μ0I1I2/(2πd).", "categoria": "Hilos paralelos"},
        {"id": "fis2_fc_016", "frente": "¿Flujo magnético en campo uniforme?", "reverso": "Phi_B=BAcos(theta).", "categoria": "Flujo magnético"},
        {"id": "fis2_fc_017", "frente": "En flujo magnético, ¿theta es con la superficie o la normal?", "reverso": "Con la normal.", "categoria": "Flujo magnético"},
        {"id": "fis2_fc_018", "frente": "¿Ley de Biot-Savart?", "reverso": "dB=(μ0/4π)I(dl×r_hat)/r².", "categoria": "Biot-Savart"},
        {"id": "fis2_fc_019", "frente": "¿Campo en el centro de una espira circular?", "reverso": "B=μ0I/(2R).", "categoria": "Espira"},
        {"id": "fis2_fc_020", "frente": "¿Campo en el centro de N espiras?", "reverso": "B=μ0NI/(2R).", "categoria": "Espira"},
        {"id": "fis2_fc_021", "frente": "¿Ley de Ampère?", "reverso": "∮B·dl=μ0I_enc.", "categoria": "Ampère"},
        {"id": "fis2_fc_022", "frente": "¿Cuándo conviene usar Ampère?", "reverso": "Con simetría: hilo largo, solenoide, toroide.", "categoria": "Ampère"},
        {"id": "fis2_fc_023", "frente": "¿Campo dentro de un solenoide ideal?", "reverso": "B=μ0nI.", "categoria": "Solenoide"},
        {"id": "fis2_fc_024", "frente": "¿Qué es n en un solenoide?", "reverso": "Número de espiras por unidad de longitud: n=N/L.", "categoria": "Solenoide"},
        {"id": "fis2_fc_025", "frente": "¿Campo dentro de un toroide?", "reverso": "B=μ0NI/(2πr).", "categoria": "Toroide"},
        {"id": "fis2_fc_026", "frente": "¿Momento magnético de una espira?", "reverso": "μ=NIA.", "categoria": "Dipolo magnético"},
        {"id": "fis2_fc_027", "frente": "¿Torque sobre una espira?", "reverso": "τ=μ×B, módulo τ=μBsin(theta).", "categoria": "Torque"},
        {"id": "fis2_fc_028", "frente": "¿Energía de un dipolo magnético?", "reverso": "U=-μ·B=-μBcos(theta).", "categoria": "Dipolo magnético"},
        {"id": "fis2_fc_029", "frente": "¿Valor de μ0?", "reverso": "μ0=4π×10^-7 T·m/A.", "categoria": "Constantes"},
        {"id": "fis2_fc_030", "frente": "¿Qué significa una × en diagramas de B?", "reverso": "Campo entrando en la pantalla.", "categoria": "Dirección"},
        {"id": "fis2_fc_031", "frente": "¿Qué significa un punto • en diagramas de B?", "reverso": "Campo saliendo de la pantalla.", "categoria": "Dirección"},
        {"id": "fis2_fc_032", "frente": "¿Qué trayectoria amperiana usas para un hilo largo?", "reverso": "Una circunferencia centrada en el hilo.", "categoria": "Ampère"},
        {"id": "fis2_fc_033", "frente": "¿Qué trayectoria amperiana usas para un toroide?", "reverso": "Una circunferencia dentro del toroide.", "categoria": "Ampère"},
        {"id": "fis2_fc_034", "frente": "¿Qué ley usarías para un arco circular de corriente?", "reverso": "Biot-Savart.", "categoria": "Biot-Savart"},
        {"id": "fis2_fc_035", "frente": "¿Campo de un arco circular de ángulo phi en el centro?", "reverso": "B=μ0Iphi/(4πR), con phi en radianes.", "categoria": "Biot-Savart"}
    ],

    "preguntas_vf": [
        {"id": "fis2_vf_001", "pregunta": "Una carga en reposo en un campo magnético uniforme siente fuerza magnética.", "respuesta": False, "explicacion": "La fuerza magnética sobre una carga es qv×B; si v=0, F=0.", "categoria": "Fuerza magnética", "dificultad": "facil"},
        {"id": "fis2_vf_002", "pregunta": "Si v es paralela a B, la fuerza magnética es máxima.", "respuesta": False, "explicacion": "Si v es paralela a B, sin(theta)=0 y F=0.", "categoria": "Fuerza magnética", "dificultad": "facil"},
        {"id": "fis2_vf_003", "pregunta": "Si v es perpendicular a B, la fuerza magnética tiene módulo |q|vB.", "respuesta": True, "explicacion": "Para theta=90°, sin(theta)=1.", "categoria": "Fuerza magnética", "dificultad": "facil"},
        {"id": "fis2_vf_004", "pregunta": "La fuerza magnética es perpendicular a la velocidad.", "respuesta": True, "explicacion": "F=qv×B, producto vectorial perpendicular a v y B.", "categoria": "Fuerza magnética", "dificultad": "facil"},
        {"id": "fis2_vf_005", "pregunta": "Para una carga negativa se invierte la dirección obtenida con v×B.", "respuesta": True, "explicacion": "El factor q negativo cambia el sentido de la fuerza.", "categoria": "Fuerza magnética", "dificultad": "facil"},
        {"id": "fis2_vf_006", "pregunta": "La fuerza magnética realiza trabajo sobre una carga y aumenta su rapidez.", "respuesta": False, "explicacion": "La fuerza magnética es perpendicular a v, por eso no realiza trabajo.", "categoria": "Fuerza magnética", "dificultad": "media"},
        {"id": "fis2_vf_007", "pregunta": "Una carga que entra perpendicularmente a B puede describir una trayectoria circular.", "respuesta": True, "explicacion": "La fuerza magnética actúa como fuerza centrípeta.", "categoria": "Movimiento circular", "dificultad": "facil"},
        {"id": "fis2_vf_008", "pregunta": "El radio de giro magnético es r=mv/(|q|B).", "respuesta": True, "explicacion": "Sale de igualar |q|vB=mv²/r.", "categoria": "Movimiento circular", "dificultad": "facil"},
        {"id": "fis2_vf_009", "pregunta": "Si aumenta B, el radio de la trayectoria aumenta.", "respuesta": False, "explicacion": "r=mv/(|q|B), así que si B aumenta, r disminuye.", "categoria": "Movimiento circular", "dificultad": "media"},
        {"id": "fis2_vf_010", "pregunta": "La fuerza sobre un conductor con corriente es F=IL×B.", "respuesta": True, "explicacion": "Es la forma vectorial para un tramo recto de conductor.", "categoria": "Conductor", "dificultad": "facil"},
        {"id": "fis2_vf_011", "pregunta": "Si un conductor con corriente es paralelo a B, la fuerza magnética sobre él es cero.", "respuesta": True, "explicacion": "El ángulo es 0 y sin(theta)=0.", "categoria": "Conductor", "dificultad": "facil"},
        {"id": "fis2_vf_012", "pregunta": "El campo magnético alrededor de un hilo recto largo apunta radialmente hacia afuera.", "respuesta": False, "explicacion": "Las líneas de B son circunferencias alrededor del hilo.", "categoria": "Hilo recto", "dificultad": "facil"},
        {"id": "fis2_vf_013", "pregunta": "Para un hilo recto largo, B=μ0I/(2πr).", "respuesta": True, "explicacion": "Es el resultado estándar por Ampère o Biot-Savart.", "categoria": "Hilo recto", "dificultad": "facil"},
        {"id": "fis2_vf_014", "pregunta": "Dos hilos paralelos con corrientes en el mismo sentido se atraen.", "respuesta": True, "explicacion": "Es el resultado magnético entre corrientes paralelas.", "categoria": "Hilos paralelos", "dificultad": "facil"},
        {"id": "fis2_vf_015", "pregunta": "Dos hilos paralelos con corrientes opuestas se atraen.", "respuesta": False, "explicacion": "Corrientes opuestas se repelen.", "categoria": "Hilos paralelos", "dificultad": "facil"},
        {"id": "fis2_vf_016", "pregunta": "El flujo magnético se calcula con el ángulo entre B y la superficie.", "respuesta": False, "explicacion": "Se usa el ángulo entre B y la normal de la superficie.", "categoria": "Flujo magnético", "dificultad": "media"},
        {"id": "fis2_vf_017", "pregunta": "Si B es paralelo a una superficie, el flujo magnético a través de ella es cero.", "respuesta": True, "explicacion": "B no atraviesa la superficie; el ángulo con la normal es 90°.", "categoria": "Flujo magnético", "dificultad": "facil"},
        {"id": "fis2_vf_018", "pregunta": "La Ley de Biot-Savart usa un producto vectorial dl×r_hat.", "respuesta": True, "explicacion": "La dirección de dB viene de ese producto vectorial.", "categoria": "Biot-Savart", "dificultad": "media"},
        {"id": "fis2_vf_019", "pregunta": "Biot-Savart siempre evita integrar.", "respuesta": False, "explicacion": "Biot-Savart normalmente requiere integrar contribuciones dB.", "categoria": "Biot-Savart", "dificultad": "media"},
        {"id": "fis2_vf_020", "pregunta": "El campo en el centro de una espira circular es B=μ0I/(2R).", "respuesta": True, "explicacion": "Es el resultado estándar para una espira de radio R.", "categoria": "Espira", "dificultad": "facil"},
        {"id": "fis2_vf_021", "pregunta": "Para N espiras iguales, el campo en el centro se multiplica por N.", "respuesta": True, "explicacion": "Cada espira aporta el mismo campo en el centro.", "categoria": "Espira", "dificultad": "facil"},
        {"id": "fis2_vf_022", "pregunta": "La Ley de Ampère es ∮B·dl=μ0I_enc.", "respuesta": True, "explicacion": "Es la forma magnetostática de Ampère.", "categoria": "Ampère", "dificultad": "facil"},
        {"id": "fis2_vf_023", "pregunta": "Ampère siempre permite calcular B fácilmente aunque no haya simetría.", "respuesta": False, "explicacion": "La ley es válida, pero solo simplifica con simetría.", "categoria": "Ampère", "dificultad": "media"},
        {"id": "fis2_vf_024", "pregunta": "En un solenoide ideal largo, B=μ0nI.", "respuesta": True, "explicacion": "n es el número de espiras por unidad de longitud.", "categoria": "Solenoide", "dificultad": "facil"},
        {"id": "fis2_vf_025", "pregunta": "En un solenoide, n significa número total de espiras.", "respuesta": False, "explicacion": "n=N/L, espiras por unidad de longitud.", "categoria": "Solenoide", "dificultad": "media"},
        {"id": "fis2_vf_026", "pregunta": "En un toroide ideal, el campo dentro puede escribirse B=μ0NI/(2πr).", "respuesta": True, "explicacion": "Sale de Ampère con trayectoria circular interna.", "categoria": "Toroide", "dificultad": "media"},
        {"id": "fis2_vf_027", "pregunta": "El momento magnético de una espira es paralelo al plano de la espira.", "respuesta": False, "explicacion": "El momento magnético es perpendicular al plano de la espira.", "categoria": "Dipolo magnético", "dificultad": "media"},
        {"id": "fis2_vf_028", "pregunta": "El torque sobre una espira es máximo cuando μ es perpendicular a B.", "respuesta": True, "explicacion": "τ=μBsin(theta), máximo para theta=90°.", "categoria": "Torque", "dificultad": "media"},
        {"id": "fis2_vf_029", "pregunta": "La energía U=-μBcos(theta) es mínima cuando μ y B están alineados.", "respuesta": True, "explicacion": "Si theta=0, U=-μB, el valor mínimo.", "categoria": "Dipolo magnético", "dificultad": "dificil"},
        {"id": "fis2_vf_030", "pregunta": "En un dibujo, una cruz × suele indicar campo entrando en la pantalla.", "respuesta": True, "explicacion": "Se usa como la cola de una flecha que se aleja de ti.", "categoria": "Dirección", "dificultad": "facil"}
    ],

    "preguntas_mc": [
        {
            "id": "fis2_mc_001",
            "pregunta": "¿Qué fórmula representa la fuerza magnética sobre una carga?",
            "opciones": ["F=qv×B", "F=kq1q2/r²", "V=IR", "Phi=EAcos(theta)"],
            "respuesta": 1,
            "explicacion": "La fuerza magnética sobre una carga móvil es F=qv×B.",
            "categoria": "Fuerza magnética",
            "dificultad": "facil"
        },
        {
            "id": "fis2_mc_002",
            "pregunta": "Si v es paralela a B, la fuerza magnética es:",
            "opciones": ["Máxima", "Cero", "Igual a qvB", "Infinita"],
            "respuesta": 2,
            "explicacion": "F=|q|vBsin(theta); si theta=0, F=0.",
            "categoria": "Fuerza magnética",
            "dificultad": "facil"
        },
        {
            "id": "fis2_mc_003",
            "pregunta": "Si la carga es negativa, la dirección de F respecto a v×B es:",
            "opciones": ["La misma", "La opuesta", "Siempre hacia arriba", "Siempre nula"],
            "respuesta": 2,
            "explicacion": "El signo negativo de q invierte el sentido.",
            "categoria": "Fuerza magnética",
            "dificultad": "facil"
        },
        {
            "id": "fis2_mc_004",
            "pregunta": "El radio de una partícula cargada moviéndose perpendicular a B es:",
            "opciones": ["r=mv/(|q|B)", "r=|q|B/(mv)", "r=vB/q", "r=IR"],
            "respuesta": 1,
            "explicacion": "Sale de igualar fuerza magnética y centrípeta.",
            "categoria": "Movimiento circular",
            "dificultad": "facil"
        },
        {
            "id": "fis2_mc_005",
            "pregunta": "Si aumenta el campo magnético B, el radio de giro:",
            "opciones": ["Aumenta", "Disminuye", "No cambia", "Se vuelve infinito"],
            "respuesta": 2,
            "explicacion": "r=mv/(|q|B), por tanto r disminuye si B aumenta.",
            "categoria": "Movimiento circular",
            "dificultad": "media"
        },
        {
            "id": "fis2_mc_006",
            "pregunta": "La fuerza sobre un conductor recto con corriente en B se calcula con:",
            "opciones": ["F=IL×B", "F=qE", "B=μ0I/(2R)", "U=qV"],
            "respuesta": 1,
            "explicacion": "Para un tramo conductor, el vector L sigue la corriente.",
            "categoria": "Conductor",
            "dificultad": "facil"
        },
        {
            "id": "fis2_mc_007",
            "pregunta": "¿Qué fórmula usarías para B alrededor de un hilo recto largo?",
            "opciones": ["B=μ0I/(2πr)", "B=μ0I/(2R)", "B=μ0nI", "B=F/qv"],
            "respuesta": 1,
            "explicacion": "El hilo recto largo tiene simetría circular.",
            "categoria": "Hilo recto",
            "dificultad": "facil"
        },
        {
            "id": "fis2_mc_008",
            "pregunta": "Las líneas de B alrededor de un hilo recto largo son:",
            "opciones": ["Radiales", "Circunferencias", "Paralelas al hilo", "Nulas"],
            "respuesta": 2,
            "explicacion": "El campo rodea al hilo.",
            "categoria": "Hilo recto",
            "dificultad": "facil"
        },
        {
            "id": "fis2_mc_009",
            "pregunta": "Dos hilos con corrientes en el mismo sentido:",
            "opciones": ["Se atraen", "Se repelen", "No interactúan", "Siempre se cruzan"],
            "respuesta": 1,
            "explicacion": "Corrientes paralelas en el mismo sentido se atraen.",
            "categoria": "Hilos paralelos",
            "dificultad": "facil"
        },
        {
            "id": "fis2_mc_010",
            "pregunta": "La fuerza por unidad de longitud entre dos hilos paralelos es:",
            "opciones": ["F/L=μ0I1I2/(2πd)", "F/L=kq1q2/r²", "F/L=BAcosθ", "F/L=IR"],
            "respuesta": 1,
            "explicacion": "Es el resultado para hilos largos paralelos separados distancia d.",
            "categoria": "Hilos paralelos",
            "dificultad": "media"
        },
        {
            "id": "fis2_mc_011",
            "pregunta": "El flujo magnético en campo uniforme es:",
            "opciones": ["Phi_B=BAcos(theta)", "Phi_B=B/A", "Phi_B=qvB", "Phi_B=μ0I"],
            "respuesta": 1,
            "explicacion": "Cuenta la componente de B perpendicular al área.",
            "categoria": "Flujo magnético",
            "dificultad": "facil"
        },
        {
            "id": "fis2_mc_012",
            "pregunta": "En Phi_B=BAcos(theta), theta es el ángulo entre:",
            "opciones": ["B y la superficie", "B y la normal a la superficie", "I y B", "q y v"],
            "respuesta": 2,
            "explicacion": "El vector área es normal a la superficie.",
            "categoria": "Flujo magnético",
            "dificultad": "media"
        },
        {
            "id": "fis2_mc_013",
            "pregunta": "La Ley de Biot-Savart contiene:",
            "opciones": ["dl×r_hat", "qE", "IR", "dV/dx"],
            "respuesta": 1,
            "explicacion": "La dirección de dB viene del producto vectorial dl×r_hat.",
            "categoria": "Biot-Savart",
            "dificultad": "media"
        },
        {
            "id": "fis2_mc_014",
            "pregunta": "Para el centro de una espira circular de radio R:",
            "opciones": ["B=μ0I/(2R)", "B=μ0I/(2πR)", "B=μ0nI", "B=kq/r²"],
            "respuesta": 1,
            "explicacion": "Es el resultado estándar para una espira circular.",
            "categoria": "Espira",
            "dificultad": "facil"
        },
        {
            "id": "fis2_mc_015",
            "pregunta": "Si hay N espiras iguales, el campo en el centro:",
            "opciones": ["Se divide entre N", "Se multiplica por N", "No cambia", "Se vuelve cero"],
            "respuesta": 2,
            "explicacion": "Las contribuciones de cada espira se suman.",
            "categoria": "Espira",
            "dificultad": "facil"
        },
        {
            "id": "fis2_mc_016",
            "pregunta": "La Ley de Ampère es:",
            "opciones": ["∮B·dl=μ0I_enc", "∮E·dA=Q/epsilon0", "F=kq1q2/r²", "V=IR"],
            "respuesta": 1,
            "explicacion": "Relaciona circulación de B con corriente encerrada.",
            "categoria": "Ampère",
            "dificultad": "facil"
        },
        {
            "id": "fis2_mc_017",
            "pregunta": "¿Cuál es un caso típico para usar Ampère?",
            "opciones": ["Hilo recto largo", "Dos cargas puntuales", "Circuito RC", "Movimiento con rozamiento"],
            "respuesta": 1,
            "explicacion": "El hilo largo tiene simetría circular.",
            "categoria": "Ampère",
            "dificultad": "facil"
        },
        {
            "id": "fis2_mc_018",
            "pregunta": "Dentro de un solenoide ideal largo:",
            "opciones": ["B=μ0nI", "B=μ0I/(2πr)", "B=0 siempre", "B=kq/r²"],
            "respuesta": 1,
            "explicacion": "n=N/L es el número de espiras por longitud.",
            "categoria": "Solenoide",
            "dificultad": "facil"
        },
        {
            "id": "fis2_mc_019",
            "pregunta": "En un solenoide, n representa:",
            "opciones": ["Número total de vueltas", "Espiras por unidad de longitud", "Radio", "Masa"],
            "respuesta": 2,
            "explicacion": "n=N/L.",
            "categoria": "Solenoide",
            "dificultad": "facil"
        },
        {
            "id": "fis2_mc_020",
            "pregunta": "En un toroide ideal:",
            "opciones": ["B=μ0NI/(2πr)", "B=μ0nI en todo punto externo", "B=kq/r²", "B=IR"],
            "respuesta": 1,
            "explicacion": "Sale de Ampère con trayectoria circular dentro del toroide.",
            "categoria": "Toroide",
            "dificultad": "media"
        },
        {
            "id": "fis2_mc_021",
            "pregunta": "El momento magnético de una espira es:",
            "opciones": ["μ=NIA", "μ=IR", "μ=qV", "μ=mv/r"],
            "respuesta": 1,
            "explicacion": "Corriente por área, multiplicado por N si hay N vueltas.",
            "categoria": "Dipolo magnético",
            "dificultad": "facil"
        },
        {
            "id": "fis2_mc_022",
            "pregunta": "El torque sobre una espira cumple:",
            "opciones": ["τ=μ×B", "τ=qE", "τ=IR", "τ=kq/r"],
            "respuesta": 1,
            "explicacion": "El campo tiende a alinear μ con B.",
            "categoria": "Torque",
            "dificultad": "facil"
        },
        {
            "id": "fis2_mc_023",
            "pregunta": "La energía de un dipolo magnético es:",
            "opciones": ["U=-μ·B", "U=qV", "U=IR²", "U=mvB"],
            "respuesta": 1,
            "explicacion": "Es mínima cuando μ y B están alineados.",
            "categoria": "Dipolo magnético",
            "dificultad": "dificil"
        },
        {
            "id": "fis2_mc_024",
            "pregunta": "Si un dibujo muestra cruces × para B, significa:",
            "opciones": ["B sale de la pantalla", "B entra en la pantalla", "B es cero", "B va a la derecha"],
            "respuesta": 2,
            "explicacion": "La cruz representa la cola de una flecha alejándose de ti.",
            "categoria": "Dirección",
            "dificultad": "facil"
        },
        {
            "id": "fis2_mc_025",
            "pregunta": "Si un dibujo muestra puntos • para B, significa:",
            "opciones": ["B entra en la pantalla", "B sale de la pantalla", "B es cero", "B apunta hacia abajo"],
            "respuesta": 2,
            "explicacion": "El punto representa la punta de una flecha viniendo hacia ti.",
            "categoria": "Dirección",
            "dificultad": "facil"
        }
    ]
}
