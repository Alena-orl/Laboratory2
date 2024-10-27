# -*- coding: utf-8 -*-
money_capital = 12000 #подушка безопасности
salary = 2000 #ежемесячная зп
spend = 2500 #расходы на проживание в 1 месяц
increase = 0.05 #ежемесячный рост цен

month = 0

while salary+money_capital-spend>=0:
    month+=1
    money_capital+=salary-spend
    spend+=increase*spend
print("Без долгов удастся прожить ",month," месяцев")