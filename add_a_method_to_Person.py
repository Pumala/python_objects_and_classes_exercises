class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def greet(self, other_person):
        print "Hello %s, I am %s!" % (other_person.name, self.name)

    def print_contact_info(self):
        print "%s's email: %s, %s's phone number: %s" % (self.name, self.email, self.name, self.phone)


# 1. Instantiate an instance object of Person with name of 'Sonny', email of 'sonny@hotmail.com', and phone of '483-485-4948', store it in the variable sonny.
sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")

# 2. Instantiate another person with the name of 'Jordan', email of 'jordan@aol.com', and phone of '495-586-3456', store it in the variable 'jordan'.
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

# 3. Have sonny greet jordan using the greet method.
sonny.greet(jordan)

# 4. Have jordan greet sonny using the greet method.
jordan.greet(sonny)

# 5. Write a print statement to print the contact info (email and phone) of Sonny.
print "Name: %s, Email: %s, Phone: %s " % (sonny.name, sonny.email, sonny.phone)

# 6. Write another print statement to print the contact info of Jordan.
print "Name: %s, Email: %s, Phone: %s " % (jordan.name, jordan.email, jordan.phone)

#7. Add a print_contact_info method to the Person class that will print out the contact info for a object instance of Person. You will use it thus:
sonny.print_contact_info()
