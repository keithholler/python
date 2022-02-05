import pandas
import random
import string
from art import text2art
import string
import sys
from termcolor import colored, cprint
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# Destroyer
destroyerColumn = random.randint(0, 25)
destroyerRow = random.randint(1, 26)
while destroyerColumn > 24 and destroyerRow > 24:
    destroyerRow = random.randint(0, 25)
    destroyerColumn = random.randint(0, 25)
if random.randint(0, 1) == 0:
    if not destroyerColumn > 24:
        destroyerRow2 = destroyerRow
        destroyerCol2 = string.ascii_lowercase[destroyerColumn + 1]
    else:
        destroyerRow2 = destroyerRow+1
        destroyerCol2 = string.ascii_lowercase[destroyerColumn]
else:
    if not destroyerRow > 24:
        destroyerRow2 = destroyerRow+1
        destroyerCol2 = string.ascii_lowercase[destroyerColumn]
    else:
        destroyerRow2 = destroyerRow
        destroyerCol2 = string.ascii_lowercase[destroyerColumn + 1]
destroyer = [[destroyerRow, string.ascii_lowercase[destroyerColumn]], [
    destroyerRow2, destroyerCol2]]


# Submarine
submarineColumn = random.randint(0, 25)
submarineRow = random.randint(1, 26)
while submarineColumn > 23 and submarineRow > 23:
    submarineRow = random.randint(0, 25)
    submarineColumn = random.randint(0, 25)
if random.randint(0, 1) == 0:
    if not submarineColumn > 23:
        submarineRow2 = submarineRow
        submarineRow3 = submarineRow
        submarineCol2 = string.ascii_lowercase[submarineColumn + 1]
        submarineCol3 = string.ascii_lowercase[submarineColumn + 2]
    else:
        submarineRow2 = submarineRow+1
        submarineRow3 = submarineRow+2
        submarineCol2 = string.ascii_lowercase[submarineColumn]
        submarineCol3 = string.ascii_lowercase[submarineColumn]
else:

    if not submarineRow > 23:
        submarineRow2 = submarineRow+1
        submarineRow3 = submarineRow+2
        submarineCol2 = string.ascii_lowercase[submarineColumn]
        submarineCol3 = string.ascii_lowercase[submarineColumn]
    else:
        submarineRow2 = submarineRow
        submarineRow3 = submarineRow
        submarineCol2 = string.ascii_lowercase[submarineColumn + 1]
        submarineCol3 = string.ascii_lowercase[submarineColumn + 2]

submarine = [[submarineRow, string.ascii_lowercase[submarineColumn]], [
    submarineRow2, submarineCol2], [submarineRow3, submarineCol3]]


# Cruiser
cruiserColumn = random.randint(0, 25)
cruiserRow = random.randint(1, 26)
while cruiserColumn > 23 and cruiserRow > 23:
    cruiserRow = random.randint(0, 25)
    cruiserColumn = random.randint(0, 25)
if random.randint(0, 1) == 0:
    if not cruiserColumn > 23:
        cruiserRow2 = cruiserRow
        cruiserRow3 = cruiserRow
        cruiserCol2 = string.ascii_lowercase[cruiserColumn + 1]
        cruiserCol3 = string.ascii_lowercase[cruiserColumn + 2]
    else:
        cruiserRow2 = cruiserRow+1
        cruiserRow3 = cruiserRow+2
        cruiserCol2 = string.ascii_lowercase[cruiserColumn]
        cruiserCol3 = string.ascii_lowercase[cruiserColumn]
else:
    if not cruiserRow > 23:
        cruiserRow2 = cruiserRow+1
        cruiserRow3 = cruiserRow+2
        cruiserCol2 = string.ascii_lowercase[cruiserColumn]
        cruiserCol3 = string.ascii_lowercase[cruiserColumn]
    else:
        cruiserRow2 = cruiserRow
        cruiserRow3 = cruiserRow
        cruiserCol2 = string.ascii_lowercase[cruiserColumn + 1]
        cruiserCol3 = string.ascii_lowercase[cruiserColumn + 2]

cruiser = [[cruiserRow, string.ascii_lowercase[cruiserColumn]],
           [cruiserRow2, cruiserCol2], [cruiserRow3, cruiserCol3]]


# Battleship
battleshipColumn = random.randint(0, 25)
battleshipRow = random.randint(1, 26)
while battleshipColumn > 22 and battleshipRow > 22:
    battleshipRow = random.randint(0, 25)
    battleshipColumn = random.randint(0, 25)
if random.randint(0, 1) == 0:
    if not battleshipColumn > 22:
        battleshipRow2 = battleshipRow
        battleshipRow3 = battleshipRow
        battleshipRow4 = battleshipRow
        battleshipCol2 = string.ascii_lowercase[battleshipColumn + 1]
        battleshipCol3 = string.ascii_lowercase[battleshipColumn + 2]
        battleshipCol4 = string.ascii_lowercase[battleshipColumn + 3]
    else:
        battleshipRow2 = battleshipRow+1
        battleshipRow3 = battleshipRow+2
        battleshipRow4 = battleshipRow+3
        battleshipCol2 = string.ascii_lowercase[battleshipColumn]
        battleshipCol3 = string.ascii_lowercase[battleshipColumn]
        battleshipCol4 = string.ascii_lowercase[battleshipColumn]
