import sys

if len(sys.argv) < 2 or not sys.argv[1].isdigit():
    print("Ошибка во входных параметрах")
else:
    digit_string = sys.argv[1]
    sum = 0

    for digit in digit_string:
        sum += int(digit)
    print(sum)