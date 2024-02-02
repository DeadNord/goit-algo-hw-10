from pulp import LpProblem, LpMaximize, LpVariable, value
import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt
from tabulate import tabulate


class ProductionOptimization:
    def __init__(self):
        self.model = LpProblem("Maximize_Production", LpMaximize)
        self.lemonade = LpVariable("Lemonade", lowBound=0, cat="Integer")
        self.fruit_juice = LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

    def setup_problem(self):
        # Додавання функції цілі
        self.model += self.lemonade + self.fruit_juice, "Total_Production"
        # Обмеження ресурсів
        self.model += 2 * self.lemonade + self.fruit_juice <= 100, "Water"
        self.model += self.lemonade <= 50, "Sugar"
        self.model += self.lemonade <= 30, "Lemon_Juice"
        self.model += 2 * self.fruit_juice <= 40, "Fruit_Puree"

    def solve(self):
        self.model.solve()
        results = [
            ["Lemonade", self.lemonade.varValue],
            ["Fruit Juice", self.fruit_juice.varValue],
            ["Total Production", value(self.model.objective)],
        ]
        print(tabulate(results, headers=["Product", "Amount"]))


class MonteCarloIntegration:
    def __init__(self, func, a, b, samples=10000):
        self.func = func
        self.a = a
        self.b = b
        self.samples = samples

    def integrate(self):
        random_samples = np.random.uniform(self.a, self.b, self.samples)
        func_values = self.func(random_samples)
        area = (self.b - self.a) * np.mean(func_values)
        return area

    def compare_with_quad(self):
        mc_result = self.integrate()
        quad_result, _ = spi.quad(self.func, self.a, self.b)
        results = [
            ["Method", "Result"],
            ["Monte Carlo", mc_result],
            ["Quad", quad_result],
        ]
        print(tabulate(results, headers="firstrow"))
        self.visualize()

    def visualize(self):
        x = np.linspace(self.a - 1, self.b + 1, 400)
        y = self.func(x)
        plt.plot(x, y, "r", linewidth=2)
        plt.fill_between(x, y, color="gray", alpha=0.3)
        plt.title(f"Integration of f(x) from {self.a} to {self.b}")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True)
        plt.show()


def main():
    # Виконання оптимізації виробництва
    prod_opt = ProductionOptimization()
    prod_opt.setup_problem()
    prod_opt.solve()

    # Виконання та візуалізація Монте-Карло інтеграції
    def f(x):
        return x**2

    mc_integration = MonteCarloIntegration(f, 0, 2)
    mc_integration.compare_with_quad()


if __name__ == "__main__":
    main()
