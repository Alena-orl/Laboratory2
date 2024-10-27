money_capital = 12000
salary = 2000
spend = 3500
increase = 0.05

months = 0

while True:
    budget = money_capital + salary

    if budget>=spend:
        months+=1
        money_capital -= (spend-salary)
        spend += spend*increase
    else:
        print("Количество месяцев, которые можно протянуть без долгов:", months)