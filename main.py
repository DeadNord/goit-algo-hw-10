from pulp import *
import numpy as np
import scipy.integrate as spi

# Ініціалізація моделі
model = LpProblem("Maximize_Production", LpMaximize)

# Визначення змінних
lemonade = LpVariable("Lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

# Додавання функції цілі
model += lemonade + fruit_juice, "Total_Production"

# Обмеження ресурсів
model += 2 * lemonade + fruit_juice <= 100, "Water"
model += lemonade <= 50, "Sugar"
model += lemonade <= 30, "Lemon_Juice"
model += 2 * fruit_juice <= 40, "Fruit_Puree"

# Розв'язання задачі
model.solve()

# Виведення результатів
print(f"Lemonade: {lemonade.varValue}")
print(f"Fruit Juice: {fruit_juice.varValue}")
print(f"Total Production: {value(model.objective)}")


# Визначення функції
def f(x):
    return x**2


# Метод Монте-Карло
def monte_carlo_integration(func, a, b, samples=10000):
    random_samples = np.random.uniform(a, b, samples)
    func_values = func(random_samples)
    area = (b - a) * np.mean(func_values)
    return area


# Обчислення інтеграла методом Монте-Карло
mc_result = monte_carlo_integration(f, 0, 2)

# Обчислення інтеграла за допомогою quad
quad_result, error = spi.quad(f, 0, 2)

print(f"Монте-Карло: {mc_result}")
print(f"Quad: {quad_result}")
