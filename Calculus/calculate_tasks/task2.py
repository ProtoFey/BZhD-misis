import math


class Task2Calculus:
    SCHEMES = {1: 'звезда-звезда', 2: 'не звезда-звезда'}
    MATERIALS = {1: 'алюминий', 2: 'медь'}
    POWERS = {1: 40, 2: 63, 3: 400, 4: 630}

    RESISTANCES = {40: (1.950, 0.562), 63: (1.240, 0.360), 400: (0.195, 0.056), 630: (0.129, 0.042)}

    In = {
        0.5: {80: (5.24, 3.14), 120: (3.66, 2.2), 150: (3.38, 2.03), 160: (2.8, 1.68),
              200: (2.28, 1.37), 250: (2.1, 1.26), 300: (1.77, 1.06)},
        1: {80: (4.2, 2.52), 120: (2.91, 1.75), 150: (2.56, 1.54), 160: (2.24, 1.34),
            200: (1.79, 1.07), 250: (1.60, 0.96), 300: (1.34, 0.8)},
        1.5: {80: (3.48, 2.09), 120: (2.38, 1.43), 150: (2.08, 1.25), 160: (1.81, 1.09), 200: (1.45, 0.87),
              250: (1.28, 0.77), 300: (1.08, 0.65)},
        2: {80: (2.97, 1.78), 120: (2.04, 1.22), 150: (1.6, 0.98), 160: (1.54, 0.92), 200: (1.24, 0.74)}
    }

    def __init__(self, power_key: int, scheme_key: int, length: int, phase_material_id: int, phase_quantity: int,
                 diameter: int, tok_power: int, type_electro):
        # User input
        self.power = self.POWERS[power_key]
        self.scheme = self.SCHEMES[scheme_key]
        self.length = length
        self.material = self.MATERIALS[phase_material_id]
        self.material_quantity = phase_quantity
        self.diameter = diameter
        self.tok_power = tok_power
        self.voltage = 220
        self.type_electro = type_electro

        # Tasks variables
        self.Z = None
        self.tok = None
        self.current_density = None
        self.Ri = None
        self.Xi = None
        self.Rn = None
        self.Xn = None
        self.Rf = None
        self.Zn = None
        self.Zf = None
        self.d = None
        self.Xp = None
        self.Zp = None
        self.Ii = None
        self.Ln = None

    def step_one(self):
        if self.scheme == 'звезда-звезда':
            self.Z = self.RESISTANCES[self.power][0]
        else:
            self.Z = self.RESISTANCES[self.power][1]

    def step_two(self):
        if self.type_electro == 1 and self.tok_power < 100:
            self.tok = round(self.tok_power * 1.4, 2)
        elif self.type_electro == 1:
            self.tok = round(self.tok_power * 1.25, 2)
        else:
            self.tok = round(self.tok_power * 3, 2)

    def step_three(self, Ln):
        self.current_density = self.tok / Ln

        if self.current_density < 1:
            self.current_density = 0.5
        elif self.current_density < 1.5:
            self.current_density = 1
        else:
            self.current_density = 1.5

        self.Ri = self.In[self.current_density][Ln][0]
        self.Xi = self.In[self.current_density][Ln][1]

    def step_four(self):
        self.Rn = round(self.Ri * (self.length / 1000), 3)
        self.Xn = round(self.Xi * (self.length / 1000), 3)

    def step_five(self):
        if self.material == 'алюминий':
            self.Rf = round((0.028 * self.length) / self.material_quantity, 3)
        else:
            self.Rf = round((0.018 * self.length) / self.material_quantity, 3)

    def step_six(self):
        self.Zn = round(math.sqrt(math.pow(self.Rn, 2) + math.pow(self.Xn, 2)), 3)
        self.Zf = self.Rf

    def step_seven(self):
        return self.Zn <= 2 * self.Zf

    def step_eight(self):
        odd = self.material_quantity / 3.14
        self.d = round(2 * math.sqrt(odd), 2)
        self.Xp = round(0.1256 * (self.length / 1000) * math.log(2 * self.diameter / (self.d * 10 ** -6)), 3)

    def step_nine(self):
        self.Zp = round(math.sqrt(math.pow(self.Rf + self.Rn, 2) + math.pow(0 + self.Xn + self.Xp, 2)), 2)

    def step_ten(self):
        self.Ii = round(220 / (self.Z / 3 + self.Zp), 1)

    def step_eleven(self):
        return self.Ii >= self.tok

    def __call__(self, *args, **kwargs):
        keys = (80, 120, 150, 160, 200, 250, 300)

        self.step_one()
        self.step_two()

        for self.Ln in keys:

            self.step_three(self.Ln)
            self.step_four()
            self.step_five()
            self.step_six()

            if not self.step_seven():
                if self.Ln == 300:
                    return -100
                continue

            self.step_eight()
            self.step_nine()
            self.step_ten()

            if self.step_eleven():
                if self.Ln == 300:
                    return -100
                break

        return self.Ln


if __name__ == '__main__':
    task2 = Task2Calculus(2, 1, 250, 2, 15, 0.3, 40, 2)
    print(task2())
