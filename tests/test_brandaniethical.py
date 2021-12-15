from brandaniethical import brandaniethical
import re
import lxml
from lxml import html
import requests
from bs4 import BeautifulSoup
import pandas as pd
import pytest

df1 = pd.DataFrame(
{'company':'nike',
 'animal_score':'2 out of 5',
 'update':'Last Updated: July 2020',
 'fur':0,
 'angora':0,
 'leather':1,
 'wool':1,
 'shearling':0,
 'karakul':0,
 'down':1,
 'feather':0,
 'exotic animal hair':1,
 'exotic animal skin':0,
 'down_RDS':0,
 'wool_mulesing':0
},index=[0])

ans = 'please check company name of a\nno animal material information of ani'

df2 = pd.DataFrame(
{'company':'adidas',
 'animal_score':'3 out of 5',
 'update':'Last Updated: July 2020',
 'fur':0,
 'angora':0,
 'leather':1,
 'wool':1,
 'shearling':0,
 'karakul':0,
 'down':0,
 'feather':0,
 'exotic animal hair':1,
 'exotic animal skin':0,
 'down_RDS':0,
 'wool_mulesing':1
},index=[0])



def test_fashion_animaterial():
    example = ['adidas']
    expected = df2
    result = brandaniethical(example)
    assert result.equals(expected)

def test_uppercase_brand():
    example2 = ['NIKE']
    expected = df1
    result = brandaniethical(example2)
    assert result.equals(expected)

def test_invalid_brand():
    example3 = ['a']
    expected = ans1
    result = brandaniethical(example3)
    assert result.equals(expected)