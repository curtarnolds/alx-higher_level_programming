import unittest
from unittest.mock import patch
from models.base import Base


class TestBase(unittest.TestCase):

    def setUp(self):
        self.base = Base()

    def test_init_with_id(self):
        base = Base(1)
        self.assertEqual(base.id, 1)

    def test_init_without_id(self):
        self.assertEqual(self.base.id, 1)

    def test_to_json_string_empty_list(self):
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_non_empty_list(self):
        result = Base.to_json_string([{"key": "value"}])
        self.assertEqual(result, '[{"key": "value"}]')

    def test_save_to_file(self):
        with patch('builtins.open') as mock_file:
            self.base.save_to_file([self.base])
            mock_file.assert_called_once_with('Base.json', mode='w')
            mock_file.return_value.write.assert_called_once()

    def test_from_json_string_empty_string(self):
        result = Base.from_json_string('')
        self.assertEqual(result, [])

    def test_from_json_string_non_empty_string(self):
        result = Base.from_json_string('[{"key": "value"}]')
        self.assertEqual(result, [{"key": "value"}])

    def test_create(self):
        dummy_dict = {'key': 'value'}
        result = Base.create(**dummy_dict)
        self.assertEqual(result.key, 'value')

    @patch('builtins.open')
    def test_load_from_file(self, mock_file):
        mock_file.return_value.__enter__.return_value.read.return_value =\
            '[{"key": "value"}]'
        result = Base.load_from_file()
        self.assertEqual(result[0].key, 'value')

    @patch('builtins.open')
    def test_load_from_file_csv(self, mock_file):
        mock_file.return_value.__enter__.return_value.__next__.return_value = [
            'key']
        mock_file.return_value.__enter__.return_value.__iter__.return_value = [
            ['value']]
        result = Base.load_from_file_csv()
        self.assertEqual(result[0].key, 'value')

    @patch('builtins.open')
    def test_save_to_file_csv(self, mock_file):
        with patch('csv.writer') as mock_writer:
            self.base.save_to_file_csv([self.base])
            mock_file.assert_called_once_with('Base.csv', 'wt')
            mock_writer.return_value.writerow.assert_called_once()


if __name__ == '__main__':
    unittest.main()
