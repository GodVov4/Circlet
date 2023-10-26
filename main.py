from alphabets.eng import ENGLISH


def printer(text: str) -> tuple[str, int]:
    result = ''
    string = 0
    while string < 5:
        for index, char in enumerate(text):
            listed_char = ENGLISH.get(char.upper()).split('\n')
            result += listed_char[string]
            if index+1 != len(text):
                result += '-'
        result += '\n'
        string += 1
    return result, (len(result)-5)//5


def main():
    text, length = printer('action precedes motivation')
    print(text)
    print(f'Довжина браслета: {length}.')


if __name__ == '__main__':
    main()
