class ExtractiveSummarizer():
    def __init__(self, raw_text = None, file_name = None):
        if raw_text != None:
            self.raw_text = raw_text
        elif file_name != None:
            try:
                with open(file_name, 'r', encoding='utf-8') as f:
                    self.raw_text = f.read()
            except FileNotFoundError:
                self.raw_text = None
                print('File not found')
        else:
            self.raw_text = None


    def tokenize(self):
        if self.raw_text == None:
            return 'No text was Provided at the time of object creation to tokenize!!!!...'
        else:
            import spacy
            nlp = spacy.load('en_core_web_sm')
            text = self.raw_text
            special_chars = ('~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', ';', ':', '"', "'", ',', '<', '.', '>', '?', '/', '\\', '|', '\n')
            for char in special_chars:
                if char in text:
                    text = text.replace(char, ' ')
            rawWords = [word for word in text.split()]
            rawSents = [sent.text for sent in nlp(self.raw_text).sents]
            return rawWords, rawSents
    def wordFrequency(self, rawWords):
        from spacy.lang.en.stop_words import STOP_WORDS
        wordFrequency = {}
        for word in rawWords:
            if word.lower() not in STOP_WORDS:
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
    def summarize(self, n: int):
        # text = self.raw_text
        summary = ''
        # Text preprocessing.
        # replace = ['\n', '  ', '\t']
        # for rpl in replace:
        #     if rpl in text:
        #         text = text.replace(rpl, ' ')
        # getting words and sentences.
        rawWords, rawSents = self.tokenize()

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
                    summary += f'{sent.strip()}\n'
        except:
            print('Enter proper value for n')

        # Writing to a file
        with open('summary.txt', 'w') as f:
            f.write(summary)

        return summary

if __name__ == '__main__':
    str = '''Consciousness is everything you experience. It is the tune stuck in your head, the sweetness of chocolate mousse, the throbbing pain of a toothache, the fierce love for your child and the bitter knowledge that eventually all feelings will end.

            The origin and nature of these experiences, sometimes referred to as qualia, have been a mystery from the earliest days of antiquity right up to the present. Many modern analytic philosophers of mind, most prominently perhaps Daniel Dennett of Tufts University, find the existence of consciousness such an intolerable affront to what they believe should be a meaningless universe of matter and the void that they declare it to be an illusion. That is, they either deny that qualia exist or argue that they can never be meaningfully studied by science.

            If that assertion was true, this essay would be very short. All I would need to explain is why you, I and most everybody else is so convinced that we have feelings at all. If I have a tooth abscess, however, a sophisticated argument to persuade me that my pain is delusional will not lessen its torment one iota. As I have very little sympathy for this desperate solution to the mind-body problem, I shall move on.
            The majority of scholars accept consciousness as a given and seek to understand its relationship to the objective world described by science. More than a quarter of a century ago Francis Crick and I decided to set aside philosophical discussions on consciousness (which have engaged scholars since at least the time of Aristotle) and instead search for its physical footprints. What is it about a highly excitable piece of brain matter that gives rise to consciousness? Once we can understand that, we hope to get closer to solving the more fundamental problem.'''
    sum = ExtractiveSummarizer(raw_text=str)
    print(sum.summarize(4))












