# -*- coding: utf-8 -*-
# Thorsten Sideboard's Flying Circus text highlighting guff.
import sys
import re


def highlight_doc(doc,query):
    query_words = query.split()
    query_word_count = len(query_words) 
    #if len(query_words) > 1:
    #    for word in query_words:
    #        print "WORD:: {0}".format(word)
    #        single_word_highlight(displaytext,word)

    # FIRST RUN FOR FULL QUERY
    result = re.search(query, doc)

    if result is None:
        if query_word_count > 1:
            #print "SINGLE WORD SEARCH"
            displaytext = single_word_highlight(doc,query_words)
            #print "\n\n{0}\n\n".format(displaytext)
            return displaytext
    else:
        #print "RESULT! {0}".format(result)
        #displaytext = re.sub('(.*)(%s)(.*)' % query, '\\1%s\\2%s\\3' % (highlightOn,highlightOff), doc)
        #displaytext = re.sub(".*(.{,70})(%s)(.*)" % query, '\\1%s\\2%s\\3' % (highlightOn,highlightOff), doc)
        displaytext = re.sub(".*?(.{,150})(%s)(.{,350})" % query, "\\1%s\\2%s\\3" % (highlightOn,highlightOff), doc, count=1)
        displaytext = displaytext[:400]

        #print "\n\n{0}\n\n".format(displaytext)
        return displaytext


def single_word_highlight(text,query_words):
    wordtransform = text
    x = 0
    for word in query_words:
        wordresult = re.search(word,wordtransform)
        if wordresult is not None:
            #print "FOUND WORD {0}".format(word)
            #print "WORDRESULT = {0}".format(wordtransform)
            #wordtransform = re.sub("(.{300})(%s)(.*)" % word, "\\1%s\\2%s\\3" % (highlightOn,highlightOff), wordtransform, count=12)
            if x < 1:
                print "X LESS THAN ONE"
                wordtransform = re.sub(".*?(.{,150})(%s)(.{,250})" % word, "\\1%s\\2%s\\3" % (highlightOn,highlightOff), wordtransform, count=1)
                wordtransform = wordtransform[:600]
            else:
                wordtransform = re.sub("(.*)(%s)(.*)" % word, "\\1%s\\2%s\\3" % (highlightOn,highlightOff), wordtransform, count=12)
            print "\n\nWORDDD{0}\n\n".format(wordtransform)
        x += 1
    return wordtransform

if __name__ == "__main__":

    if len(sys.argv) != 3: 
        print 'Usage: sb_highlighter.py <FILE> <SEARCH_TERM>' 
        sys.exit(1) 

    #file = open(sys.argv[1])
    doc = open(sys.argv[1]).read().replace('\n', '')
    query = sys.argv[2]

    doc_length = len(doc)
    query_length = len(query)

    if doc_length < query_length:
      print "bzzt - does not compute - query should be longer than document"
      exit(1)

    highlightOn = "[[HIGHLIGHT]]"
    highlightOff = "[[ENDHIGHLIGHT]]"
    searchresult = highlight_doc(doc,query)

    print "\nSEARCH REZULT: \n{0}\n".format(searchresult)

    #pat = re.compile(r'([A-Z][^\.!?]*[\.!?])', re.M)
