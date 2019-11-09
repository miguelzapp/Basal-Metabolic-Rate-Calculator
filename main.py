import math
import time

########################
# CODE BY PYJAVAPULVER #
#    COPYRIGHT  2019   #
########################

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CYAN = '\033[0;36m'

def initial():
    print(colors.CYAN + ' ')

    print('           _____                    _____                    _____           ')
    time.sleep(0.1)
    print('          /\    \                  /\    \                  /\    \          ')
    time.sleep(0.1)
    print('         /::\    \                /::\____\                /::\    \         ')
    time.sleep(0.1)
    print('        /::::\    \              /::::|   |               /::::\    \        ')
    time.sleep(0.1)
    print('       /::::::\    \            /:::::|   |              /::::::\    \       ')
    time.sleep(0.1)
    print('      /:::/\:::\    \          /::::::|   |             /:::/\:::\    \      ')
    time.sleep(0.1)
    print('     /:::/__\:::\    \        /:::/|::|   |            /:::/__\:::\    \     ')
    time.sleep(0.1)
    print('    /::::\   \:::\    \      /:::/ |::|   |           /::::\   \:::\    \    ')
    time.sleep(0.1)
    print('   /::::::\   \:::\    \    /:::/  |::|___|______    /::::::\   \:::\    \   ')
    time.sleep(0.1)
    print('  /:::/\:::\   \:::\ ___\  /:::/   |::::::::\    \  /:::/\:::\   \:::\____\  ')
    time.sleep(0.1)
    print(' /:::/__\:::\   \:::|    |/:::/    |:::::::::\____\/:::/  \:::\   \:::|    | ')
    time.sleep(0.1)
    print(' \:::\   \:::\  /:::|____|\::/    / ~~~~~/:::/    /\::/   |::::\  /:::|____| ')
    time.sleep(0.1)
    print('  \:::\   \:::\/:::/    /  \/____/      /:::/    /  \/____|:::::\/:::/    /  ')
    time.sleep(0.1)
    print('   \:::\   \::::::/    /               /:::/    /         |:::::::::/    /   ')
    time.sleep(0.1)
    print('    \:::\   \::::/    /               /:::/    /          |::|\::::/    /    ')
    time.sleep(0.1)
    print('     \:::\  /:::/    /               /:::/    /           |::| \::/____/     ')
    time.sleep(0.1)
    print('      \:::\/:::/    /               /:::/    /            |::|  ~|           ')
    time.sleep(0.1)
    print('       \::::::/    /               /:::/    /             |::|   |           ')
    time.sleep(0.1)
    print('        \::::/    /               /:::/    /              \::|   |           ')
    time.sleep(0.1)
    print('         \::/____/                \::/    /                \:|   |           ')
    time.sleep(0.1)
    print('          ~~                       \/____/                  \|___|           ')

    time.sleep(0.2)

    print('                        _               _         _                          ')
    print('            ___   __ _ | |  ___  _   _ | |  __ _ | |_   ___   _ __           ')
    print("           / __| / _` || | / __|| | | || | / _` || __| / _ \ | '__|          ")
    print('          | (__ | (_| || || (__ | |_| || || (_| || |_ | (_) || |             ')
    print('           \___| \__,_||_| \___| \__,_||_| \__,_| \__| \___/ |_|             ')
                                                                       


                                                                           


    print(' ' + colors.ENDC)
    time.sleep(1)


def start():
    home_input = input(colors.WARNING + 'Press "S" to start calculator, "E" to exit the program or "I" to show info. Then press enter. ' + colors.ENDC)
    if home_input in ['S','s']:
        input1 = input(colors.CYAN + "Are you a Man (M) or a Woman (W) ? " + colors.ENDC)
        if input1 in ['M','m']:
            input2 = int(input(colors.CYAN + "What is your mass (kg) ? " + colors.ENDC))
            input3 = int(input(colors.CYAN + "How tall are you (cm) ? " + colors.ENDC))
            input4 = int(input(colors.CYAN + "How old are you ? " + colors.ENDC))

            #print("you're a man")
            cal = 66.5 + ( 13.7 * input2 ) + ( 5 * input3 ) - ( 6.7 * input4 )
            print(colors.OKGREEN + "Your Basal Metabolic Rate (BMR) is " + str(cal) + " kcal" + colors.ENDC)
            time.sleep(2)
            start()
        elif input1 in ['W', 'w']:
            input2 = int(input(colors.CYAN + "What is your mass (kg) ? " + colors.ENDC))
            input3 = int(input(colors.CYAN + "How tall are you (cm) ? " + colors.ENDC))
            input4 = int(input(colors.CYAN + "How old are you ? " + colors.ENDC))

            #print("you're a woman")
            cal = 55 + ( 9.5 * input2 ) + ( 4.8 * input3 ) - ( 4.7 * input4 )
            print(colors.OKGREEN + "Your Basal Metabolic Rate (BMR) is " + str(cal) + " kcal" + colors.ENDC)
            time.sleep(2)
            start()
    elif home_input in ['E','e']:
        print(colors.FAIL + 'Leaving program' + colors.ENDC)
        exit()
    elif home_input in ['I','i']:
        print(colors.OKGREEN + 'This is a basic BMS (Basal Metabolic Rate Calculator) terminal script calculator\nwritten in Python! The Basal Metabolic Rate is the number of calories\nrequired to keep your body functioning at rest.' + colors.ENDC)
        time.sleep(3)
        start()
    else:
        print(colors.FAIL + 'Error, type a valid input' + colors.ENDC)
        start()

initial()
start()




