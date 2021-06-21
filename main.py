from string import Template


class MyTemplate(Template):
    delimiter = '#'


def Main():
    cart = []
    cart.append(dict(item="Fanta", price=9, qty=3))
    cart.append(dict(item="Pizza", price=61, qty=2))
    cart.append(dict(item="Chocolate", price=14, qty=2))
    cart.append(dict(item="Cola", price=3, qty=1))
    cart.append(dict(item="Water", price=2, qty=1))
    cart.append(dict(item="Laptop", price=2000, qty=1))
    cart.append(dict(item="Smartphone", price=800, qty=1))
    cart.append(dict(item="Airpods", price=650, qty=2))
    cart.append(dict(item="Sneakers", price=469, qty=1))
    cart.append(dict(item="suit", price=1400, qty=2))

    t = MyTemplate("#qty x #item = #price")
    total = 0
    print("Cart:")
    for data in cart:
        print(t.substitute(data))
        total += data["price"]
    print("Total: " + str(total))


if __name__ == '__main__':
    Main()
