import json
import random

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
    

class character:
    def __init__(self):
        self.race = ""
        self.charClass = ""
        self.name = ""
        self.abilityScores = ""
    
    def __repr__(self):
        attrs = [self.race,self.charClass,self.name,self.abilityScores]
        return " ".join(attrs)

    def __str__(self):
        attrs = [self.race,self.charClass,self.name,self.abilityScores]
        return " ".join(attrs)


def genCharRandom(data):
    char = character
    char.race = random.choice(data['race']) 
    return char 

if __name__ == '__main__':
    f = open("attributes.json","r")
    data = json.loads(f.read())
    f.close()

    #listAttr(data)
    npc1 = genCharRandom(data)
    print(str(npc1))