# UTILS AND FUNCTIONALITY
from data import population, clubs
from components import Club, Person

my_name = input("What's your name?: ")
while True:
    try:
        my_age = int(input("How old are you?: "))
    except ValueError:
        print("Non-numeric value: ")
        continue
    break
my_bio = input("Describe yourself: ")
myself = Person(my_name, my_bio, my_age)


def introduction():
    print("Hello, %s. Welcome to our portal." % my_name)
    print("---------------------")


def options():
    # your code goes here!
    while True:
        print_menu()
        try:
            opt = int(input("Type the number of the option: "))
            while opt != -1:
                if opt == 1:
                    create_club()
                elif opt == 2:
                    view_clubs()
                    join_clubs()
                elif opt == 3:
                    view_clubs()
                elif opt == 4:
                    view_club_members()
                elif opt == 5:
                    quit_president()
                elif opt == 6:
                    kick_member()
                elif opt == 7:
                    """Since the user can join many clubs i have to check which club they want to quit"""
                    club=""
                    not_in_club = True
                    for i in clubs:
                        if myself in i.members_list:
                            not_in_club = False
                            print(i.name)
                            inp = input("is this the club you want to quit? (y/n) ").lower().strip()
                            if inp == "y":
                                club = i
                                break
                    if club != "" and len(club.members_list) >1:
                        club.remove_member(myself)
                        club.assign_president(club.members_list[0])
                    elif club != "" and len(club.members_list) ==1:
                        print("Club only has you as a member")
                    elif not not_in_club:
                        print("You didn't quit any clubs")
                    else:
                        print("You are not in a club")
                elif opt == 8:
                    not_in_club = True
                    club=""
                    for i in clubs:
                        # checks which clubs the user is a president for and asks which one they want to continue with
                        if myself == i.president:
                            not_in_club = False
                            print(i.name)
                            inp = input("is this the club you want to quit? (y/n) ").lower().strip()
                            if inp == "y":
                                club = i
                                break
                    if club!="":
                        club.disband_club()
                        clubs.remove(club)
                        print("The club has been disbanded")
                    elif not not_in_club:
                        print("You didn't quit any clubs")
                    else:
                        print("You are not a president of a club")

                print_menu()
                opt = int(input("Type the number of the option: "))
        except ValueError:
            print("Non-numeric Value")
            continue
        break


def print_menu():
    print("Would you like to:\n"
          "1) Create a club \n"
          "2) Browse and join clubs\n"
          "3) View Existing clubs\n"
          "4) Display members of a club \n"
          "5) Quit a club as president\n"
          "6) Kick a member out of your club\n"
          "7) Quit a club \n"
          "8) Disband your club\n"
          "or \n-1) Close application\n")
    print("---------------------")


def create_club():
    # your code goes here!
    club_exists = False
    club_added = False
    while not club_added:
        """I have to check if the club name already exists to avoid repetition problems"""
        club_name = input("Pick a name for your club: ")
        for i in clubs:
            if club_name.lower().strip() == i.name.lower().strip():
                club_exists = True
        if not club_exists: # only add the club if it doesn't exist
            club_description = input("What is your club about?\n")
            club = Club(club_name, club_description)
            club.assign_president(myself)
            club.recruit_member(myself)
            print("Enter the number of the member you want to add to your club or '-1' to stop")
            for i in range(0, len(population)):
                print("[%d] %s" % (i + 1, population[i].name))
            opt = 0
            # Loops through asking the user to add members and checks if they've been already added
            while opt != -1:
                try:
                    opt = int(input("Enter the number :"))
                    if 0 < opt <= len(population) and population[opt - 1] not in club.members_list:
                        club.recruit_member(population[opt - 1])
                    else:
                        print("Member non-existent or already added")
                except ValueError:
                    print("Non-numeric value")
            club.print_club()
            clubs.append(club)
            club_added = True
        else:
            print("Club name already exists")
            club_exists = False


