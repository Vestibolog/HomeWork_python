import input_data
import output_data

phoneBook = []


def click():
    print("добро пожаловать в телефонный справочник")
    printMenu()


def printMenu():
    print("")
    print("Что вы хотите сделать?")
    print("1 поиск")
    print("2 удалить по имени или номеру")
    print("3 добавить новую запись")
    print("4 выйти")
    msg = input()
    if msg == "1":
        find()
    elif msg == "2":
        delite()
    elif msg == "3":
        addNew()
    elif msg == "4":
        print("До новых встреч")
    else: 
        print("Неккоректна команда")
        printMenu()



def find():
    print("Введите информацию для поиска")
    msg = input()
    tempArray = output_data.findInfo(msg)
    if len(tempArray) == 0:
        print("ничего не найдено")
    else:
        print("Результаты поиска")
        for i in range(len(tempArray)):
            print(
                f"№ {i}   фамилия: {tempArray[i][0]}   имя:{tempArray[i][1]}  телефон:{tempArray[i][2]}    описание {tempArray[i][3]} ")
    printMenu()

def delite():
    print("Введите информацию для поиска")
    msg = input()
    tempArray = output_data.findInfo(msg)
    if len(tempArray) == 0:
        print("ничего не найдено")
    else:
        print("Результаты поиска")
        for i in range(len(tempArray)):
            print(
                f"№ {i}   фамилия: {tempArray[i][0]}   имя:{tempArray[i][1]}  телефон:{tempArray[i][2]}    описание {tempArray[i][3]} ")
        print("Введите номер строки для удаления")
        msg = input()
        if ( msg.isdigit() ) and (  0 <= int(msg) < len(tempArray)):
            input_data.delObject(tempArray[int(msg)])
            print('контакт удален')
        else :
            print('неккоректный номер')
    printMenu()

def addNew():
    print("Введите информацию для вставки")
    msg = input()  
    tempArray = output_data.lineToArray( msg )
    if len(tempArray) < 4 :
        tempArray = [msg]
        while len(tempArray)< 4:
            msg = input() 
            tempArray.append(msg)
    print("проверте корректность информации")            
    print(
          f"фамилия: {tempArray[0]}   имя:{tempArray[1]}  телефон:{tempArray[2]}    описание {tempArray[3]} ")
    print("сохранить? 1 - да ")
    msg = input()
    if (  msg == "1" ):
        input_data.addObject(tempArray)
        print("сохранено")
        printMenu()
    else :
        printMenu()