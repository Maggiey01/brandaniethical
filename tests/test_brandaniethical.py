import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
from requests.exceptions import HTTPError
import requests.auth
import os
from brandaniethical.brandaniethical import brandaniethical
from brandaniethical.brandaniethical import trendyesg
from pandas._testing import assert_frame_equal

#function1 test
df1 = pd.DataFrame(
{'company':'adidas',
 'animal_score':'3/5',
 'update':'July 2020',
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

df2 = pd.DataFrame(
{'company':'nike',
 'animal_score':'2/5',
 'update':'July 2020',
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

def test_fashion_animaterial():
    example = ['adidas']
    expected = df1
    result = brandaniethical(example)
    assert_frame_equal(df1, result)
    

def test_uppercase_brand():
    example2 = ['NIKE']
    expected = df2
    result = brandaniethical(example2)
    assert_frame_equal(df2, result)

def test_invalid_brand():
    example3 = ['a']
    result = brandaniethical(example3)
    assert isinstance(result, type(None))
    
    
    
#function2 test
import pytest
def test_invalid_region():
    region = 'ak'
    with pytest.raises(AssertionError):
        trendyesg(region, start=5)


def test_invalid_start():
    start = 'ak'
    with pytest.raises(AssertionError):
        trendyesg(region='US', start=start)
