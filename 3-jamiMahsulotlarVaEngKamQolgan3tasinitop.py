#  Ombor nomli list berilgan, listdagi jami mahsulotlar miqdorini va eng kam qolgan 3ta mahsulotni toping.
# ombor = [
#     {"mahsulot": "olma", "miqdor": 5},
#     {"mahsulot": "nok", "miqdor": 9},
#     {"mahsulot": "shaftoli", "miqdor": 7},
#     {"mahsulot": "anor", "miqdor": 4},
#     {"mahsulot": "banan", "miqdor": 6},
#     {"mahsulot": "uzum", "miqdor": 8},
#     {"mahsulot": "gilos", "miqdor": 2},
#     {"mahsulot": "tarvuz", "miqdor": 1},
#     {"mahsulot": "qovun", "miqdor": 3},
#     {"mahsulot": "limon", "miqdor": 5}
# ]
# Output: Umumiy mahsulotlar miqdori: 44
# 	Eng kam qolgan 3 ta mahsulot: tarvuz, gilos, qovun

def eng_kam(ombor):
    jami = 0
    for item in ombor:
        jami += item["miqdor"]
    tartib = sorted(ombor, key=lambda x: x["miqdor"])
    kam3 = [x["mahsulot"] for x in tartib[:3]]
    return jami, kam3
ombor = [
 {"mahsulot": "olma", "miqdor": 5}, 
 {"mahsulot": "nok", "miqdor": 9}, 
 {"mahsulot": "shaftoli", "miqdor": 7},
 {"mahsulot": "anor", "miqdor": 4},
 {"mahsulot": "banan", "miqdor": 6}, 
 {"mahsulot": "uzum", "miqdor": 8},
 {"mahsulot": "gilos", "miqdor": 2},
 {"mahsulot": "tarvuz", "miqdor": 1}, 
 {"mahsulot": "qovun", "miqdor": 3},
 {"mahsulot": "limon", "miqdor": 5} 
 ]
jami, kam3 = eng_kam(ombor)
print("Umumiy mahsulotlar miqdori: ", jami)
print("eng kam qolgan 3 ta mahsulot: ",', '.join(kam3))