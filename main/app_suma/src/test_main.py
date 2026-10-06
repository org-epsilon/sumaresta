from main import sumar

def test_sumar_positivos():
    assert sumar(15, 25) == 40

def test_sumar_decimales():
    assert sumar(10.5, 4.5) == 15.0