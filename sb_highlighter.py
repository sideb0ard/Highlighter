# -*- coding: utf-8 -*-
# Thorsten Sideboard's Flying Circus text highlighting guff.
import sys
import re

def highlight_doc(doc,query):
    result = re.search(query, doc)
    if result is None:
        print "Sorry bud, no dice"
    else:
        highlightOn = "[[HIGHLIGHT]]"
        highlightOff = "[[ENDHIGHLIGHT]]"
        #print "RESULT! {0}".format(result)
        #displaytext = re.sub('(.*)(%s)(.*)' % query, '\\1%s\\2%s\\3' % (highlightOn,highlightOff), doc)
        displaytext = re.sub('(.*)(%s)(.*)' % query, '\\1%s\\2%s\\3' % (highlightOn,highlightOff), doc)
        print "DISPLAYTEXT: {0}".format(displaytext)


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

    highlight_doc(doc,query)

    #pat = re.compile(r'([A-Z][^\.!?]*[\.!?])', re.M)
