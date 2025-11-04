from src.parse import parse_1
def main() -> None:
    while True:
        input1 = input()
        if input1=='cmd q':
            break
        else:
            parse_1(input1)
if __name__ == "__main__":
    main()
