# wordcount.py 
# This script finds the number of words, P, in the longest consecutive sequence of words of the same length.
# This is a script to be executed from the command line
# It takes one argument: the relative path to a valid input file (see below)
# Example execution:
# $> python wordcount.py input.txt
#
# Input
# The input file consists of several datasets. The first line of the input file 
# contains the number of data sets which is a positive integer and is not bigger 
# than 20. The following lines describe the data sets. For each data test, there 
# is one single line containing the string to count words. There are less than 1000 
# words in the string. The length of each word does not exceed 20 characters.
#
# Output
# For each dataset, write in one line the number P
#


import sys


# get path to input file
if len(sys.argv) != 2:
	sys.exit("Must provide only a path to a valid input file!\nExample command: `python wordcount.py input.txt`")
else:
	input_path = sys.argv[1]

# open input file
with open(input_path, 'r') as f:

	# get number of datasets from the first line
	numds = int(f.readline())

	# loop through each dataset in the input file
	for ds in f:

		# split dataset into words
		words = ds.split(' ')

		# loop through each word of the dataset
		prev_wordlength = 0
		wordlength = 0
		curP = 1
		maxP = 1
		for word in words:

			wordlength = len(word)

			# if this word's length is the same as the previous
			if wordlength == prev_wordlength:

				# increase P count
				curP += 1

			# if this word's length is different from the previous
			else:

				# reset current P count
				curP = 1

			# update max P count
			if curP > maxP:
				maxP = curP

			# set previous word length for next iteration
			prev_wordlength = wordlength

		# print max P count for this dataset
		print(maxP)