def search_member(club):
    """Searches for a member the user chooses and returns their index in the clubs member_list"""
    if len(club.members_list) > 1:
        for i in range(0, len(club.members_list)):
            if myself.name != club.members_list[i].name:
                print("[%d] %s" % (i , club.members_list[i].name))
        while True:
            try:
                num = int(input("Enter their number: "))
                if 0 < num <= len(club.members_list):
                    return num
                else:
                    print("Member non-existent")

            except ValueError:
                print("Non-numeric value")
                continue
            break
    else:
        print("Club only has you as a member")


def view_clubs():
    # your code goes here!
    print("---------------------")
    for i in clubs:
        print("NAME: %s\nDESCRIPTION: %s\nMEMBERS:%d\n" % (i.name, i.description, len(i.members_list)))
    print("---------------------")


def view_club_members():
    # your code goes here!
    view_clubs()
    opt = ""
    while opt != "back":
        # Loops through asking the user to which club members they want to see and if it's a valid club
        valid_club = False
        opt = input("Enter the name of the club you wish to see its members: or 'back' to go back ")
        for i in clubs:
            if opt.lower().strip() == i.name.lower().strip():
                valid_club = True
                print("Members: ")
                i.print_club()
        if not valid_club and opt != "back":
            print("Club non-existent")
            valid_club = False


def join_clubs():
    # your code goes here!
    opt = ""
    while opt != "back":
        # Loops through asking the user to which club they want to join
        # and if it's a valid club or if they're already a member
        valid_club = False
        opt = input("Enter the name of the club you wish to join: or 'back' to go back ")
        for i in clubs:
            if opt.lower().strip() == i.name.lower().strip():
                valid_club = True
                if myself not in i.members_list and myself != i.president:
                    i.recruit_member(myself)
                    print(myself.name, "just joined", i.name)
                else:
                    print("You're already in", i.name)
        if not valid_club and opt != "back":
            print("Club non-existent or was misspelled")
            valid_club = False


def quit_president():
    """User needs to be a president of a club to assign someone else as president or disband the club"""
    club =""
    opt=0
    for i in clubs:
        # checks which clubs the user is a president for and asks which one they want to continue with
        if myself == i.president:
            print(i.name)
            inp = input("is this the club you want to quit? (y/n) ").lower().strip()
            if inp == "y":
                club = i
                break
    if club!="" and len(club.members_list) >1:
        while True:
            try:
                opt = int(input("1) Do you want to assign someone else as president? \n"
                                "2) Do you want to quit and assign someone else as president?\n"
                                "-1) Go back\n"))
                if opt ==1:
                            print("Who do you want to assign as president? ")
                            member = search_member(club)
                            if member is not None:
                                club.assign_president(club.members_list[member])
                                print(club.president.name,"assigned as president")
                                me, pres= club.members_list.index(myself), member
                                club.members_list[pres], club.members_list[me] = club.members_list[me],club.members_list[pres]
                elif opt ==2:
                            print("Who do you want to assign as president? ")
                            member = search_member(club)
                            if member is not None:
                                club.assign_president(club.members_list[member])
                                print(club.president.name,"assigned as president")
                                me, pres = club.members_list.index(myself), member
                                club.members_list[pres], club.members_list[me] = club.members_list[me], club.members_list[pres]
                                club.members_list.remove(myself)
                                print(myself.name,"removed from",club.name)
                elif opt ==-1:
                    return
            except ValueError:
                print("Non-numeric value")
                continue
            break
    elif club != "" and len(club.members_list) == 1:
        print("Club only has you as a member")
    else:
        print("You didn't quit any clubs or You are not a president of a club")


def kick_member():
    """User needs to be a president of a club and can't kick themselves out"""
    club = ""
    not_in_club = True
    for i in clubs:
        # checks which clubs the user is a president for and asks which one they want to continue with
        if myself == i.president:
            not_in_club = False
            print(i.name)
            inp = input("is this the club you want to quit? (y/n) ").lower().strip()
            if inp == "y":
                club = i
                break
    if club !="":
        print("Who would you like to kick out?")
        member= search_member(club)
        if member is not None:
            club.remove_member(club.members_list[member])
    elif not not_in_club:
        print("You didn't kick anyone")
    else:
        print("You are not a president of a club")


def application():
    introduction()
    # your code goes here!
    options()
