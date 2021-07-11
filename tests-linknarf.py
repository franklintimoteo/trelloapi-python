import unittest
from tibiatool_linknarf import request_highscores

class Testtibiatool(unittest.TestCase):
    
    hash_request = []    

    def test_request_highscores(self):
        """Test invalid type world argument"""
        result = 0
        with self.assertRaises(TypeError):
            result = request_highscores(1313)
        self.hash_request.append(str(id(result)))
        

    def test_error_world_category_vocation_notexists(self):
        "Test world not exists"
        result = request_highscores('men')
        self.hash_request.append(str(id(result)))


    def test_hash_request(self):
        "Check if only one request been generated"
        self.assertEqual(len(self.hash_request), 1)



if __name__ == "__main__":
    unittest.main(verbosity=2)