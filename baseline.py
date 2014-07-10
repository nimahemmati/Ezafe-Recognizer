from __future__ import unicode_literals
import codecs
import re
import random

def createFiles():
	try:
		corpus_file = codecs.open("gold_data.txt", "r", "utf-8")
	except:
		#print "corpus file not found!"
		exit()

	lines = corpus_file.readlines()
	corpus_file.close()
	ezafe = "EZ" 

	gold_for_eval_file = codecs.open("gold_has_EZ.txt", "w", "utf-8")

	for line in lines:
		line = line.strip()
		line = re.sub(" +", " ", line)
		# list of words in sentence
		words = line.split(" ")

		for word in words:
			if ezafe in word:
				word = word[:-3]
				gold_for_eval_file.write(str(word))
				gold_for_eval_file.write("\t")
		gold_for_eval_file.write("\n")

	gold_for_eval_file.close()


	try:
		corpus_file = codecs.open("test_data.txt", "r", "utf-8")
	except:
		#print "corpus file not found!"
		exit()

	lines = corpus_file.readlines()
	corpus_file.close()
	ezafe = "EZ" 

	gold_for_eval_file = codecs.open("test_has_EZ.txt", "w", "utf-8")

	for line in lines:
		line = line.strip()
		line = re.sub(" +", " ", line)
		# list of words in sentence
		words = line.split(" ")

		for word in words:
			if ezafe in word:
				word = word[:-3]
				gold_for_eval_file.write(str(word))
				gold_for_eval_file.write("\t")
		gold_for_eval_file.write("\n")

	gold_for_eval_file.close()


def evaluation():


	try:
		corpus_file_1 = codecs.open("test_has_EZ.txt", "r", "utf-8")
		corpus_file_2 = codecs.open("gold_has_EZ.txt", "r", "utf-8")
	except:
		#print "corpus file not found!"
		exit()

	lines1 = corpus_file_1.readlines()
	corpus_file_1.close()

	lines2 = corpus_file_2.readlines()
	corpus_file_2.close()

	count = 0.0

	corpus_file_1_length = 0.0
	corpus_file_2_length = 0.0

	count_line_1 = 0
	count_line_2 = 0

	words_in_test_EZ = {}
	words_in_gold_EZ = {}

	for line1 in lines1:
		count_line_1 += 1
		words = line1.strip().split("\t")
		words_in_test_EZ[count_line_1] = words


	for line2 in lines2:
		count_line_2 += 1
		words = line2.strip().split("\t")
		words_in_gold_EZ[count_line_2] = words
			
	for line in words_in_test_EZ:
		corpus_file_1_length += len(words_in_test_EZ[line])
		corpus_file_2_length += len(words_in_gold_EZ[line])
		for word in words_in_test_EZ[line]:
			if word in words_in_gold_EZ[line]:
				count +=1

	perecision = count / corpus_file_1_length
	recall = count / corpus_file_2_length
	f1_measure = 2 * (perecision * recall) / (perecision+recall)

	Evaluation_Measure_file = codecs.open("Evaluation_Measure.txt", "w", "utf-8")
	Evaluation_Measure_file.write("Perecision" + " ------> " + str(perecision) + "\n")
	Evaluation_Measure_file.write("Recall" + " ------> " + str(recall) + "\n")
	Evaluation_Measure_file.write("F1" + " ------> " + str(f1_measure))

def tokenizeToPso():
	try:
		corpus_file = codecs.open("1.txt", "r", "utf-8")
	except:
		##print "corpus file not found!"
		exit()

	lines = corpus_file.readlines()
	corpus_file.close()

	tokenized = codecs.open("tokenized_test_for_POSـWithUnderScore.txt", "w", "utf-8")


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

def createBaseLine():

	try:
		corpus_file = codecs.open("test_base.txt", "r", "utf-8")
		prob_file = codecs.open("prob_of_pos.txt", "r", "utf-8")
	except:
		#print "corpus file not found!"
		exit()

	lines = corpus_file.readlines()
	corpus_file.close()

	lines1 = prob_file.readlines()
	prob_file.close()

	out_put = codecs.open("out_put_base_line.txt", "w", "utf-8")

	prob = dict()

	for line in lines1:
		words = line.strip().split("\t")
		prob[words[0]] = words[1]

	# print(prob)

	ezafe_notation = "EZ"
	for line in lines: 
		if ("/--\\" in line) :
			out_put.write("\n")
		else:	
			words = line.strip().split("\t")
			rand = random.random()
			# print(words[0] + " \t "+words[1])
			# print(prob[words[1]])
			print(words[0] + "\t" +words[1])
			if words[1] in prob:
				if (rand <= float(prob[words[1]])):
					words[0] = words[0] + ezafe_notation
			out_put.write(words[0] + " ")







if __name__ == "__main__":
	# tokenizeToPso()
	createBaseLine()