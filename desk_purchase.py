students_in_class1 = int(input("Введіть кількість учнів у першому класі: "))
students_in_class2 = int(input("Введіть кількість учнів у другому класі: "))
students_in_class3 = int(input("Введіть кількість учнів у третьому класі: "))

desks_need = (students_in_class1 // 2 + students_in_class1 % 2) + \
               (students_in_class2 // 2 + students_in_class2 % 2) + \
               (students_in_class3 // 2 + students_in_class3 % 2)
print("Кількість парт що треба закупити: ", desks_need)
