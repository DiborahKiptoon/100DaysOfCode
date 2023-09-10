# This is an example of the for loop
# we'll have 3 examples done
#For loop() syntax
#for x in y:
#    statements

#case study
#Fruits list
Fruits = ['Mang', 'oran', 'paw', 'app', 'Avo', 'Mel']

# For loop structure
'''for Fruits[3] in Fruits:
    print(Fruits[0:3])'''


#Case study 2
# Number For Loop
num = 5

#for Loop structure
'''for i in range(num):
    print(i)'''


#case study 3
#Character print out

charct = "Pythonista"

#for Loop()
'''for i in charct:
    print(i)'''

#Case 3
# Print words instead
my_str = "I am learning to code"
word = my_str.split()

#For loop structure
'''for w in word:
    print(w)'''


'''sentences = paragraph.split(". ")
  for index, sentence in enumerate(sentences):
    if sentence == sentence:
      print(f"The sentence '{sentence}' is found in the paragraph at index {index}")'''

#Case study Paragraph
my_par = '''I am new to this.
            I love how I code.
            I am excited to learn python.
            Python is my 4th Language.'''

sentences = my_par.split("\n")

#For Loop starts here
'''for sentence in my_par:
    print(sentence)'''

#Bronch's Suggestion
'''for i in sentences:
    print(i)'''

#Ivan's suggestion
paragraph = "This is the first sentence. This is the second sentence. This is the third sentence."
sentences = paragraph.split(". ")

#For Loop starts here
for sentence in sentences:
    print(sentence)