else:
    if not battleshipRow > 22:
        battleshipRow2 = battleshipRow+1
        battleshipRow3 = battleshipRow+2
        battleshipRow4 = battleshipRow+3
        battleshipCol2 = string.ascii_lowercase[battleshipColumn]
        battleshipCol3 = string.ascii_lowercase[battleshipColumn]
        battleshipCol4 = string.ascii_lowercase[battleshipColumn]
    else:
        battleshipRow2 = battleshipRow
        battleshipRow3 = battleshipRow
        battleshipRow4 = battleshipRow
        battleshipCol2 = string.ascii_lowercase[battleshipColumn + 1]
        battleshipCol3 = string.ascii_lowercase[battleshipColumn + 2]
        battleshipCol4 = string.ascii_lowercase[battleshipColumn + 3]

battleship = [[battleshipRow, string.ascii_lowercase[battleshipColumn]],
              [battleshipRow2, battleshipCol2], [
                  battleshipRow3, battleshipCol3],
              [battleshipRow4, battleshipCol4]]

# Carrier
carrierColumn = random.randint(0, 25)
carrierRow = random.randint(1, 26)
while carrierColumn > 21 and carrierRow > 21:
    carrierRow = random.randint(0, 25)
    carrierColumn = random.randint(0, 25)

if random.randint(0, 1) == 0:
    if not carrierColumn > 21:
        carrierRow2 = carrierRow
        carrierRow3 = carrierRow
        carrierRow4 = carrierRow
        carrierRow5 = carrierRow
        carrierCol2 = string.ascii_lowercase[carrierColumn + 1]
        carrierCol3 = string.ascii_lowercase[carrierColumn + 2]
        carrierCol4 = string.ascii_lowercase[carrierColumn + 3]
        carrierCol5 = string.ascii_lowercase[carrierColumn + 4]

    else:
        carrierRow2 = carrierRow+1
        carrierRow3 = carrierRow+2
        carrierRow4 = carrierRow+3
        carrierRow5 = carrierRow+4
        carrierCol2 = string.ascii_lowercase[carrierColumn]
        carrierCol3 = string.ascii_lowercase[carrierColumn]
        carrierCol4 = string.ascii_lowercase[carrierColumn]
        carrierCol5 = string.ascii_lowercase[carrierColumn]

else:
    if not carrierRow > 21:
        carrierRow2 = carrierRow+1
        carrierRow3 = carrierRow+2
        carrierRow4 = carrierRow+3
        carrierRow5 = carrierRow+4
        carrierCol2 = string.ascii_lowercase[carrierColumn]
        carrierCol3 = string.ascii_lowercase[carrierColumn]
        carrierCol4 = string.ascii_lowercase[carrierColumn]
        carrierCol5 = string.ascii_lowercase[carrierColumn]

    else:
        carrierRow2 = carrierRow
        carrierRow3 = carrierRow
        carrierRow4 = carrierRow
        carrierRow5 = carrierRow
        carrierCol2 = string.ascii_lowercase[carrierColumn + 1]
        carrierCol3 = string.ascii_lowercase[carrierColumn + 2]
        carrierCol4 = string.ascii_lowercase[carrierColumn + 3]
        carrierCol5 = string.ascii_lowercase[carrierColumn + 4]

carrier = [[carrierRow, string.ascii_lowercase[carrierColumn]],
           [carrierRow2, carrierCol2], [carrierRow3, carrierCol3],
           [carrierRow4, carrierCol4], [carrierRow5, carrierCol5]]

'''Cheat Locations'''
print(f'destroyer {destroyer}')
print(f'submarine {submarine}')
print(f'cruiser {cruiser}')
print(f'battleship {battleship}')
print(f'carrier {carrier}')
ships = [destroyer, submarine, cruiser, battleship, carrier]


'''Battlefield'''
df = pandas.DataFrame
area = []
col = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
       'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i in range(0, 26, 1):
    area.append(['X']*26)
battle = df(area, columns=col)
battle.index += 1

