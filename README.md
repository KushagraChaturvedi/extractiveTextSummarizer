# extractiveTextSummarizer
Extractive text summarization using python using spacy module.
# Approch
  1 Text cleansing and processing.
    removing stopwords, punctuation, and making words in lowercase.
  2 Word tokenization. 
    tokenize processed data by words
  3 Make word frequency table.
    Count frequency of each word and divide it with highest frequency(to get normalize frequency data.)
  4 Sentence tokenize.
    Tokenize sentence from orignal text.
  5 Return summariezed text.
    Calculate score of each sentence by its word frequency and return top 30% sentence.
    
