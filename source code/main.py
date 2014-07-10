from __future__ import unicode_literals
# from hazm 		import Normalizer, word_tokenize, Stemmer
import codecs
import re

def preprocessing():


	# try:
	# 	corpus_file = codecs.open("All.txt", "r", "utf-8")
	# except:
	# 	#print "corpus file not found!"
	# 	exit()

	# lines = corpus_file.readlines()
	# corpus_file.close()

	# i = 0
	# largetext = codecs.open("littletext.txt", "w", "utf-8")

	# for line in lines:
	# 	i += 1
	# 	if i <=  50000:
	# 		largetext.write(line)

	# try:
	# 	corpus_file = codecs.open("All_WithUnderScore.txt", "r", "utf-8")
	# except:
	# 	#print "corpus file not found!"
	# 	exit()

	# lines = corpus_file.readlines()
	# corpus_file.close()

	# i = 0
	# largetext_WithUnderScore = codecs.open("littletext_WithUnderScore.txt", "w", "utf-8")

	# for line in lines:
	# 	i += 1
	# 	if i <=  50000:
	# 		largetext_WithUnderScore.write(line)



	# try:
	# 	corpus_file = codecs.open("littletext.txt", "r", "utf-8")
	# except:
	# 	#print "corpus file not found!"
	# 	exit()

	# lines = corpus_file.readlines()
	# corpus_file.close()
	# normalizer 	= Normalizer()

	# normalized = codecs.open("normalized_littletext.txt", "w", "utf-8")


	# for line in lines:
	# 	normalize_line = normalizer.normalize(line.strip())
	# 	normalized.write(normalize_line + "\n")

	# try:
	# 	corpus_file_WithUnderScore = codecs.open("littletext_WithUnderScore.txt", "r", "utf-8")
	# except:
	# 	#print "corpus file not found!"
	# 	exit()

	# lines = corpus_file_WithUnderScore.readlines()
	# corpus_file_WithUnderScore.close()
	# normalizer 	= Normalizer()

	# normalized = codecs.open("normalized_littletext_WithUnderScore.txt", "w", "utf-8")

	# for line in lines:
	# 	normalize_line = normalizer.normalize(line.strip())
	# 	normalized.write(normalize_line + "\n")




	try:
		corpus_file = codecs.open("normalized_ALL.txt", "r", "utf-8")
	except:
		# #print "corpus file not found!"
		exit()

	lines = corpus_file.readlines()
	corpus_file.close()

	i = 0
	train = codecs.open("trainـnormalized_ALL.txt", "w", "utf-8")
	test = codecs.open("testـnormalized_ALL.txt", "w", "utf-8")

	# #print "write WithoutUnderScore ..."
	for line in lines:
		i += 1
		if i <=  (3 *len(lines)) / 4:
			train.write(line)
		else:
			test.write(line)
	train.close()
	test.close() 

	try:
		corpus_file = codecs.open("normalized_All_WithUnderScore.txt", "r", "utf-8")
	except:
		# #print "All_WithUnderScore file not found!"
		exit()

	lines = corpus_file.readlines()
	corpus_file.close()

	j= 0
	train_WithUnderScore = codecs.open("train_normalized_ALLـWithUnderScore.txt", "w", "utf-8")
	test_WithUnderScore = codecs.open("test_normalized_ALLـWithUnderScore.txt", "w", "utf-8")

	# #print "write WithUnderScore ..."
	for line in lines:
		j += 1
		if j <=  (3 *len(lines)) / 4:
			train_WithUnderScore.write(line)
		else:
			test_WithUnderScore.write(line)
	train_WithUnderScore.close()
	test_WithUnderScore.close()


def tokenizeToPso():
	try:
		corpus_file = codecs.open("train_normalized_littletextـWithUnderScore.txt", "r", "utf-8")
	except:
		##print "corpus file not found!"
		exit()

	lines = corpus_file.readlines()
	corpus_file.close()

	tokenized = codecs.open("tokenized_for_POSـWithUnderScore.txt", "w", "utf-8")


	for line in lines:
		# normalize_line = normalizer.normalize(line.strip())
		# words = word_tokenize(normalize_line)
		line = line.strip()
		line = re.sub(" +", " ", line)
		# list of words in sentence
		words = line.split(" ")

		for word in words:
			tokenized.write(word + "\n")
		tokenized.write("/--\\" + "\n")
	tokenized.close()

def creatingProbabolityModels():
	try:
		corpus_file = codecs.open("tokenized_for_POSـWithUnderScore.txt", "r", "utf-8")
	except:
		##print "tokenized_WithUnderScore file not found!"
		exit()

	lines = corpus_file.readlines()
	corpus_file.close()

	ezafe = "EZ"
	count_of_ez = 0.0
	words_with_underscore	= {}
	pos_with_underscore	={}
	prob_of_words = {}
	prob_of_pos = {}
	# word_with_pos	= {}
	count_of_pos_ez	= 0.0

	for line in lines:
		if ezafe in line:
			count_of_ez += 1.0
			word = line[:-4]
			if word in words_with_underscore:
				words_with_underscore[word] += 1.0
			else:
				words_with_underscore[word] = 1.0

	# tokenized = codecs.open("test.txt", "w", "utf-8")

	try:
		wordpos = codecs.open("wordpos.txt", "r", "utf-8")
	except:
		#print "wordpos file not found!"
		exit()

	lines = wordpos.readlines()
	wordpos.close()
	
	for word in words_with_underscore:
		prob_of_words[word] = words_with_underscore[word] / count_of_ez
		for line in lines:
			linesword = line.split("\t")
			if linesword[0] == word:
				# tokenized.write(linesword[0] + "\t" + word + "\n")
				count_of_pos_ez += 1.0
				if linesword[1] in pos_with_underscore:
					pos_with_underscore[linesword[1]] += 1.0
				else:
					pos_with_underscore[linesword[1]] = 1.0

	for pos in pos_with_underscore:
		prob_of_pos[pos] = pos_with_underscore[pos] / count_of_pos_ez
		# tokenized.write(str(pos_with_underscore[pos]))
	# tokenized.close()

	prob_of_pos_file = codecs.open("prob_of_pos.txt", "w", "utf-8")


	for pose in prob_of_pos:
		prob_of_pos_file.write(str(pose) + "\t" + str(prob_of_pos[pose]))


	final_format = codecs.open("final_output.txt", "w", "utf-8")

	try:
		wordpos = codecs.open("wordpos.txt", "r", "utf-8")
	except:
		#print "wordpos file not found!"
		exit()

	lines = wordpos.readlines()
	wordpos.close()

	for line in lines:
		linewithpos = line.split("\t")
		if linewithpos[0] == "/--\\" :
			final_format.write("\n")
		else:
			if linewithpos[0] not in prob_of_words:
				# prob_of_words[linewithpos[0]] = 0.0
				final_format.write(linewithpos[0] + "|" + linewithpos[1] + "|" + "0.0" + "|" + str(prob_of_pos[linewithpos[1]]) + " ")
			elif linewithpos[1] not in prob_of_pos:
				final_format.write(linewithpos[0] + "|" + linewithpos[1] + "|" + str(prob_of_words[linewithpos[0]]) + "|" + "0.0" + " ")
				# prob_of_pos[linewithpos[1]] = 0.0
			else :
				final_format.write(linewithpos[0] + "|" + linewithpos[1] + "|" + str(prob_of_words[linewithpos[0]]) + "|" + str(prob_of_pos[linewithpos[1]]) + " ")
	final_format.close()


if __name__ == "__main__":
	# preprocessing()
	# tokenizeToPso()
	creatingProbabolityModels()