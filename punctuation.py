class punct:
    def __init__(self, string):
        self.string = string
    

    def do(self):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

        wpunct = ""
        for char in self.string:
            if char not in punctuations:
                wpunct = wpunct + char

        # display the unpunctuated string
        print(wpunct)