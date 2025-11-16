def tozalash(lst):
    yangi = []
    for s in lst:
        if s != "" and s not in yangi:
            yangi.append(s)
    return yangi
mylist = ["olma", "", "olma", "gilos", ""]
mylist = tozalash(mylist)
print(mylist)