from model.creature import Creature

_creatures = [
    Creature(
        name = "Godzilla",
        country = "Japan",
        area = "Tokyo",
        description = "Tall lizard with blast breathe ",
        aka = "Godzilla"
    ),
    Creature(
        name = "Bigfoot",
        country = "Kenya" ,
        description = "7 feet tall",
        area = "Baringo",
        aka = "Goliath"
    )
]

def get_all() -> list[Creature]:
    """ Return all the list of noted Creatures"""
    return _creatures

def get_one(name: str) -> Creature | None:
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None

def create(creature: Creature) -> Creature:
    """ List new creature"""
    return creature

def modify(creature: Creature) -> Creature:
    """ Partially modify a creature"""
    return creature

def replace(creature: Creature) -> Creature:
    """ Replace fully the creature"""
    return creature

def delete(name: str):
    """delete the creature entirely"""
    return None
