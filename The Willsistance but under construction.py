import random

ten_players_no_special = ['Get Jiggy Pharoh - Bad','Gemini - Bad','After Earth - Bad','Shark Tale Character - Bad','The bird from his new movie - Good','Dr. Hitchens - Good','I,Robot - Good','Independence Day Will - Good','Jim West - Good','Agent J - Good']
nine_players_no_special = ['Get Jiggy Pharoh - Bad','Gemini - Bad','After Earth - Bad','The bird from his new movie - Good','Dr. Hitchens - Good','I,Robot - Good','Independence Day Will - Good','Jim West - Good','Agent J - Good']
eight_players_no_special = ['Get Jiggy Pharoh - Bad','Gemini - Bad','After Earth - Bad','Dr. Hitchens - Good','I,Robot - Good','Independence Day Will - Good','Jim West - Good','Agent J - Good']
seven_players_no_special = ['Get Jiggy Pharoh - Bad','Gemini - Bad','After Earth - Bad','Dr. Hitchens - Good','Independence Day Will - Good','Jim West - Good','Agent J - Good']
six_players_no_special = ['Get Jiggy Pharoh - Bad','After Earth - Bad','Dr. Hitchens - Good','Independence Day Will - Good','Jim West - Good','Agent J - Good']
five_players_no_special = ['Get Jiggy Pharoh - Bad','Gemini - Bad','After Earth - Bad','Dr. Hitchens - Good','Jim West - Good','Agent J - Good']

ten_players_merlin = ['Get Jiggy Pharoh - Bad','Gemini - Bad','Deadshot - Bad','Hancock - Bad','Fresh Prince - Good','Dr. Hitchens - Good','I,Robot - Good','Miami Will - Good','Jim West - Good','Agent J - Good']
nine_players_merlin = ['Get Jiggy Pharoh - Bad','Deadshot - Bad','Hancock - Bad','Fresh Prince - Good','Dr. Hitchens - Good','I,Robot - Good','Miami Will - Good','Jim West - Good','Agent J - Good']
eight_players_merlin = ['Get Jiggy Pharoh - Bad','Deadshot - Bad','Hancock - Bad','Fresh Prince - Good','Dr. Hitchens - Good','Miami Will - Good','Jim West - Good','Agent J - Good']
seven_players_merlin = ['Get Jiggy Pharoh - Bad','Deadshot - Bad','Hancock - Bad','Fresh Prince - Good','Miami Will - Good','Jim West - Good','Agent J - Good']
six_players_merlin = ['Deadshot - Bad','Hancock - Bad','Fresh Prince - Good','Miami Will - Good','Jim West - Good','Agent J - Good']
five_players_merlin = ['Deadshot - Bad','Hancock - Bad','Fresh Prince - Good','Miami Will - Good','Agent J - Good']

ten_players_merlin_and_mordred = ['Get Jiggy Pharoh - Bad','Will Smith Genie - Bad','Deadshot - Bad','Hancock - Bad','Fresh Prince - Good','Dr. Hitchens - Good','I,Robot - Good','Miami Will - Good','Jim West - Good','Agent J - Good']
nine_players_merlin_and_mordred = ['Deadshot - Bad','Will Smith Genie - Bad','Hancock - Bad','Fresh Prince - Good','Dr. Hitchens - Good','I,Robot - Good','Miami Will - Good','Jim West - Good','Agent J - Good']
eight_players_merlin_and_mordred = ['Deadshot - Bad','Will Smith Genie - Bad','Hancock - Bad','Fresh Prince - Good','Dr. Hitchens - Good','Miami Will - Good','Jim West - Good','Agent J - Good']
seven_players_merlin_and_mordred = ['Deadshot - Bad','Will Smith Genie - Bad','Hancock - Bad','Fresh Prince - Good','Miami Will - Good','Jim West - Good','Agent J - Good']
six_players_merlin_and_mordred = ['Will Smith Genie - Bad','Hancock - Bad','Fresh Prince - Good','Miami Will - Good','Jim West - Good','Agent J - Good']
five_players_merlin_and_mordred = ['Will Smith Genie - Bad','Hancock - Bad','Fresh Prince - Good','Miami Will - Good','Agent J - Good']

ten_players_all_roles = ['Will Smith on Youtube - Bad','Will Smith Genie - Bad','Deadshot - Bad','Hancock - Bad','Fresh Prince - Good','Dr. Hitchens - Good','I,Robot - Good','Miami Will - Good','Jim West - Good','Agent J - Good']
nine_players_all_roles = ['Will Smith on Youtube - Bad','Will Smith Genie - Bad','Hancock - Bad','Fresh Prince - Good','Dr. Hitchens - Good','I,Robot - Good','Miami Will - Good','Jim West - Good','Agent J - Good']
eight_players_all_roles = ['Will Smith on Youtube - Bad','Will Smith Genie - Bad','Hancock - Bad','Fresh Prince - Good','Dr. Hitchens - Good','Miami Will - Good','Jim West - Good','Agent J - Good']
seven_players_all_roles = ['Will Smith on Youtube - Bad','Will Smith Genie - Bad','Hancock - Bad','Fresh Prince - Good','Miami Will - Good','Jim West - Good','Agent J - Good']


def game_info():
    global players
    global roles
    global player_one
    global player_two
    global player_three
    global player_four
    global player_five
    global player_six
    global player_seven
    global player_eight
    global player_nine
    global player_ten
    global player_list
    
    players = int(input('How many people are playing? '))
    roles = int(input('''Please select an option:
                  1. Merlin, Morgana, Percival
                  2. Merlin, Morgana, Percival, Mordred
                  3. All roles
                  4. No special roles
                  '''))
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

def player_assignments():
    global assignments
    assignments = {ten_players_no_special[i]: player_list[i] for i in range(len(ten_players_no_special))}
    assignments = [(k, v) for k, v in assignments.items()]
    random.shuffle(assignments)
    print (str(assignments))

game_info ()
player_assignments ()
