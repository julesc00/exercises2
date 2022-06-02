
class User:

    def sign_in(self):
        print("log in")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        return print(f"attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        return print(f"attacking with arrows of {self.num_arrows}")


wizard1 = Wizard("Merlin", 50)
archer1 = Archer("Robin", 100)
print(isinstance(wizard1, object))


# Base class
class Mouse(object):
    def __init__(self, mouse_qty):
        self.mouse_qty = mouse_qty

    def product_availability(self):
        return f"Mouse qty from mouse class: {self.mouse_qty}"


# Drive class
class ProductStock(Mouse):
    def __init__(self, mouse_qty, keyboard_qty, display_qty):
        self.keyboard_qty = keyboard_qty
        self.display_qty = display_qty
        Mouse.__init__(self, mouse_qty)

    def product_stock_details(self):
        return f"Mouse Qty: {self.mouse_qty}\nKeyboard Qty: {self.keyboard_qty}\nDisplay Qty: {self.display_qty}"


prod_obj = ProductStock(200, 300, 400)
print(prod_obj.product_availability())
print(prod_obj.product_stock_details())
