import unittest
from Funct import writetofile, check, checkau

class TestCase(unittest.TestCase):
    def test_checklogindtata(self):
        data = {"log": "123"}
        self.assertTrue(check(data, "log"))
        self.assertFalse(check(data, "login"))

    def test_write_to_file(self):
        log = "sim"
        pas = "salabim"
        data = {}
        writetofile(log, pas)
        with open("Bd.txt", "r") as file:
            for line in file:
                key, *value = line.split()
                data[key] = value
        self.assertIn(log, data)
        val = data[log][0]
        self.assertEqual(val, pas)

    def test_check_auntification(self):
        log = "123"
        pas = "123"
        data = {log: [pas]}
        self.assertEqual(checkau(data,log,pas), 'Авторизация выполнена успешно')
        self.assertNotEqual(checkau(data,log,pas), 'Пароль введён неверно')

if __name__ == '__main__':
    unittest.main()