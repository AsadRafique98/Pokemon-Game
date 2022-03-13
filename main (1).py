import numpy as np
import random
from time import sleep
import os
import sys
from attacks import Attack
from player import Player
from os import system as OSsys, name as OSname
#**********************************MAIN MENU***************************
def my_print_routine(*args, **kwargs):
    print('\t\t', *args, **kwargs)
def clearScreen():
    if OSname == 'nt': OSsys('cls')
    else: OSsys('clear')
    my_print_routine()
    my_print_routine()
#comment

def main_menu():
    my_print_routine(); sleep(0.5)
    my_print_routine("(N)ew Game"); sleep(0.5)
    my_print_routine("(E)xit"); sleep(0.5)
    
    my_print_routine()
    my_print_routine('What would you like to do?', end=' ')
    response = input()
    
    if response in ['e', 'E']:
        my_print_routine()
        my_print_routine("Exiting the game...."); sleep(0.8)
        sys.exit(0)
    
    if response in ['n', 'N']:
        my_print_routine("Starting New Game...")
        sleep(0.3)
        my_print_routine();   my_print_routine("Tap Enter to Go On", end=' ');     input()
    return None



class Grid_squares:
    def __init__(self,tile_number,terrain=None):
        self.pos = tile_number
        self.terrain = terrain if terrain is not None else 0
        
    def set_Terrain(self,objec):
        self.terrain = objec


class Grid:
    def __init__(self,r,c):
        self.rows = r
        self.cols = c
        self.indx = np.zeros(shape=(r,c))
        self.grid_obj = []
        self.myposr = 0
        self.myposc = 0
        
        for i in range(r):
            self.grid_obj.append([])
            for j in range(c):
                self.grid_obj[i].append(Grid_squares(j))
        count =0
        for i in range(self.rows):
            for j in range(self.cols):
                self.grid_obj[i][j].pos=count
                self.grid_obj[i][j].terrain=random.randint(0,4) if not i==0 or not j==0 else 5
                count+=1
    def __repr__(self):
        a ='**************((YOUR MAP))*************\n'
        for i in range(self.rows):
            a+='\n|'
            for j in range(self.cols):
                a+="|  "+ str(self.grid_obj[i][j].terrain) +"  |" if not self.grid_obj[i][j].terrain==5 else "|"+'*(5)*|'
            a+='|\n'
        return a
#************pokemon data*******************
#attacks
thundershock = Attack('Thundershock', 'Electric', 40, 0, 30, 0, 0, 1)
tackle = Attack('Tackle', 'Normal', 40, 0, 25, 0, 0, 1)
quickattack = Attack('Quick Attack', 'Normal', 45, 0, 20, 0, 0, 0.95)
catastropika = Attack('Catastropika', 'Electric', 285, 0, 1, 0, 0,0, 1)
#original pokis data
small_pokemons = ['Pikachu', 'Charmander']
pokemonWorld = {
        'Pikachu':      {'type': 'electric',    'evolveAt': None,   'evolveTo': 'raichu',       'baseDef': 10,  'baseSpeed': 30, 'startAttacks': [(thundershock), (tackle), None, None],'learnableAttacks': [(quickattack),(catastropika)][::-1]},
        'Charmander':   {'type': 'fire',        'evolveAt': 18,     'evolveTo': 'charmeleon',   'baseDef': 15,  'baseSpeed': 20, 'startAttacks': [(thundershock), (tackle), None, None],'learnableAttacks': [(quickattack),(catastropika)][::-1]},
        'Himmachu':      {'type': 'electric',    'evolveAt': None,   'evolveTo': 'raichu',       'baseDef': 10,  'baseSpeed': 30, 'startAttacks': [(thundershock), (tackle), None, None],'learnableAttacks': [(quickattack),(catastropika)][::-1]},           
        'Goki':   {'type': 'fire',        'evolveAt': 18,     'evolveTo': 'charmeleon',   'baseDef': 15,  'baseSpeed': 20, 'startAttacks': [(thundershock), (tackle), None, None],'learnableAttacks': [(quickattack),(catastropika)][::-1]}
}

