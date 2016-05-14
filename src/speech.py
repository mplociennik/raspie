import urllib2

class Speech(object):

    def hello(self, text):
        self.create_speech(text)

    def filter_spaces(self, text):
        return text.replace(" ", "%20")

    def create_speech(self, text):
        url_speak = "http://127.0.0.1:8000/speech?text=" + self.filter_spaces(text)
        try:
            response = urllib2.urlopen(url_speak)
            print response
        except Exception as e:
            print e
    

if __name__ == "__main__":
    speech = Speech()
    speech.hello('Hello World!')
