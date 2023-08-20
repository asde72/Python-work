import sys
class VendingMachine:
    def __init__(self):
        self.bottles = 20
    def purchase(self, amount):
        if self.bottles < amount:
            print("Not Enough Stock")
            sys.exit()
        else:
            self.bottles -= amount
            return self.bottles
    def restock(self, amount):
        self.bottles += amount
    def get_inventory(self):
        return self.bottles
    def report(self):
        print(f'Inventory: {self.bottles} bottles')
if __name__ == "__main__":
    purchases = int(input("How many drinks would you like to purchase"))
    restocker = int(input("How many drinks would you like to restock"))
    Vending = VendingMachine()
    Vending.purchase(purchases)
    Vending.restock(restocker)
    Vending.get_inventory()
    Vending.report()