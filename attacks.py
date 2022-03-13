from random import random, seed, randint
from math import floor

def my_print_routine(*args, **kwargs):
    print('\t\t', *args, **kwargs)
    

class Attack(object):
    
    def __init__(self, name, CAtgeories, Dmage_onHit, Levels, Count, increserr_abled=1,Recoiling_ratio=0, Healings=0, accuraies=1, *args, **kwargs):
        self.name = name
        self.CAtgeories = CAtgeories
        self.Dmage_onHit = Dmage_onHit
        self.accuraies = accuraies
        self.Recoiling_ratio = - Recoiling_ratio
        self.maxcount = Count
        self.count = self.maxcount
        self.pLevel = Levels
        self.increserr_abled = increserr_abled
        self.Healings = Healings

    def printAttack(self):
        my_print_routine('|***************************************************************************************************************************************')
        my_print_routine(f"| Attack: {self.name:15} | Type:   {self.CAtgeories:10} | Damage: {self.Dmage_onHit:5} | Count: {self.maxcount:3}")
        my_print_routine(f"| Healings:   {self.Healings:15} | Recoiling_ratio: {self.Recoiling_ratio:10} | accuraies: {self.accuraies}")
        my_print_routine('|***************************************************************************************************************************************')
        