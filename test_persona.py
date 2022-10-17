import unittest
import person

class Test_Check_Occurrences(unittest.TestCase):

    def test_create_user_in_file(self):
        p = person.Persona(1, "Trump", "Donald")
        pers = p.store()
        self.assertFalse(pers)

    def test_create_user_not_in_file(self):
        p = person.Persona(2000, "Oliver", "Jamie")
        pers = p.store()
        self.assertTrue(pers)

    def test_check_if_exist(self):
        p = person.Persona(1, "Trump", "Donald")
        pers = p.check_if_exist()
        self.assertTrue(pers)

    def test_check_if_exist_not(self):
        p = person.Persona(2000, "Oliver", "Jamie")
        pers = p.check_if_exist()
        self.assertFalse(pers)

    def test_update(self):
        p = person.Persona(2, "example", "One")
        pers = p.update('apellido', 'nombre')
        self.assertTrue(pers)

    def test_delete(self):
        p = person.Persona(2, "example", "One")
        pers = p.delete(3)
        self.assertTrue(pers)



if __name__ == '__main__':
    unittest.main()
