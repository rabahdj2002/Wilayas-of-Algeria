import unittest
import wilayati

class TestSearch(unittest.TestCase):
    def test_searchByCode(self):
        """
        Test the searchByCode method of Search.
        """
        obj = wilayati.handler()
        self.assertEqual(obj.searchByCode(wilayaCode=25)['name'], "Constantine")
    
    def test_searchByName(self):
        """
        Test the searchByName method of Search.
        """
        obj = wilayati.handler()
        self.assertEqual(obj.searchByName(name="Naama")['code'], '45')

    def test_getBaladiyat(self):
        """
        Test the getBaladiyat method of Search.
        """
        obj = wilayati.handler()
        self.assertEqual(len(obj.getBaladiyat(wilayaCode=25)), 12)

    def test_searchBaladiya(self):
        """
        Test the searchBaladiya method of Search.
        """
        obj = wilayati.handler()
        self.assertEqual(obj.searchBaladiya(baladiyaName="hamma bo")['name'], "Hamma Bouziane")

if __name__ == '__main__':
    unittest.main()