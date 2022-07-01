import ttrpg_char

import json
import random
import fantasynames as names
import math

def list_attr(ttrpg_json):
    """List contents of dnd.json
    """

    print("\nRaces:")
    for r in ttrpg_json['race']:
        print(r['name'])
    
    print("\nClasses:")
    for c in ttrpg_json['class']:
        print(c['name'])
    
    print("\nAbilities:")
    for a in ttrpg_json['ability']:
        print(a['short'])

def test_chars(ttrpg_json):
    """Test method for creating character objects
    """
    print("Creating empty character...")
    npc1 = ttrpg_char.Character(ttrpg_json)
    print(npc1)

    print()

    print("Generating Random Character...")
    npc1.gen_random_char()
    print(npc1)




if __name__ == '__main__':
    with open("dnd.json","r",encoding="utf-8") as f:
        dnd = json.loads(f.read())
    #test_chars(dnd)

    sard_roh = ttrpg_char.Character(
        ttrpg_json=dnd,
        level=2,
        race="Tiefling",
        char_class="Cleric 1 / Rogue 1",
        name="Sard Roh",
        abil_scores={
            "STR":13,
            "DEX":15,
            "CON":13,
            "INT":10,
            "WIS":10,
            "CHA":15
        },
        stats={
            "HP":15,
            "SPEED":30,
            "INIT":2,
            "AC":12,
            "PROF":2
        },
        inventory=["Potion of Healing (Greater)","Dagger","Padded","Quarterstaff"],
        actions=["Unarmed Strike"]
    )
    print(sard_roh)