def gameloop():
    player = main_menu()
    clearScreen()
    gameOver = False
    
    if player is None:
        my_print_routine("***POKEMON WORLDDD!!!!!...\n"); sleep(0.5)
        my_print_routine("Your Goal is to catch all pokemons in the grid and \n\t\t  become the greatest pokemon collector of.\n"); sleep(0.2)
        my_print_routine("Start you journey and \"Catch them All\""); sleep(0.5)
        
        my_print_routine()
        my_print_routine("Tap Enter to Go On"); input()
        clearScreen()
        
        my_print_routine("What's your Name?", end=" ")
        name = input()
        player = Player(name)
        sleep(0.2)
        my_print_routine()
        my_print_routine("We would like you to choose a pokemon before starting your Journey\n"); sleep(0.5)
        my_print_routine("press C for Charmander"); sleep(0.5)
        my_print_routine("press H for Himmachu"); sleep(0.5)
        my_print_routine("press G for Goki"); sleep(0.5)
        
        my_print_routine()
        my_print_routine("Choose any one. By default, you get a Pikachu. Press enter for Pikachu : ", end='')
        pokem = input()
        sleep(0.4)
        if pokem in ['c', 'C']:    firstpoke = 'Charmander'
        elif pokem in ['h', 'H']:    firstpoke = 'Himmachu'
        elif pokem in ['g', 'G']:    firstpoke = 'Goki'
        else:   firstpoke = 'Pikachu' #default
        
        pokedata = pokemonWorld[firstpoke]
        
        
        my_print_routine("Let's Start our BAttle VS GAry!!!!!..."); sleep(0.8)
        
        my_print_routine()
        my_print_routine(f"'Hi {player.name}!! I am Gary.. See you Face to Face...'"); sleep(0.3)
        my_print_routine(f"'Let's start a Pokemon battle' - Gary"); sleep(0.8)
        
        my_print_routine();   my_print_routine("Tap Enter to Go On", end=' ');     input()
        clearScreen()
        my_print_routine("Let the Fight Begin.....",end=' ')
        sleep(3)
        """

        thundershock = Attack('thundershock', 'electric', 40, 0, 30, 0, 0, 1)
        tackle = Attack('tackle', 'normal', 40, 0, 25, 0, 0, 1)
        quickattack = Attack('quick attack', 'normal', 45, 0, 20, 0, 0, 0.95)
        catastropika = Attack('Catastropika', 'electric', 285, 0, 1, 0, 0,0, 1)
"""
        my_print_routine()
        my_print_routine("We would like you to choose a ATTACK TYPE before starting your BATTLE\n"); sleep(0.5)
        my_print_routine("press C for Thundershock"); sleep(0.5)
        my_print_routine("press H for Tackle"); sleep(0.5)
        my_print_routine("press G for Quick attack"); sleep(0.5)
        my_print_routine("press B for Catastropika"); sleep(0.5)
        attack = input()
        if attack in ['c', 'C']:    Domination = thundershock
        elif attack in ['h', 'H']:    Domination = tackle
        elif attack in ['g', 'G']:    Domination = quickattack
        elif attack in ['b', 'B']:    Domination = catastropika
        else:   Domination = thundershock #default
        
        attack_data = Domination
        clearScreen()
        my_print_routine()
        my_print_routine("Your attack and Pickachu detail is as following.....\n"); sleep(0.5)
        attack_data.printAttack()
        my_print_routine("\n\nNOW STARTING FIGHT JUST WAITING FOR YOU TO PRESSS ANY KEY\n\n")
        input()

        my_print_routine("FIGHT STARTED......\n\n\n",end=' ')
        sleep(3)

        my_print_routine("U WON AGAINST GARYY! YEAAH",end=' ')
        
        my_print_routine("This area on grids is yours now \n", end=' ')
        sleep(1)
        my_print_routine("Tap Enter to Go On", end=' '); input()
        clearScreen()
        
        if name != player.name: 
            gameOver = True
            my_print_routine()
            my_print_routine("You LOST  against gary.\n"); sleep(1.4)
            clearScreen()
            my_print_routine("Game Over...\n"); sleep(1.6)
            my_print_routine("But you can Restart the game..."); sleep(1.8)
            my_print_routine();   my_print_routine("Tap Enter to Go On", end=' ');     input()
            exit(1)
        clearScreen()

