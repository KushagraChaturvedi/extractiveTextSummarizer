# importing libraries.
import spacy as cy
from string import punctuation
import re

# loading English module and creating nlp object.
nlp = cy.load('en_core_web_sm')

# input  text and process to remove spaces and format specifier.
rawText = '''Consciousness is everything you experience. It is the tune stuck in your head, the sweetness of chocolate mousse, the throbbing pain of a toothache, the fierce love for your child and the bitter knowledge that eventually all feelings will end.

The origin and nature of these experiences, sometimes referred to as qualia, have been a mystery from the earliest days of antiquity right up to the present. Many modern analytic philosophers of mind, most prominently perhaps Daniel Dennett of Tufts University, find the existence of consciousness such an intolerable affront to what they believe should be a meaningless universe of matter and the void that they declare it to be an illusion. That is, they either deny that qualia exist or argue that they can never be meaningfully studied by science.

If that assertion was true, this essay would be very short. All I would need to explain is why you, I and most everybody else is so convinced that we have feelings at all. If I have a tooth abscess, however, a sophisticated argument to persuade me that my pain is delusional will not lessen its torment one iota. As I have very little sympathy for this desperate solution to the mind-body problem, I shall move on.
The majority of scholars accept consciousness as a given and seek to understand its relationship to the objective world described by science. More than a quarter of a century ago Francis Crick and I decided to set aside philosophical discussions on consciousness (which have engaged scholars since at least the time of Aristotle) and instead search for its physical footprints. What is it about a highly excitable piece of brain matter that gives rise to consciousness? Once we can understand that, we hope to get closer to solving the more fundamental problem.'''
rawText = re.sub("  " and "\n" and "\t",'',rawText)

# getting stopwords of english language.
stopWords = list(cy.lang.en.stop_words.STOP_WORDS)

# tokenizing rawtext in word and sentences.
doc = nlp(rawText)
# print(doc[1])
# print(type(doc))
rawWords = [word.text for word in doc]
rawSents = [sent.text for sent in doc.sents]


# creating Word frequency duct.
wordFrequency = {}
for word in rawWords:
  if word.lower() not in stopWords:
    if word not in punctuation:
      if word not in wordFrequency.keys():
        wordFrequency[word] = 1
      else:
        wordFrequency[word] += 1

# normalizing word frequency
maxWordFrequency = max(wordFrequency.values())
for word in wordFrequency.keys():
  wordFrequency[word] = wordFrequency[word]/maxWordFrequency

# sentences ke socre ki dict.
sentsScore = {}
for sent in rawSents:
  for word in wordFrequency.keys():
    if word.lower() in sent.lower():
      if sent not in sentsScore.keys():
        sentsScore[sent] = wordFrequency[word]
      else:
        sentsScore[sent] += wordFrequency[word]

# sorting dict by value
sents = [keys for keys in sorted(sentsScore, key = sentsScore.get,reverse = True)]
range = (len(sentsScore))//3
# print(sentsScore)

# printing the summarized text
for sent in sents[:range]:
  print(sent)
