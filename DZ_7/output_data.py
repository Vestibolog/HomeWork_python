def findInfo( value ):
    tempArray = []
    with open('db.csv','r',encoding="utf-8") as file:
        for line in file:
            if value in line:
                tempArray.append(lineToArray(line))
    return tempArray;

def lineToArray( value:str ):
    tempArray = value.split(',')
    return tempArray