from django.test import TestCase
from http import HTTPStatus

from Calculus.calculate_tasks.task2 import Task2Calculus
from Calculus.models import Task1, ResultTask1, Task2, ResultTask2
from Calculus.calculate_tasks.task1 import TaskCalculus
from django.urls import reverse


# Create your tests here.
class TestCalculus(TestCase):

    def test_index(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertIn('Проектировка защитного заземление', response.content.decode())
        self.assertIn('Подборка площади сечения нулевого провода', response.content.decode())

    def test_task1(self):
        response = self.client.get('/task1/')
        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertIn(
            'Определить параметры заземляющего устройства', response.content.decode()
        )
        self.assertIn(
            'Спроектировать защитное заземление оборудования лаборатории', response.content.decode()
        )

    def test_task2(self):
        response = self.client.get('/task2/')
        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertIn(
            'Цель расчета зануления – определить сечение защитного нулевого провода', response.content.decode()
        )

        self.assertIn(
            'Подобрать площадь сечения нулевого провода', response.content.decode()
        )

    def test_info(self):
        response = self.client.get('/info-task1/')
        self.assertEquals(response.status_code, HTTPStatus.OK)

    def test_about_team(self):
        response = self.client.get('/about_team/')
        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertIn('Состав команды', response.content.decode())

    def test_targets(self):
        response = self.client.get('/targets/')
        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertIn('Цели проекта', response.content.decode())

    def test_result1(self):
        task1 = Task1(power=100, climate_zone=3, soil=1, scheme=0)
        task1.save()
        result = TaskCalculus(power=task1.power, climate_zone=task1.climate_zone, soil_index=task1.soil,
                              scheme_index=task1.scheme)
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
        response = self.client.get(reverse('main:result1', args=(task1.id, )))
        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertEquals(1, task1.id)
        self.assertEqual(30, result1.diameter)
        self.assertEqual(14, result1.num_accurate)
        self.assertEqual(6.0, result1.distance_between)
        self.assertEqual(81.9, result1.length)
        self.assertEqual(0.8, result1.depth)
        self.assertEqual(6.11, result1.total_resistance)
        self.assertEqual(10, result1.normative_resistance)
        self.assertIn('Результат', response.content.decode())

    def test_result2(self):
        task2 = Task2(
            scheme=1,
            power=3,
            length=450,
            phase_material=1,
            phase_square=10,
            distance_between_conductors=0.5,
            amperage_nominal=40,
            type_electro=1,
            phase_voltage=220
        )
        task2.save()

        result = Task2Calculus(
            task2.power,
            task2.scheme,
            task2.length,
            task2.phase_material,
            task2.phase_square,
            task2.distance_between_conductors,
            task2.amperage_nominal,
            task2.type_electro
        )

        result2 = ResultTask2(
            task=task2,
            square=result()
        )
        result2.save()
        response = self.client.get(reverse('main:result2', args=(task2.id,)))
        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertEquals(1, task2.id)
        self.assertEquals(120, result2.square)
        self.assertIn('Результат', response.content.decode())