'''Start of Game'''
shipsSunk = []
TURNS = 50
Welcome = text2art("WELCOME   TO   BATTLESHIP !!!")
Win = text2art("YOU   WIN !!!")
Lose = text2art("YOU   LOSE !!!")
cprint(Welcome, 'yellow')
print(f'You have {TURNS} turns to sink the fleet!')
while True:
    if TURNS == 50:
        input("Press Enter to start...")
        print(battle)
    # print(ships)
    print(f'You have {TURNS} turns left')
    TURNS -= 1
    print(f'Sunken Ships: {shipsSunk}')
    while True:
        try:
            rowInput = int(input("Choose a row number: "))

        except ValueError:
            print('Please enter an integer between 1 and 25')
        else:
            if rowInput < 1 or rowInput > 26:
                print('Out of Range')
                continue
            else:
                break
    while True:

        colInput = input("Choose a column letter: ")
        if colInput.isalpha() and len(colInput) == 1:
            break
        else:
            print('Please enter a letter')
            continue

    '''If location from user matches ships location'''
    if rowInput == destroyer[0][0] and colInput == destroyer[0][1] or rowInput == destroyer[1][0] and colInput == destroyer[1][1]:
        battle.at[int(rowInput), colInput.upper()] = 'DE'
        print(battle)
        cprint('You hit the Destroyer!!!', 'green')
    elif rowInput == submarine[0][0] and colInput == submarine[0][1] or rowInput == submarine[1][0] and colInput == submarine[1][1] or rowInput == submarine[2][0] and colInput == submarine[2][1]:
        battle.at[int(rowInput), colInput.upper()] = 'SU'
        print(battle)
        cprint('You hit the Submarine!!!', 'green')
    elif rowInput == cruiser[0][0] and colInput == cruiser[0][1] or rowInput == cruiser[1][0] and colInput == cruiser[1][1] or rowInput == cruiser[2][0] and colInput == cruiser[2][1]:
        battle.at[int(rowInput), colInput.upper()] = 'CR'
        print(battle)
        cprint('You hit the Cruiser!!!', 'green')
    elif rowInput == battleship[0][0] and colInput == battleship[0][1] or rowInput == battleship[1][0] and colInput == battleship[1][1] or rowInput == battleship[2][0] and colInput == battleship[2][1] or rowInput == battleship[3][0] and colInput == battleship[3][1]:
        battle.at[int(rowInput), colInput.upper()] = 'BA'
        print(battle)
        cprint('You hit the Battleship!!!', 'green')
    elif rowInput == carrier[0][0] and colInput == carrier[0][1] or rowInput == carrier[1][0] and colInput == carrier[1][1] or rowInput == carrier[2][
            0] and colInput == carrier[2][1] or rowInput == carrier[3][0] and colInput == carrier[3][1] or rowInput == carrier[4][0] and colInput == carrier[4][1]:
        battle.at[int(rowInput), colInput.upper()] = 'CA'
        print(battle)
        cprint('You hit the Carrier!!!', 'green')
    else:
        battle.at[rowInput, colInput.upper()] = ' '
        print(battle)
        cprint("You Missed!!!", 'red')

    '''IF all ship locations are hit show it has sunk'''
    if battle.at[destroyer[0][0], str(destroyer[0][1]).upper()] == 'DE' and battle.at[destroyer[1][0], str(destroyer[1][1]).upper()] == 'DE':
        if 'Destroyer' not in shipsSunk:
            print("You Sunk the Destroyer!")
            shipsSunk.append('Destroyer')

    if battle.at[submarine[0][0], str(submarine[0][1]).upper()] == 'SU' and battle.at[submarine[1][0], str(submarine[1][1]).upper()] == 'SU' and battle.at[submarine[2][0], str(submarine[2][1]).upper()] == 'SU':
        if 'Submarine' not in shipsSunk:
            print("You Sunk the Submarine!")
            shipsSunk.append('Submarine')

    if battle.at[cruiser[0][0], str(cruiser[0][1]).upper()] == 'CR' and battle.at[cruiser[1][0], str(cruiser[1][1]).upper()] == 'CR' and battle.at[cruiser[2][0], str(cruiser[2][1]).upper()] == 'CR':
        if 'Cruiser' not in shipsSunk:
            print("You Sunk the Cruiser!")
            shipsSunk.append('Cruiser')

    if battle.at[battleship[0][0], str(battleship[0][1]).upper()] == 'BA' and battle.at[battleship[1][0], str(battleship[1][1]).upper()] == 'BA' and battle.at[battleship[2][0], str(battleship[2][1]).upper()] == 'BA' and battle.at[battleship[3][0], str(battleship[3][1]).upper()] == 'BA':
        if 'Battleship' not in shipsSunk:
            print("You Sunk the Battleship!")
            shipsSunk.append('Battleship')

    if battle.at[carrier[0][0], str(carrier[0][1]).upper()] == 'CA' and battle.at[carrier[1][0], str(carrier[1][1]).upper()] == 'CA' and battle.at[carrier[2][0], str(carrier[2][1]).upper()] == 'CA' and battle.at[carrier[3][0], str(carrier[3][1]).upper()] == 'CA' and battle.at[carrier[4][0], str(carrier[4][1]).upper()] == 'CA':
        if 'Carrier' not in shipsSunk:
            print("You Sunk the Carrier!")
            shipsSunk.append('Carrier')

    '''Win and lose logic'''
    if len(shipsSunk) == 5:
        cprint(Win, 'green')
        break
    elif TURNS == 0:
        cprint(Lose, 'red')
        break
