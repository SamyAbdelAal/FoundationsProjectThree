# CREATION OF DATA
######################### DO NOT MODIFY THIS CODE ###########################
from components import Person, Club
steve = Person("Steve", "average joe", 27)
michelle = Person("Michelle", "average jane", 12)
john = Person("John", "a blond guy", 32)
ron = Person("Ron", "a red guy", 23)
maha = Person("Maha", "a shy girl", 22)
fatma = Person("Fatma", "a fruit", 24)
dude = Person("Dude", "a college 'dude'", 25)
dudette = Person("Dudette", "a meme", 7)
forever_alone = Person("Forever Alone", "a more popular meme", 9)
confession_bear = Person("Confession Bear", "an even more popular meme", 10)
jack = Person("Jack", "an american", 43)
audrey = Person("Audrey", "just some woman", 31)
asis = Person("Asis", "a joke we have at Coded", 1)
caesar = Person("Julius Caesar", "Google me.", 56)
marcus_aurelius = Person("Marcus Aurelius", "Roman Emperor, philosopher. 'Nuff said.", 61)

people = [
	steve,
	michelle,
	john,
	ron,
	maha,
	fatma,
	dude,
	dudette,
	forever_alone,
	confession_bear,
	jack,
	audrey,
	asis,
	caesar,
	marcus_aurelius
]

population = []
for person in people:
	population.append(person)


book = Club("Book Club", "A book club")
book.assign_president(ron)
book.recruit_member(ron)
book.recruit_member(steve)
book.recruit_member(maha)
book.recruit_member(confession_bear)
book.recruit_member(audrey)


sports = Club("Sports Club", "A sports club")
sports.recruit_member(jack)
sports.assign_president(jack)
sports.recruit_member(michelle)
sports.recruit_member(john)
sports.recruit_member(caesar)
sports.recruit_member(marcus_aurelius)

coding = Club("Coding Club", "A coding club")
coding.recruit_member(dudette)
coding.assign_president(dudette)
coding.recruit_member(dude)
coding.recruit_member(forever_alone)
coding.recruit_member(confession_bear)
coding.recruit_member(asis)

glub = Club("Glub Club", "A glubbing club")
glub.recruit_member(fatma)
glub.assign_president(fatma)
glub.recruit_member(steve)
glub.recruit_member(john)
glub.recruit_member(maha)
glub.recruit_member(caesar)



clubs = [book, sports, coding, glub]


