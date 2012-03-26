import unittest
from sb_highlighter import *

class TestHighlightFunctions(unittest.TestCase):

    def test_correct_answer_full_query(self):
        print "Test Full Query Match"
        doc = "THIS IS A BIG TEXT TEST"
        query = "BIG TEXT TEST"
        match = highlight_doc(doc,query)
        self.assertTrue("THIS IS A [[HIGHLIGHT]]BIG TEXT TEST[[ENDHIGHLIGHT]]", match)

    def test_correct_answer_singleword_query(self):
        print "Test Single Word Query Match"
        doc = "THIS IS A BIG TEXT TEST"
        query = "TEXT"
        match = highlight_doc(doc,query)
        self.assertTrue("THIS IS A BIG [[HIGHLIGHT]]TEXT[[ENDHIGHLIGHT]] TEST", match)

    def test_correct_answer_multiple_singlewords_query(self):
        print "Test Single Word Query Match"
        doc = "THIS IS A BIG TEXT TEST"
        query = "TEXT THIS"
        match = highlight_doc(doc,query)
        self.assertTrue("[[HIGHLIGHT]]THIS[[ENDHIGHLIGHT]] IS A BIG [[HIGHLIGHT]]TEXT[[ENDHIGHLIGHT]] TEST", match)

    def test_no_answer_multiple_words_query(self):
        print "Test Full Query Miss"
        doc = "THIS IS A BIG TEXT TEST"
        query = "BURGER BOOGALOO"
        match = highlight_doc(doc,query)
        self.assertTrue("THIS IS A BIG TEXT TEST", match)

    def test_no_answer_singlewords_query(self):
        print "Test Single Query Miss"
        doc = "THIS IS A BIG TEXT TEST"
        query = "BURGER"
        match = highlight_doc(doc,query)
        self.assertTrue("THIS IS A BIG TEXT TEST", match)

if __name__ == '__main__':
    unittest.main()
