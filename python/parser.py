
class Tag:

    def __init__(self, tag_open, tag_close, placeholder):
        self.tag_open = tag_open
        self.tag_close = tag_close
        self.placeholder = placeholder

class h(Tag):

    def __init__(self, tag_open, tag_close, placeholder):
        super().__init__(tag_open, tag_close, placeholder)

    def insert_tag(self, text):
        index = 0


        # Replace all occourances of placeholder
        text = text.replace(self.placeholder, self.tag_open)

        while index != -1:

            index = text.find(self.tag_open, index)

            if index == -1:
                continue

            # add a tag_close ahead of the '\n'.
            index = text.find('\n', index)

            text = text[:index] + self.tag_close + text[index:]

        return text;


def main():
    fileName = "../TextFiles/index.txt"

    h2 = h("<h2>", "</h2>", "~!")
    h3 = h("<h3>", "</h3>", '~@')

    text = readFromFile(fileName)
    
    text = h2.insert_tag(text)
    text = h3.insert_tag(text)

    print(text)

def readFromFile(fileName):
    file = open(fileName, 'r')

    text = file.read()

    return text

main()

