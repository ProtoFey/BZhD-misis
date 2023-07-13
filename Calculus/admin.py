from django.contrib import admin
from Calculus.models import Task1, Task2, ResultTask1, ResultTask2


# Register your models here.
@admin.register(Task1)
class Task1Admin(admin.ModelAdmin):
    list_display = ('power', 'scheme', 'soil', 'climate_zone')
    fields = ('power', 'scheme', 'soil', 'climate_zone')
    readonly_fields = ('power', 'scheme', 'soil', 'climate_zone')


@admin.register(ResultTask1)
class ResultTask1Admin(admin.ModelAdmin):
    list_display = ('diameter', 'vertical_length', 'num_accurate', 'task')
    fields = (
        'task', 'diameter', 'num_accurate', 'vertical_length',
        'scheme', 'distance_between', 'section',
        'length', 'depth', 'total_resistance', 'normative_resistance'
    )

    readonly_fields = (
        'task', 'diameter', 'num_accurate', 'vertical_length', 'scheme', 'distance_between',
        'section', 'length', 'depth', 'total_resistance', 'normative_resistance'
    )


@admin.register(Task2)
class Task2Admin(admin.ModelAdmin):
    list_display = ('scheme', 'power', 'phase_material', 'type_electro')
    fields = (
        'scheme', 'length', 'power', 'phase_voltage',
        'phase_square', 'phase_material', 'distance_between_conductors',
        'amperage_nominal', 'type_electro'
    )
    readonly_fields = (
        'scheme', 'length', 'power', 'phase_voltage',
        'phase_square', 'phase_material', 'distance_between_conductors',
        'amperage_nominal', 'type_electro'
    )


@admin.register(ResultTask2)
class ResultTask2Admin(admin.ModelAdmin):
    list_display = ('square', 'task')
    fields = ('task', 'square')
    readonly_fields = ('task', 'square')
