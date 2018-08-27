import unittest
from patternCount import patternCount, frequentWords

class UtilitiesTestCase(unittest.TestCase):
    pass

class PatternCountTestCase(unittest.TestCase):

    def test_patternCount(self):
        self.text_ = "GCGCG"
        self.pattern_ = "GCG"
        self.assertEqual(patternCount(self.text_, self.pattern_), 2,
                         msg=patternCount(self.text_, self.pattern_))


class FrequentWordsTestCase(unittest.TestCase):

    def test_frequentWords(self):
        self.text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
        self.kmerSize = 4
        self.assertEqual(frequentWords(self.text, self.kmerSize), "\t".join(["CATG", "GCAT"]))


if __name__ == "__main__":
    unittest.main()
