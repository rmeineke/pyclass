def main():
    print(GiveAsciiChart())
    
    
def GiveAsciiChart():
    return str(''.join(' ' * (3 - len(str(num + 32))) + str(num + 32) + ':  ' + ch + '\t\t' + "\n" * (num % 4 == 3) for num, ch in enumerate([chr(x) for x in range(32, 127)])))


if __name__ == "__main__":
    main()
