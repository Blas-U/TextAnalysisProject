class text:
    '''analyze text using stats'''
    def __init__(self,filename):
        self.fname = filename
        with open('terence.txt') as f:
            self.lines = f.readlines()
        self.f = open(filename,"r")

    def fileLength(self):
        n = len(self.lines)
        return(n)

