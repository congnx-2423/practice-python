celcius = input()

def cToF(cel):
    try:
        result = (float(cel) * 9 / 5) + 32
        print(f"{result} F")
    except ValueError:
        print('Enter a number')

cToF(celcius)
