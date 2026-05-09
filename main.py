# -*- coding: utf-8 -*-

from datos_tema1 import TEMA1
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
    mostrar_progreso
)


def mostrar_menu():
    print("\n" + "=" * 80)
    print("ASISTENTE DE ESTUDIO DE FISICA".center(80))
    print("=" * 80)
    print("Tema actual:", TEMA1["nombre"])
    print()
    print("1. Ver resumen del tema")
    print("2. Ver formulas importantes")
    print("3. Ver formulas derivadas / despejes")
    print("4. Ver cuando usar cada formula")
    print("5. Modo flashcards")
    print("6. Mini test verdadero/falso")
    print("7. Mini test multiple choice")
    print("8. Mini test numerico")
    print("9. Mini test mixto aleatorio")
    print("10. Practicar solo preguntas falladas")
    print("11. Ver progreso")
    print("12. Salir")


def main():
    progreso = cargar_progreso()

    while True:
        mostrar_menu()
        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            mostrar_resumen(TEMA1)

        elif opcion == "2":
            mostrar_formulas(TEMA1)

        elif opcion == "3":
            mostrar_despejes(TEMA1)

        elif opcion == "4":
            mostrar_cuando_usar(TEMA1)

        elif opcion == "5":
            modo_flashcards(TEMA1, progreso)

        elif opcion == "6":
            mini_test_vf(TEMA1, progreso)

        elif opcion == "7":
            mini_test_mc(TEMA1, progreso)

        elif opcion == "8":
            mini_test_numerico(TEMA1, progreso)

        elif opcion == "9":
            mini_test_mixto(TEMA1, progreso)

        elif opcion == "10":
            mini_test_falladas(TEMA1, progreso)

        elif opcion == "11":
            mostrar_progreso(progreso)

        elif opcion == "12":
            print("Saliendo del asistente de fisica...")
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()