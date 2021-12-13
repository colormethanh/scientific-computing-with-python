class Category():

    """
    A class the makes a budget category where can be deposited to,
    withdrawn from, and transfered in and out.
    """

    def __init__(self, name):
        self.name = name.title()
        self.ledger = []
        self.led_desc = [f"{self.name:*^30}\n", ]

    def __str__(self):

        for i in self.ledger:
            d = i.get('des')[:23] if len(i.get('des')) > 23 else i.get('des')
            a = f"{i.get('amnt'):.2f}"
            desc = f"{d:<23}{a[:7]:>7}\n"
            self.led_desc.append(desc)

        self.led_desc.append(f"Total: {self.get_balance():<23.2f}")
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

        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {destination.name}")
            destination.deposit(amount, f"Transfer from {self.name}")
            return(True)
        else:
            return(False)


def create_spend_chart(*categories):
    """
    A funtion that collects a list of categories and prints out them
    average spent by categories
    """
    total_spent = 0
    cat_lst = []
    spend_chart = [
        ["Percentage spent by category"],
        ["100|", ],
        [f"{90:>3}|", ],
        [f"{80:>3}|", ],
        [f"{70:>3}|", ],
        [f"{60:>3}|", ],
        [f"{50:>3}|", ],
        [f"{40:>3}|", ],
        [f"{30:>3}|", ],
        [f"{20:>3}|", ],
        [f"{10:>3}|", ],
        [f"{0:>3}|", ],
    ]

    spend_name = [
        [f"    {'_' * 10}"]
    ]

    # looping through the categories and making a cat_dic for them
    for cat in categories:
        cat_dic = {"name": cat.name, "spending": 0}
        cat_lst.append(cat_dic)

        # getting total withdraws of all categories and invidual categories
        for item in cat.ledger:
            if item.get("amnt") < 0:
                spending = abs(item.get("amnt"))
                total_spent += spending
                cat_dic["spending"] += spending

    # Getting the percent of total from each category
    for dic in cat_lst:
        average = round((dic.get("spending") / total_spent) * 100)
        dic["average"] = average

    print(cat_lst)
    print(f"Total amount spent: {total_spent}")

    for col in spend_chart:
        for row in col:
            print(row)

    for col_1 in spend_name:
        for row_1 in col_1:
            print(row_1)

    for cat in cat_dic:


food = Category("food")
food.deposit(900, "deposit")
entertainment = Category("entertainment")
entertainment.deposit(900, "deposit")
business = Category("business")
business.deposit(900, "deposit")

food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

create_spend_chart(food, entertainment, business)
