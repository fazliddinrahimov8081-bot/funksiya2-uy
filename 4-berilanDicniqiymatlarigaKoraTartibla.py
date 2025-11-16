def tartibla(d):
    # d.iitems  -> ('t',3), ("p",1)...
    # key=lambda x: x[1] -> qiymat boyicha tartiblaydi
    tartib = sorted(d.items(), key=lambda x: x[1])
    # faqat kalitlarni chiqaramiz
    for kalit, qiymat in tartib:
        print(kalit)
my_dict = {
    "t": 3,
    "p": 1,
    "y": 2,
    "o": 5,
    "h": 4,
    "n": 6,
}
tartibla(my_dict)