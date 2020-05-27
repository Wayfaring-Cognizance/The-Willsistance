import random

Good_Roles = ['The bird from his new movie - Good','Dr. Hitchens - Good','I,Robot - Good','Independence Day Will - Good','Jim West - Good','Agent J - Good']
Bad_Roles = ['Get Jiggy Pharoh - Bad','Gemini - Bad','After Earth - Bad', 'Shark Tale Character - Bad']
bad_special_roles = ['Will Smith Genie - Bad', 'Hancock - Bad', 'Deadshot - Bad', 'Will Smith on Youtube - Bad']#ended up needing this or deadshot, along with ten players needing 4 speis, cause a lot of trouble

def game_info():
    global player_list
    global special_roles
    players = int(input('How many people are playing? '))
    special_roles = int(input('''Please select an option:
                  1. Merlin, Morgana, Percival
                  2. Merlin, Morgana, Percival, Mordred
                  3. All roles
                  4. No special roles
                  '''))

    if players == 10:
        player_one = input('Player One: ')
        player_two = input('Player Two: ')
        player_three = input('Player Three: ')
        player_four = input('Player Four: ')
        player_five = input('Player Five: ')
        player_six = input('Player Six: ')
        player_seven = input('Player Seven: ')
        player_eight = input('Player Eight: ')
        player_nine = input('Player Nine: ')
        player_ten = input('Player Ten: ')
        player_list = [player_one, player_two, player_three, player_four, player_five, player_six, player_seven, player_eight, player_nine, player_ten]
    elif players == 9:
        bad_special_roles.remove ('Deadshot - Bad')
        Bad_Roles.remove('Gemini - Bad')
        player_one = input('Player One: ')
        player_two = input('Player Two: ')
        player_three = input('Player Three: ')
        player_four = input('Player Four: ')
        player_five = input('Player Five: ')
        player_six = input('Player Six: ')
        player_seven = input('Player Seven: ')
        player_eight = input('Player Eight: ')
        player_nine = input('Player Nine: ')
        player_list = [player_one, player_two, player_three, player_four, player_five, player_six, player_seven, player_eight, player_nine]
    elif players == 8:
        bad_special_roles.remove ('Deadshot - Bad')
        Bad_Roles.remove('Gemini - Bad')
        Good_Roles.remove('The bird from his new movie - Good')
        player_one = input('Player One: ')
        player_two = input('Player Two: ')
        player_three = input('Player Three: ')
        player_four = input('Player Four: ')
        player_five = input('Player Five: ')
        player_six = input('Player Six: ')
        player_seven = input('Player Seven: ')
        player_eight = input('Player Eight: ')
        player_list = [player_one, player_two, player_three, player_four, player_five, player_six, player_seven, player_eight]
    elif players == 7:
        bad_special_roles.remove ('Deadshot - Bad')
        Bad_Roles.remove('Gemini - Bad')
        Good_Roles.remove('I,Robot - Good')
        Good_Roles.remove('The bird from his new movie - Good')
        player_one = input('Player One: ')
        player_two = input('Player Two: ')
        player_three = input('Player Three: ')
        player_four = input('Player Four: ')
        player_five = input('Player Five: ')
        player_six = input('Player Six: ')
        player_seven = input('Player Seven: ')
        player_list = [player_one, player_two, player_three, player_four, player_five, player_six, player_seven]
    elif players <= 6 and special_roles == 3:
        print('Sorry, that does not work, please try more players or less roles')
        exit() #is there a better program termination to use?
    elif players == 6:
        bad_special_roles.remove ('Deadshot - Bad')
        bad_special_roles.remove ('Will Smith on Youtube - Bad')
        Bad_Roles.remove('After Earth - Bad')
        Bad_Roles.remove('Gemini - Bad')
        Good_Roles.remove('I,Robot - Good')
        Good_Roles.remove('The bird from his new movie - Good')
        player_one = input('Player One: ')
        player_two = input('Player Two: ')
        player_three = input('Player Three: ')
        player_four = input('Player Four: ')
        player_five = input('Player Five: ')
        player_six = input('Player Six: ')
        player_list = [player_one, player_two, player_three, player_four, player_five, player_six]
    elif players <= 5 and special_roles == 3:
        print('Sorry, that does not work, please try more players or less roles')
        exit() #is there a better program termination to use?
    else:
        bad_special_roles.remove ('Deadshot - Bad')
        bad_special_roles.remove ('Will Smith on Youtube - Bad')
        Bad_Roles.remove('After Earth - Bad')
        Bad_Roles.remove('Gemini - Bad')
        Good_Roles.remove('I,Robot - Good')
        Good_Roles.remove('The bird from his new movie - Good')
        Good_Roles.remove('Dr. Hitchens - Good')
        player_one = input('Player One: ')
        player_two = input('Player Two: ')
        player_three = input('Player Three: ')
        player_four = input('Player Four: ')
        player_five = input('Player Five: ')
        player_list = [player_one, player_two, player_three, player_four, player_five]


def player_assignments():

    if special_roles == 4:
        roles =  (Good_Roles + Bad_Roles)
        random.shuffle(roles)
        assignments = zip(roles, player_list)
        money_shot = list(assignments)
        print(list(money_shot))
    elif special_roles == 3:
        roles = (Good_Roles + bad_special_roles) 
        roles.append('The Fresh Prince - Good')
        roles.append('Miami Will - Good')
        roles.remove('Independence Day Will - Good')
        roles.remove('Jim West - Good')
        random.shuffle(roles)
        assignments = zip(roles, player_list)
        money_shot = list(assignments)
        print(list(money_shot))
    elif special_roles == 2: #Deadshot (The Assassin for Willsistance) is not added here, which annoys me, but if he is added there will be too many spies for 6 and 5 player games. 
        roles = (Good_Roles + Bad_Roles)
        roles.append('The Fresh Prince - Good')
        roles.append('Miami Will - Good')
        roles.append('Will Smith Genie - Bad')
        roles.append('Hancock - Bad')
        roles.remove('Independence Day Will - Good')
        roles.remove('Jim West - Good')
        roles.remove('Shark Tale Character - Bad')
        roles.remove('Get Jiggy Pharoh - Bad')
        random.shuffle(roles)
        assignments = zip(roles, player_list)
        money_shot = list(assignments)
        print(list(money_shot))
    else:
        roles = (Good_Roles + Bad_Roles)
        roles.append('The Fresh Prince - Good')
        roles.append('Miami Will - Good')
        roles.append('Hancock - Bad')
        roles.append('Deadshot - Bad')
        roles.remove('Independence Day Will - Good')
        roles.remove('Jim West - Good')
        roles.remove('Shark Tale Character - Bad')
        roles.remove('Get Jiggy Pharoh - Bad')
        random.shuffle(roles)
        assignments = zip(roles, player_list)
        money_shot = list(assignments)
        print(list(money_shot))
        

game_info ()
player_assignments ()

