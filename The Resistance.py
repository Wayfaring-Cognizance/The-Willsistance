# Python Program for The Resistance

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

players = int(input('How many people are playing? '))
roles = int(input('''Please select an option:
                  1. Merlin, Morgana, Percival
                  2. Merlin, Morgana, Percival, Mordred
                  3. All roles
                  4. No special roles
                  '''))

if players == 10 and roles == 4:
    random.shuffle(ten_players_no_special)
    player_one = input('Player One: ')
    print (player_one + ' is ' + ten_players_no_special [0])
    del ten_players_no_special [0]
    player_two = input('Player Two: ')
    print (player_two + ' is ' + ten_players_no_special [0])
    del ten_players_no_special [0]
    player_three = input('Player Three: ')
    print (player_three + ' is ' + ten_players_no_special [0])
    del ten_players_no_special [0]
    player_four = input('Player Four: ')
    print (player_four + ' is ' + ten_players_no_special [0])
    del ten_players_no_special [0]
    player_five = input('Player Five: ')
    print (player_five + ' is ' + ten_players_no_special [0])
    del ten_players_no_special [0]
    player_six = input('Player Six: ')
    print (player_six + ' is ' + ten_players_no_special [0])
    del ten_players_no_special [0]
    player_seven = input('Player Seven: ')
    print (player_seven + ' is ' + ten_players_no_special [0])
    del ten_players_no_special [0]
    player_eight = input('Player Eight: ')
    print (player_eight + ' is ' + ten_players_no_special [0])
    del ten_players_no_special [0]
    player_nine = input('Player Nine: ')
    print (player_nine + ' is ' + ten_players_no_special [0])
    del ten_players_no_special [0]
    player_ten = input('Player Ten: ')
    print (player_ten + ' is ' + ten_players_no_special [0])
    del ten_players_no_special [0]
elif players == 10 and roles == 3:
    random.shuffle(ten_players_all_roles)
    player_one = input('Player One: ')
    print (player_one + ' is ' + ten_players_all_roles [0])
    del ten_players_all_roles [0]
    player_two = input('Player Two: ')
    print (player_two + ' is ' + ten_players_all_roles [0])
    del ten_players_all_roles [0]
    player_three = input('Player Three: ')
    print (player_three + ' is ' + ten_players_all_roles [0])
    del ten_players_all_roles [0]
    player_four = input('Player Four: ')
    print (player_four + ' is ' + ten_players_all_roles [0])
    del ten_players_all_roles [0]
    player_five = input('Player Five: ')
    print (player_five + ' is ' + ten_players_all_roles [0])
    del ten_players_all_roles [0]
    player_six = input('Player Six: ')
    print (player_six + ' is ' + ten_players_all_roles [0])
    del ten_players_all_roles [0]
    player_seven = input('Player Seven: ')
    print (player_seven + ' is ' + ten_players_all_roles [0])
    del ten_players_all_roles [0]
    player_eight = input('Player Eight: ')
    print (player_eight + ' is ' + ten_players_all_roles [0])
    del ten_players_all_roles [0]
    player_nine = input('Player Nine: ')
    print (player_nine + ' is ' + ten_players_all_roles [0])
    del ten_players_all_roles [0]
    player_ten = input('Player Ten: ')
    print (player_ten + ' is ' + ten_players_all_roles [0])
    del ten_players_all_roles [0]
elif players == 10 and roles == 2:
    random.shuffle(ten_players_merlin_and_mordred)
    player_one = input('Player One: ')
    print (player_one + ' is ' + ten_players_merlin_and_mordred [0])
    del ten_players_merlin_and_mordred [0]
    player_two = input('Player Two: ')
    print (player_two + ' is ' + ten_players_merlin_and_mordred [0])
    del ten_players_merlin_and_mordred [0]
    player_three = input('Player Three: ')
    print (player_three + ' is ' + ten_players_merlin_and_mordred [0])
    del ten_players_merlin_and_mordred [0]
    player_four = input('Player Four: ')
    print (player_four + ' is ' + ten_players_merlin_and_mordred [0])
    del ten_players_merlin_and_mordred [0]
    player_five = input('Player Five: ')
    print (player_five + ' is ' + ten_players_merlin_and_mordred [0])
    del ten_players_merlin_and_mordred [0]
    player_six = input('Player Six: ')
    print (player_six + ' is ' + ten_players_merlin_and_mordred [0])
    del ten_players_merlin_and_mordred [0]
    player_seven = input('Player Seven: ')
    print (player_seven + ' is ' + ten_players_merlin_and_mordred [0])
    del ten_players_merlin_and_mordred [0]
    player_eight = input('Player Eight: ')
    print (player_eight + ' is ' + ten_players_merlin_and_mordred [0])
    del ten_players_merlin_and_mordred [0]
    player_nine = input('Player Nine: ')
    print (player_nine + ' is ' + ten_players_merlin_and_mordred [0])
    del ten_players_merlin_and_mordred [0]
    player_ten = input('Player Ten: ')
    print (player_ten + ' is ' + ten_players_merlin_and_mordred [0])
    del ten_players_merlin_and_mordred [0]
