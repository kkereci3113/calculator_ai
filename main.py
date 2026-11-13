
from calculator import add, subtract, multiply, divide

def main():
    print("===== PYTHON CALCULATOR =====")
    print("1. Mbledhje")
    print("2. Zbritje")
    print("3. Shumezim")
    print("4. Pjesetim")

    choice = input("Zgjidh operacionin (1-4): ")

    try:
        a = float(input("Vendos numrin e pare: "))
        b = float(input("Vendos numrin e dyte: "))

        if choice == "1":
            result = add(a, b)
        elif choice == "2":
            result = subtract(a, b)
        elif choice == "3":
            result = multiply(a, b)
        elif choice == "4":
            result = divide(a, b)
        else:
            print("Operacion i pavlefshem!")
            return

        print("Rezultati:", result)

    except ValueError as error:
        print("Gabim:", error)


if __name__ == "__main__":
    main()
