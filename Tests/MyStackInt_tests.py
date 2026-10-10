from Classes.MyStackInt import MyStackInt
from unittest import TestCase, main


class TestMyStackInt(TestCase):

    def setUp(self):
        self.stack = MyStackInt()

    def test_empty_stack(self):
        self.assertTrue(self.stack.is_empty())

        self.stack.push(10)

        self.assertFalse(self.stack.is_empty())

    def test_push(self):
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(5)

        self.assertEqual(self.stack.stack, [10, 20, 5])

    def test_pop(self):
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(5)

        self.assertEqual(self.stack.pop(), 5)
        self.assertEqual(self.stack.pop(), 20)
        self.assertEqual(self.stack.pop(), 10)

        self.assertTrue(self.stack.is_empty())

    def test_max(self):
        self.stack.push(10)
        self.assertEqual(self.stack.max(), 10)

        self.stack.push(20)
        self.assertEqual(self.stack.max(), 20)

        self.stack.push(5)
        self.assertEqual(self.stack.max(), 20)

        self.stack.push(30)
        self.assertEqual(self.stack.max(), 30)

    def test_max_after_pop(self):
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(5)
        self.stack.push(30)

        self.assertEqual(self.stack.max(), 30)

        self.stack.pop()
        self.assertEqual(self.stack.max(), 20)

        self.stack.pop()
        self.assertEqual(self.stack.max(), 20)

        self.stack.pop()
        self.assertEqual(self.stack.max(), 10)

    def test_duplicate_max(self):
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(20)
        self.stack.push(5)

        self.assertEqual(self.stack.max(), 20)

        self.stack.pop()
        self.assertEqual(self.stack.max(), 20)

        self.stack.pop()
        self.assertEqual(self.stack.max(), 20)

        self.stack.pop()
        self.assertEqual(self.stack.max(), 10)

    def test_negative_numbers(self):
        self.stack.push(-10)
        self.stack.push(-5)
        self.stack.push(-20)

        self.assertEqual(self.stack.max(), -5)

        self.stack.pop()
        self.assertEqual(self.stack.max(), -5)

        self.stack.pop()
        self.assertEqual(self.stack.max(), -10)

    def test_pop_empty_stack(self):
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_max_empty_stack(self):
        with self.assertRaises(IndexError):
            self.stack.max()

    def test_empty_after_pop(self):
        self.stack.push(10)
        self.stack.pop()

        self.assertTrue(self.stack.is_empty())

        with self.assertRaises(IndexError):
            self.stack.max()

        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_push_after_emptying(self):
        self.stack.push(20)
        self.stack.pop()

        self.stack.push(5)
        self.stack.push(15)

        self.assertEqual(self.stack.max(), 15)
        self.assertEqual(self.stack.pop(), 15)
        self.assertEqual(self.stack.max(), 5)


if __name__ == "__main__":
    main()