elif players == 10 and roles == 1:
    random.shuffle(ten_players_merlin)
    player_one = input('Player One: ')
    print (player_one + ' is ' + ten_players_merlin [0])
    del ten_players_merlin [0]
    player_two = input('Player Two: ')
    print (player_two + ' is ' + ten_players_merlin [0])
    del ten_players_merlin [0]
    player_three = input('Player Three: ')
    print (player_three + ' is ' + ten_players_merlin [0])
    del ten_players_merlin [0]
    player_four = input('Player Four: ')
    print (player_four + ' is ' + ten_players_merlin [0])
    del ten_players_merlin [0]
    player_five = input('Player Five: ')
    print (player_five + ' is ' + ten_players_merlin [0])
    del ten_players_merlin [0]
    player_six = input('Player Six: ')
    print (player_six + ' is ' + ten_players_merlin [0])
    del ten_players_merlin [0]
    player_seven = input('Player Seven: ')
    print (player_seven + ' is ' + ten_players_merlin [0])
    del ten_players_merlin [0]
    player_eight = input('Player Eight: ')
    print (player_eight + ' is ' + ten_players_merlin [0])
    del ten_players_merlin [0]
    player_nine = input('Player Nine: ')
    print (player_nine + ' is ' + ten_players_merlin [0])
    del ten_players_merlin [0]
    player_ten = input('Player Ten: ')
    print (player_ten + ' is ' + ten_players_merlin [0])
    del ten_players_merlin [0]
elif players == 9 and roles == 4:
    random.shuffle(nine_players_no_special)
    player_one = input('Player One: ')
    print (player_one + ' is ' + nine_players_no_special [0])
    del nine_players_no_special [0]
    player_two = input('Player Two: ')
    print (player_two + ' is ' + nine_players_no_special [0])
    del nine_players_no_special [0]
    player_three = input('Player Three: ')
    print (player_three + ' is ' + nine_players_no_special [0])
    del nine_players_no_special [0]
    player_four = input('Player Four: ')
    print (player_four + ' is ' + nine_players_no_special [0])
    del nine_players_no_special [0]
    player_five = input('Player Five: ')
    print (player_five + ' is ' + nine_players_no_special [0])
    del nine_players_no_special [0]
    player_six = input('Player Six: ')
    print (player_six + ' is ' + nine_players_no_special [0])
    del nine_players_no_special [0]
    player_seven = input('Player Seven: ')
    print (player_seven + ' is ' + nine_players_no_special [0])
    del nine_players_no_special [0]
    player_eight = input('Player Eight: ')
    print (player_eight + ' is ' + nine_players_no_special [0])
    del nine_players_no_special [0]
    player_nine = input('Player Nine: ')
    print (player_nine + ' is ' + nine_players_no_special [0])
    del nine_players_no_special [0]
elif players == 9 and roles == 3:
    random.shuffle(nine_players_all_roles)
    player_one = input('Player One: ')
    print (player_one + ' is ' + nine_players_all_roles [0])
    del nine_players_all_roles [0]
    player_two = input('Player Two: ')
    print (player_two + ' is ' + nine_players_all_roles [0])
    del nine_players_all_roles [0]
    player_three = input('Player Three: ')
    print (player_three + ' is ' + nine_players_all_roles [0])
    del nine_players_all_roles [0]
    player_four = input('Player Four: ')
    print (player_four + ' is ' + nine_players_all_roles [0])
    del nine_players_all_roles [0]
    player_five = input('Player Five: ')
    print (player_five + ' is ' + nine_players_all_roles [0])
    del nine_players_all_roles [0]
    player_six = input('Player Six: ')
    print (player_six + ' is ' + nine_players_all_roles [0])
    del nine_players_all_roles [0]
    player_seven = input('Player Seven: ')
    print (player_seven + ' is ' + nine_players_all_roles [0])
    del nine_players_all_roles [0]
    player_eight = input('Player Eight: ')
    print (player_eight + ' is ' + nine_players_all_roles [0])
    del nine_players_all_roles [0]
    player_nine = input('Player Nine: ')
    print (player_nine + ' is ' + nine_players_all_roles [0])
    del nine_players_all_roles [0]
