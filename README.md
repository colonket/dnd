# Untitled TTRPG Python Library

Python library that allows you to create and interact with TTRPG characters
based on the specifications of a TTRPG through a JSON file.

Created as a way to model Dungeons and Dragons characters in Python.

Just a fun little side project that can change one way or another.

## Usage

Inside this repo, install the requirements with:

```pip3 install -r```

Run `test.py` to see examples of the library in action

```python3 test.py```

### Creating a Random Character

```python3
import ttrpg_char

with open("dnd.json","r",encoding="utf-8") as f:
    dnd = json.loads(f.read())

randChar = ttrpg_char.Character()
randChar.gen_random_char()
print(randChar)
```

### Creating a Character Manually 

```python3
import ttrpg_char

with open("dnd.json","r",encoding="utf-8") as f:
    dnd = json.loads(f.read())

someChar = ttrpg_char.Character(
        ttrpg_json=dnd,
        level=2,
        race="Tiefling",
        char_classes={
            "Cleric":1,
            "Rogue":1
        },
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
print(someChar)
```

