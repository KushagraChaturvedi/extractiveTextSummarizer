class ExtractiveSummarizer():
    def tokenize(self, text):
        import spacy as cy
        nlp = cy.load('en_core_web_sm')
        doc = nlp(text)
        rawWords = [word.text for word in doc]
        rawSents = [sent.text for sent in doc.sents]
        return rawWords, rawSents
    def wordFrequency(self, rawWords):
        from spacy.lang.en.stop_words import STOP_WORDS
        from string import punctuation   
        wordFrequency = {}
        for word in rawWords:
            if word.lower() not in STOP_WORDS:
                if word not in punctuation:
                    if word not in wordFrequency.keys():
                        wordFrequency[word] = 1
                    else:
                        wordFrequency[word] += 1
        maxWordFrequency = max(wordFrequency.values())
        for word in wordFrequency.keys():
            wordFrequency[word] = wordFrequency[word]/maxWordFrequency
        return wordFrequency
    def sentScore(self, rawSents, wordFrequency):
        sentsScore = {}
        for sent in rawSents:
            for word in wordFrequency.keys():
                if word.lower() in sent.lower():
                    if sent not in sentsScore.keys():
                        sentsScore[sent] = wordFrequency[word]
                    else:
                        sentsScore[sent] += wordFrequency[word]
        return sentsScore
    def summarise(self, text: str, n: int) -> str:
        from re import sub
        summary = ''
        # Text preprocessing.
        text = sub("  " and "\n" and "\t",'', text)

        # getting words and sentences.
        rawWords, rawSents = self.tokenize(text)
        
        # Creating word Frequency dictionary.
        wordFrequency = self.wordFrequency(rawWords)
        
        # Scoring sentences as per most frequent words.
        sentScore = self.sentScore(rawSents, wordFrequency)
        
        # sorting sentences as per their scores.
        finalSents = [keys for keys in sorted(sentScore, key = sentScore.get,reverse = True)] 
        
        # creating n line of summary
        try:
            for sent in rawSents:
                if sent in finalSents[:n]:
                    summary += f'{sent}\n\n'
        except:
            print('Enter proper value for n')
        return summary

if __name__ == '__main__':
    str = '''Consciousness is everything you experience. It is the tune stuck in your head, the sweetness of chocolate mousse, the throbbing pain of a toothache, the fierce love for your child and the bitter knowledge that eventually all feelings will end.

            The origin and nature of these experiences, sometimes referred to as qualia, have been a mystery from the earliest days of antiquity right up to the present. Many modern analytic philosophers of mind, most prominently perhaps Daniel Dennett of Tufts University, find the existence of consciousness such an intolerable affront to what they believe should be a meaningless universe of matter and the void that they declare it to be an illusion. That is, they either deny that qualia exist or argue that they can never be meaningfully studied by science.

            If that assertion was true, this essay would be very short. All I would need to explain is why you, I and most everybody else is so convinced that we have feelings at all. If I have a tooth abscess, however, a sophisticated argument to persuade me that my pain is delusional will not lessen its torment one iota. As I have very little sympathy for this desperate solution to the mind-body problem, I shall move on.
            The majority of scholars accept consciousness as a given and seek to understand its relationship to the objective world described by science. More than a quarter of a century ago Francis Crick and I decided to set aside philosophical discussions on consciousness (which have engaged scholars since at least the time of Aristotle) and instead search for its physical footprints. What is it about a highly excitable piece of brain matter that gives rise to consciousness? Once we can understand that, we hope to get closer to solving the more fundamental problem.'''
    sum = ExtractiveSummarizer()
    print(sum.summarise(str, 3))        