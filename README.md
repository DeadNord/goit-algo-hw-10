| Product          |     Amount |
| :--------------- | ---------: |
| Lemonade         |         30 |
| Fruit Juice      |         20 |
| Total Production |         50 |
| Method           |     Result |
| :------------    | ---------: |
| Monte Carlo      |      2.652 |
| Quad             |    2.66667 |

![Alt text](image.png)

## Task 1: Production Optimization

Using the PuLP library for linear programming, we solved the task of optimizing the production of two types of products: "Lemonade" and "Fruit Juice". The task was to maximize the total production quantity considering limited resources: water, sugar, lemon juice, and fruit puree.

The results obtained from the CBC MILP Solver showed that to achieve the maximum total production (50 units), it is necessary to produce 30 units of "Lemonade" and 20 units of "Fruit Juice". This optimal solution takes into account all resource constraints and demonstrates the effectiveness of using linear programming to solve similar optimization tasks.

## Task 2: Calculating a Definite Integral Using the Monte Carlo Method

The Monte Carlo method was used to calculate the definite integral of the function \(f(x) = x^2\) over the interval from 0 to 2. The value of the integral obtained by the Monte Carlo method (2.621712173311222) was compared with the precise value obtained using the `quad` function (2.666666666666667), which corresponds to the analytical calculation of the integral.

The minor difference between the results demonstrates that the Monte Carlo method can be effective for approximate calculation of definite integrals, especially when an analytical solution is difficult to find. However, it should be noted that the accuracy of the Monte Carlo method depends on the number of trials used, and it can be improved by increasing the number of trials.

## General Conclusion

Both tasks demonstrate the importance and effectiveness of applying numerical methods and linear programming in various fields. The results obtained using linear programming and the Monte Carlo method confirm their suitability for solving optimization tasks and calculating integrals, respectively.
