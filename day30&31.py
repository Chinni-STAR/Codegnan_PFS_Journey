#Regular Expressions(RegEx)
'''
-->this regular expression or RegEx is a sequence of characters that forms a searching pattern.
-->To use this we have to import re,which will unlock the package

'''
#Functions of re
'''
1.findall:
----------> by using this function, it will find all sequence in the string
SYNTAX--> re.findall("metachar",variable_name)
e.g:
import re
any="python is a programming"
so=re.findall("a",any)
print(so)                   o/p:['a','a']


2.search:
--------->by using this function,it will only find first sequence in the string
SYNTAX-->re.search("metachar",variable_name)
e.g:
import re
any="python is a programming"
so=re.search("a",any)
print(so)                   o/p:<re.Match object; span=(10, 11), match='a'>

'''

'''
MetaCharacters
--------------
-->metacharacters are used to form searching pattern

1.[]
----
-->Tn this meta character we can search for [a-z],[0-9],[A-Z],[a-z0-9]

e.g:
import re
a="Python is a programming language and today we learned abo2ut regular expressions 12345666789"
#s=re.findall("[a-z]",a)
#s=re.findall("[a-g]",a)
#s=re.findall("[abc]",a)
#s=re.findall("[aeh]",a)
#s=re.findall("[]",a) -->it becomes error
#s=re.findall("[0-6a-z]",a) #we search both numeric or alphabetic at same time
s=re.findall("[0-6A-Z]",a) 
print(s)


import re
a="Python is a programming language and today we learned abo2ut regular expressions 12345666789"
s=re.findall("[0-6A-Z]",a)
print(s)

r="This is the regular expression"
t=re.search("[a]",r)
print(t)


2.dot(.):
--------
-->This meta character will form a searching pattern as it will take any single character for (.)

import re
w= "hello"
t=re.findall("h...o",w)
#t=re.findall("h....o",w) -->it becomes [] 
r=re.search("he..o",w)
print(t)
print(r)

3.^
----
-->this is used to find the string is starting with the sequence or not

SYNTAX:
       re.findall("^",variable_name)

import re
h="this is used to find the string is starting with the sequence of characters"
w=re.findall("^this",h)
r=re.search("^this ",h)
print(w)
print(r)

4.$
----
-->this is used to find the string is ending with the sequence or not

SYNTAX:
       re.findall("$",variable_name)

import re
o="python is a programming language  "
p=re.findall("language  $",o)
#r=re.search("language  $",o)
r=re.search("python$",o)
print(r)
print(p)

5.*
---
->This meta character will form a searching pattern as it will take any zero or more character for (*).

SYNTAX:
       re.findall(".*",variable_name)

import re
o="python is a programming language "
p=re.findall("t.*i",o)#it output comes ending of it character start with t to until it i comes string last
p=re.findall("t.*",o)
k=re.search("i.*",o)
k=re.search("i.*g",o)
print(p)
print(k)

6.+
---
-->this meta character will form a searching pattern as it will take any one or more character for (+).

SYNTAX:
       re.findall(".+",variable_name)
       
import re
o="this meta character will form a searching pattern as it will take any one or more character"
#p=re.findall("an.*y",o)
p=re.findall("an.+y",o)
k=re.search("t.+",o)
print(p)
print(k)

7.?
---
-->this meta character will form a searching pattern as it will take any zero or one character.

SYNTAX:
       re.findall(".?",variable_name)

import re
a="this meta character"
an=re.findall("th.?",a)
print(an)
any=re.search("th.?",a)
print(any)

8.{}
----
-->this meta character will form a searching pattern as we can mention the size in the {}.

SYNTAX:
      re.findall(".{size",variable_name)

import re
a="This meta character will form a searching pattern as it will take"
#an=re.findall("me.{24}",a)
an=re.findall(".{24}ta",a)
print(an)
t=re.search("ch.{25}",a)
print(t)


9.|
---
-->This meta character will form a searching pattern as it consider right or left any string is
present or not for (|).

SYNTAX:


import re
a="This meta character will form"
#r=re.findall("this|will",a)
#r=re.findall("that|will",a)
r=re.findall("This|will",a)
print(r)
'''

'''
Special Sequence
----------------
-->A special sequence is a \ followed by one of the characters in the list below,and has a
special meaning:

1.\A
----
-->Returns a match if the specified characters are at the beginning of the string
E.g:"\AThe"

import re
text="Python programming"
#check if the string starts with beginning
a=re.findall("\Ay",text)
print(a)
if a:
    print("yes,there is a match")
else:
    print("No match")

2.\b
----
-->Returns a match where the specified characters are at the beginning and at the end of a word
E.g: r"\bain"


import re
a="The rain in spain"
#check if " is present at the beginning of a word:
x=re.findall(r"\bspain",a)
print(x)
if x:
    print("yes,there is a atleast one match")
else:
    print("No match")

3.\d
----
-->returns a match where the string contains digits(numbers from 0-9)
Eg:"\d"

import re
text="Python programming 89"
#
a=re.findall("\d",text)
print(a)
if a:
    print("Yes,there is a match")
else:
    print("No match")

4.\D
----
-->returns a match where the string Does not contains digits(numbers from 0-9)
E.g:"\D"

import re
#text="2344566789"
text="Python is a programming 123 language"
#return a match at every no-digit character:
a=re.findall("\D",text)
print(a)
if a:
    print("Yes,there is a match")
else:
    print("No match")

5.\s
----
-->returns a match where the string contains a white space character
E.g:"\s"

import re
text="the rain in spain"
#return a match at every white-space character:
a=re.findall("\s",text)
print(a)
if a:
    print("Yes, there is a match")
else:
    print("No match")

5.\S
----
-->returns a match where the string Does Not contains a white space character
E.g:"\S"

import re
text="the rain in spain"
#return a match at every NON white-space character:
a=re.findall("\S",text)
an=re.search("\S",text)
print(a)
print(an)
if a:
    print("Yes, there is a match")
else:
    print("No match")
'''

'''
Time and Date
-------------
%d--->day
%m--->month
%y--->year
%H--->Hour
%M--->minute
%S--->Sec
%p--->AM/PM
%A--->Day Name
%B--->Month Name

'''
import datetime
now=datetime.datetime.now()
print(now)

import datetime
today=datetime.datetime.today()
print(today.strftime("%d-%m-%Y"))
print(today.strftime("%A"))
print(today.strftime("%B"))

      














