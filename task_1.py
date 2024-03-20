from pulp import LpMaximize, LpProblem, LpVariable, lpSum

# Створення задачі лінійного програмування для максимізації виробництва напоїв
problem = LpProblem("Maximize_Production", LpMaximize)

# Визначення змінних рішення для кількості одиниць "Лимонаду" та "Фруктового соку" до виробництва
lemonade = LpVariable("Lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

# Додавання функції цілі для максимізації загальної кількості продуктів
problem += lpSum([lemonade, fruit_juice])

# Додавання обмежень на основі обмежених ресурсів
problem += 2 * lemonade + 1 * fruit_juice <= 100, "Water"
problem += 1 * lemonade <= 50, "Sugar"
problem += 1 * lemonade <= 30, "Lemon_Juice"
problem += 2 * fruit_juice <= 40, "Fruit_Puree"

# Розв'язання задачі
problem.solve()

# Виведення результатів
print(f"Виробити {lemonade.varValue} одиниць 'Лимонаду'")
print(f"Виробити {fruit_juice.varValue} одиниць 'Фруктового соку'")
