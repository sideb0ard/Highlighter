# -*- coding: utf-8 -*-
# Thorsten Sideboard's Flying Circus text highlighting guff.
import re
import sys

#def compute_prefix(list):
#    size = len(list)
#    k = 0
#    q = 0
#    result = {}
#    while q < size:
      
      

def prepare_badcharacter_heuristic(query_list):
    result = {}
    for index,item in enumerate(query_list):
      print index,item
      result[item] = index
    return result

def prepare_goodsuffix_heuristic(query_list):
    size = len(query_list)
    result = {}

    reverse = query_list[::-1]
    print reverse


def highlight_doc(doc,query):    # 
    doc_length = len(doc)
    query_length = len(query)

    if doc_length < query_length:
      print "bzzt - does not compute - query should be longer than document"
      exit(1)
  
    doc_list = list(doc)
    query_list = list(query)

    #print doc_list[0:3]

    badcharacter = prepare_badcharacter_heuristic(query_list)
    goodsuffix = prepare_goodsuffix_heuristic(query_list)
    #print "BADBOTS", badcharacter
    #print "GOODGUYS", goodsuffix

    m = 0
    s = 0 # index - position within Doc
    while  s < doc_length - query_length:
      j = query_length # ie. last character of query
      print "Run ", s, "looking for ", query_list[j-1]
      print "Looking at ", doc_list[s+j-1], " for ", query_list[j-1]
    
      while ((j > 0) and (query_list[j-1] == doc_list[s+j-1])):
        print "MATCH FOUND! -- ", query_list[j-1], doc_list[s+j-1]

        j -= 1 # now, with one match, lets move the char position postion within query to the left by one place
        print "NOw looking for ", query_list[j-1]

        if (j > 0): # i.e. not the first character
          k = badcharacter.get(doc_list[s+j-1])
          print "Moved k back one ", k
        #  k = -1 unless k
        #  if (k < j) and ((j-k-1) > goodsuffix[j]):
        #    s += (j-k-1)
        #  else
        #    s+= goodsuffix[j];

      s += 1


if __name__ == "__main__":
    highlight_doc(sys.argv[1],sys.argv[2])
