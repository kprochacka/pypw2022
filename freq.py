def freq(sentence): #liczymy frequence słów
    freq = {}
    for word in sentence.lower().split():
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
        return freq
if __name__ == "__main__":
    print (calculate_freq("this is a simple text"))







