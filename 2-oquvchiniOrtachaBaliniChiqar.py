# Har bir o'quvchining fanlar bo'yicha baholari berilgan. Har bir o'quvchi uchun o'rtacha ballni hisoblang.
# students = {
#   "Ali": {"math": 90, "en": 80},
#   "Vali": {"math": 70, "en": 85}
# }
# Output:
# Natija: Ali: 85.0, Vali: 77.5

def ortacha_ball(students):
    for ism,fanlar in students.items():
        ortacha = sum(fanlar.values()) / len(students)
        print(f"{ism}: {ortacha}")
students ={
    "Ali":{"math": 90, "en": 80},
    "Vali":{"math": 70, "en": 85}
}
ortacha_ball(students)