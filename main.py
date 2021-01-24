### @REMEMBER1NG ###
# All rights reserved - @Copyright 2020 #
# Begginer Project #

#USED MODULES
import time   #Interacts with Time
import os   #Interacts with the Operative System
import random   #Use Random module to sort items of an list and other things
import webbrowser
import sys   #Interacts with System functions

#CAR BRAND LIST
cars = ['Porsche', 'Volvo', 'KIA', 'Toyota', 'Hyundai', 'Honda', 'Suzuki', 'Nissan', 'Mitsubishi', 'Mercedes', 'Citroen',
        'Ford', 'Lamborghini', 'Bugatti', 'Ferrari', 'Mazda', 'Jaguar', 'BMW', 'Land Rover', 'Mini', 'Skoda', 'Tesla',
        'Audi', 'Peugeot', 'Seat', 'Maserati', 'Porsche', 'Alfa Romeo', 'Volks Wagen', 'Chevrolet', 'Lexus', 'Jeep',
        'Lotus', 'Subaru', 'Chery', 'Fiat', 'Bentley', 'Range Rover', 'Renault', 'Rolls Royce', 'Aston Martin', 'GMC']

#PERSON NAME
name = str(input('name: '))   #name input field
car = random.choice(cars)   #car random choice

#MAIN FUNCTION
def randomCar(carBrand):   #Parametre
    os.system('cls')   #clears the console
    print('Choosing...')
    time.sleep(2)   #it makes a break between the code lines
    print(f"{name}'s Future Car Is: \033[33m{carBrand}\033[m")
randomCar(car)   #code line that assigns a value to the function parametre (In this case carBrand is the Parametre)

#CAR IMAGES FUNCTION
def carImages(carBrand):
    loop = True   #the value of the loop variable
    while loop == True:   #loop that allows you to if the answer isn't the correct the program will move to the beggining
        img = str(input(f"Do You Want to See \033[33m{carBrand}'s\033[m Images?[y/n] "))
        if img == 'y':
            os.system('cls')
            print('Opening...')
            time.sleep(1.5)

            #module that allows you to open Webpages
            webbrowser.open(   #Google images search source code
                f'https://www.google.com/search?q={carBrand}'
                f'&tbm=isch&ved=2ahUKEwi8pqfeiK7uAhVR_4UKHWKeC74Q2-cCegQIABAA&oq={carBrand}'
                '&gs_lcp=CgNpbWcQA1AAWABgxxZoAHAAeACAAQCIAQCSAQCYAQCqAQtnd3Mtd2l6LWltZw&'
                'sclient=img&ei=TP8JYLzQEdH-lwTivK7wCw&bih=975&biw=1920&hl=en'
            )
            break   #code line that stops the loop
        elif img == 'n':
            sys.exit()   #code line that allows you to quit of the program
        elif img == '':
            print('\033[31mCHOOSE SOMETHING\033[m')
            continue  #code line that allows us to go to the beggining of the loop
        elif img != str:  #if input isn't a string value
            print('\033[31mCHOOSE A VALID OPTION\033[m')
            continue
        elif img == int:  #if input is an integer number
            print('\033[31mCHOOSE A STRING VALUE\033[m')
            continue
carImages(car)