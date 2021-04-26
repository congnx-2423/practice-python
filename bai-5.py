listProds = []
n = int(input('Enter size of list:'))
for i in range(0, n):
    name = input('Title: ')
    quantity = int(input('Quantity: '))
    prod = {
        'title': name,
        'quantity': quantity
    }

    listProds.append(prod)

key = input('Search: ')
result = [i for i in listProds if i['title'] == key]

if (result):
    quantity = 0
    for p in result:
        quantity += p['quantity']

    print(f"{quantity} items available")
else:
    print('Out of stock!')

