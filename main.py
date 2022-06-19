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
    

class Character:
    def __init__(self, data):
        self.race = random.choice(data['race'])['name']
        self.charClass = random.choice(data['class'])['name']
        self.name = random.choice(data['ability'])['short']
        self.pretty = " ".join([self.race,self.charClass])

    def __repr__(self):
        return self.pretty

    def __str__(self):
        return self.pretty


if __name__ == '__main__':
    f = open("attributes.json","r")
    data = json.loads(f.read())
    f.close()

    #listAttr(data)
    npc1 = Character(data)
    print(npc1)
