from django.db import models


class Task1(models.Model):
    # SCHEMES
    IN_A_ROW = 0
    ALONG_THE_CONTOUR = 1

    # ZONES
    FIRST_ZONE = 1
    SECOND_ZONE = 2
    THIRD_ZONE = 3
    FOURTH_ZONE = 4

    # SOILS
    BLACK_SOIL = 1
    SANDY_LOAM = 2
    SAND = 3
    LOAM = 4
    CLAY = 5

    SCHEMES = (
        (IN_A_ROW, 'в ряд'),
        (ALONG_THE_CONTOUR, 'по контуру'),
    )

    ZONES = (
        (FIRST_ZONE, 'первой'),
        (SECOND_ZONE, 'второй'),
        (THIRD_ZONE, 'третьей'),
        (FOURTH_ZONE, 'четвертой'),
    )

    SOILS = (
        (BLACK_SOIL, 'чернозем'),
        (SANDY_LOAM, 'супесок'),
        (SAND, 'песок'),
        (LOAM, 'суглинок'),
        (CLAY, 'глина'),
    )

    power = models.PositiveSmallIntegerField()
    scheme = models.PositiveSmallIntegerField(choices=SCHEMES)
    soil = models.PositiveSmallIntegerField(choices=SOILS)
    climate_zone = models.PositiveSmallIntegerField(choices=ZONES)

    def __str__(self):
        return f'power: {self.power} | scheme: {self.get_scheme_display()} | soil: {self.get_soil_display()} | ' \
               f'climate_zone: {self.get_climate_zone_display()}'

    class Meta:
        verbose_name = 'First Task'
        verbose_name_plural = 'First Tasks'


class ResultTask1(models.Model):
    task = models.ForeignKey(to=Task1, on_delete=models.CASCADE)
    diameter = models.FloatField()
    vertical_length = models.FloatField()
    num_accurate = models.FloatField()
    scheme = models.CharField(max_length=32)
    distance_between = models.FloatField()
    section = models.FloatField()
    length = models.FloatField()
    depth = models.FloatField()
    total_resistance = models.FloatField()
    normative_resistance = models.FloatField()

    class Meta:
        verbose_name = 'Result from first Task'
        verbose_name_plural = 'results from first Tasks'


class Task2(models.Model):
    # SCHEMES

    STAR_STAR = 1
    STAR_DELTA = 2

    # Materials
    AL = 1
    CU = 2

    # TYPES
    AB = 1
    P = 2

    # POWERS
    POWER_40 = 1
    POWER_63 = 2
    POWER_400 = 3
    POWER_630 = 4

    SCHEMES = (
        (STAR_STAR, 'Y/Yн'),
        (STAR_DELTA, 'Δ/Yн'),
    )

    MATERIALS = (
        (AL, 'алюминий'),
        (CU, 'медь')
    )

    TYPES = (
        (AB, 'AB'),
        (P, 'П'),
    )

    POWERS = (
        (POWER_40, 40),
        (POWER_63, 63),
        (POWER_400, 400),
        (POWER_630, 630),
    )

    scheme = models.PositiveSmallIntegerField(choices=SCHEMES)
    length = models.IntegerField()
    power = models.PositiveSmallIntegerField(choices=POWERS)
    phase_voltage = models.IntegerField()
    phase_square = models.IntegerField()
    phase_material = models.PositiveSmallIntegerField(choices=MATERIALS)
    distance_between_conductors = models.FloatField()
    amperage_nominal = models.IntegerField()
    type_electro = models.PositiveSmallIntegerField(choices=TYPES)

    def __str__(self):
        return f'scheme: {self.get_scheme_display()} | length: {self.length} | power: {self.get_power_display()} ' \
               f'| phase_voltage: {self.phase_voltage} | phase_square: {self.phase_square} |' \
               f' phase_material: {self.get_phase_material_display()} | distance_between_conductors: {self.distance_between_conductors} |' \
               f' amperage_nominal: {self.amperage_nominal} | type_electro: {self.get_type_electro_display()}'

    class Meta:
        verbose_name = 'Second Task'
        verbose_name_plural = 'Second Tasks'


class ResultTask2(models.Model):
    task = models.ForeignKey(to=Task2, on_delete=models.CASCADE)
    square = models.FloatField()

    class Meta:
        verbose_name = 'Result from second Task'
        verbose_name_plural = 'results from second Tasks'
