""" module with testing flower module """
from unittest import TestCase
from unittest import main as unittest_run
import flower


class TestFlower(TestCase):
    def test_init(self):
        with self.assertRaises(ValueError):
            _ = flower.Flower('', 1., 1.)
        flower0 = flower.Flower('func', 10, 5)
        self.assertEqual(flower0.color, 'func', 'color not equal given val')
        self.assertEqual(flower0.petals, 10, 'petals not equal given val')
        self.assertEqual(flower0.price, 5, 'price not equal given val')

    def test_hash(self):
        flower0 = flower.Flower('green', 1, 1)
        self.assertIsInstance(hash(flower0), int)

    def test_check_color(self):
        with self.assertRaises(ValueError):
            _ = flower.Flower.check_color(1)
        color = flower.Flower.check_color('green')
        self.assertTrue(color == 'green')

    def test_check_number(self):
        with self.assertRaises(ValueError):
            _ = flower.Flower.check_number(12.)
        with self.assertRaises(ValueError):
            _ = flower.Flower.check_number(-2)
        num = flower.Flower.check_number(2)
        self.assertTrue(num == 2)

    def test_hash(self):
        flower_set = flower.FlowerSet()
        self.assertEqual(flower_set.flowers_set, set())
        flower_set.add_flower(flower.Flower('green', 1, 1))
        self.assertIsInstance(hash(flower_set), int)

    def test_add_flower(self):
        flower_set = flower.FlowerSet()
        with self.assertRaises(ValueError):
            flower_set.add_flower(12.)
        flower_set.add_flower(flower.Rose(1, 1))
        flower_set.add_flower(flower.Tulip(1, 1))
        flower_set.add_flower(flower.Rose(2, 4))
        self.assertEqual(len(flower_set.flowers_set), 3)

    @staticmethod
    def define_bucket():
        bucket = flower.Bucket()

        rose_set = flower.FlowerSet()
        rose_set.add_flower(flower.Rose(1, 1))
        rose_set.add_flower(flower.Rose(2, 1))
        bucket.add_set(rose_set)

        tulip_set = flower.FlowerSet()
        tulip_set.add_flower(flower.Tulip(1, 2))
        tulip_set.add_flower(flower.Tulip(2, 12))
        bucket.add_set(tulip_set)

        chamomile_set = flower.FlowerSet()
        chamomile_set.add_flower(flower.Chamomile(12, 14))
        bucket.add_set(chamomile_set)
        return bucket

    def test_add_set_and_init(self):
        bucket = flower.Bucket()
        self.assertEqual(bucket.set_of_flower_sets, set())
        self.assertEqual(bucket.prise, 0)
        with self.assertRaises(ValueError):
            bucket.add_set(12.)
        with self.assertRaises(ValueError):
            bucket.add_set(flower.Flower('aa', 1, 1))

        bucket = self.define_bucket()
        self.assertEqual(len(bucket.set_of_flower_sets), 3)

        with self.assertRaises(ValueError):
            bucket.add_set(12.)
        with self.assertRaises(ValueError):
            bucket.add_set(flower.Flower('aa', 1, 1))

    def test_total_price(self):
        bucket = flower.Bucket()
        self.assertEqual(bucket.total_price(), 0)
        bucket = self.define_bucket()
        self.assertEqual(bucket.total_price(), 30)


if __name__ == '__main__':
    unittest_run()
