class text:
    '''analyze text using stats'''
    def __init__(self,filename):
        self.fname = filename
        with open('text.txt') as f:
            self.lines = f.readlines()
        self.f = open(filename,"r")

    def fileLenggth(self):
        n = len(self.lines)
        return(n)
        
    def stanzaCount(self):
        n = 0 
        for line in self.lines:
            line = line.strip()
            if line == '':
                n =n +1
            c = n+1
        return c

    def fileLength0(self):
        n = 0
        for line in self.lines:
            print(line, len(line))
            if line != '':
                n = n +1
#            if len(line) == 0:
        return(n)

    def getSentences(self):
        with open(self.fname) as f:
            fullText = f.read()
        fullText = fullText.replace('/n', ' ')
        self.sentences = fullText.split('.')

    def countWord(self,word):
        with open(self.fname) as f:
            fulltext = f.read()
            fulltext = fulltext.replace("\n", '')
            split_text = fulltext.split(" ")
            n = 0
            for s in split_text:
                if word.lower() in s.lower():
                    n += 1
            return(n)


    def critique(self,word):
        # with open(self.fname) as f:
        #     fullText = f.read()
        if self.countWord(word) > 1:
            print('adicto a las drogas')
        if self.countWord(word) > 1:
            print("Good for you")
    
    def critique2(self):
        db = {
            'DRugs': 'Adicto a las drogas',
            'alcohol': 'good for you'
        }
        for word in db:
            if self.countWord(word) > 1:
                print(db[word])
        # if self.countWord(word) > 1:
        #     print('adicto a las drogas')
        # if self.countWord(word) > 1:
        #     print("Good for you")

    def multiCrit(self):
        with open(self.fname) as f:
            fulltext = f.read()
            fulltext = fulltext.replace("\n", '')
            split_text = fulltext.split(". ")
            w = []
            for s in split_text:
                if ("drugs" in s) and ("children" in s):
                    # print("Good for the chilren")
                    w.append("Good for the chilren")
                if ("children" in s) and ("vulnerable" in s):
                    # print("Children should never be in a vulnerable situation.")
                    w.append('Children should never be in a vulnerable situation.')
                    break
            return w


