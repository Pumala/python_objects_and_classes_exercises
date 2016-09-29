class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeted_people = []
        self.greeting_count = 0
        self.unique_count = 0

    def greet(self, other_person):
        print "Hello %s, I am %s!" % (other_person.name, self.name)
        self.greeting_count += 1
        if other_person.name not in self.greeted_people:
            self.greeted_people.append(other_person.name)
            self.unique_count += 1
        else:
            pass

    def print_contact_info(self):
        print "%s's email: %s, %s's phone number: %s" % (self.name, self.email, self.name, self.phone)

    def add_friend(self, friend):
        self.friends.append(friend)

    def num_friends(self):
        print len(self.friends)

    def __repr__(self):
        return '%s %s %s' % (self.name, self.email, self.phone)

    def num_unique_people_greeted(self):
        print self.unique_count
        # if self.greet(other_person) not in self.friends:
        #     return False
        # else:
        #     return True
        # if self.unique_count[index] not in
        # for index in len(self.unique_count):
        #     if self.unique_count[index] not in

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
opal = Person("Opal", "opal@yahoo.com", "856-542-9562")

# sonny.add_friend(jordan)
#
# sonny.num_friends()

print sonny.greeting_count

sonny.greet(jordan)
sonny.greet(jordan)

sonny.greet(jordan)
opal.greet(jordan)
sonny.greet(opal)
sonny.greet(opal)
sonny.greet(opal)

# print sonny.friends

# print jordan

print sonny.greeting_count
sonny.num_unique_people_greeted()
print sonny.greeted_people

# sonny.friends.append(jordan)
# print len(sonny.friends)
# print sonny.friends


# # 1. Instantiate an instance object of Person with name of 'Sonny', email of 'sonny@hotmail.com', and phone of '483-485-4948', store it in the variable sonny.
# sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
#
# # 2. Instantiate another person with the name of 'Jordan', email of 'jordan@aol.com', and phone of '495-586-3456', store it in the variable 'jordan'.
# jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
#
# # 3. Have sonny greet jordan using the greet method.
# sonny.greet(jordan)
#
# # 4. Have jordan greet sonny using the greet method.
# jordan.greet(sonny)
#
# # 5. Write a print statement to print the contact info (email and phone) of Sonny.
# print "Name: %s, Email: %s, Phone: %s " % (sonny.name, sonny.email, sonny.phone)
#
# # 6. Write another print statement to print the contact info of Jordan.
# print "Name: %s, Email: %s, Phone: %s " % (jordan.name, jordan.email, jordan.phone)
#
# #7. Add a print_contact_info method to the Person class that will print out the contact info for a object instance of Person. You will use it thus:
# sonny.print_contact_info()
