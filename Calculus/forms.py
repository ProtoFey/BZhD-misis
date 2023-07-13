from django import forms
from Calculus.models import Task1, ResultTask1, Task2, ResultTask2
from Calculus.calculate_tasks.task1 import TaskCalculus
from Calculus.calculate_tasks.task2 import Task2Calculus


class Task1Form(forms.ModelForm):
    power = forms.IntegerField(min_value=1)
    scheme = forms.CharField(widget=forms.Select(choices=Task1.SCHEMES))
    climate_zone = forms.CharField(widget=forms.Select(choices=Task1.ZONES))
    soil = forms.CharField(widget=forms.Select(choices=Task1.SOILS))

    def save(self, commit=True):
        task1 = super().save(commit=True)
        result = TaskCalculus(task1.power, task1.climate_zone, task1.soil, task1.scheme)
        diameter, length, number_of_vertical_conductors, scheme, distance_between, width, length_band, depth, resistance, normative_resistance = result()

        result1 = ResultTask1(
            task=task1,
            diameter=diameter,
            vertical_length=length,
            num_accurate=number_of_vertical_conductors,
            scheme=scheme,
            distance_between=distance_between,
            section=width,
            length=length_band,
            depth=depth,
            total_resistance=resistance,
            normative_resistance=normative_resistance,
        )
        result1.save()
        return task1

    class Meta:
        model = Task1
        fields = ('power', 'scheme', 'climate_zone', 'soil')


class Task2Form(forms.ModelForm):
    scheme = forms.CharField(widget=forms.Select(choices=Task2.SCHEMES))
    length = forms.IntegerField(min_value=1)
    power = forms.IntegerField(widget=forms.Select(choices=Task2.POWERS))
    phase_voltage = forms.IntegerField(min_value=1)
    phase_square = forms.IntegerField(min_value=1)
    phase_material = forms.CharField(widget=forms.Select(choices=Task2.MATERIALS))
    distance_between_conductors = forms.FloatField(min_value=0.0)
    amperage_nominal = forms.IntegerField(min_value=1)
    type_electro = forms.CharField(widget=forms.Select(choices=Task2.TYPES))

    def save(self, commit=True):
        task2 = super().save(commit=True)
        result2 = Task2Calculus(
            power_key=task2.power,
            scheme_key=task2.scheme,
            length=task2.length,
            phase_material_id=task2.phase_material,
            phase_quantity=task2.phase_square,
            diameter=task2.distance_between_conductors,
            tok_power=task2.amperage_nominal
        )
        result2 = ResultTask2(task=task2, square=result2())
        result2.save()
        return task2

    class Meta:
        model = Task2
        fields = ('scheme', 'length', 'power', 'phase_voltage', 'phase_square', 'phase_material',
                  'distance_between_conductors', 'amperage_nominal', 'type_electro')
