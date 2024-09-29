import pyautogui
import time
from time import sleep
import keyboard
import colorama
from colorama import init, Fore, Back
init()



print(Fore.BLUE+'''
            ,--.-,    ,----.    ,-,--.               _,.---._           ___               
     |==' -| ,-.--` , \ ,-.'-  _\   _..---.  ,-.' , -  `.  .-._ .'=.'\    _..---.   
     |==|- ||==|-  _.-`/==/_ ,_.' .' .'.-. \/==/_,  ,  - \/==/ \|==|  | .' .'.-. \  
   __|==|, ||==|   `.-.\==\  \   /==/- '=' /==|   .=.     |==|,|  / - |/==/- '=' /  
,--.-'\=|- /==/_ ,    / \==\ -\  |==|-,   '|==|_ : ;=:  - |==|  \/  , ||==|-,   '   
|==|- |=/ ,|==|    .-'  _\==\ ,\ |==|  .=. \==| , '='     |==|- ,   _ ||==|  .=. \  
|==|. /=| -|==|_  ,`-._/==/\/ _ |/==/- '=' ,\==\ -    ,_ /|==| _ /\   |/==/- '=' ,| 
\==\, `-' //==/ ,     /\==\ - , /==|   -   / '.='. -   .' /==/  / / , /==|   -   /  
 `--`----' `--`-----``  `--`---'`-._`.___,'    `--`--''   `--`./  `--``-._`.___,'  
                                                                                       1.3.5                  
                                                                      made by: jescoin

''')

print(Fore.RED+'Choose:')
a1 = int(input('How many lines will in bomber?'))
amount = 1
print(Fore.GREEN+'')
for i in range(a1):
    f = open("h1.txt", "a")
    f.write("jescoin\n")
    print(amount, 'line was added')
    amount+=1
    f.close()



print(Fore.RED+'Warn!\nYou should place your cursor on the text input in Telegram, Whatsapp, etc.')
answer = input(Fore.GREEN+'Start?y/n')
amountoftext = 1

def spam():
    print(Fore.RED+'Type Q for finish spam program')
    time.sleep(7);
    f = open('h1.txt', 'r')
    for line in f:
        pyautogui.typewrite(line)
        pyautogui.press('enter')
        if keyboard.is_pressed("q"):
            exit()


if answer=='y':
    spam()
else:
    print('Program will exit during 5 sec..')
    print('1')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('4')
    time.sleep(1)
    print('5')
    time.sleep(1)
    exit()

