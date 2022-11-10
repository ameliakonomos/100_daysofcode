#pass in as many parameters as you want and return total sum
#passing in args
def add(*args):

    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3, 10, 100, 1000, 100000))
#asteric packs all input into a tuple

#kwargs: many keywork arguments
def calculate(n, **kwargs):
    #kwargs is a dictionary of remainder arguments
    # for key, value in kwargs.items()
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add= 3, multiply=5)

#create a class
class Car:

    def __init__(self, **kw):
        #kw is optional arguments that we pass in when initializing new object from class
        self.make = kw["make"]
        self.model = kw["model"]
        self.color = kw.get("color")

my_car = Car(make = "Nissan", model = "GT-R", color = "black")
print(my_car)
print(my_car.color)


