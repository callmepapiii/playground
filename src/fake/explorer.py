from model.explorer import Explorer

_explorers  = [
    Explorer(
        name = "Claude",
        country = "USa",
        description = "Short"
    ),
    Explorer(
        name = "Jean-Claude",
        country = "USA",
        description = "Tall"
    )
]

#Return all explorers
def return_all() -> list[Explorer]:
    return _explorers

def get_one(name: str) -> Explorer | None:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return None

def create(explorer: Explorer) -> Explorer:
    """create an explorer"""
    return explorer

def delete(name: str) -> bool:
    return None

def modify(explorer: Explorer) -> Explorer:
    """PArtially modify the explorer list."""
    return explorer

def replace(explorer: Explorer) -> Explorer:
    """ Replace the explorer fully."""
    return explorer        
