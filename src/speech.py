import urllib2

class Speech(object):
    @staticmethod
    def hello(self, text):
        self.create_speech(text)

    @staticmethod
    def filter_spaces(self, text):
        return text.replace(" ", "%20")

    @staticmethod
    def create_speech(self, text):
        url_speak = "http://127.0.0.1:8000/speech?text=" + filter_spaces(text)
        response = urllib2.urlopen(url_speak)
        print response
    

if __name__ == "__main__":
    Speech.hello('Hello World!')
