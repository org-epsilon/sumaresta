from resta_logic import restar

def test_restar_positivos():
    assert restar(20, 5) == 15.0

def test_restar_decimales():
    assert restar(10.5, 2.5) == 8.0
