import math

class LinearRegression():
    def __init__(self, x, y, n):
        self.x = x
        self.y = y
        self.n = n
    def get_multiply(self):
        multiply = []
        for i in range(0, self.n):
            multiply.append(self.x[i] * self.y [i])
        return multiply
    def get_pow_x(self):
        pow_x = []
        for i in range(0, self.n):
            pow_x.append(pow(self.x[i], 2))
        return pow_x
    def get_pow_y(self):
        pow_y = []
        for i in range(0, self.n):
            pow_y.append(pow(self.y[i], 2))
        return pow_y
    def get_sum_of_array(self, array):
        summatory = 0
        for i in range(0, len(array)):
            summatory += array[i]
        return summatory

    
annual_rent = [12, 15, 20, 25, 30]
holiday_spending = [1, 1.5, 2, 3, 4]
n_elements = 5

lr = LinearRegression(annual_rent, holiday_spending, n_elements)

summatory_x = lr.get_sum_of_array(annual_rent)
summatory_y = lr.get_sum_of_array(holiday_spending)

mean_x = summatory_x / n_elements
mean_y = summatory_y / n_elements
  
variance_x = math.sqrt((lr.get_sum_of_array(lr.get_pow_x())) / n_elements - pow(mean_x, 2))
variance_y = math.sqrt((lr.get_sum_of_array(lr.get_pow_y())) / n_elements - pow(mean_y, 2))

co_variance = ((lr.get_sum_of_array(lr.get_multiply())) / n_elements) - (mean_x * mean_y)

pearson_coefficient = co_variance / (variance_x * variance_y)

print("Covarianza: ", co_variance)
print("Coeficiente de Pearson: ", pearson_coefficient)

# Recta de regresión => y = mx + b
m = co_variance / pow(variance_x, 2)
print("Pediente: ", m)


# b = y - mx
b = mean_y - (m * mean_x)
print("Término independiente: ", b)

# x es la media de x
x = mean_x

y = m * x + b
print("La recta es: ", y)

# Coeficiente de correlación lineal 96% = 0.96 (Coeficiente de Pearson) {-1 a 1}
# Si la relación es directa (si aumenta X, aumenta Y). R será positiva
# Si la relación es directa (si aumenta X, disminuye Y). R será negativa
# Mientras más próxima esté a 1 o a -1, la recta se ajusta mejor a la nube de puntos
# * (Dependencia más fuerte)