elif players == 9 and roles == 2:
    random.shuffle(nine_players_merlin_and_mordred)
    player_one = input('Player One: ')
    print (player_one + ' is ' + nine_players_merlin_and_mordred [0])
    del nine_players_merlin_and_mordred [0]
    player_two = input('Player Two: ')
    print (player_two + ' is ' + nine_players_merlin_and_mordred [0])
    del nine_players_merlin_and_mordred [0]
    player_three = input('Player Three: ')
    print (player_three + ' is ' + nine_players_merlin_and_mordred [0])
    del nine_players_merlin_and_mordred [0]
    player_four = input('Player Four: ')
    print (player_four + ' is ' + nine_players_merlin_and_mordred [0])
    del nine_players_merlin_and_mordred [0]
    player_five = input('Player Five: ')
    print (player_five + ' is ' + nine_players_merlin_and_mordred [0])
    del nine_players_merlin_and_mordred [0]
    player_six = input('Player Six: ')
    print (player_six + ' is ' + nine_players_merlin_and_mordred [0])
    del nine_players_merlin_and_mordred [0]
    player_seven = input('Player Seven: ')
    print (player_seven + ' is ' + nine_players_merlin_and_mordred [0])
    del nine_players_merlin_and_mordred [0]
    player_eight = input('Player Eight: ')
    print (player_eight + ' is ' + nine_players_merlin_and_mordred [0])
    del nine_players_merlin_and_mordred [0]
    player_nine = input('Player Nine: ')
    print (player_nine + ' is ' + nine_players_merlin_and_mordred [0])
    del nine_players_merlin_and_mordred [0]
elif players == 9 and roles == 1:
    random.shuffle(nine_players_merlin)
    player_one = input('Player One: ')
    print (player_one + ' is ' + nine_players_merlin [0])
    del nine_players_merlin [0]
    player_two = input('Player Two: ')
    print (player_two + ' is ' + nine_players_merlin [0])
    del nine_players_merlin [0]
    player_three = input('Player Three: ')
    print (player_three + ' is ' + nine_players_merlin [0])
    del nine_players_merlin [0]
    player_four = input('Player Four: ')
    print (player_four + ' is ' + nine_players_merlin [0])
    del nine_players_merlin [0]
    player_five = input('Player Five: ')
    print (player_five + ' is ' + nine_players_merlin [0])
    del nine_players_merlin [0]
    player_six = input('Player Six: ')
    print (player_six + ' is ' + nine_players_merlin [0])
    del nine_players_merlin [0]
    player_seven = input('Player Seven: ')
    print (player_seven + ' is ' + nine_players_merlin [0])
    del nine_players_merlin [0]
    player_eight = input('Player Eight: ')
    print (player_eight + ' is ' + nine_players_merlin [0])
    del nine_players_merlin [0]
    player_nine = input('Player Nine: ')
    print (player_nine + ' is ' + nine_players_merlin [0])
    del nine_players_merlin [0]
elif players == 8 and roles == 4:
    random.shuffle(eight_players_no_special)
    player_one = input('Player One: ')
    print (player_one + ' is ' + eight_players_no_special [0])
    del eight_players_no_special [0]
    player_two = input('Player Two: ')
    print (player_two + ' is ' + eight_players_no_special [0])
    del eight_players_no_special [0]
    player_three = input('Player Three: ')
    print (player_three + ' is ' + eight_players_no_special [0])
    del eight_players_no_special [0]
    player_four = input('Player Four: ')
    print (player_four + ' is ' + eight_players_no_special [0])
    del eight_players_no_special [0]
    player_five = input('Player Five: ')
    print (player_five + ' is ' + eight_players_no_special [0])
    del eight_players_no_special [0]
    player_six = input('Player Six: ')
    print (player_six + ' is ' + eight_players_no_special [0])
    del eight_players_no_special [0]
    player_seven = input('Player Seven: ')
    print (player_seven + ' is ' + eight_players_no_special [0])
    del eight_players_no_special [0]
    player_eight = input('Player Eight: ')
    print (player_eight + ' is ' + eight_players_no_special [0])
    del eight_players_no_special [0]
