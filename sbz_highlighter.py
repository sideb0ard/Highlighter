# Thorsten Sideboard's Flying Circus text highlighting guff.
import re

def highlight_doc(doc,query):    # 
    m = re.search(query, doc)
    split_query = re.split('\W+', query)
    #(m is not None) and (print "m.group(0)")
    if m is not None:
        print m.group(0)

    print len(split_query)
    print split_query
    for word in split_query: print word,

if __name__ == "__main__":
    import sys
    highlight_doc(sys.argv[1],sys.argv[2])
