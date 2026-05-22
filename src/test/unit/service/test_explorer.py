from service import explorer as code
from model.explorer import Explorer

sample = Explorer(
    name = "War",
    country = "Kenya",
    description = "Saudi"
)

def test_create():
    resp = code.get_all()
    assert resp == sample
    
def test_get_exists():
    resp = code.get_one("War")
    assert resp == sample
    
def test_get_missing():
    resp = code.get_one("Erw")
    assert data is None