elif players == 8 and roles == 3:
    random.shuffle(eight_players_all_roles)
    player_one = input('Player One: ')
    print (player_one + ' is ' + eight_players_all_roles [0])
    del eight_players_all_roles [0]
    player_two = input('Player Two: ')
    print (player_two + ' is ' + eight_players_all_roles [0])
    del eight_players_all_roles [0]
    player_three = input('Player Three: ')
    print (player_three + ' is ' + eight_players_all_roles [0])
    del eight_players_all_roles [0]
    player_four = input('Player Four: ')
    print (player_four + ' is ' + eight_players_all_roles [0])
    del eight_players_all_roles [0]
    player_five = input('Player Five: ')
    print (player_five + ' is ' + eight_players_all_roles [0])
    del eight_players_all_roles [0]
    player_six = input('Player Six: ')
    print (player_six + ' is ' + eight_players_all_roles [0])
    del eight_players_all_roles [0]
    player_seven = input('Player Seven: ')
    print (player_seven + ' is ' + eight_players_all_roles [0])
    del eight_players_all_roles [0]
    player_eight = input('Player Eight: ')
    print (player_eight + ' is ' + eight_players_all_roles [0])
    del eight_players_all_roles [0]
elif players == 8 and roles == 2:
    random.shuffle(eight_players_merlin_and_mordred)
    player_one = input('Player One: ')
    print (player_one + ' is ' + eight_players_merlin_and_mordred [0])
    del eight_players_merlin_and_mordred [0]
    player_two = input('Player Two: ')
    print (player_two + ' is ' + eight_players_merlin_and_mordred [0])
    del eight_players_merlin_and_mordred [0]
    player_three = input('Player Three: ')
    print (player_three + ' is ' + eight_players_merlin_and_mordred [0])
    del eight_players_merlin_and_mordred [0]
    player_four = input('Player Four: ')
    print (player_four + ' is ' + eight_players_merlin_and_mordred [0])
    del eight_players_merlin_and_mordred [0]
    player_five = input('Player Five: ')
    print (player_five + ' is ' + eight_players_merlin_and_mordred [0])
    del eight_players_merlin_and_mordred [0]
    player_six = input('Player Six: ')
    print (player_six + ' is ' + eight_players_merlin_and_mordred [0])
    del eight_players_merlin_and_mordred [0]
    player_seven = input('Player Seven: ')
    print (player_seven + ' is ' + eight_players_merlin_and_mordred [0])
    del eight_players_merlin_and_mordred [0]
    player_eight = input('Player Eight: ')
    print (player_eight + ' is ' + eight_players_merlin_and_mordred [0])
    del eight_players_merlin_and_mordred [0]
elif players == 8 and roles == 1:
    random.shuffle(eight_players_merlin)
    player_one = input('Player One: ')
    print (player_one + ' is ' + eight_players_merlin [0])
    del eight_players_merlin [0]
    player_two = input('Player Two: ')
    print (player_two + ' is ' + eight_players_merlin [0])
    del eight_players_merlin [0]
    player_three = input('Player Three: ')
    print (player_three + ' is ' + eight_players_merlin [0])
    del eight_players_merlin [0]
    player_four = input('Player Four: ')
    print (player_four + ' is ' + eight_players_merlin [0])
    del eight_players_merlin [0]
    player_five = input('Player Five: ')
    print (player_five + ' is ' + eight_players_merlin [0])
    del eight_players_merlin [0]
    player_six = input('Player Six: ')
    print (player_six + ' is ' + eight_players_merlin [0])
    del eight_players_merlin [0]
    player_seven = input('Player Seven: ')
    print (player_seven + ' is ' + eight_players_merlin [0])
    del eight_players_merlin [0]
    player_eight = input('Player Eight: ')
    print (player_eight + ' is ' + eight_players_merlin [0])
    del eight_players_merlin [0]
elif players == 7 and roles == 4:
    random.shuffle(seven_players_no_special)
    player_one = input('Player One: ')
    print (player_one + ' is ' + seven_players_no_special [0])
    del seven_players_no_special [0]
    player_two = input('Player Two: ')
    print (player_two + ' is ' + seven_players_no_special [0])
    del seven_players_no_special [0]
    player_three = input('Player Three: ')
    print (player_three + ' is ' + seven_players_no_special [0])
    del seven_players_no_special [0]
    player_four = input('Player Four: ')
    print (player_four + ' is ' + seven_players_no_special [0])
    del seven_players_no_special [0]
    player_five = input('Player Five: ')
    print (player_five + ' is ' + seven_players_no_special [0])
    del seven_players_no_special [0]
    player_six = input('Player Six: ')
    print (player_six + ' is ' + seven_players_no_special [0])
    del seven_players_no_special [0]
    player_seven = input('Player Seven: ')
    print (player_seven + ' is ' + seven_players_no_special [0])
    del seven_players_no_special [0]
