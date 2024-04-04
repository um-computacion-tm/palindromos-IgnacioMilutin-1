import unittest

def is_palindrome(value):
    print(value)
    print(value[::-1])
    if value == value[::-1]:
        return True
    else:
        return False

#Otras opciones:

#def is_palindrome(value):
#    prin=0
#    fin=len(value)-1
#    while prin!=fin:
#        if value[prin]==value[fin]:
#            prin+=1
#            fin-=1
#            return True
#        else: False


#    for indice in range(len(value)):
#         reverse = -(indice + 1)
#         if value [indice] != value[reverse]:
#             return False



class TestIsPalindrome(unittest.TestCase):
    def test_with_a(self):
        input = "a"
        result = is_palindrome(input)
        self.assertTrue(result)

    def test_with_ala(self):
        input = "ala"
        result = is_palindrome(input)
        self.assertTrue(result)

    def test_with_neuquen(self):
        input = "neuquen"
        result = is_palindrome(input)
        self.assertTrue(result)

    def test_with_hola(self):
        input = "hola"
        result = is_palindrome(input)
        self.assertFalse(result)


unittest.main()