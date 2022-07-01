import json
import random
import fantasynames as names
import math

def listAttr():
    f = open("attributes.json","r")
    data = json.loads(f.read())
    f.close()

    print("\nRaces:")
    for r in data['race']:
        print(r['name'])
    
    print("\nClasses:")
    for c in data['class']:
        print(c['name'])
    
    print("\nAbilities:")
    for a in data['ability']:
        print(a['short'])
    

class Character:
    def __init__(self, data):
        self.level = 1
        self.race = random.choice(data['race'])['name']
        self.charClass = random.choice(data['class'])['name']
        self.name = names.human('any')

        # Generate Ability Scores
        self.AS = {}
        for a in data['ability']:
            self.AS[ a["short"] ] = rollAbilScore()

        self.hp = rollD(10)
        self.speed = 30
        self.init = 2
        self.ac = 12
        self.prof = 6
            
        self.backpack = []
        self.attacks = []

        self.title = f"{self.name}, Lvl. {self.level} {self.race} {self.charClass}"
        for key in self.AS.items():
            self.title += f"\n{key[0]} -> {str(key[1]).rjust(2)} ({abilScoreMod(key[1])})"
        self.title += f"\nBackpack: {self.backpack}"
        self.title += f"\nAttacks:  {self.attacks}"

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title
    

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
        

if __name__ == '__main__':
    with open("attributes.json","r",encoding="utf-8") as f:
        data = json.loads(f.read())

    npc1 = Character(data)
    print(npc1)
