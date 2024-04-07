import unittest
import py_compile

class TestSyntax(unittest.TestCase):
    def test_syntax(self):
        # Путь к файлу с вашим кодом
        file_path = '/bus_stops_service/main.py'
        
        # Компиляция файла
        compile_result = py_compile.compile(file_path, doraise=False)
        
        # Проверка наличия синтаксических ошибок
        self.assertFalse(compile_result, f"Syntax error found in {file_path}")

if __name__ == '__main__':
    unittest.main()
