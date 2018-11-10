import unittest
class Treeit:
    def tree(self, string):
        return ""

class Lexer:
    input = ""
    def __init__(self, input):
        self.input = input

    def lex(self):
        for c in self.input:
            if (string.isl)
            



class Test_StringMsethods(unittest.TestCase):

    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)
    
    def test_simple_relation_parent(self):
        actual = Treeit().tree("a b")
        expected = """"a
|
b
"""
        self.assertEqual(actual, expected )

if __name__ == '__main__':
    unittest.main()