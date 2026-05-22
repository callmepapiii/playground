from model.creature import Creature
from service import creature as code

sample = Creature(
    name = "Chula",
    description = "War-like angry dude",
    area = "Ruai",
    aka = "Maina",
    country = "KE"
)

def test_create():
    resp = code.create(sample)
    assert resp == sample
    
def test_get_exists():
    resp = code.get_one("Maina")
    assert resp == sample
    
def test_get_missing():
    resp = code.get_one("Mithelle")
    assert data is None