elif players == 7 and roles == 3:
    random.shuffle(seven_players_all_roles)
    player_one = input('Player One: ')
    print (player_one + ' is ' + seven_players_all_roles [0])
    del seven_players_all_roles [0]
    player_two = input('Player Two: ')
    print (player_two + ' is ' + seven_players_all_roles [0])
    del seven_players_all_roles [0]
    player_three = input('Player Three: ')
    print (player_three + ' is ' + seven_players_all_roles [0])
    del seven_players_all_roles [0]
    player_four = input('Player Four: ')
    print (player_four + ' is ' + seven_players_all_roles [0])
    del seven_players_all_roles [0]
    player_five = input('Player Five: ')
    print (player_five + ' is ' + seven_players_all_roles [0])
    del seven_players_all_roles [0]
    player_six = input('Player Six: ')
    print (player_six + ' is ' + seven_players_all_roles [0])
    del seven_players_all_roles [0]
    player_seven = input('Player Seven: ')
    print (player_seven + ' is ' + seven_players_all_roles [0])
    del seven_players_all_roles [0]
elif players == 7 and roles == 2:
    random.shuffle(seven_players_merlin_and_mordred)
    player_one = input('Player One: ')
    print (player_one + ' is ' + seven_players_merlin_and_mordred [0])
    del seven_players_merlin_and_mordred [0]
    player_two = input('Player Two: ')
    print (player_two + ' is ' + seven_players_merlin_and_mordred [0])
    del seven_players_merlin_and_mordred [0]
    player_three = input('Player Three: ')
    print (player_three + ' is ' + seven_players_merlin_and_mordred [0])
    del seven_players_merlin_and_mordred [0]
    player_four = input('Player Four: ')
    print (player_four + ' is ' + seven_players_merlin_and_mordred [0])
    del seven_players_merlin_and_mordred [0]
    player_five = input('Player Five: ')
    print (player_five + ' is ' + seven_players_merlin_and_mordred [0])
    del seven_players_merlin_and_mordred [0]
    player_six = input('Player Six: ')
    print (player_six + ' is ' + seven_players_merlin_and_mordred [0])
    del seven_players_merlin_and_mordred [0]
    player_seven = input('Player Seven: ')
    print (player_seven + ' is ' + seven_players_merlin_and_mordred [0])
    del seven_players_merlin_and_mordred [0]
elif players == 7 and roles == 1:
    random.shuffle(seven_players_merlin)
    player_one = input('Player One: ')
    print (player_one + ' is ' + seven_players_merlin [0])
    del seven_players_merlin [0]
    player_two = input('Player Two: ')
    print (player_two + ' is ' + seven_players_merlin [0])
    del seven_players_merlin [0]
    player_three = input('Player Three: ')
    print (player_three + ' is ' + seven_players_merlin [0])
    del seven_players_merlin [0]
    player_four = input('Player Four: ')
    print (player_four + ' is ' + seven_players_merlin [0])
    del seven_players_merlin [0]
    player_five = input('Player Five: ')
    print (player_five + ' is ' + seven_players_merlin [0])
    del seven_players_merlin [0]
    player_six = input('Player Six: ')
    print (player_six + ' is ' + seven_players_merlin [0])
    del seven_players_merlin [0]
    player_seven = input('Player Seven: ')
    print (player_seven + ' is ' + seven_players_merlin [0])
    del seven_players_merlin [0]
elif players == 6 and roles == 4:
    random.shuffle(six_players_no_special)
    player_one = input('Player One: ')
    print (player_one + ' is ' + six_players_no_special [0])
    del six_players_no_special [0]
    player_two = input('Player Two: ')
    print (player_two + ' is ' + six_players_no_special [0])
    del six_players_no_special [0]
    player_three = input('Player Three: ')
    print (player_three + ' is ' + six_players_no_special [0])
    del six_players_no_special [0]
    player_four = input('Player Four: ')
    print (player_four + ' is ' + six_players_no_special [0])
    del six_players_no_special [0]
    player_five = input('Player Five: ')
    print (player_five + ' is ' + six_players_no_special [0])
    del six_players_no_special [0]
    player_six = input('Player Six: ')
    print (player_six + ' is ' + six_players_no_special [0])
    del six_players_no_special [0]
