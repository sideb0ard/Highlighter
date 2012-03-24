# -*- coding: utf-8 -*-
# Thorsten Sideboard's Flying Circus text highlighting guff.
import sys

def compute_prefix(list): # THIS IS CALLED BY GOODSUFFIX_HEURISTIC TO WORK OUT DISTANCE FROM LEFT OF PATTERN
    size = len(list)
    k = 0
    q = 1
    result = {0:0}
    #result[0] = 0
    #print "In compute_prefix, result is ".format(result)
    while q < size:
        #print "K is {0}, list[k] is {1} and list[q] is {2}. Q is {3} and size is {4}".format(k,list[k],list[q],q,size)
        while (k > 0) and (list[k] != list[q]):
            #print "testing", k
            k = result.get(k-1)

        if( k is not None and list[k] == list[q]):
            k += 1 
        result[q] = k
        q += 1
    #print "Returning result {0}".format(result)
    return result

def prepare_badcharacter_heuristic(query_list): # for each char in query, work out furthest right position
    result = {}
    for index,item in enumerate(query_list):
      result[item] = index
    return result

def prepare_goodsuffix_heuristic(query_list): # THIS BIT I KINDA FOLLOW BUT IT BOGGLES MY HEAD
    size = len(query_list)
    result = {}

    reversd = query_list[::-1]
    #print "REVERSED IS {0}".format(reversd)
    prefix_normal = compute_prefix(query_list)
    prefix_reversed = compute_prefix(reversd)

    #print "PREFIX_NORMAL IS {0}".format(prefix_normal)
    #print "PREFIX____REV IS {0}".format(prefix_reversed)

    i = 0
    while i <= size:
        normpre = size - prefix_normal[size-1]
        #print "NORMPRE is {0}".format(normpre)
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

    s = 0 # OUR STARTING POSITION WITHING THE DOCUMENT
    #print "\n"
    while  s <= doc_length - query_length:
      j = query_length # J is our position within the QUERY PATTERN WHICH WE'LL COUNT BACKWARDS FROM
      print "\n**STARTING HERE** - J is {0} and S is {1}".format(j,s)
      print "Looking at ", doc_list[s+j-1], " for ", query_list[j-1], "S is",s+j-1,"J is", j
      print "DOC_LENGTH is {0}, QUERY_LENGTH is {1}".format(doc_length,query_length)
    
      while ((j > 0) and (s+j-1 < doc_length) and (query_list[j-1] == doc_list[s+j-1])):
      #while ((j > 0) and (query_list[j-1] == doc_list[s+j-1])):
        print "\n"
        print "MATCH FOUND! QUERY - {0}, DOC - {1}, S - {2}, J - {3}".format(query_list[j-1],doc_list[s+j-1],s,j)
        #print "Decremented J by one", j
        j -= 1 # 
        print "AFTER THE DECREMENT = querylist[j minus one is {0} and doclist(s plus j minus one) is {1}".format(query_list[j-1], doc_list[s+j-1])
        print "J is {0}".format(j)

      print "FELL THROUGH - {0} didn't match {1}".format(query_list[j-1],doc_list[s+j-1])
      print "J is {0}".format(j)
      if (j > 0): # 
        k = badcharacter.get(doc_list[s+j-1])
        print "BADCHARS {0}".format(badcharacter)
        #print "Moved k back one ", k
        print "Kmonster", k
        if k is None:
          print "K is NONE, making it minus 1"
          k =-1
          #print "newK", k
        if k is not None and k < j and ((j-k-1) > goodsuffix[j]):
          s += (j-k-1)
          print "K IS NOT NONE AND LESS THAN J - NEW STEP S", s
        else:
          print "AT THIS POINT S IS {0}".format(s)
          print "GOOD SUFFIX RETURNS", goodsuffix[j]
          print "FULL GOOD SUFFIX is {0}".format(goodsuffix)
          s += goodsuffix[j];
          print "GOOD SUFFIX NEW STEP S - J ", s, j
        if s == 0:
            s += 1
      else:
        print "RETURNED WITH POSITION S", s, "ON CHAR", doc_list[s:(s+query_length)]
        return s

      #j -= 1 # 
      print "DOWN HERE NOW and J is {0} // S is {1}".format(j,s)

      #s += 1
      #print "AH, NOT MATCHED - MOVING on.."
    print "Sorry - no match found in document for pattern {0}".format(query)
    return None


if __name__ == "__main__":
    #print "LENGTH IS {0}".format(len(sys.argv))
    if len(sys.argv) != 3: 
        print 'Usage: sbz_highlighter.py <FILE> <SEARCH_TERM>' 
        sys.exit(1) 
    #print "ARGV[0] = {0} and ARGV[1] = {1} 2 - {2}".format(sys.argv[0],sys.argv[1],sys.argv[2])

    file = open(sys.argv[1])
    lines = file.read()

    #print "\n{0}".format(lines)

    matchpoint = highlight_doc(lines,sys.argv[2])
    print "METHOD RETURNED WITH MATCHPOINT {0}".format(matchpoint)
