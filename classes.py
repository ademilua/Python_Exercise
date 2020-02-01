# Create class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age =age
        
def greeting(self):
    return ('My name is {self.name} and I am {self.age}')
        
# Init user object

Tolu = User('Tolu Ademilua', 'tolu@gmail.com', 33)
Precious = User('Precious Ademilua', 'precious@gmail.com', 33)

# Edit Property
Tolu.age = 34
#print(Tolu.age)
#print(Precious.email)

# call methods

print(Tolu.greeting())