# Thorsten Sideboard's Flying Circus text highlighting guff.
import re
import sys

def highlight_doc(doc,query):    # 
    doc_length = len(doc)
    query_length = len(query)

    if doc_length < query_length:
      print "bzzt - does not compute - query should be longer than document"
      exit(1)
  
    doc_list = list(doc)
    query_list = list(query)

    print doc_list[0:3]

    s = 0
    while  s < doc_length - query_length:
      print "boom! ", s
      s += 1

   
    
#    print "LENGTHZ::"
#    print doc_length, query_length
#
#    m = re.search(query, doc)
#    split_query = re.split('\W+', query)
#    #(m is not None) and (print "m.group(0)")
#    if m is not None:
#        print m.group(0)
#
#    print len(split_query)
#    print split_query
#    for word in split_query: print word,


if __name__ == "__main__":
    highlight_doc(sys.argv[1],sys.argv[2])
