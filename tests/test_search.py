import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category


class TestSearchByCategory(unittest.TestCase):
    def test_search_by_category(self):
        dvd1 = DigitalVideoDisc("The Lion King", "Animation")
        dvd2 = DigitalVideoDisc("Titanic", "Romance")
        dvd3 = DigitalVideoDisc("Frozen", "Animation")

        result = search_by_category([dvd1, dvd2, dvd3], "Animation")

        self.assertEqual(len(result), 2)
        self.assertIn(dvd1, result)
        self.assertIn(dvd3, result)


if __name__ == "__main__":
    unittest.main()