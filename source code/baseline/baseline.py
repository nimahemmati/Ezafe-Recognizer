from __future__ import unicode_literals
import codecs
import glob
import random
prob_of_words = {}
prob_of_poses = {}
ezafe = ",EZ"


def creatingProbabolityModels():
    list_of_files =  glob.glob("F://Personal/Projects/NLP/Baseline/main_bij/BijanKhan II/TextLabelData/*.txt")
    words_with_underscore = {}
    words = {}
    pos_with_underscore	={}
    prob_of_pos = {}
    count_of_pos_ez	= 0.0
    final_output = codecs.open("prob_of_word.txt", "w",encoding='latin-1')

    for file in list_of_files:
        corpus_file = codecs.open(file, "r" , encoding='latin-1')
        lines = corpus_file.readlines()
        corpus_file.close()
        for line in lines:
            line = line.strip()
            word = line.split(" ")[-1]
            if word in words:
                words[word] += 1.0
            else:
                words[word] = 1.0
            if ezafe in line:
                if word in words_with_underscore:
                    words_with_underscore[word] += 1.0
                else:
                    words_with_underscore[word] = 1.0
    for word in words:
        if word in words_with_underscore:
            prob_of_words[word] = words_with_underscore[word] / words[word]
        else :
            prob_of_words[word] = 0.0
        final_output.write(str(word) + "\t" +str(prob_of_words[word]) + "\n")
    final_output.close()

def testBaseLine():
    count_of_gold_ez = 0.0
    count_of_test_ez = 0.0
    count_of_gold_absence_ez = 0.0
    count_of_test_absence_ez = 0.0
    count_of_joined = 0.0
    count_of_not_joined = 0.0
    word_form_evaluation_format = codecs.open("word_form_evaluation.txt", "w",encoding='latin-1')
    output_test_format = codecs.open("output_test_format.txt", "w",encoding='latin-1')
    gold_test_format = codecs.open("gold_test_format.txt", "w",encoding='latin-1')
    list_of_files =  glob.glob("F://Personal/Projects/NLP/Baseline/main_bij/BijanKhan II/TextLabelData/test/*.txt")
    for file in list_of_files:
        corpus_file = codecs.open(file, "r" , encoding='latin-1')
        lines = corpus_file.readlines()
        corpus_file.close()
        for line in lines:
            line = line.strip()
            word = line.split(" ")[-1]
            if ezafe in line:
                count_of_gold_ez += 1.0
                gold_test_format.write(str(word) + ezafe + "\n")
            else:
                count_of_gold_absence_ez += 1.0
                gold_test_format.write(str(word) + "\n")
            if prob_of_words[word] == 0.0:
                count_of_test_absence_ez += 1.0
                if ezafe not in line:
                    count_of_not_joined += 1.0
            if prob_of_words[word] >= 0.8 :
                count_of_test_ez += 1.0
                output_test_format.write(str(word) + ezafe + "\n")
                if ezafe in line:
                    count_of_joined += 1.0
            else:
                output_test_format.write(str(word)+"\n")
    ez_presence_accuracy = count_of_joined / count_of_test_ez
    ez_absence_accuracy = count_of_not_joined / count_of_test_absence_ez
    total_accuracy = (count_of_joined + count_of_not_joined) / (count_of_test_ez + count_of_test_absence_ez)
    recall = count_of_joined / count_of_gold_ez
    word_form_evaluation_format.write("Ezafe presence accuracy : " + str(ez_presence_accuracy) + "\n")
    word_form_evaluation_format.write("Ezafe absence accuracy : " + str(ez_absence_accuracy) + "\n")
    word_form_evaluation_format.write("Total accuracy : " + str(total_accuracy) + "\n")
    word_form_evaluation_format.write("Recall : " + str(recall) + "\n")
    output_test_format.close()
    gold_test_format.close()
    word_form_evaluation_format.close()

