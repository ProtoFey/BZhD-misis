from unittest import TestCase
from task1 import TaskCalculus
from task2 import Task2Calculus


class TaskTest(TestCase):

    def test_task1(self):
        task_v1 = TaskCalculus(100, 3, 1, 0)
        results_v1 = task_v1()
        task_v2 = TaskCalculus(630, 1, 2, 1)
        results_v2 = task_v2()
        task_v3 = TaskCalculus(40, 4, 3, 1)
        results_v3 = task_v3()
        task_v4 = TaskCalculus(63, 3, 4, 1)
        results_v4 = task_v4()
        task_v5 = TaskCalculus(250, 2, 5, 0)
        results_v5 = task_v5()
        self.assertEqual((14, 6, 81.9, 6), (results_v1[2], int(results_v1[4]), round(results_v1[6], 1), int(results_v1[8])))
        self.assertEqual((69, 9, 642.6, 3.5), (results_v2[2], int(results_v2[4]), round(results_v2[6], 1), round(results_v2[8], 1)))
        self.assertEqual((43, 9, 396.9, 7.0), (results_v3[2], int(results_v3[4]), round(results_v3[6], 1), round(results_v3[8])))
        self.assertEqual((7, 9, 56.7, 5.0), (results_v4[2], int(results_v4[4]), round(results_v4[6], 1), round(results_v4[8])))
        self.assertEqual((7, 6, 37.8, 3), (results_v5[2], int(results_v5[4]), round(results_v5[6], 1), round(results_v5[8])))

    def test_task2(self):
        task_v1 = Task2Calculus(3, 1, 450, 1, 10, 0.5, 40, 1)
        task_v2 = Task2Calculus(2, 1, 250, 2, 15, 0.3, 40, 1)
        task_v3 = Task2Calculus(2, 2, 375, 1, 8, 0.4, 40, 2)
        task_v4 = Task2Calculus(1, 1, 200, 2, 12, 0.7, 80, 1)
        task_v5 = Task2Calculus(4, 1, 100, 2, 20, 0.2, 125, 1)

        self.assertEqual(120, task_v1())
        self.assertEqual(-100, task_v2())
        self.assertEqual(300, task_v3())
        self.assertEqual(200, task_v4())
        self.assertEqual(-100, task_v5())
