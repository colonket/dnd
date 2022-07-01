import json
import random
import fantasynames as names
import math


class Character:
    def __init__(
            self,
            ttrpg_json=None,
            level=None,
            race=None,
            char_class=None,
            name=None,
            abil_scores={},
            stats={},
            backpack=[],
            attacks=[]
        ):
        self.data = ttrpg_json
        self.level = level
        self.race = race
        self.char_class = char_class
        self.name = name

        self.abil_scores = abil_scores

        self.stats = stats
            
        self.backpack = backpack
        self.attacks = attacks

    def generateRandom(self):
        self.level = 1
        self.race = random.choice(self.data['race'])['name']
        self.char_class = random.choice(self.data['class'])['name']
        self.name = names.human('any')

        # Generate Ability Scores
        self.abil_scores = {}
        for abil in self.data['ability']:
            self.abil_scores[ abil['name'] ] = rollAbilScore()

        self.stats = {}
        for stat in self.data['stats']:
            self.stats[ stat['name'] ] = stat['default']
            
        self.backpack = []
        self.attacks = []

    def __repr__(self):
        return f"Character(data,{self.level},{self.race},{self.char_class},{self.name},{self.abil_scores},{self.hp},{self.speed},{self.init},{self.ac},{self.prof},{self.backpack},{self.attacks})"

    def __str__(self):
        title = f"{self.name}, Lvl. {self.level} {self.race} {self.char_class}"
        for key in self.abil_scores.items():
            title += f"\n{key[0]} -> {str(key[1]).rjust(2)} ({abilScoreMod(key[1])})"
        title += f"\nBackpack: {self.backpack}"
        title += f"\nAttacks:  {self.attacks}"
        return title
    

def rollD(value):
    return random.randint(1,value) 

def rollAbilScore(r=4,k=3):
    # Roll 'r' d6's, and keep the 'k' highest dice
    rolls = [rollD(6) for i in range(r)]
    return sum(sorted(rolls,reverse=True)[:k])

def abilScoreMod(abilityScore):
    sign = ""
    mod = math.floor( (abilityScore - 10) / 2)
    if mod >= 0:
        sign += "+"
    else:
        sign += ""
    return sign+str(mod)
        