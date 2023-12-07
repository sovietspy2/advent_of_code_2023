import unittest

from task5 import GardenMap

class Task5Test(unittest.TestCase):

    def test_GardenMap_79(self):

        map = GardenMap()

        map.add_range(50, 98, 2)
        map.add_range(52, 50, 48)

        val = map.translate(79)

        self.assertEquals(val, 81)

    def test_GardenMap_14(self):

        map = GardenMap()

        map.add_range(50, 98, 2)
        map.add_range(52, 50, 48)

        val = map.translate(14)

        self.assertEquals(val, 14)

    def test_GardenMap_55(self):

        map = GardenMap()

        map.add_range(50, 98, 2)
        map.add_range(52, 50, 48)

        val = map.translate(55)

        self.assertEquals(val, 57)


if __name__ == "__main__":
    unittest.main()