# Matn berilgan. Eng ko'p uchraydigan 3 ta so'zni toping. 
# ( So'zlar faqat harflardan iborat bo'ladi.)
# Input: "olma nok olma gilos olma nok shaftoli" Output: olma nok gilos

def top3(matn):
    soz = matn.split()
    hisob = {}
    for i in soz:
        if i in hisob:
            hisob[i]+=1
        else: hisob[i]=1
    eng_kop=sorted(hisob.items(), key= lambda x: x[1], reverse=True)
    top3 = [item[0] for item in eng_kop[:3]]
    return ' '.join(top3)
matn = "olma nok olma gilos olma nok shaftoli"
print(top3(matn))