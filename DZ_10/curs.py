import random
import math
from math import sqrt
from google_currency import convert
import json


def curd_found(currency1:str,currency2:str,value:float) ->str :


    result = convert(currency1,currency2,value)
    print(result)

    data = json.loads(result)

    tempStr = str(value) +" "
    tempStr += data['from'] + " это " 
    tempStr += str(data['amount']) + " в " + data['to']
    return tempStr;

print(curd_found('usd','usd',100))