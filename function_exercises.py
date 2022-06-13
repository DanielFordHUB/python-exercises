#!/usr/bin/env python
# coding: utf-8

# In[83]:


#Define a function named is_two. It should accept one input and 
#return True if the passed input is either the number 
#or the string 2, False otherwise

def is_two(n):
    if n == 2 or n == '2' or n.lower() in['two'] :    #__fixed__##<how to lower specify two??????
        print('this is 2!')
        return '2!'
    else:
        return 'not 2!'
        
is_two('2')
#nice###################################


# In[35]:


#Define a function named is_vowel. It should return True 
#if the passed string is a vowel, False otherwise.

def is_vowel(n):
    while n.lower() in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False
is_vowel('2')
##################_____done_______


# In[85]:


#3 Define consonant

def is_consonant(n):
    while n.lower() in ['a', 'e', 'i', 'o', 'u']:
        return False
    else:
        return True
is_consonant('W')
##############________done___________


# In[84]:


#4 Define a function that accepts a string that is a word. 
#The function should capitalize the first letter of the word 
#if the word starts with a consonant.

#def cap_if_cons(string):
 #   if [0] for n.lower() in ['a', 'e', 'i', 'o', 'u']:
  #      return False
   # else:
    #    return string.capitalize()
    
#cap_if_cons('agsfga')

#__________COME BACK TO____________????????????????????????????????????


# In[89]:


def cap_if_cons(n):
    first_letter = n[0]
    if is_consonant(first_letter):
        n = n.capitalize()
    return n
cap_if_cons('sdfasd')


# In[59]:


# 5 Define a function named calculate_tip. It should accept a 
#   tip percentage (a number between 0 and 1) and the 
#   bill total, and return the amount to tip.

def tip(n):
    n = n * 0.2
    print('your 20% tip is', '$',n)
    return
tip(30)

#_____________________Done


# In[82]:


# 6
#Define a function named apply_discount. It should 
#accept a original price, and a discount percentage, 
#and return the price after the discount is applied.

#def discount(n):
   # n = n - (n * 0.30)
    #print('Your discounted total is now', '$', n)
    #return
#discount(25)

discount = lambda n: n-(n*.3)
discount(100)
#___________________DONE


# In[90]:


# 7

# Define a function named handle_commas. 
#It should accept a string that is a number that 
#contains commas in it as input, and return a number as output.

def handle_commas(s):
    s = s.replace(',', '')
    int(s)
    print(s)
    return s

handle_commas("1,342,543,345")
    
    


# In[69]:


# 8

#Define a function named get_letter_grade. It should accept a number 
#and return the letter grade associated with that number (A-F).

#def get_letter_grade(g):
    


# In[ ]:


# 9
#Define a function named remove_vowels that accepts 
#a string and returns a string with all the vowels removed.

def remove_vowels(v):
    out = ''
    for char in v:
        if is_consonant(v):
            out += v
    return out


# In[ ]:


#def remove_vowels(v):
 #   return ''.join([c for c in v ])


# In[ ]:


# 10
#Define a function named normalize_name. It should accept a 
#string and return a valid python identifier, that is:

#def normalize_name(n):


# In[ ]:


# 11
#Write a function named cumulative_sum that accepts a 
#list of numbers and returns a list 
#that is the cumulative sum of the numbers in the list.

def cumulative_sum(s):
    cumulative = []
    length = len(s)
    cumulative = [sum(s[0:x:1]) for x in range(0, length+1)]
    return cumulative[1:]
list = [12, 14, 3, 2, 9]


# In[ ]:




