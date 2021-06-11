def solve(meal_Cost , tip_Percent , tax_Percent):
    tip = meal_Cost * (tip_Percent / 100)
    tax = meal_Cost * (tax_Percent / 100)

    print(round(meal_Cost + tip + tax))

mealcost = float(input())
tippercent=int(input())
taxpercent=int(input())
solve(mealcost,tippercent,taxpercent)
