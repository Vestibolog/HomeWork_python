def addObject(value):
    with open('db.csv','a',encoding="utf-8") as file:
        file.write(f'{arrayToStr(value)}\n')

def delObject(value):
    tempStr = arrayToStr( value )
    print(tempStr)
    with open('db.csv','r+',encoding="utf-8") as file:
        new_f = file.readlines()
        file.seek(0)
        for line in new_f:
            if tempStr not in line:
                file.write(line)
        file.truncate()

def arrayToStr( value ):
    tempStr =  ",".join(str(x) for x in value)
    return tempStr