def creatingProbabolityModelsForPOSTag():
    list_of_files =  glob.glob("F://Personal/Projects/NLP/Baseline/main_bij/BijanKhan II/TextLabelData/*.txt")
    pos_with_underscore	={}
    poses = {}
    final_output = codecs.open("prob_of_pos.txt", "w",encoding='latin-1')
    for file in list_of_files:
        corpus_file = codecs.open(file, "r" , encoding='latin-1')
        lines = corpus_file.readlines()
        corpus_file.close()
        # print(file)
        # print("__________________________________________")
        for line in lines:
            line = line.strip()
            # print(line)
            # print(line.split(" "))
            pos = line.split(" ")[2]
            if pos in poses:
                poses[pos] += 1.0
            else:
                poses[pos] = 1.0
            if ezafe in line:
                if pos in pos_with_underscore:
                    pos_with_underscore[pos] += 1.0
                else:
                    pos_with_underscore[pos] = 1.0
    for pos in poses:
        if pos in pos_with_underscore:
            prob_of_poses[pos] = pos_with_underscore[pos] / poses[pos]
        else :
            prob_of_poses[pos] = 0.0
        final_output.write(str(pos) + "\t" +str(prob_of_poses[pos]) + "\n")
    final_output.close()

def testBaseLineForPOSTag():
    count_of_gold_ez = 0.0
    count_of_test_ez = 0.0
    count_of_gold_absence_ez = 0.0
    count_of_test_absence_ez = 0.0
    count_of_joined = 0.0
    count_of_not_joined = 0.0
    POSTag_form_evaluation_format = codecs.open("POSTag_form_evaluation.txt", "w",encoding='latin-1')
    output_test_format = codecs.open("POSTag_output_test_format.txt", "w",encoding='latin-1')
    gold_test_format = codecs.open("POSTag_gold_test_format.txt", "w",encoding='latin-1')
    list_of_files =  glob.glob("F://Personal/Projects/NLP/Baseline/main_bij/BijanKhan II/TextLabelData/test/*.txt")
    for file in list_of_files:
        corpus_file = codecs.open(file, "r" , encoding='latin-1')
        lines = corpus_file.readlines()
        corpus_file.close()
        for line in lines:
            line = line.strip()
            word = line.split(" ")[-1]
            pos = line.split(" ")[2]
            if ezafe in line:
                count_of_gold_ez += 1.0
                gold_test_format.write(str(word)+ ezafe +"\t"+ str(pos)  + "\n")
            else:
                count_of_gold_absence_ez += 1.0
                gold_test_format.write(str(word) +"\t"+ str(pos) +"\n")
            rand = random.random()
            if rand  <= prob_of_poses[pos]:
                count_of_test_ez += 1.0
                output_test_format.write(str(word)+ ezafe +"\t"+ str(pos) + "\n")
                if ezafe in line:
                    count_of_joined += 1.0
            else:
                count_of_test_absence_ez += 1.0
                output_test_format.write(str(word) +"\t"+ str(pos)+"\n")
                if ezafe not in line:
                    count_of_not_joined += 1.0
    ez_presence_accuracy = count_of_joined / count_of_test_ez
    ez_absence_accuracy = count_of_not_joined / count_of_test_absence_ez
    total_accuracy = (count_of_joined + count_of_not_joined) / (count_of_test_ez + count_of_test_absence_ez)
    recall = count_of_joined / count_of_gold_ez
    POSTag_form_evaluation_format.write("Ezafe presence accuracy : " + str(ez_presence_accuracy) + "\n")
    POSTag_form_evaluation_format.write("Ezafe absence accuracy : " + str(ez_absence_accuracy) + "\n")
    POSTag_form_evaluation_format.write("Total accuracy : " + str(total_accuracy) + "\n")
    POSTag_form_evaluation_format.write("Recall : " + str(recall) + "\n")
    output_test_format.close()
    gold_test_format.close()
    POSTag_form_evaluation_format.close()


if __name__ == "__main__":
    creatingProbabolityModels()
    testBaseLine()
    creatingProbabolityModelsForPOSTag()
    testBaseLineForPOSTag()