'''
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

'''
s="likhitha is   a good girl"

def rev_words(s):
    slst=s.split(" ")
    slst2=[]
    print(slst)
    for i in range(len(slst)-1,-1,-1):
        if slst[i]!="":
            slst2.append(slst[i])
    return " ".join(slst2)
print(rev_words(s))
            
        