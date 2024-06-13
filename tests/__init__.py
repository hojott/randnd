import unittest

import randnd


class TestGenderRandomizer(unittest.TestCase):
    def test_randomizer(self):
        r = randnd.randomizer.Randomizer()
        r.generate_gender()
        self.assertIn(str(r.character.gender), ["male", "female", "nonbinary"])


class TestClass(unittest.TestCase):
    def test_class_instance(self):
        cclass = randnd.data.functions.get_class("fighter")
        self.assertIsInstance(cclass, randnd.data.classes.Class)

    def test_class_equal(self):
        c1 = randnd.data.functions.get_class("fighter")
        c2 = randnd.data.functions.get_class("fighter")
        self.assertEqual(str(c1), str(c2))


class TestBackground(unittest.TestCase):
    def test_background_instance(self):
        background = randnd.data.functions.get_background("soldier")
        self.assertIsInstance(background, randnd.data.classes.Background)

    def test_class_equal(self):
        b1 = randnd.data.functions.get_background("soldier")
        b2 = randnd.data.functions.get_background("soldier")
        self.assertEqual(str(b1), str(b2))


class TestGender(unittest.TestCase):
    def test_gender_instance(self):
        gender = randnd.data.functions.get_gender("male")
        self.assertIsInstance(gender, randnd.data.classes.Gender)

    def test_gender_equal(self):
        g1 = randnd.data.functions.get_gender("male")
        g2 = randnd.data.functions.get_gender("male")
        self.assertEqual(str(g1), str(g2))


class TestGenderTable(unittest.TestCase):
    def test_gender_table(self):
        table = randnd.data.functions.get_gender_table()
        self.assertIsInstance(table, dict)

    def test_gender_male(self):
        table = randnd.data.functions.get_gender_table()
        self.assertEqual(str(table[1]), "male")


if __name__ == "__main__":
    unittest.main()
