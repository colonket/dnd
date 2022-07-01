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
    npc1.generateRandom()
    print(npc1)

if __name__ == '__main__':
    with open("dnd.json","r",encoding="utf-8") as f:
        dnd = json.loads(f.read())
    test_chars(dnd)