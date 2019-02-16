import keyboard
import os
import sys
from colorama import Fore, Back, Style, init
init()
clear = lambda: os.system('cls')
cwd = os.getcwd()
header = """
   ____      _          ____      _       _       _                ___   _
  / ___|___ (_)_ __    / ___|__ _| |_   _| | __ _| |_ ___  _ __   / _ \\ / |
 | |   / _ \\| | '_ \\  | |   / _` | | | | | |/ _` | __/ _ \\| '__| | | | || |
 | |__| (_) | | | | | | |__| (_| | | |_| | | (_| | || (_) | |    | |_| || |
  \\____\\___/|_|_| |_|  \\____\\__,_|_|\\__,_|_|\\__,_|\\__\\___/|_|     \\___(_)_|
                                                   Omar "Michael Abdo" 2019
                                                                'Q' to Quit
"""


def end():
    print(Style.BRIGHT + Fore.RED + "\n\n\t\tCLOSING.")
    os._exit(0)

def commit(cs, vs, opened="CoinCount"):
    inp = ""
    total = "\n\nTOTAL ${0:.2f}".format(sum(map(lambda x, y: x*y, cs, vs)))
    while inp.upper() != "N" and inp.upper() != "Y":
        inp = input("{} Save? [Y/N]: ".format(total))
    if inp.upper() == "Y":
        temp = input("Enter filename or press enter to use default ({}).txt:  ".format(opened))
        if temp: opened = temp
        if not opened.endswith(".txt"): opened += ".txt"
        conf = ""
        while conf.upper() not in ['Y', 'N']:
            conf = input("Saving file as {}\\{} - Confirm? [Y/N]: ".format(cwd, opened))
        if conf.upper() == "Y":
            with open(opened, "w+") as f:
                f.write(",".join(map(lambda x: str(x), cs)))
                f.write(total)
            clear()
            print("Total saved to {}\\{}!\n\n\n\n".format(cwd, opened))
    end()

def changeVal(dir, cursor_pos, cs, vs):
    ch = (len(cs) - 1) - cursor_pos[0]
    if dir == "D":
        if cs[ch] >= 1:
            cs[ch] -= 1
            moveCursor('n', cursor_pos, cs, vs)
    elif dir == "U":
            cs[ch] += 1
            moveCursor('n', cursor_pos, cs, vs)

def moveCursor(dir, cursor_pos, cs, vs):
    total = "TOTAL ${0:.2f}".format(sum(map(lambda x, y: x*y, cs, vs)))
    neutral = """



        0.05    0.10    0.25    1.00    2.00    5.00    10.00   20.00   50.00   100.00

         {}       {}       {}       {}       {}       {}        {}       {}       {}        {}

                """.format(cs[9], cs[8], cs[7], cs[6], cs[5], cs[4], cs[3], cs[2], cs[1], cs[0])
    if dir != 'n':
        if cursor_pos[0] != 0 and dir == 'L':
            cursor_pos[0] -= 1
        elif cursor_pos[0] != 9 and dir == 'R':
            cursor_pos[0] += 1
        elif cursor_pos[0] == 0 and dir == 'L':
            cursor_pos[0] = 9
        elif cursor_pos[0] == 9 and dir == 'R':
            cursor_pos[0] = 0
    clear()
    print(total)
    if cursor_pos[0] == 0:
        print(neutral[:12] + Style.BRIGHT + Fore.GREEN + neutral[12:16] + Style.RESET_ALL + neutral[16:]) #Nickel
    elif cursor_pos[0] == 1:
        print(neutral[:20] + Style.BRIGHT + Fore.GREEN + neutral[20:24] + Style.RESET_ALL  + neutral[24:]) #Dime
    elif cursor_pos[0] == 2:
        print(neutral[:28] + Style.BRIGHT + Fore.GREEN + neutral[28:32] + Style.RESET_ALL  + neutral[32:]) #Quarter
    elif cursor_pos[0] == 3:
        print(neutral[:36] + Style.BRIGHT + Fore.GREEN + neutral[36:40] + Style.RESET_ALL  + neutral[40:]) #loon
    elif cursor_pos[0] == 4:
        print(neutral[:44] + Style.BRIGHT + Fore.GREEN + neutral[44:48] + Style.RESET_ALL  + neutral[48:]) #toon
    elif cursor_pos[0] == 5:
        print(neutral[:52] + Style.BRIGHT + Fore.GREEN + neutral[52:56] + Style.RESET_ALL  + neutral[56:]) #fiver
    elif cursor_pos[0] == 6:
        print(neutral[:60] + Style.BRIGHT + Fore.GREEN + neutral[60:65] + Style.RESET_ALL  + neutral[65:]) #tens
    elif cursor_pos[0] == 7:
        print(neutral[:68] + Style.BRIGHT + Fore.GREEN + neutral[68:73] + Style.RESET_ALL  + neutral[73:]) #twenties
    elif cursor_pos[0] == 8:
        print(neutral[:76] + Style.BRIGHT + Fore.GREEN + neutral[76:81] + Style.RESET_ALL  + neutral[81:]) #fifties
    elif cursor_pos[0] == 9:
        print(neutral[:84] + Style.BRIGHT + Fore.GREEN + neutral[84:91] + Style.RESET_ALL  + neutral[91:]) #hundreds
    print("CONTROLS:\n-> / <-\t:\tMOVE\nZ\t:\tINCREMENT\nX\t:\tDECREMENT\nENTER\t:\tSAVE\nQ\t:\tQUIT")
