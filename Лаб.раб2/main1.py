money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
wrk_capital = money_capital
spending = spend
month = 0
while (salary+wrk_capital)-spending > 0:
    wrk_capital = wrk_capital+salary-spending
    spending = spending * (1+increase)
    month = month + 1
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", month)
