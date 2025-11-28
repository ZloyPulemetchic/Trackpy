money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
n = 0
x = money_capital+salary
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while spend<=(x):
    n += 1
    spend = spend*(1+increase)
    x = x+salary-spend
print("Количество месяцев, которое можно протянуть без долгов:", n)