def navigate_A(a,counter=4):
    print("**KEY TO MAP**\n**0 for an inaccessible spot on the grid\n**1 for an accessible spot \n**2 for an item\n **3 for a Pokemon \n**4 for a CPU-trainer \n5**The actual player has a number like 5")
    print("Press WASD to move in grid\n")
    while(True):
        clearScreen()
        print(a)
        key = input()
        if key in ['W','w'] and not a.myposr<1:
            if a.grid_obj[a.myposr-1][a.myposc].terrain==0:
                print("Sorry you can not go there or Wrong input!! See map again and do right choices again\n")
                sleep(1)
                continue
            a.myposr-=1
            if a.grid_obj[a.myposr][a.myposc].terrain == 1:
                a.grid_obj[a.myposr][a.myposc].terrain = 5
                print("Moved there")
                sleep(1)
                continue
            if a.grid_obj[a.myposr][a.myposc].terrain == 2:
                a.grid_obj[a.myposr][a.myposc].terrain = 5
                print("Healing added to the bag\n")
                sleep(1)
                continue
            elif a.grid_obj[a.myposr][a.myposc].terrain == 3:
                a.grid_obj[a.myposr][a.myposc].terrain = 5
                print("Another Pokemon(Pikachu) added to the bag\n")
                sleep(1)
                continue
            elif a.grid_obj[a.myposr][a.myposc].terrain == 4:
                a.grid_obj[a.myposr][a.myposc].terrain = 5
                print("Entering the battle now\n")
                gameloop()
                sleep(1)
            
        elif key in ['A','a'] and not a.myposc<1 :
            if a.grid_obj[a.myposr][a.myposc-1].terrain==0:
                print("Sorry you can not go there or Wrong input!! See map again and do right choices again\n")
                sleep(1)
                continue
            a.myposc-=1
            if a.grid_obj[a.myposr][a.myposc].terrain == 1:
                a.grid_obj[a.myposr][a.myposc].terrain = 5
                print("Moved there")
                sleep(1)
                continue
            if a.grid_obj[a.myposr][a.myposc].terrain == 2:
                a.grid_obj[a.myposr][a.myposc].terrain = 5
                print("Healing added to the bag\n")
                sleep(1)
                continue
            elif a.grid_obj[a.myposr][a.myposc].terrain == 3:
                a.grid_obj[a.myposr][a.myposc].terrain = 5
                print("Another Pokemon(Pikachu) added to the bag\n")
                sleep(1)
                continue
            elif a.grid_obj[a.myposr][a.myposc].terrain == 4:
                a.grid_obj[a.myposr][a.myposc].terrain = 5
                print("Entering the battle now\n")
                gameloop()
                sleep(1)

        elif key in ['S','s'] and not a.myposr==a.rows-1:
            if a.grid_obj[a.myposr+1][a.myposc].terrain==0:
                print("Sorry you can not go there or Wrong input!! See map again and do right choices again\n")
                sleep(1)
                continue
            
            a.myposr+=1
            if a.grid_obj[a.myposr][a.myposc].terrain == 1:
                a.grid_obj[a.myposr][a.myposc].terrain = 5
                print("Moved there")
                sleep(1)
                continue
            if a.grid_obj[a.myposr][a.myposc].terrain == 2:
                a.grid_obj[a.myposr][a.myposc].terrain = 5
                print("Healing added to the bag\n")
                sleep(1)
                continue
            elif a.grid_obj[a.myposr][a.myposc].terrain == 3:
                a.grid_obj[a.myposr][a.myposc].terrain = 5
                print("Another Pokemon(Pikachu) added to the bag\n")
                sleep(1)
                continue
            elif a.grid_obj[a.myposr][a.myposc].terrain == 4:
                a.grid_obj[a.myposr][a.myposc].terrain = 5
                print("Entering the battle now\n")
                gameloop()
                sleep(1)

        elif key in ['D','d'] and not a.myposc==a.cols-1:
            if a.grid_obj[a.myposr][a.myposc+1].terrain==0:
                print("Sorry you can not go there or Wrong input!! See map again and do right choices again\n")
                sleep(1)
                continue
            a.myposc+=1
            if a.grid_obj[a.myposr][a.myposc].terrain == 1:
                a.grid_obj[a.myposr][a.myposc].terrain = 5
                print("Moved there")
                sleep(1)
                continue
            elif a.grid_obj[a.myposr][a.myposc].terrain == 2:
                a.grid_obj[a.myposr][a.myposc].terrain = 5
                print("Healing added to the bag\n")
                sleep(1)
                continue
            elif a.grid_obj[a.myposr][a.myposc].terrain == 3:
                a.grid_obj[a.myposr][a.myposc].terrain = 5
                print("Another Pokemon(Pikachu) added to the bag\n IF YOU ACQUIRED ANOTHER "  +str(counter)+  " POKEMONS YOU WON THE GAME/N")
                sleep(2)
                continue
            elif a.grid_obj[a.myposr][a.myposc].terrain == 4:
                a.grid_obj[a.myposr][a.myposc].terrain = 5
                print("Entering the battle now\n")
                gameloop()
                sleep(1)

        else:
            counter-=counter
            if counter==0:
                print("All Pokemons collected YOU WON THE WORLD\n")
                sleep(2)
                return
            else:
                clearScreen()
                navigate_A(a,counter)


if __name__ == '__main__':
    #main_menu()
    a = Grid(4,4)
    navigate_A(a) #navigates on the grid




















        
