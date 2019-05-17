
#  /!\ = a modifier en metant son curseur sur l'emplacement et marquant "pyautogui.position()" dans la console

import time
import pyscreenshot as ImageGrab
import cv2
import numpy as np
import pyautogui
import sys
from pynput.keyboard import Key, Controller
while 1:
    pyautogui.moveTo(360, 636, 1)  # selection du clip      /!\
    time.sleep(2)
    pyautogui.click()  # Clique pour sortir de L'IDLE
    time.sleep(1)
    pyautogui.click()   # Clique sur la selection des clips     /!\
    time.sleep(1)
    pyautogui.moveTo(630, 530, 1)   # Vas sur le clip 1
    time.sleep(2)
    pyautogui.click()  # Clique sur le clip
    time.sleep(2)
    pyautogui.click()   # active le clip tipee
    time.sleep(3)
    pyautogui.click()
    im = ImageGrab.grab(bbox=(578, 425, 971, 617))  #Prend capture d'écran
    im.save('original.jpg')
    time.sleep(2)
    im = ImageGrab.grab(bbox=(578, 425, 971, 617))  #capture d'écran
    im.save('duplicate.jpg')

    original = cv2.imread("original.jpg")           #Comparaison capture image
    duplicate = cv2.imread("duplicate.jpg")

    if original.shape == duplicate.shape:  #Comparaison capture image       
        difference = cv2.subtract(original, duplicate)
        b, g, r = cv2.split(difference)
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            print ("Image parei")
            time.sleep(2)
            pyautogui.click() #Clique sur le clip
            time.sleep(70)#Regarde le clip pendent 70s pour les chargements
            pyautogui.moveTo(1358, 209, 1)#Ferme la fenètre     /!\
            time.sleep(1)
            pyautogui.click()
            time.sleep(3)
            pyautogui.moveTo(1016, 316, 1) #Ferme la 2 fenètre      /!\
            time.sleep(1)
            pyautogui.click() #Clique pour fermer la fenetre
            time.sleep(5)
        else:
            print ("Image diff")
            time.sleep(70)  #Regarde le clip pendent 70s pour les chargements
            pyautogui.moveTo(1358, 209, 1)#Ferme la fenètre     /!\
            time.sleep(1)
            pyautogui.click()
            time.sleep(3)
            pyautogui.moveTo(1016, 316, 1) #Ferme la 2 fenètre      /!\
            time.sleep(1)
            pyautogui.click() #Clique pour fermer la fenetre
            time.sleep(5)

    pyautogui.moveTo(360, 636, 1)  #selection du clip       /!\
    time.sleep(1)
    pyautogui.click()   #Clique sur la selection des clips
    time.sleep(1)
    pyautogui.moveTo(914, 549, 1)   #Vas sur le clip 2      /!\
    time.sleep(2)
    pyautogui.click() #Clique sur le clip
    time.sleep(2)
    pyautogui.click()   #active le clip tipee
    time.sleep(3)
    im = ImageGrab.grab(bbox=(578, 425, 971, 617)) # Prend capture d'écran
    im.save('original.jpg')
    time.sleep(2)
    im = ImageGrab.grab(bbox=(578, 425, 971, 617)) # Prend une autre capture d'écran
    im.save('duplicate.jpg')
    original = cv2.imread("original.jpg")           #Comparaison capture image
    duplicate = cv2.imread("duplicate.jpg") 

    if original.shape == duplicate.shape:          #Comparaison capture image
        difference = cv2.subtract(original, duplicate)
        b, g, r = cv2.split(difference)
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            print ("Image parei")
            time.sleep(1)
            pyautogui.click() #Clique sur le clip
            time.sleep(70)  #Regarde le clip pendent 70s pour les chargements
            pyautogui.moveTo(1358, 209, 1)#Ferme la fenètre     /!\
            time.sleep(1)
            pyautogui.click()
            time.sleep(3)
            pyautogui.moveTo(1016, 316, 1) #Ferme la 2 fenètre      /!\
            time.sleep(1)
            pyautogui.click() #Clique pour fermer la fenetre
            time.sleep(5)
        else:
            print ("Image diff")
            time.sleep(70)  #Regarde le clip pendent 70s pour les chargements
            pyautogui.moveTo(1358, 209, 1)#Ferme la fenètre     /!\
            time.sleep(1)
            pyautogui.click()
            time.sleep(3)
            pyautogui.moveTo(1016, 316, 1) #Ferme la 2 fenètre      /!\
            time.sleep(1)
            pyautogui.click()  #Clique pour fermer la fenetre
            time.sleep(5)

    keyboard = Controller()   #Fait ctrl+tab
    keyboard.press(Key.ctrl)
    time.sleep(0.1)
    keyboard.press(Key.tab)
    time.sleep(0.5)
    keyboard.release(Key.tab)
    keyboard.release(Key.ctrl)
