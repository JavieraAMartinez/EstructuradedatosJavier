def main():
    frutas = []

    frutas.append("mango")
    frutas.append("manzana")
    frutas.append("banana")
    frutas.append("uvas")

    print(frutas)

    frutas.pop(0)

    frutas.pop(1)

    frutas.append("sandia")

    print(frutas)

if __name__ == "__main__":
    main()
