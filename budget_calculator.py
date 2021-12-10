class Category():

    """
    A class the makes a budget category where can be deposited to,
    withdrawn from, and transfered in and out.
    """

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.led_desc = [f"{self.name:*^30}\n", ]

    def __str__(self):

        for i in self.ledger:
            d = i.get('des')[:23] if len(i.get('des')) > 23 else i.get('des')
            a = f"{i.get('amnt'):.2f}"
            desc = f"{d:<23}{a[:7]:>7}\n"
            self.led_desc.append(desc)

        self.led_desc.append(f"Total: ${self.get_balance():<23.2f}")
        message = "".join(self.led_desc)
        return(str(message))

    def get_balance(self):
        balance = sum([i.get("amnt") for i in self.ledger])
        return(balance)

    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return (True)
        elif self.get_balance() < amount:
            return (False)

    def deposit(self, amount, description=""):
        dep = {
            "amnt": amount,
            "des": description,
        }
        self.ledger.append(dep)

    def withdraw(self, amount, description=""):
        amount = 0 - amount
        if self.check_funds(amount):
            wdrw = {
                "amnt": amount,
                "des": description
            }
            self.ledger.append(wdrw)
            return(True)
        else:
            return(False)

    def transfer(self, amount, destination):
        amount_with = 0 - amount

        if self.check_funds(amount):
            self.withdraw(amount_with, f"Transfer to {destination.name}")
            destination.deposit(amount, f"Transfer from {self.name}")
            return(True)
        else:
            return(False)


Food = Category("Food")
Food.deposit(1000, "initial deposit")
Food.deposit(2000, "second deposit")
Food.withdraw(500, "first withdraw")

Entertainment = Category("Entertainment")
Entertainment.deposit(500, "strip club")
Food.transfer(500, Entertainment)

print(Entertainment)
print(Food)

print("added some stuff from computer")
