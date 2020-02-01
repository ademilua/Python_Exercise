# Create class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age =age
        
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1

 # Extending User with customer class
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age =age
        self.balance = 0
    def set_balance(self, balance):
        self.balance = balance
     # Overide greeting() method in class User
    
    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and I owe a balance of {self.balance}'
# Init user object

Tolu = User('Tolu Ademilua', 'tolu@gmail.com', 33)
Precious = User('Precious Ademilua', 'precious@gmail.com', 32)

# Edit Property
Tolu.age = 34

Tolu.has_birthday()
 # Init Customer
James = Customer('James brat', 'james@gmail.com', 50)
James.set_balance(500)
print(James.name)
#print(Tolu.age)
print(Precious.email)
print(James.greeting())

# call methods

print(Tolu.greeting())
