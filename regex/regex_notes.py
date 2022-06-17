# import modules
import re # regular expressions module
import time # time module


""" # ========================================================================= Begin Methods =========================================================================
    target_string = "Lucht is blauw en water is blauw"
    uncompiled_expression = ["water", "Lucht", "blauw", "au"]
    compiled_expression = []
    for x in range(len(uncompiled_expression)):
        compiled_expression.append(re.compile(uncompiled_expression[x]))

    print("==="*7)
    x_match1 = re.match("water", target_string) # create a var for re.match object. Match will return exactly 1 match, if any, looking at the beginning of a string. ---> We used water for this one, match will not return a result. We'll need a second try
    x_match2 = re.match("Lucht", target_string) # create a var for re.match object. Match will return exactly 1 match, if any, looking at the beginning of a string. ---> We used Lucht for this one, match will return a result for this 
    x_match_group = x_match2.group() # get the complete match found, or partial match found 
    x_match_span = x_match2.span() # get the span of the match found (tuple(start,end))
    x_match_start = x_match2.start() # et the start of the span of the match found
    x_match_end = x_match2.end() # get the end of the span of the match found


    
    # for x in x_match2: # this will crash, TypeError: 're.Match' object is not iterable
    #    print(x) 
    

    print("Applied re.Match with the expression \"{}\" to the string: {}".format("water", target_string))
    print("Found: {} at the beginning of the string......retrying with \"{}\"".format(x_match1, "Lucht"))
    print("."*10)
    print("."*10)
    print("Applied re.Match with the expression \"{}\" to the string: {}".format("Lucht", target_string))
    print("found: {} in the string".format(x_match2))
    print("Returning \"{}\" from position {} to {}".format(x_match_group, x_match_start,x_match_end))

    print("==="*7)

    x_search1 = re.search("water", target_string) # create a var for re.search object. Search will return exactly 1 match, if any, looking at the whole string
    x_search_group = x_search1.group() # get the complete match found, or partial match found
    x_search_span = x_search1.span() # get the span of the match found (tuple(start,end))
    x_search_start = x_search1.start() # get the first position of the match found
    x_search_end = x_search1.end() # get the last position of the match found



    
    # for x in x_search1: # this will crash, TypeError: 're.Search' object is not iterable
    #    print(x)


    print("Applied re.Search with the expression \"{}\" to the string: {}".format("Lucht", target_string))
    print("Found: {} somewhere in the the string".format(x_search1))
    print("Returning \"{}\" from position {} to {}".format(x_search_group, x_search_start,x_search_end))

    print("==="*7)

    x_findall1 = re.findall("blauw", target_string) # create a var for re.search object. Search will return exactly 1 match, if any, looking at the whole string
    x_findall2 = re.findall(compiled_expression[2], target_string) # create a var for re.search object. Search will return exactly 1 match, if any, looking at the whole string
    # x_findall_group = x_findall1.group()   --> will not work, findall does not have this option
    # x_findall_start = x_findall1.start()   --> will not work, findall does not have this option
    # x_findall_end = x_findall1.end()       --> will not work, findall does not have this option
    # x_findall_span = x_findall1.span()     --> will not work, findall does not have this option

    for x in x_findall1:  # this works, findall is iterable.
        print(x)   # It will print out the values for each match, not a re.Match object.


    print("Applied re.FindAll with the expression \"{}\" to the string: {}".format("blauw", target_string))
    print("Found: {} somewhere in the the string through uncompiled expressions".format(x_findall1))
    print("Applied re.FindAll with the expression \"{}\" to the string: {}".format(compiled_expression[2], target_string))
    print("Found: {} somewhere in the the string through compiled expressions.".format(x_findall2))

    x_finditer1 = re.finditer("au", target_string)
        for x in x_finditer1: # this works, finditer is iterable
        print(x) # finditer returns a re.Match oject for each value found
        print(x.group(),x.start(),x.end(), x.span())  # and we can call the values just like a re.Search

# ========================================================================= END METHODS ========================================================================= """



""" # ========================================================================= Begin Quantifiers ===============================================================
target_string = "Vandaag eet ik krabburgers en krabcake."
x_asterix = re.findall("abc*", target_string) #match 'ab' followed by 0 or more c's
x_plus = re.findall("abc+", target_string) #match 'ab' followed by 1 or more c's
x_questionmark = re.findall("abc?", target_string) #match 'ab' followed by 0 or 1 c's
x_n1 = re.findall("abc{1}", target_string) # using {n}: match 'ab' followed by exact n c's, in this case {1} meaning 1 c
x_n2 = re.findall("abc{0,}", target_string) # using {n,}: match 'ab' followed by at least n or more c's, in this case {0,} meaning 0 or more
x_nm = re.findall("abc{1,2}", target_string) # using {n,m} match 'ab' followed by at least n c's, but max m c's in this case {2,6} at least two, max 6 c's

print(x_asterix)
print(x_plus)
print(x_n1)
print(x_n2)
print(x_nm)
# ========================================================================= END METHODS ========================================================================= """ 