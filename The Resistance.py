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
        
#Turned out to be useful for assigning special spy roles. (We got Deadshot now! xD)
def dirty_spies(players):
    if len(players) == 10:
        return 4
    elif len(players) >= 7:
        return 3
    else:
        return 2

#Finishing touches and meat of program
def player_assignments(player_list):
    global spies
    special_roles = int(input('''Please select an option:
                  1. Merlin, Morgana, Percival
                  2. Merlin, Morgana, Percival, Mordred
                  3. All roles
                  4. No special roles
                  '''))
    
    spies = dirty_spies(player_list)
    num_good = len(player_list) - spies
    random.shuffle(Good_Roles)
    random.shuffle(Bad_Roles)
    if special_roles == 4:
        roles = (Good_Roles[0:num_good] + Bad_Roles[0:spies])
    elif special_roles == 3:
        num_good -= 2
        if spies == 3:
            del bad_special_roles[1]
        elif spies == 2:
            print('Sorry, but you can\'t have all roles with this few players. Please re-run program with a different special role selection.')
            exit()
        roles = (good_special_roles + bad_special_roles) + Good_Roles[0:num_good]
    elif special_roles == 2:
        num_good -= 2
        if spies == 2:
            del bad_special_roles[1]
            spies -= 2
        else:
            spies -= 3
        roles = (good_special_roles + bad_special_roles[:-1]) + (Good_Roles[0:num_good] + Bad_Roles[0:spies])
    elif special_roles == 1:
        num_good -= 2
        spies -= 2
        roles = (good_special_roles + bad_special_roles[:-2]) + (Good_Roles[0:num_good] + Bad_Roles[0:spies])
    random.shuffle(roles)
    assignments = list(zip(roles, player_list))
    for assn in assignments:
        print("\n{0} : {1}\r\n".format(assn[0],assn[1]))
        
#All you need to execute it
player_list = game_info ()
player_assignments (player_list)

