import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
    def test_add_20_dvds_success(self):
        cart = Cart()

        for i in range(20):
            dvd = DigitalVideoDisc(f"DVD {i}")
            self.assertTrue(cart.add_dvd(dvd))

        self.assertEqual(len(cart.items), 20)

    def test_reject_21st_dvd(self):
        cart = Cart()

        for i in range(20):
            dvd = DigitalVideoDisc(f"DVD {i}")
            cart.add_dvd(dvd)

        dvd_21 = DigitalVideoDisc("DVD 21")
        self.assertFalse(cart.add_dvd(dvd_21))


if __name__ == "__main__":
    unittest.main()