elif players == 6 and roles == 3:
    print('Not possible with this few players. Try less roles.')
elif players == 6 and roles == 2:
    random.shuffle(six_players_merlin_and_mordred)
    player_one = input('Player One: ')
    print (player_one + ' is ' + six_players_merlin_and_mordred [0])
    del six_players_merlin_and_mordred [0]
    player_two = input('Player Two: ')
    print (player_two + ' is ' + six_players_merlin_and_mordred [0])
    del six_players_merlin_and_mordred [0]
    player_three = input('Player Three: ')
    print (player_three + ' is ' + six_players_merlin_and_mordred [0])
    del six_players_merlin_and_mordred [0]
    player_four = input('Player Four: ')
    print (player_four + ' is ' + six_players_merlin_and_mordred [0])
    del six_players_merlin_and_mordred [0]
    player_five = input('Player Five: ')
    print (player_five + ' is ' + six_players_merlin_and_mordred [0])
    del six_players_merlin_and_mordred [0]
    player_six = input('Player Six: ')
    print (player_six + ' is ' + six_players_merlin_and_mordred [0])
    del six_players_merlin_and_mordred [0]
elif players == 6 and roles == 1:
    random.shuffle(six_players_merlin)
    player_one = input('Player One: ')
    print (player_one + ' is ' + six_players_merlin [0])
    del six_players_merlin [0]
    player_two = input('Player Two: ')
    print (player_two + ' is ' + six_players_merlin [0])
    del six_players_merlin [0]
    player_three = input('Player Three: ')
    print (player_three + ' is ' + six_players_merlin [0])
    del six_players_merlin [0]
    player_four = input('Player Four: ')
    print (player_four + ' is ' + six_players_merlin [0])
    del six_players_merlin [0]
    player_five = input('Player Five: ')
    print (player_five + ' is ' + six_players_merlin [0])
    del six_players_merlin [0]
    player_six = input('Player Six: ')
    print (player_six + ' is ' + six_players_merlin [0])
    del six_players_merlin [0]
elif players == 5 and roles == 4:
    random.shuffle(five_players_no_special)
    player_one = input('Player One: ')
    print (player_one + ' is ' + five_players_no_special [0])
    del five_players_no_special [0]
    player_two = input('Player Two: ')
    print (player_two + ' is ' + five_players_no_special [0])
    del five_players_no_special [0]
    player_three = input('Player Three: ')
    print (player_three + ' is ' + five_players_no_special [0])
    del five_players_no_special [0]
    player_four = input('Player Four: ')
    print (player_four + ' is ' + five_players_no_special [0])
    del five_players_no_special [0]
    player_five = input('Player Five: ')
    print (player_five + ' is ' + five_players_no_special [0])
    del five_players_no_special [0]
elif players == 5 and roles == 3:
    print('Not possible with this few players. Try less roles.')
elif players == 5 and roles == 2:
    random.shuffle(five_players_merlin_and_mordred)
    player_one = input('Player One: ')
    print (player_one + ' is ' + five_players_merlin_and_mordred [0])
    del five_players_merlin_and_mordred [0]
    player_two = input('Player Two: ')
    print (player_two + ' is ' + five_players_merlin_and_mordred [0])
    del five_players_merlin_and_mordred [0]
    player_three = input('Player Three: ')
    print (player_three + ' is ' + five_players_merlin_and_mordred [0])
    del five_players_merlin_and_mordred [0]
    player_four = input('Player Four: ')
    print (player_four + ' is ' + five_players_merlin_and_mordred [0])
    del five_players_merlin_and_mordred [0]
    player_five = input('Player Five: ')
    print (player_five + ' is ' + five_players_merlin_and_mordred [0])
    del five_players_merlin_and_mordred [0]
elif players == 5 and roles == 1:
    random.shuffle(five_players_merlin)
    player_one = input('Player One: ')
    print (player_one + ' is ' + five_players_merlin [0])
    del five_players_merlin [0]
    player_two = input('Player Two: ')
    print (player_two + ' is ' + five_players_merlin [0])
    del five_players_merlin [0]
    player_three = input('Player Three: ')
    print (player_three + ' is ' + five_players_merlin [0])
    del five_players_merlin [0]
    player_four = input('Player Four: ')
    print (player_four + ' is ' + five_players_merlin [0])
    del five_players_merlin [0]
    player_five = input('Player Five: ')
    print (player_five + ' is ' + five_players_merlin [0])
    del five_players_merlin [0]

