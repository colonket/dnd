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
        self.level = 0
        self.race = random.choice(data['race'])['name']
        self.charClass = random.choice(data['class'])['name']
        self.name = random.choice(data['ability'])['short']
        self.title = f"Level {self.level} {self.race} {self.charClass}"

        self.equipment = []
        self.attacks = []

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title


if __name__ == '__main__':
    with open("attributes.json","r",encoding="utf-8") as f:
        data = json.loads(f.read())

    #listAttr(data)
    npc1 = Character(data)
    print(npc1)
