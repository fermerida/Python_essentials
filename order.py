class order:
        
    def __init__(self, string):
        self.string = string
    
    def do(self):

        words = self.string.split()
        # sort the list
        words.sort()
        print("The sorted words are:")
        for word in words:
            print(word)

