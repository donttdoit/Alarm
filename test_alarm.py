import unittest
from alarm import Alarm


class TestAlarm(unittest.TestCase):

    def test_results(self):
        alarm = Alarm(15, 15, 1)

        alarm.set_hour(10)
        self.assertEqual(alarm.get_hour(), 10)


    def test_values(self):
        alarm = Alarm(15, 15, 1)

        with self.assertRaises(ValueError):
            alarm.set_hour(25)
            alarm.set_hour(-40)


    def test_types(self):
        alarm = Alarm(15, 15, 1)

        with self.assertRaises(TypeError):
            alarm.set_hour('1')
            alarm.set_hour([1, 2, 3])
            alarm.set_hour(True)







