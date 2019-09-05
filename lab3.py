def main():
    start = ""
    gap = 0
    end = ""
    print('*** Welcome to the Unicode Explorer ***')
    user_input = input('Would you like to start exploring with an alphabet: [Y/N]: ').upper()
    if user_input == "Y":
        start = input("Enter first character in exploration: ")
        gap = int(input("Enter gap between successive Unicode values, starting with {}: ".format(ord(start))))
        user_input = input('Choose Unicode value or letter as exploration endpoint [U/L]: ').upper()
        if user_input == 'U':
            end = int(input("Enter last possible unicode in exploration"))
            return_result(ord(start), end, gap)
        elif user_input == 'L':
            end = input("Enter last possible character in exploration: ")
            return_result(ord(start), ord(end), gap)
        else:
            print("Wrong input format, please try again later")
    elif user_input == "N":
        start = int(input("Enter first unicode in exploration: "))
        gap = int(input("Enter gap between successive Unicode values, starting with {}: ".format(start)))
        user_input = input('Choose Unicode value or letter as exploration endpoint [U/L]: ').upper()
        if user_input == 'U':
            end = int(input("Enter last possible unicode in exploration"))
            return_result(start, end, gap)
        elif user_input == 'L':
            end = input("Enter last possible character in exploration: ")
            return_result(start, ord(end), gap)
        else:
            print("Wrong input format, please try again later")
    else:
        print("Wrong input format, please try again later")


def return_result(start, end, gap):
    for x in range(start, end+1, gap):
        print('"{0}" is {1} in Unicode, which is {2:b} in binary'.
              format(chr(x),x,x))
    print("Thank you for using the Unicode explorer")

main()
