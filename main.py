# -*- coding: utf-8 -*-

from datos_tema1 import TEMA1
from datos_tema2 import TEMA2
from datos_conexiones import CONEXIONES

from funciones_estudio import (
    cargar_progreso,
    mostrar_resumen,
    mostrar_formulas,
    mostrar_despejes,
    mostrar_cuando_usar,
    modo_flashcards,
    mini_test_vf,
    mini_test_mc,
    mini_test_numerico,
    mini_test_mixto,
    mini_test_falladas,
    mostrar_progreso,
    mostrar_conexiones
)


TEMAS = {
    "1": TEMA1,
    "2": TEMA2
}


def elegir_tema():
    print("\n" + "=" * 80)
    print("ELEGIR TEMA".center(80))
    print("=" * 80)
    print("1. Tema 1 - Campo electrico y electrostatica")
    print("2. Tema 2 - Campo magnetostatico")

    while True:
        opcion = input("Elige un tema: ").strip()

        if opcion in TEMAS:
            return TEMAS[opcion]

        print("Opcion no valida.")


def mostrar_menu(tema_actual):
    print("\n" + "=" * 80)
    print("ASISTENTE DE ESTUDIO DE FISICA".center(80))
    print("=" * 80)
    print("Tema actual:", tema_actual["nombre"])
    print()
    print("1. Cambiar tema")
    print("2. Ver resumen del tema")
    print("3. Ver formulas importantes")
    print("4. Ver formulas derivadas / despejes")
    print("5. Ver cuando usar cada formula")
    print("6. Modo flashcards")
    print("7. Mini test verdadero/falso")
    print("8. Mini test multiple choice")
    print("9. Mini test numerico")
    print("10. Mini test mixto aleatorio")
    print("11. Practicar solo preguntas falladas del tema actual")
    print("12. Ver progreso")
    print("13. Ver conexiones entre temas")
    print("14. Salir")


def main():
    progreso = cargar_progreso()
    tema_actual = elegir_tema()

    while True:
        mostrar_menu(tema_actual)
        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            tema_actual = elegir_tema()

        elif opcion == "2":
            mostrar_resumen(tema_actual)

        elif opcion == "3":
            mostrar_formulas(tema_actual)

        elif opcion == "4":
            mostrar_despejes(tema_actual)

        elif opcion == "5":
            mostrar_cuando_usar(tema_actual)

        elif opcion == "6":
            modo_flashcards(tema_actual, progreso)

        elif opcion == "7":
            mini_test_vf(tema_actual, progreso)

        elif opcion == "8":
            mini_test_mc(tema_actual, progreso)

        elif opcion == "9":
            mini_test_numerico(tema_actual, progreso)

        elif opcion == "10":
            mini_test_mixto(tema_actual, progreso)

        elif opcion == "11":
            mini_test_falladas(tema_actual, progreso)

        elif opcion == "12":
            mostrar_progreso(progreso)

        elif opcion == "13":
            mostrar_conexiones(CONEXIONES)

        elif opcion == "14":
            print("Saliendo del asistente de fisica...")
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()