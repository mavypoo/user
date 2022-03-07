class User:
    
    def __init__(self, name, email):
        self.name = name 
        self.email = email
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount

    def with_drawal(self, amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f'User: {self.name}, Balance: {self.amount}')

    def transfer_money(self, amount, user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self


mav = User('mav', 'mav@gmail.com')
mav.make_deposit(800 )
mav.make_deposit(100 )
mav.make_deposit(100 )
mav.with_drawal(50)
mav.display_user_balance()

rob = User('rob', 'rob@gmail.com')
rob.make_deposit(200)
rob.make_deposit(600)
rob.with_drawal(100)
rob.with_drawal(100)
rob.display_user_balance()

derek = User('derek', 'derek@gmail.com')
derek.make_deposit(500)
derek.with_drawal(50)
derek.with_drawal(50)
derek.with_drawal(50)
derek.display_user_balance()
