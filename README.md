# Persian Ezafe Recognition

In  Persian  language,  Ezafe  is  an  unstressed short vowel /-e/ (or /-ye/ after vowels) which is used  to  link  two  words  in  some  contexts. Although  Ezafe  is  an  important  part  of  the Persian  phonology  and  morphology,  it  does  not have a specific character representation, and so is not usually written.However, it is pronounced as a short vowel /e/. Sometimes, for disambiguation purposes  it  is  preferred  to  explicitly  mark  its presence by a written symbol (the diacritic __Kasre__) after some words in order to facilitate the correct pronunciation. 

The  most  important  application  of  Ezafe recognition is a text to phoneme tool for Text To Speech  (__TTS__)  Systems.  Other  applications include  Ezafe  recognition  for  identifying  the dependency  of  a  word  in  a  Noun  Phrase. (Oskueepour, 2011,Mavvaji, and Eslami, 2012)

## My Approach

In this research I examine a [factored translation model](http://www.statmt.org/moses/?n=Moses.CodeGuideFactors) which is an extension of phrase based SMT model. It is proved that in machine translation prob-lems, this model can provide better performance with respect to traditional phrase based SMT systems.

To implementation this, I used [Moses](http://www.statmt.org/moses/?n=Moses.Overview), an implementation of the __statistical__ (or data-driven) approach to machine translation (MT).

## Implementation

### Step 1
Create parallel corpuses as inputs to a machine translation system. The `test.en` file that has factore's feature in it and `test.fa` file that has `EZ` mark. This tow file most be cleaned. for cleaning operation I used moses instruction, such as: 

` /home/alireze/mosesdecoder/scripts/training./clean-corpus-n.perl /home/test/test en fa clean-corpus 1 100 `

### Step 2
Building a [Language Model](http://www.statmt.org/moses/?n=FactoredTraining.BuildingLanguageModel) from `test.fa` file with below command:

` /home/alireza/mosesdecoder/bin/lmplz -o 3 -S 90% -T /tmp < /home/test/test.fa > /home/test/model.lm `

with this command, I used [KenLM language model toolkit](http://kheafield.com/code/kenlm/), which is included in Moses by default. So, language model type in `moses.ini` file must be changed to `KENLM`.

### Step 3
[Factored Training](http://www.statmt.org/moses/?n=FactoredTraining.FactoredTraining), For training a factored model, I will specify some additional training parameters:

```
/home/alireza/mosesdecoder/scripts/training/train-model.perl -corpus /home/test/test -f en -e fa -external-bin-dir '/bin/' -root-dir '/home/test/' -lm 0:3:/home/test/model.lm -alignment grow-diag-final-and -reordering msd-bidirectional-fe -parallel -sort-parallel 5 -mgiza -mgiza-cpus 3 -cores 6 -translation-factors 0,1,2,-0 -reordering-factors 0-0 -decoding-steps t0
```

### Step 4

As with the LM, the phrase table can be processed and read from disk on-demand instead of being loaded in its entirety into memory. To binarize phrase tables, I used moses instruction, such as:

` gzip -cd /home/test/model/phrase-table.gz | LC_ALL=C sort | /home/alireza/mosesdecoder/bin/processPhraseTable -ttable 0 0 - -nscores 5 -out /home/test/model/phrase-table`

### Step 5 

Edit `moses.ini` file:

```
	* Change language model type from "IRSTLM" to "KENLM".
	* Change "PhraseDictionaryMemory" to "PhraseDictionaryBinary".
	* Remove the ".gz" suffix from the path of the PhraseDictionary feature.
```

### Step 6

in this step we can translate input file with below instruction: 

`/home/alireza/mosesdecoder/bin/moses -f /home/test/model/moses.ini < /home/test/input.txt > /home/test/translate.txt` 

## Tasks

* ~~tests with different size of sentence in test.~~
* ~~tests with different size of corpus for train.~~
* ~~feature selection to find best features for factored model~~

## TODO

* [X] write the results. 
* [ ] make codes readable.
* [ ] cleanup code and write commands.
