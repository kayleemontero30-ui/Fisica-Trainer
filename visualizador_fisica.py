# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch
from matplotlib.path import Path
import matplotlib.patches as patches


def crear_figura_2d(titulo):
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.set_title(titulo)
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True, alpha=0.25)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-4, 4)
    return fig, ax


def flecha(ax, x1, y1, x2, y2, texto=None, escala=12):
    ax.annotate(
        "",
        xy=(x2, y2),
        xytext=(x1, y1),
        arrowprops=dict(arrowstyle="->", lw=2)
    )
    if texto:
        ax.text(x2, y2, " " + texto, fontsize=escala)


def dibujar_carga(ax, x, y, signo="+", etiqueta=None):
    color = "tomato" if signo == "+" else "royalblue"
    circ = Circle((x, y), 0.35, color=color, alpha=0.85)
    ax.add_patch(circ)
    ax.text(x, y, signo, color="white", fontsize=18, ha="center", va="center", weight="bold")
    if etiqueta:
        ax.text(x, y - 0.65, etiqueta, ha="center")


def escena_coulomb():
    fig, ax = crear_figura_2d("Ley de Coulomb: atracción y repulsión")
    dibujar_carga(ax, -2, 0, "+", "q1")
    dibujar_carga(ax, 2, 0, "-", "q2")
    flecha(ax, -1.55, 0, -0.5, 0, "F sobre q1")
    flecha(ax, 1.55, 0, 0.5, 0, "F sobre q2")
    ax.plot([-2, 2], [0, 0], "--", alpha=0.5)
    ax.text(0, -0.35, "r", ha="center")

    explicacion = """
LEY DE COULOMB

Si aparecen dos cargas separadas una distancia r, casi siempre debes usar:

F = k |q1 q2| / r²

Qué mirar:
- Signos iguales: repulsión.
- Signos opuestos: atracción.
- La fuerza va sobre la línea que une las cargas.
- Convierte μC, nC, cm, mm a SI antes de calcular.

En el dibujo:
q1 es positiva y q2 negativa, por eso se atraen.
"""
    return fig, explicacion


def escena_campo_carga():
    fig, ax = crear_figura_2d("Campo eléctrico de una carga positiva")
    dibujar_carga(ax, 0, 0, "+", "q positiva")

    for ang in np.linspace(0, 2*np.pi, 12, endpoint=False):
        x1, y1 = 0.55*np.cos(ang), 0.55*np.sin(ang)
        x2, y2 = 2.2*np.cos(ang), 2.2*np.sin(ang)
        flecha(ax, x1, y1, x2, y2)

    explicacion = """
CAMPO ELÉCTRICO DE UNA CARGA

Para una carga puntual:

E = k |q| / r²

Dirección:
- Si q es positiva, el campo sale de la carga.
- Si q es negativa, el campo entra hacia la carga.

Consejo de ejercicio:
Si te piden el campo en un punto, dibuja primero la dirección de E.
Luego calcula módulo y componentes si hace falta.
"""
    return fig, explicacion


def escena_superposicion():
    fig, ax = crear_figura_2d("Superposición de campos eléctricos")
    dibujar_carga(ax, -2, 0, "+", "q1")
    dibujar_carga(ax, 2, 0, "+", "q2")
    ax.scatter(0, 1.8, s=60)
    ax.text(0.1, 1.8, "P")
    flecha(ax, 0, 1.8, 1.2, 2.6, "E1")
    flecha(ax, 0, 1.8, -1.2, 2.6, "E2")
    flecha(ax, 0, 1.8, 0, 3.1, "E total")

    explicacion = """
SUPERPOSICIÓN

Cuando hay varias cargas:

E_total = E1 + E2 + ...

Importante:
- E es vector.
- Debes sumar componentes, no solo módulos.
- Usa simetría: a veces las componentes horizontales se cancelan.

En el ejemplo:
Las dos cargas positivas producen campos simétricos en P.
Las componentes horizontales se cancelan y queda un campo vertical.
"""
    return fig, explicacion


