while True: 
    print ("Напишите номер расы для выведения его характеристик")
    print ("1-Орк")
    print ("2-Человек")
    print ("3-Эльф")
    print ("4-Гном")
    print ("5-Дворф")
    print ("6-Нежить")
    print ("7-Гоблин")
    print ("8-Пандарен")
    a=int(input())
    if a==1:
            file=open('1.txt',encoding='utf-8')
            content=file.readline()
            s=content[0]
            print("Орк",s)
    elif a==2:
            file-open('1.txt',encoding='utf-8')
            content=file.readline()
            s=content[1]
            print("Человек",s)
    elif a==3:
            file-open('1.txt',encoding='utf-8')
            content=file.readline()
            s=content[2]
            print("Эльф",s)
    elif a==4:
            file-open('1.txt',encoding='utf-8')
            content=file.readline()
            s=content[3]
            print("Гном",s)
    elif a==5:
            file-open('1.txt',encoding='utf-8')
            content=file.readline()
            s=content[4]
            print("Дворф",s)
    elif a==6:
            file-open('1.txt',encoding='utf-8')
            content=file.readline()
            s=content[5]
            print("Нежить",s)
    elif a==7:
            file-open('1.txt',encoding='utf-8')
            content=file.readline()
            s=content[6]
            print("Гоблин",s)
    elif a==8:
            file-open('1.txt',encoding='utf-8')
            content=file.readline()
            s=content[7]
            print("Пандарен",s)
    else:
        print ("Такой расы не существует")                                       
