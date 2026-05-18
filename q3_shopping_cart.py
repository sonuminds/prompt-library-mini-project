# Part A: Spot the Bug

def wrong_add_item(item, cart=[]):
    cart.append(item)
    return cart


print("Part A - Mutable Default Argument Bug:")
print(wrong_add_item("apple"))
print(wrong_add_item("banana"))
print(wrong_add_item("milk", cart=["bread"]))
print(wrong_add_item("eggs"))


# Part B: Fix It

def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart


print("\nPart B - Correct Version:")
print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", cart=["bread"]))
print(add_item("eggs"))


# Part C: Build the Cart

def create_cart(owner, discount=0):
    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }


def add_to_cart(cart, name, price, qty=1):
    cart["items"].append({
        "name": name,
        "price": price,
        "qty": qty
    })


def update_price(price_tuple, new_price):
    try:
        price_tuple[1] = new_price
    except TypeError:
        print("TypeError: Tuple values cannot be changed because tuples are immutable.")


def calculate_total(cart):
    total = 0

    for item in cart["items"]:
        total += item["price"] * item["qty"]

    discount_amount = total * cart["discount"] / 100
    final_total = total - discount_amount

    return final_total


cart1 = create_cart("Aarav", 10)
cart2 = create_cart("Meera", 5)

add_to_cart(cart1, "Notebook", 50, 2)
add_to_cart(cart1, "Pen", 10, 5)

add_to_cart(cart2, "Bag", 800, 1)
add_to_cart(cart2, "Bottle", 200, 2)

print("\nPart C - Shopping Carts:")
print(cart1)
print(cart2)

print("Cart 1 Total:", calculate_total(cart1))
print("Cart 2 Total:", calculate_total(cart2))

sample_price = ("Notebook", 50)
update_price(sample_price, 60)


# Discussion Points:
# 1. discount=0 is safe because integers are immutable, but cart=[] is dangerous because lists are mutable.
# 2. Rebinding means assigning a variable to a new object, while mutating means changing the same object.
# 3. Mutable: list, dict, set. Immutable: tuple, str, int.
# 4. Yes, if a list is passed into a function and modified, the changes reflect outside because the same list object is used.