def escena_gauss():
    fig, ax = crear_figura_2d("Ley de Gauss: superficie gaussiana")
    dibujar_carga(ax, 0, 0, "+", "Q encerrada")
    circ = Circle((0, 0), 2.2, fill=False, lw=2)
    ax.add_patch(circ)
    ax.text(0, -2.6, "Superficie gaussiana", ha="center")
    for ang in np.linspace(0, 2*np.pi, 10, endpoint=False):
        flecha(ax, 1.2*np.cos(ang), 1.2*np.sin(ang), 2.0*np.cos(ang), 2.0*np.sin(ang))

    explicacion = """
LEY DE GAUSS

Φ_E = Q_enc / ε0

Cuándo usarla:
- Esfera.
- Cilindro.
- Plano infinito.
- Situaciones con simetría clara.

La idea:
Escoges una superficie cerrada imaginaria.
Si E tiene la misma magnitud en esa superficie, Gauss simplifica mucho.

Consejo:
Si no hay simetría, Gauss sigue siendo cierta, pero no te ayuda a despejar E fácilmente.
"""
    return fig, explicacion


def escena_fuerza_magnetica():
    fig, ax = crear_figura_2d("Fuerza magnética: F = q v × B")
    ax.set_xlim(-4, 4)
    ax.set_ylim(-3, 3)
    ax.scatter(0, 0, s=120)
    ax.text(0.1, -0.25, "q+")
    flecha(ax, 0, 0, 2.2, 0, "v")
    # B entrando en la hoja con cruces
    for x in np.linspace(-3, 3, 5):
        for y in np.linspace(-2, 2, 4):
            ax.text(x, y, "×", fontsize=16, ha="center", va="center", alpha=0.7)
    flecha(ax, 0, 0, 0, 2.0, "F")

    explicacion = """
FUERZA MAGNÉTICA

F = q v × B

Cómo leer el dibujo:
- La velocidad v va hacia la derecha.
- El campo B entra en la pantalla: símbolo ×.
- Para q positiva, la fuerza sale según la regla de la mano derecha.
- Para q negativa, el sentido se invierte.

Consejo:
Si v es paralela a B, F=0.
"""
    return fig, explicacion


def escena_hilo_magnetico():
    fig, ax = crear_figura_2d("Campo magnético alrededor de un hilo")
    ax.scatter(0, 0, s=140)
    ax.text(0, 0, "I", ha="center", va="center", color="white", weight="bold")
    for r in [1.0, 1.8, 2.6]:
        circ = Circle((0, 0), r, fill=False, lw=1.8, alpha=0.8)
        ax.add_patch(circ)
    # arrows tangent
    for ang in [0.3, 1.6, 3.2, 4.7]:
        r = 2.0
        x, y = r*np.cos(ang), r*np.sin(ang)
        dx, dy = -0.5*np.sin(ang), 0.5*np.cos(ang)
        flecha(ax, x, y, x+dx, y+dy)
    ax.text(0, -3.2, "Líneas de B rodean al hilo", ha="center")

    explicacion = """
HILO RECTO LARGO

B = μ0 I / (2πr)

Qué visualizar:
- El campo B no sale radialmente.
- B rodea al hilo en circunferencias.
- Usa la regla de la mano derecha:
  pulgar = corriente,
  dedos = sentido de B.

Consejo:
Si el ejercicio dice 'hilo largo' y distancia r, esta fórmula suele ser la primera opción.
"""
    return fig, explicacion


def escena_circuito_serie():
    fig, ax = crear_figura_2d("Circuito simple: resistencias en serie")
    ax.axis("off")
    # wires
    ax.plot([-3, 3, 3, -3, -3], [2, 2, -2, -2, 2], lw=2)
    # battery
    ax.plot([-3.2, -3.2], [-0.5, 0.5], lw=3)
    ax.plot([-2.8, -2.8], [-0.25, 0.25], lw=3)
    ax.text(-3.55, 0.7, "Batería")
    # resistors as rectangles
    ax.add_patch(Rectangle((-1.5, 1.75), 1, 0.5, fill=False, lw=2))
    ax.text(-1.0, 2.45, "R1", ha="center")
    ax.add_patch(Rectangle((0.7, 1.75), 1, 0.5, fill=False, lw=2))
    ax.text(1.2, 2.45, "R2", ha="center")
    flecha(ax, -2.2, 2.35, -1.7, 2.35, "I")

    explicacion = """
RESISTENCIAS EN SERIE

En serie:
- La misma corriente pasa por todas las resistencias.
- La resistencia equivalente es:
  R_eq = R1 + R2 + ...

Procedimiento:
1. Suma resistencias.
2. Calcula I = V / R_eq.
3. Calcula caídas: V1=IR1, V2=IR2.

Pista:
Serie = misma corriente.
"""
    return fig, explicacion


