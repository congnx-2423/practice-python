s = input()
name = input()
s = s.replace(' ', '')
b = s.split(',')

if name in b:
    print('Available')
else:
    print('Out of stock!')
