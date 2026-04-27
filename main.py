from src.calculadora import somar, subtrair


def main():
    print("Calculadora")
    print(f"2 + 3 = {somar(2, 3)}")
    print(f"5 - 1 = {subtrair(5, 1)}")


if __name__ == "__main__":
    main()