def escena_circuito_paralelo():
    fig, ax = crear_figura_2d("Circuito: resistencias en paralelo")
    ax.axis("off")
    ax.plot([-3, -1, -1, 2.5, 2.5, -3, -3], [2, 2, 1, 1, -1, -1, 2], lw=2)
    ax.plot([-1, -1], [1, -1], lw=2)
    ax.plot([2.5, 2.5], [1, -1], lw=2)
    ax.add_patch(Rectangle((0, 0.75), 1, 0.5, fill=False, lw=2))
    ax.text(0.5, 1.45, "R1", ha="center")
    ax.add_patch(Rectangle((0, -1.25), 1, 0.5, fill=False, lw=2))
    ax.text(0.5, -1.55, "R2", ha="center")
    ax.plot([-3.2, -3.2], [-0.5, 0.5], lw=3)
    ax.plot([-2.8, -2.8], [-0.25, 0.25], lw=3)
    ax.text(-3.55, 0.7, "Batería")

    explicacion = """
RESISTENCIAS EN PARALELO

En paralelo:
- Todas las ramas tienen el mismo voltaje.
- La corriente se divide en ramas.
- La resistencia equivalente cumple:
  1/R_eq = 1/R1 + 1/R2 + ...

Procedimiento:
1. Identifica los dos nodos comunes.
2. Usa el mismo V en cada rama.
3. Calcula I1=V/R1, I2=V/R2.
4. Suma corrientes: I_total=I1+I2.

Pista:
Paralelo = mismo voltaje.
"""
    return fig, explicacion


def escena_rc():
    fig, ax = plt.subplots(figsize=(7, 5))
    t = np.linspace(0, 5, 300)
    carga = 1 - np.exp(-t)
    descarga = np.exp(-t)
    ax.plot(t, carga, label="carga: 1-e^{-t/RC}")
    ax.plot(t, descarga, label="descarga: e^{-t/RC}")
    ax.axvline(1, linestyle="--", alpha=0.7)
    ax.text(1.05, 0.5, "τ=RC")
    ax.set_xlabel("t / RC")
    ax.set_ylabel("fracción")
    ax.set_title("Circuito RC: carga y descarga")
    ax.grid(True, alpha=0.3)
    ax.legend()

    explicacion = """
CIRCUITO RC

Constante de tiempo:
τ = RC

Carga:
q(t)=CV(1-e^{-t/RC})

Descarga:
q(t)=Q0 e^{-t/RC}

Qué recordar:
- En t=τ, la carga llega a ~63% de su valor final.
- En descarga, queda ~37% de la carga inicial.
- Si aparece una exponencial con RC, el problema es de carga/descarga de capacitor.
"""
    return fig, explicacion


def escena_faraday():
    fig, ax = crear_figura_2d("Inducción: flujo magnético cambiante")
    ax.axis("off")
    # coil
    for i in range(5):
        circ = Circle((0, 0), 1.2 + 0.08*i, fill=False, lw=1.5)
        ax.add_patch(circ)
    # B arrows
    for x in [-2.8, -1.8, 1.8, 2.8]:
        flecha(ax, x, -2.2, x, 2.2, "B" if x == -2.8 else None)
    ax.text(0, -2.7, "Bobina / espira", ha="center")
    ax.text(0, 2.7, "Si cambia ΦB, aparece fem inducida", ha="center")

    explicacion = """
LEY DE FARADAY-LENZ

ε = -N dΦB/dt

Qué debe cambiar para inducir fem:
- B,
- el área A,
- el ángulo θ,
- o la orientación/movimiento de la bobina.

Si el flujo magnético ΦB es constante, no hay fem inducida.

El signo menos es Lenz:
la corriente inducida se opone al cambio de flujo.
"""
    return fig, explicacion


EJEMPLOS = {
    "Tema 1 - Coulomb: atracción entre cargas": escena_coulomb,
    "Tema 1 - Campo de una carga positiva": escena_campo_carga,
    "Tema 1 - Superposición de campos": escena_superposicion,
    "Tema 1 - Ley de Gauss": escena_gauss,
    "Tema 2 - Fuerza magnética q v x B": escena_fuerza_magnetica,
    "Tema 2 - Campo alrededor de un hilo": escena_hilo_magnetico,
    "Tema 3 - Resistencias en serie": escena_circuito_serie,
    "Tema 3 - Resistencias en paralelo": escena_circuito_paralelo,
    "Tema 3 - Circuito RC": escena_rc,
    "Tema 3 - Faraday-Lenz": escena_faraday
}


def listar_ejemplos():
    return list(EJEMPLOS.keys())


def generar_ejemplo(nombre):
    if nombre not in EJEMPLOS:
        raise ValueError("Ejemplo no encontrado.")
    return EJEMPLOS[nombre]()