def main():
    print(Fore.GREEN + Style.BRIGHT + header)
    keyboard.add_hotkey('q', end)
    mode = ""
    cursor_pos = [0]
    cs = [0,0,0,0,0,0,0,0,0,0] #100, 50, 20, 10, 5, 2, 1, 0.25, 0.10, 0.05
    vs = [100, 50, 20, 10, 5, 2, 1, 0.25, 0.10, 0.05]
    while mode != "C" and mode != "S":
        mode = input("Enter mode for entry: C for Counting, S for Static: ")
        if mode.upper() == "S":
            hund = ""
            while not hund.isdigit():
                hund = input("Enter # of $100:\t")

            fift = ""
            while not fift.isdigit():
                fift = input("Enter # of $50:\t\t")

            twen = ""
            while not twen.isdigit():
                twen = input("Enter # of $20:\t\t")

            tens = ""
            while not tens.isdigit():
                tens = input("Enter # of $10:\t\t")

            five = ""
            while not five.isdigit():
                five = input("Enter # of $5:\t\t")

            toon = ""
            while not toon.isdigit():
                toon = input("Enter # of $2:\t\t")

            loon = ""
            while not loon.isdigit():
                loon = input("Enter # of $1:\t\t")

            quar = ""
            while not quar.isdigit():
                quar = input("Enter # of $0.25:\t")

            dime = ""
            while not dime.isdigit():
                dime = input("Enter # of $.10:\t")

            nick = ""
            while not nick.isdigit():
                nick = input("Enter # of $0.05:\t")

            save = ""
            while save.upper() != "Y" and save.upper() != "N":
                save = input("Total is ${}. Save amount?\n\n\t\t[Y/N]:\t".format(int(nick)*0.05 + int(dime)*0.10 + int(quar)*0.25 + int(loon)*1 + int(toon)*2 + int(five)*5 + int(tens)*10 + int(twen)*20 + int(fift)*50 + int(hund)*100))
            if save.upper() == "Y":
                conf = ""
                while conf.upper() not in ['Y', 'N']:
                    if os.path.exists("CoinCount.txt"):
                        inp = input("File exists. Enter a new name or press enter to overwrite default file CoinCount.txt: ")
                    else:
                        inp = input("Enter filename or press enter to use default (CoinCount.txt):  ")
                    if not inp: inp = "CoinCount"
                    if not inp.endswith(".txt"): inp += ".txt"
                    conf = input("Saving file as {}\\{}- Confirm? [Y/N]: ".format(cwd, inp))
                    if conf.upper() == "N":
                        conf = ""
                        continue
                    if conf.upper() == "Y":
                        with open(inp, "w+") as f:
                            f.write(",".join(list(map(lambda x: str(x),[hund, fift, twen, tens, five, toon, loon, quar, dime, nick]))))
                            f.write("\n{}".format(int(nick)*0.05 + int(dime)*0.10 + int(quar)*0.25 + int(loon)*1 + int(toon)*2 + int(five)*5 + int(tens)*10 + int(twen)*20 + int(fift)*50 + int(hund)*100))
                    clear()
                print("Total saved to {}\\{}!\n\n\n\n".format(cwd, inp))
            end()
        elif mode.upper() == "C":
            inp = ""
            mode = ""
            while mode.upper() != "N" and mode.upper() != "O":
                mode = input("Count from New or Open previous total? [N/O]: ")
            if mode.upper() == "O":
                if os.path.exists("CoinCount.txt"):
                    inp = input("File(s) exist. Enter a new name or press enter to use the default CoinCount.txt: ")
                else:
                    inp = input("Enter filename:  ")
                if not inp: inp = "CoinCount"
                if not inp.endswith(".txt"): inp += ".txt"
                conf = ""
                while conf.upper() not in ['Y', 'N']:
                    conf = input("Open from {}\\{} - Confirm? [Y/N]: ".format(cwd, inp))
                if conf.upper() == "Y":
                    try:
                        with open(inp) as f:
                            cs = list(map(lambda x: int(x), f.readline()[:-1].split(",")))
                            print("Successfully loaded data from {}\\{}".format(cwd, inp))
                    except:
                        print("BAD!")
            moveCursor('n', cursor_pos, cs, vs)
            keyboard.add_hotkey('left', moveCursor, args=('L', cursor_pos, cs, vs))
            keyboard.add_hotkey('right', moveCursor, args=('R', cursor_pos, cs, vs))
            keyboard.add_hotkey('z', changeVal, args=('U', cursor_pos, cs, vs))
            keyboard.add_hotkey('x', changeVal, args=('D', cursor_pos, cs, vs))
            keyboard.add_hotkey('enter', commit, args=(cs, vs, inp))
            while True:
                pass
main()
