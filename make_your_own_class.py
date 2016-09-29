class Vehicle(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


car = Vehicle("Nissan", "Leaf", 2015)

print "Make: %s, Model: %s, Year: %s" % (car.make, car.model, car.year)
