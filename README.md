# extractiveTextSummarizer.
Extractive text summarization using python using spacy module.
# Approch
  1 Text cleansing and processing.<br />
     &ensp; removing stopwords, punctuation, and making words in lowercase.<br />
  2 Word tokenization.<br />
    &ensp;tokenize processed data by words<br />
  3 Make word frequency table.<br />
    &ensp;Count frequency of each word and divide it with highest frequency(to get normalize frequency data.)<br />
  4 Sentence tokenize.<br />
    &ensp;Tokenize sentence from orignal text.<br />
  5 Return summariezed text.<br />
    &ensp;Calculate score of each sentence by its word frequency and return top 30% sentence.<br />
    
