"""DND Utilities Library
"""
import random
import math
import fantasynames as names

def roll_d(value):
    """Roll a dice of any value

    Args:
        value (int): The highest value of the die to be rolled. (i.e. 20 for d20)

    Returns:
        _int_: Random number from 1 to chosen value
    """
    return random.randint(1,value)

def sum_of_dice(d=6,r=4,k=3,high=True):
    """Roll 'r' dice of value 'd', and keep the 'k' highest or lowest dice depending on 'high'.
    By default, rolls 4 d6's and finds the sum of the 3 highest dice values.

    Args:
        d (int, optional): Die value. Defaults to 6
        r (int, optional): How many dice to roll. Defaults to 4.
        k (int, optional): How many dice to keep. Defaults to 3.
        high (bool, optional): If high, keep the highest dice. Defaults to True.

    Returns:
        int: Sum of the dice
    """
    # Roll 'r' d6's, and keep the 'k' highest dice
    rolls = [roll_d(d) for i in range(r)]
    return sum(sorted(rolls,reverse=high)[:k])

def calc_abil_score_mod(abil_score):
    """Calculates the ability score modifier for a given ability score

    Args:
        abil_score (int): The value of an ability score

    Returns:
        int: The ability score modifier based on the ability score
    """
    sign = ""
    mod = math.floor( (abil_score - 10) / 2)
    if mod >= 0:
        sign += "+"
    else:
        sign += ""
    return sign+str(mod)
        
def parse_dice_rolls(str_input):
    """Parses dice rolls given by user and returns sum of dice rolls and values

    Args:
        str_input (String): i.e. "2d6 + 4"

    Returns:
        int: The sum of all dice rolls and values given
    """
    sum = 0
    args = str_input.split("+") # Split string into list of arguments
    for a in args:
        a = "".join(a.split())  # Strip whitespace from each argument
    return sum

class Action:
    """An action to be used in Dungeons and Dragons
    """

    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return f"Action({self.name})"
        
    def __str__(self):
        return f"{self.name}"


class Character:
    """A TTRPG Character Instance, used to keep track of and modify
    the various stats, items, and variables related to a character
    """
    def __init__(
            self,
            ttrpg_json=None,
            level=None,
            race=None,
            char_classes=None,
            name=None,
            abil_scores=None,
            stats=None,
            inventory=None,
            actions=None
        ):
        self.data = ttrpg_json
        self.level = level
        self.race = race
        self.char_classes = char_classes
        self.name = name
        self.abil_scores = abil_scores
        self.stats = stats
        self.inventory = inventory
        self.actions = actions

    def gen_random_char(self):
        """Create a random character from the character object
        """
        self.level = 1
        self.race = random.choice(self.data['race'])['name']
        self.char_classes = {random.choice(self.data['class'])['name'] : 1}
        self.name = names.human('any')

        self.abil_scores = {}
        for abil in self.data['ability']:
            self.abil_scores[ abil['name'] ] = sum_of_dice()

        self.stats = {}
        for stat in self.data['stats']:
            self.stats[ stat['name'] ] = stat['default']
        self.stats['HP'] = roll_d(10)

        self.inventory = []
        self.actions = []

    def __repr__(self):
        output = f"Character(data,{self.level},{self.race},{self.char_classes},{self.name},"
        output += f"{self.abil_scores},{self.stats},{self.inventory},{self.actions})"
        return output

    def __str__(self):
        if None not in [self.name,self.level,self.race,self.char_classes]:
            title = f"{self.name}, Lvl. {self.level} {self.race}, "
            for c in self.char_classes.items():
                title += f"{c[0]} {c[1]} "
            if self.stats:
                for stat in self.stats.items():
                    title += f"\n\t{stat[0]}\t-> {stat[1]}"
            if self.abil_scores:
                for key in self.abil_scores.items():
                    title += f"\n\t{key[0]} -> {str(key[1]).rjust(2)} ({calc_abil_score_mod(key[1])})"
            title += f"\n\tInventory:\t{self.inventory}"
            title += f"\n\tActions:\t{self.actions}"
            return title
        return f"Character '{self.name}' is missing critical attributes"
    
