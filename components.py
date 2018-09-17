# CLASSES AND METHODS
class Person():
    def __init__(self, name, bio, age):
        # your code goes here!
        self.name = name
        self.bio = bio
        self.age = age

    def __str__(self):
        return "- %s (%d years old) - %s" % (self.name, self.age, self.bio)


class Club():

    def __init__(self, name, description):
        # your code goes here!
        self.name = name
        self.description = description
        self.president = ""
        self.members_list = []

    def assign_president(self, person):
        # your code goes here!
        self.president = person

    def recruit_member(self, person):
        # your code goes here!
        self.members_list.append(person)

    def print_member_list(self):
        # your code goes here!
        if self.president != "":
            print("- %s (%d years old, President) - %s" % (self.president.name, self.president.age, self.president.bio))
        print(*self.members_list,sep="\n")

    def print_club(self):
        print(" %s \n %s " % (self.name, self.description))
        print("Members: ")
        self.print_member_list()

    def average_age(self):
        total=0
        average=0
        for i in self.members_list:
            total += i.age
        average = total/(len(self.members_list))
        return average

    def disband_club(self):
        self.name=""
        self.description=""
        self.members_list=[]

    def remove_member(self,person):
        self.members_list.remove(person)
        print(person.name,"removed")