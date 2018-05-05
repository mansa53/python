lines, sentences,blanklines, words = 0, 0, 0,0
try:

  # use a text file you have, or google for this one ...

  filename = 'f.txt'

  textf = open(filename, 'r')

except IOError:

  print 'Cannot open file %s for reading' % filename

  import sys

  sys.exit(0)

# reads one line at a time

for line in textf:

 # print line,   # test

  #lines += 1

  

  if line.startswith('\n'):

    blanklines += 1

  else:

    # assume that each sentence ends with . or ! or ?

    # so simply count these characters

    sentences += line.count('.') + line.count('!') + line.count('?')

    

    # create a list of words

    # use None to split at any whitespace regardless of length

    # so for instance double space counts as one space

    tempwords = line.split(None)

    #print tempwords  # test

    

    # word total count

    words += len(tempwords)

    

textf.close()


#print "Sentences  : ", sentences

#print "Words      : ", words

word_mean=words/sentences
print "average number of words per sentence is:" ,word_mean

def syllables(word):
    count = 0
    vowels = 'aeiouy'
    word = word.lower().strip(".:;?!")
    if word[0] in vowels:
        count +=1
    for index in range(1,len(word)):
        if word[index] in vowels and word[index-1] not in vowels:
            count +=1
    if word.endswith('e'):
        count -= 1
    if word.endswith('le'):
        count+=1
    if count == 0:
        count +=1
    return count

fname='f.txt'
number=0
with open(fname, 'r') as f:
    for line in f:
	 words = line.split()
	 
    	 for i in words:
	 	w=i
         	n=syllables(w)
		if(n>=3):
         		number+=1
			
  
         
print "words with more then 3 syllables are",number
fog_index=(word_mean+number)*0.4
print "fog index is: ",fog_index

