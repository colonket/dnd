import dndChar

import json
import random
import fantasynames as names
import math

def list_attr(data_json):
    """List contents of attributes.json
    """

    print("\nRaces:")
    for r in data_json['race']:
        print(r['name'])
    
    print("\nClasses:")
    for c in data_json['class']:
        print(c['name'])
    
    print("\nAbilities:")
    for a in data_json['ability']:
        print(a['short'])

def test_chars(data_json):
    """Test method for creating character objects
    """
    print("Creating empty character...")
    npc1 = dndChar.Character(data_json)
    print(npc1)

    print()

    print("Generating Random Character...")
    npc1.generateRandom()
    print(npc1)

if __name__ == '__main__':
    with open("attributes.json","r",encoding="utf-8") as f:
        data = json.loads(f.read())
    test_chars(data)