import urllib2

class Speech(object):
    def __init__(self, text):
        self.text = text
        self.create_speech(self.text)
        
    def hello(self, text):
        self.create_speech()

    def filter_spaces(self):
        return self.text.replace(" ", "%20")

    @staticmethod
    def create_speech(self):
        url_speak = "http://127.0.0.1:8000/speech?text=" + self.filter_spaces()
        response = urllib2.urlopen(url_speak)
        print response
    

if __name__ == "__main__":
    Speech('Hello World!')
