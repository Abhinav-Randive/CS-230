import pytest
from class1 import Pet, Cat, Dog


def testNoiseCat(capsys):
    cat = Cat(2, "Fluffy", "White")
    cat.makeNoise()
    captured = capsys.readouterr()
    assert captured.out == "Meow\n"

def testNoiseDog(capsys):
    dog = Dog(3, "Rex", "Chihuahua")
    dog.makeNoise()
    captured = capsys.readouterr()
    assert captured.out == "Yapyapyap\n"

    dog2 = Dog(4, "Buddy", "Shitzu")
    dog2.makeNoise()
    captured = capsys.readouterr()
    assert captured.out == "Bork Bark\n"

    dog3 = Dog(1, "Max", "Havenese")
    dog3.makeNoise()
    captured = capsys.readouterr()
    assert captured.out == "Bark Bark\n"
