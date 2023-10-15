year = int(input("Введіть рік для перевірки чи є він високосним: "))
if 1900 < year < 1_000_000:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(year, "рік високосний.")
    else:
        print(year, "рік не високосний.")

else:
    print("Рік не відповідає умовам")



