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
