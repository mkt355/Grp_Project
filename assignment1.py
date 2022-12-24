#Assignment 
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# Input: s = "There is a glitch in the matrix"
# Output: 5
# Explanation: The last word is "matrix" with length 6.

# return the length of last word in the string

def length_of_lastword(word):
  word_list = word.split()
  count = 0
  for i in word_list[-1]:
    if i.isalpha()==True:
      count+=1
    else:
      count+=0
  return count

text = "There is a glitch in the matrix.......!!$%"
length_of_lastword(text)

