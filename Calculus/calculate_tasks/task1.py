import math


class TaskCalculus:
    SOILS = {1: 'чернозем', 2: 'супесок', 3: 'песок', 4: 'суглинок', 5: 'глина'}
    SCHEMES = {0: 'в ряд', 1: 'по контуру'}

    SOILS_RESISTANCE = {'глина': 40, 'суглинок': 100, 'чернозем': 200, 'супесок': 300, 'песок': 700}
    CLIMATE_ZONES_VERTICAL_ODDS = {1: (2.0, 7.0), 2: (1.8, 4.5), 3: (1.6, 2.5), 4: (1.4, 2.0)}

    CONDUCTOR_USAGE_IN_A_ROW_ODDS = {2: 0.91, 4: 0.83, 6: 0.77, 10: 0.74, 20: 0.67}
    CONDUCTOR_USAGE_BY_THE_CONTOUR_ODDS = {4: 0.85, 6: 0.8, 10: 0.76, 20: 0.71, 40: 0.66, 60: 0.64, 100: 0.62}

    def __init__(self, power: int, climate_zone: int, soil_index: int, scheme_index: int) -> None:
        # User input
        self.power: int = power
        self.climate_zone: int = climate_zone
        self.soil: str = self.SOILS[soil_index]
        self.scheme: str = self.SCHEMES[scheme_index]

        # Tasks variables
        self.diameter = 0.03
        self.length = 3
        self.width = 0.04
        self.normative_resistance = None
        self.vertical_soil_resistance = None
        self.horizontal_soil_resistance = None
        self.resistance_single_vertical_conductor = None
        self.num_vertical_conductors = None
        self.distance_between = None
        self.number_of_vertical_conductors = None
        self.conductors_resistance = None
        self.resistance_band = None
        self.length_band = None
        self.resistance = None

    def step_one(self):
        self.normative_resistance = 10 if self.power <= 100 else 4

    def step_two(self):
        vertical_odd = self.CLIMATE_ZONES_VERTICAL_ODDS[self.climate_zone][0]
        horizontal_odd = self.CLIMATE_ZONES_VERTICAL_ODDS[self.climate_zone][1]
        self.vertical_soil_resistance = self.SOILS_RESISTANCE[self.soil] * vertical_odd
        self.horizontal_soil_resistance = self.SOILS_RESISTANCE[self.soil] * horizontal_odd

    def step_three(self):
        H = 0.8 + (self.length / 2)
        first_multiplier = self.vertical_soil_resistance / (2 * 3.14 * 3)
        second_multiplier = math.log((2 * self.length) / self.diameter) + 0.5 * math.log(
            (4 * H + self.length) / (4 * H - self.length))
        self.resistance_single_vertical_conductor = round(first_multiplier * second_multiplier, 2)

    def step_four(self):
        self.num_vertical_conductors = round(self.resistance_single_vertical_conductor / self.normative_resistance)

    def step_five(self):
        if self.scheme == 'в ряд':
            self.distance_between = self.length * 2
            odd = round(0.9927 * math.pow(self.num_vertical_conductors,
                                    -0.132) if self.num_vertical_conductors not in self.CONDUCTOR_USAGE_IN_A_ROW_ODDS else \
            self.CONDUCTOR_USAGE_IN_A_ROW_ODDS[self.num_vertical_conductors], 2)
        else:
            self.distance_between = self.length * 3
            odd = round(0.9585 * math.pow(self.num_vertical_conductors,
                                    -0.098) if self.num_vertical_conductors not in self.CONDUCTOR_USAGE_BY_THE_CONTOUR_ODDS else \
            self.CONDUCTOR_USAGE_BY_THE_CONTOUR_ODDS[self.num_vertical_conductors], 2)

        self.number_of_vertical_conductors = math.ceil(self.num_vertical_conductors / odd)
        self.conductors_resistance = round(
            self.resistance_single_vertical_conductor / (self.number_of_vertical_conductors * odd), 2)

    def step_six(self):
        self.length_band = 1.05 * (self.number_of_vertical_conductors - 1) * self.distance_between
        first_multiplier = self.horizontal_soil_resistance / (2 * 3.14 * self.length_band)
        second_multiplier = math.log((2 * math.pow(self.length_band, 2)) / (0.8 * self.width))
        self.resistance_band = round(first_multiplier * second_multiplier, 2)

        if self.scheme == 'в ряд':
            odd = round(-0.0209 * self.number_of_vertical_conductors + 0.9718, 1)
        else:
            odd = round(0.9701 * math.pow(self.number_of_vertical_conductors, -0.242), 1)

        if odd:
            self.resistance_band = round(self.resistance_band / odd)

        self.resistance = round(
            (self.conductors_resistance * self.resistance_band) / (self.conductors_resistance + self.resistance_band),
            2)

    def answer(self):
        return self.diameter * 1000, self.length, self.number_of_vertical_conductors, self.scheme, self.distance_between, self.width * 1000, self.length_band, 0.8, self.resistance, self.normative_resistance

    def __call__(self, *args, **kwargs):
        self.step_one()
        self.step_two()
        self.step_three()
        self.step_four()
        self.step_five()
        self.step_six()
        return self.answer()


if __name__ == '__main__':
    task1 = TaskCalculus(100, 3, 1, 0)
    print(task1())
