class Vehicle(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print "Make: %s, Model: %s, Year: %s" % (self.make, self.model, self.year)


car = Vehicle("Nissan", "Leaf", 2015)

print car.print_info()
