#The Willsistance, a version of The Resistance staring Will Smith

import random

#Lists of All Roles
Good_Roles = ['The bird from his new movie - Good','Dr. Hitchens - Good','I,Robot - Good','Independence Day Will - Good','Jim West - Good','Agent J - Good']
Bad_Roles = ['Get Jiggy Pharoh - Bad','Gemini - Bad','After Earth - Bad', 'Shark Tale Character - Bad']
bad_special_roles = ['Hancock - Bad', 'Deadshot - Bad', 'Will Smith Genie - Bad', 'Will Smith on Youtube - Bad']
good_special_roles = ['The Fresh Prince - Good', 'Miami Will - Good']

#Makes a list of players
def game_info():
    players = int(input('How many people are playing? '))
    player_list = []
    while len(player_list) < players:
        player = input("Enter player " + str(len(player_list) + 1) + "'s name: ")
        player_list.append(player) 
    return player_list

#Tryin real hard to get technical but still needed if and elifs for 10-5 players
def good_and_bad(player_list):
    if len(player_list) == 10:
        roles = (Good_Roles[0:6] + Bad_Roles[0:4])
    elif len(player_list) == 9:
        roles = (Good_Roles[0:6] + Bad_Roles[0:3])
    elif len(player_list) == 8:
        roles = (Good_Roles[0:5] + Bad_Roles[0:3])
    elif len(player_list) == 7:
        roles = (Good_Roles[0:4] + Bad_Roles[0:3])
    elif len(player_list) == 6:
        roles = (Good_Roles[0:4] + Bad_Roles[0:2])
    elif len(player_list) == 5:
        roles = (Good_Roles[0:3] + Bad_Roles[0:2])
    return roles
        
#Turned out to be useful for assigning special spy roles. (We got Deadshot now! xD)
def dirty_spies(roles):
    spies = 0
    if len(roles) == 10:
        spies += 4
    elif len(roles) >= 7:
        spies += 3
    else:
        spies += 2
    return spies

#Finishing touches and meat of program
def player_assignments(player_list):
    global roles
    global spies
    special_roles = int(input('''Please select an option:
                  1. Merlin, Morgana, Percival
                  2. Merlin, Morgana, Percival, Mordred
                  3. All roles
                  4. No special roles
                  '''))
    roles = good_and_bad(player_list)
    spies = dirty_spies(roles)
    if special_roles == 3:
        if spies == 4:
            del roles[-4:]
        elif spies == 3:
            del roles[-3:]
            bad_special_roles.remove('Deadshot - Bad')
        elif spies == 2:
            print('Sorry, but you can\'t have all roles with this few players. Please re-run program with a different special role selection.')
            exit()
        roles = (roles + good_special_roles + bad_special_roles)
        del roles[0:2]
    elif special_roles == 2:
        if spies == 2:
            del roles[-2]
        else:
            del roles[-3:]
        roles = (roles + good_special_roles + bad_special_roles[:-1])
        del roles[0:2]
    elif special_roles == 1:
        del roles[-2:]
        roles = (roles + good_special_roles + bad_special_roles[:-2])
        del roles[0:2]
    random.shuffle(roles)
    assignments = list(zip(roles, player_list))
    for assn in assignments:
        print("\n{0} : {1}\r\n".format(assn[0],assn[1]))
        
#All you need to execute it
player_list = game_info ()
player_assignments (player_list)

