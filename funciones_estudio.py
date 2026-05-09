# -*- coding: utf-8 -*-

import json
import os
import random

PROGRESO_ARCHIVO = "progreso.json"


def cargar_progreso():
    if not os.path.exists(PROGRESO_ARCHIVO):
        return {
            "tests_realizados": 0,
            "preguntas_totales": 0,
            "preguntas_correctas": 0,
            "fallos_por_categoria": {},
            "flashcards_vistas": 0,
            "preguntas_falladas": []
        }

    with open(PROGRESO_ARCHIVO, "r", encoding="utf-8") as archivo:
        progreso = json.load(archivo)

    if "preguntas_falladas" not in progreso:
        progreso["preguntas_falladas"] = []

    return progreso


def guardar_progreso(progreso):
    with open(PROGRESO_ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(progreso, archivo, indent=4, ensure_ascii=False)


def pedir_numero(mensaje, minimo, maximo):
    while True:
        try:
            numero = int(input(mensaje))

            if minimo <= numero <= maximo:
                return numero

            print(f"Introduce un numero entre {minimo} y {maximo}.")

        except ValueError:
            print("Entrada no valida. Introduce un numero.")


def pedir_float(mensaje):
    while True:
        try:
            return float(input(mensaje).replace(",", "."))
        except ValueError:
            print("Entrada no valida. Puedes escribir, por ejemplo: 9, 0.0225 o 1.13e5")


def elegir_dificultad():
    print("\nDificultad:")
    print("1. Facil")
    print("2. Media")
    print("3. Dificil")
    print("4. Mixto")

    opcion = pedir_numero("Elige dificultad: ", 1, 4)

    if opcion == 1:
        return "facil"
    elif opcion == 2:
        return "media"
    elif opcion == 3:
        return "dificil"
    else:
        return "mixto"


def filtrar_por_dificultad(preguntas, dificultad):
    if dificultad == "mixto":
        return preguntas

    filtradas = []

    for pregunta in preguntas:
        if pregunta["dificultad"] == dificultad:
            filtradas.append(pregunta)

    return filtradas


def mostrar_resumen(tema):
    print("\n" + "=" * 80)
    print(tema["nombre"].center(80))
    print("=" * 80)
    print(tema["resumen"])


def mostrar_formulas(tema):
    print("\n" + "=" * 80)
    print("FORMULAS IMPORTANTES".center(80))
    print("=" * 80)

    for i, formula in enumerate(tema["formulas"], start=1):
        print(f"\n{i}. {formula['nombre']}")
        print("-" * 80)
        print("Formula:", formula["formula"])
        print("Uso:", formula["uso"])


def mostrar_despejes(tema):
    print("\n" + "=" * 80)
    print("FORMULAS DERIVADAS / DESPEJES".center(80))
    print("=" * 80)

    for formula in tema["formulas"]:
        print(f"\nFORMULA BASE: {formula['nombre']}")
        print("Formula:", formula["formula"])
        print("Uso:", formula["uso"])
        print("\nDespejes:")

        for despeje in formula["despejes"]:
            print("\n -", despeje["nombre"])
            print("   Formula:", despeje["formula"])
            print("   Uso:", despeje["explicacion"])

        print("-" * 80)


def mostrar_cuando_usar(tema):
    print("\n" + "=" * 80)
    print("CUANDO USAR CADA FORMULA".center(80))
    print("=" * 80)

    for formula in tema["formulas"]:
        print(f"\n{formula['nombre']}")
        print("Formula:", formula["formula"])
        print("Se usa cuando:")

        for caso in formula["cuando_usarla"]:
            print(" -", caso)


def modo_flashcards(tema, progreso):
    flashcards = tema["flashcards"].copy()
    random.shuffle(flashcards)

    cantidad = pedir_numero(
        f"Cuantas flashcards quieres estudiar? Maximo {len(flashcards)}: ",
        1,
        len(flashcards)
    )

    seleccionadas = flashcards[:cantidad]

    for i, card in enumerate(seleccionadas, start=1):
        print("\n" + "=" * 80)
        print(f"FLASHCARD {i}/{cantidad}")
        print("Categoria:", card["categoria"])
        print("-" * 80)
        print("Pregunta:")
        print(card["frente"])

        input("\nPulsa ENTER para ver la respuesta...")

        print("\nRespuesta:")
        print(card["reverso"])

        progreso["flashcards_vistas"] += 1

        input("\nPulsa ENTER para continuar...")

    guardar_progreso(progreso)


def obtener_id_pregunta(pregunta):
    return pregunta["tipo"] + ":" + pregunta["id"]


def registrar_resultado(progreso, pregunta, correcto):
    progreso["preguntas_totales"] += 1

    pregunta_id = obtener_id_pregunta(pregunta)

    if correcto:
        progreso["preguntas_correctas"] += 1

        if pregunta_id in progreso["preguntas_falladas"]:
            progreso["preguntas_falladas"].remove(pregunta_id)

    else:
        categoria = pregunta.get("categoria", "Sin categoria")

        if categoria not in progreso["fallos_por_categoria"]:
            progreso["fallos_por_categoria"][categoria] = 0

        progreso["fallos_por_categoria"][categoria] += 1

        if pregunta_id not in progreso["preguntas_falladas"]:
            progreso["preguntas_falladas"].append(pregunta_id)


def preguntar_vf(pregunta):
    print("\n" + "-" * 80)
    print("VERDADERO O FALSO")
    print("Categoria:", pregunta["categoria"])
    print("Dificultad:", pregunta["dificultad"])
    print("-" * 80)
    print(pregunta["pregunta"])

    while True:
        respuesta = input("Respuesta (v/f): ").strip().lower()

        if respuesta in ["v", "verdadero"]:
            respuesta_usuario = True
            break

        elif respuesta in ["f", "falso"]:
            respuesta_usuario = False
            break

        else:
            print("Respuesta no valida. Escribe v o f.")

    correcto = respuesta_usuario == pregunta["respuesta"]

    if correcto:
        print("Correcto.")
    else:
        print("Incorrecto.")

    print("Explicacion:", pregunta["explicacion"])

    return correcto


def preguntar_mc(pregunta):
    print("\n" + "-" * 80)
    print("MULTIPLE CHOICE")
    print("Categoria:", pregunta["categoria"])
    print("Dificultad:", pregunta["dificultad"])
    print("-" * 80)
    print(pregunta["pregunta"])

    for i, opcion in enumerate(pregunta["opciones"], start=1):
        print(f"{i}. {opcion}")

    respuesta_usuario = pedir_numero(
        "Elige una opcion: ",
        1,
        len(pregunta["opciones"])
    )

    correcto = respuesta_usuario == pregunta["respuesta"]

    if correcto:
        print("Correcto.")
    else:
        print("Incorrecto.")
        print("Respuesta correcta:", pregunta["respuesta"])

    print("Explicacion:", pregunta["explicacion"])

    return correcto


def preguntar_numerico(pregunta):
    print("\n" + "-" * 80)
    print("EJERCICIO NUMERICO")
    print("Categoria:", pregunta["categoria"])
    print("Dificultad:", pregunta["dificultad"])
    print("-" * 80)
    print(pregunta["enunciado"])

    respuesta_usuario = pedir_float("Tu respuesta numerica: ")

    respuesta_correcta = pregunta["respuesta"]
    tolerancia = pregunta.get("tolerancia_relativa", 0.05)

    error = abs(respuesta_usuario - respuesta_correcta)
    error_maximo = abs(respuesta_correcta) * tolerancia

    if error <= error_maximo:
        print("Correcto.")
        correcto = True
    else:
        print("Incorrecto.")
        print("Respuesta esperada:", respuesta_correcta, pregunta["unidad"])
        correcto = False

    print("Explicacion:", pregunta["explicacion"])

    return correcto


def preparar_vf(tema):
    preguntas = []

    for pregunta in tema["preguntas_vf"]:
        copia = pregunta.copy()
        copia["tipo"] = "vf"
        preguntas.append(copia)

    return preguntas


def preparar_mc(tema):
    preguntas = []

    for pregunta in tema["preguntas_mc"]:
        copia = pregunta.copy()
        copia["tipo"] = "mc"
        preguntas.append(copia)

    return preguntas


def preparar_numericos(tema):
    preguntas = []

    for pregunta in tema["ejercicios_numericos"]:
        copia = pregunta.copy()
        copia["tipo"] = "num"
        preguntas.append(copia)

    return preguntas


def preparar_banco_completo(tema):
    banco = []
    banco.extend(preparar_vf(tema))
    banco.extend(preparar_mc(tema))
    banco.extend(preparar_numericos(tema))
    return banco


def hacer_preguntas(preguntas, progreso, titulo):
    if len(preguntas) == 0:
        print("No hay preguntas disponibles para esta opcion.")
        return

    cantidad = pedir_numero(
        f"Cuantas preguntas quieres? Maximo {len(preguntas)}: ",
        1,
        len(preguntas)
    )

    seleccionadas = random.sample(preguntas, cantidad)

    correctas = 0

    for pregunta in seleccionadas:
        if pregunta["tipo"] == "vf":
            correcto = preguntar_vf(pregunta)
        elif pregunta["tipo"] == "mc":
            correcto = preguntar_mc(pregunta)
        elif pregunta["tipo"] == "num":
            correcto = preguntar_numerico(pregunta)
        else:
            print("Tipo de pregunta desconocido.")
            correcto = False

        registrar_resultado(progreso, pregunta, correcto)

        if correcto:
            correctas += 1

    progreso["tests_realizados"] += 1
    guardar_progreso(progreso)

    print("\n" + "=" * 80)
    print(titulo.center(80))
    print("=" * 80)
    print(f"Puntuacion: {correctas}/{cantidad}")


def mini_test_vf(tema, progreso):
    dificultad = elegir_dificultad()
    preguntas = filtrar_por_dificultad(preparar_vf(tema), dificultad)
    hacer_preguntas(preguntas, progreso, "RESULTADO TEST VERDADERO/FALSO")


def mini_test_mc(tema, progreso):
    dificultad = elegir_dificultad()
    preguntas = filtrar_por_dificultad(preparar_mc(tema), dificultad)
    hacer_preguntas(preguntas, progreso, "RESULTADO TEST MULTIPLE CHOICE")


def mini_test_numerico(tema, progreso):
    dificultad = elegir_dificultad()
    preguntas = filtrar_por_dificultad(preparar_numericos(tema), dificultad)
    hacer_preguntas(preguntas, progreso, "RESULTADO TEST NUMERICO")


def mini_test_mixto(tema, progreso):
    dificultad = elegir_dificultad()
    preguntas = filtrar_por_dificultad(preparar_banco_completo(tema), dificultad)
    hacer_preguntas(preguntas, progreso, "RESULTADO TEST MIXTO")


def mini_test_falladas(tema, progreso):
    banco = preparar_banco_completo(tema)
    falladas = []

    for pregunta in banco:
        pregunta_id = obtener_id_pregunta(pregunta)

        if pregunta_id in progreso["preguntas_falladas"]:
            falladas.append(pregunta)

    if len(falladas) == 0:
        print("\nNo tienes preguntas falladas pendientes.")
        return

    hacer_preguntas(falladas, progreso, "RESULTADO TEST DE PREGUNTAS FALLADAS")


def mostrar_progreso(progreso):
    print("\n" + "=" * 80)
    print("PROGRESO".center(80))
    print("=" * 80)

    print("Tests realizados:", progreso["tests_realizados"])
    print("Flashcards vistas:", progreso["flashcards_vistas"])
    print("Preguntas totales:", progreso["preguntas_totales"])
    print("Preguntas correctas:", progreso["preguntas_correctas"])

    if progreso["preguntas_totales"] > 0:
        porcentaje = progreso["preguntas_correctas"] / progreso["preguntas_totales"] * 100
        print(f"Porcentaje de acierto: {porcentaje:.2f}%")
    else:
        print("Porcentaje de acierto: 0%")

    print("\nPreguntas falladas pendientes:", len(progreso["preguntas_falladas"]))

    print("\nFallos por categoria:")

    if len(progreso["fallos_por_categoria"]) == 0:
        print("Todavia no hay fallos registrados.")
    else:
        for categoria, fallos in progreso["fallos_por_categoria"].items():
            print(f"- {categoria}: {fallos}")