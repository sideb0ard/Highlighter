# -*- coding: utf-8 -*-
# Thorsten Sideboard's Flying Circus text highlighting guff.
import sys

def compute_prefix(list):
    size = len(list)
    k = 0
    q = 1
    result = {}
    result[0] = 0
    while q < size:
        while (k > 0) and (list[k] != list[q]):
            print "testing", k
            k = result.get(k-1)
        if( k is not None and list[k] == list[q]):
            k += 1 
        result[q] = k
        q += 1
    return result

def prepare_badcharacter_heuristic(query_list): # for each char in query, work out furthest right position
    result = {}
    for index,item in enumerate(query_list):
      result[item] = index
    return result

def prepare_goodsuffix_heuristic(query_list):
    size = len(query_list)
    result = {}

    reversd = query_list[::-1]
    prefix_normal = compute_prefix(query_list)
    print "PREFIX NORRRRMAL", prefix_normal
    prefix_reversed = compute_prefix(reversd)
    print "PREFIX REVVVNORRRRMAL", prefix_reversed

    i = 0
    while i <= size:
        normpre = prefix_normal[size-1]
        if normpre is None:
            normpre = 0
        result[i] = size - normpre
        i += 1

    i = 0
    while i < size:
        j = size - prefix_reversed[i]
        k = i - prefix_reversed[i]+1
        if result[j] > k:
            result[j] = k
        i += 1
    return result

def highlight_doc(doc,query):    # 
    doc_length = len(doc)
    query_length = len(query)

    if doc_length < query_length:
      print "bzzt - does not compute - query should be longer than document"
      exit(1)
  
    doc_list = list(doc)
    query_list = list(query)

    badcharacter = prepare_badcharacter_heuristic(query_list)
    goodsuffix = prepare_goodsuffix_heuristic(query_list)
    print "BADBOTS", badcharacter
    print "GOODGUYS", goodsuffix

    s = 0 # index - position within Doc
    print "\n"
    while  s < doc_length - query_length:
      j = query_length # ie. last character of query
      print "Looking at ", doc_list[s+j-1], " for ", query_list[j-1], "S is",s+j-1,"J is", j
    
      while ((j > 0) and (query_list[j-1] == doc_list[s+j-1])):
        print "\n"
        print "MATCH FOUND! -- ", query_list[j-1], doc_list[s+j-1], "AT POSITION ", (s+j-1)
        j -= 1 # 
        print "Decremented J by one", j
        print "NOw looking for ", query_list[j-1], "IN", doc_list[s+j-1]

#        if (j > 0): # 
#          k = badcharacter.get(doc_list[s+j-1])
#          print "Moved k back one ", k
#          print "Kmonster", k
#          if k is None:
#            print "K is NONE, making it minus 1"
#            k =-1
#            print "newK", k
#          if (k is not None and k < j) and ((j-k-1) > goodsuffix[j]):
#            s += (j-k-1)
#            print "NEW STEP S", s
#          else:
#            s+= goodsuffix[j];
#            print "GOOD SUFFIX NEW STEP S - J ", s, j
##else:
#        print "RETURNED WITH POSITION S", s, "ON CHAR", doc_list[s:(s+query_length)]
#        return s
#        #j += 1
#        print "J", j
      s += 1
      print "AH, NOT MATCHED - MOVING on.."
    print "RETURNNZNONE!!"
    return None


if __name__ == "__main__":
    highlight_doc(sys.argv[1],sys.argv[2])
