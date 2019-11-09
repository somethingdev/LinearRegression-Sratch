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
