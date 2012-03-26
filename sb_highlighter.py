# -*- coding: utf-8 -*-
# Thorsten Sideboard's Flying Circus text highlighting guff.
import sys
import re
import os.path

#MAKING THESE GLOBAL SO UNITTEST IMPORT HAS ACCESS
highlightOn = "[[HIGHLIGHT]]"
highlightOff = "[[ENDHIGHLIGHT]]"

def highlight_doc(doc,query):
    query_words = query.split()
    query_word_count = len(query_words) 

    result = re.search(query, doc, re.IGNORECASE) # FIRST TRY A MATCH ON FULL QUERY

    if result is not None:
        displaytext = re.sub(".*?(.{,150})((?i)%s)(.{,350})" % query, "\\1%s\\2%s\\3" % (highlightOn,highlightOff), doc, count=1)
        displaytext = displaytext[:400]
        return displaytext

    else: # THEN TRY A SEPARATE MATCH WITH EACH SEARCH TERM
        if query_word_count > 1: 
            displaytext = single_word_highlight(doc,query_words)
            return displaytext

    # OTHERWISE RETURN NONE

def single_word_highlight(text,query_words):
    wordtransform = text
    x = 0
    for word in query_words:
        wordresult = re.search(word,wordtransform, re.IGNORECASE)
        if wordresult is not None:
            if x < 1: # TRIM TEXT SIZE ON FIRST RUN IN CASE DOCUMENT ES MUY GRANDE
                wordtransform = re.sub(".*?(.{,150})((?i)%s)(.{,350})" % word, "\\1%s\\2%s\\3" % (highlightOn,highlightOff), wordtransform, count=1)
                wordtransform = wordtransform[:600]
            else:
                wordtransform = re.sub("(.*)((?i)%s)(.*)" % word, "\\1%s\\2%s\\3" % (highlightOn,highlightOff), wordtransform, count=12)
            x += 1
    return wordtransform


if __name__ == "__main__":

    if len(sys.argv) != 3: 
        print 'Usage: sb_highlighter.py <FILE> <SEARCH_TERM>' 
        sys.exit(1) 

    if os.path.isfile(sys.argv[1]):
        try:
            doc = open(sys.argv[1]).read().replace('\n', '')
        except IOError as e:
            print "\nOh dear, problems opening {0} - {1}\n".format(sys.argv[1],e)
            sys.exit(1)
    else:
            print "\nYow, looks like file {0} doesn't exist.\n".format(sys.argv[1])
            sys.exit(1)

    query = sys.argv[2]
    doc_length = len(doc)
    query_length = len(query)

    if doc_length < query_length:
      print "bzzt - does not compute - query should be longer than document"
      exit(1)

    searchresult = highlight_doc(doc,query)

    print "\nSEARCH RESULT: \n{0}\n".format(searchresult)

