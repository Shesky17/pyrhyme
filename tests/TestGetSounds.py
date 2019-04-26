import unittest

from rhymes import RhymingDictionary

class TestGetSounds(unittest.TestCase):
    def setUp(self):
        pass

    def testGetSounds(self):
        input_list = ["PHOTOGRAPH", "AND", "adfsafsadf", "AND"]
        output_list = [["F", "OW1", "T", "AH0", "G", "R", "AE2", "F"], ["AH0", "N", "D"], [], ["AH0", "N", "D", "Z"]]
        valid = [True, True, True, False]
        for index in range(0, len(input_list)):
            self.assertTrue((RhymingDictionary.get_sounds("../data/cmudict-0.7b", input_list[index]) == output_list[index]) == valid[index])


if __name__ == '__main__':
    unittest.main()