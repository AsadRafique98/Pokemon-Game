from random import random, randint
from time import sleep

def my_print_routine(*args, **kwargs):
    print('\t\t', *args, **kwargs)
    

class Player(object):
    
    def __init__(self, name, cateorygy='player', pokimons_in_bag=[], totl_limit=7, balls=2, cash_inHand=300, *args, **kwargs):
        self.name = name
        self.mood = 'happy'
        self.currentPokemon = None
        self.pokemonInHand = pokimons_in_bag
        self.totl_limit = totl_limit
        self.items = {}
        self.badges = []
        self.cateorygy = cateorygy
        self.archivePokemons = []
        self.balls = balls
        self.cash_inHand = cash_inHand
    
    def printTrainer(self, showAllpoke=False):
        if self.cateorygy == 'player':
            my_print_routine("+--------------------------------------------------------------------------+"); sleep(0.2) 
            my_print_routine()
            my_print_routine(f"Name: {self.name}"); sleep(0.2)
            my_print_routine(f"Items: {self.items}"); sleep(0.2)
            my_print_routine(f"Pokemon: {self.currentPokemon.name}"); sleep(0.2)
            my_print_routine(f"Badges: {self.badges}"); sleep(0.2)
            my_print_routine(f"cash_inHand: {self.cash_inHand}"); sleep(0.2)
            my_print_routine(f"balls: {self.balls}"); sleep(0.2)
            my_print_routine()
            my_print_routine("+--------------------------------------------------------------------------+")
        else:
            my_print_routine("+-----------------------------------------------------+"); sleep(0.2) 
            my_print_routine()
            my_print_routine(f"Name: {self.name}"); sleep(0.2)
            my_print_routine(f"cash_inHand: $ {self.cash_inHand}"); sleep(0.2)
            my_print_routine(f"Number of pokemons: {len(self.pokemonInHand)}"); sleep(0.2)
            my_print_routine()
            my_print_routine("+-----------------------------------------------------+")
            
    def healAllpoke(self):#use healing from the grid
        sleep(0.2)
        if self.cateorygy == 'player':
            my_print_routine("All your pokemons ......100 hp healed..."); sleep(1.2)
        for pokemon in self.pokemonInHand:
            pokemon.visitPokemonCentre()