from string import punctuation
from collections import Counter

class FileFreqCounter:
    def __init__(self,path):
        self.path = path
        self.counter = Counter()
        self.symbols = set(punctuation)

    def read_lines(self):
        with open("story.txt", "r") as f:
            return[line.replace("\n", "") for line in f]

    def remove_punctuation(self,sentence):
        for ch in sentence:
            if ch in self.symbols:
                sentence = sentence.replace(ch, " ")
        return sentence

    def calculate_freq(self):  # liczymy frequence słów
        sentences = self.read_lines()
        self.counter = Counter()
        for sentence in sentences:
            cleaned = self.remove_punctuation(sentence)
            self.counter += Counter(cleaned.lower().split())
        return self.counter

    def most_common(self,n=3):
        self.calculate_freq()
        return  self.counter.most_common(n)


if __name__ == "__main__":
    file_counter = FileFreqCounter("story.txt")
    print(file_counter.most_common(4))
#### with open("story.txt", "r") as f: -> otwierane plików - open i close w jednej linijce
    #f = open("story.txt", "r")
    #for line in f:
        #print(line)
    #lines = [line.replace("\n","") for line in f]
    #print(calculate_freq(lines))

    #print(calculate_freq("this is a simple text"))

    #f.close() #komenda do zatrzymania czytania
