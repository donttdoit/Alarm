import unittest
from alarm import Alarm


class TestAlarm(unittest.TestCase):

    def test_results(self):
        alarm = Alarm(15, 15, 1)

        alarm.set_hour(10)
        self.assertEqual(alarm.get_hour(), 10)

        alarm.set_type(1)
        self.assertEqual(alarm.get_type(), 1)

        alarm.set_minute(18)
        self.assertEqual(alarm.get_minute(), 18)


    def test_values(self):
        alarm = Alarm(15, 15, 1)

        with self.assertRaises(ValueError):
            alarm.set_hour(25)
            alarm.set_hour(-40)

            alarm.set_type(15)
            alarm.set_type(0)
            alarm.set_type(-2)

            alarm.set_minute(70)
            alarm.set_minute(-33)


    def test_types(self):
        alarm = Alarm(15, 15, 1)

        with self.assertRaises(TypeError):
            alarm.set_hour('1')
            alarm.set_hour([1, 2, 3])
            alarm.set_hour(True)

            alarm.set_type('hello')
            alarm.set_type(['a', 'b', 'c'])
            alarm.set_type(False)

            alarm.set_minute('string')
            alarm.set_minute([10, True, '15'])
            alarm.set_minute(False)








