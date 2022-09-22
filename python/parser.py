
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

        return text


class p(Tag):

    def __init__(self, tag_open, tag_close, placeholder):
        super().__init__(tag_open, tag_close, placeholder)

    def insert_tag(self, text):
        index = index = text.find('\n', 0)
        to_set_open_tag = True

        while index != -1 and index+1 != len(text):

            # Checks if the character in next index for non '<', '\n' or '~'
            is_target = self.check_if_target(index, text)
            
            if is_target and to_set_open_tag:
                # Check for spaces ahead of '\n' and remove them
                while text[index+1] == " ":
                    index += 1

                if not self.check_if_target(index, text):
                    continue

                text = text[:index+1] + self.tag_open + text[index+1:]
                to_set_open_tag = False
            elif not to_set_open_tag:
                text = text[:index] + self.tag_close + text[index:]
                to_set_open_tag = True

            index = text.find('\n', index+1)

        return text

    def check_if_target(self, index: int, text) -> bool:

        is_tag = text[index+1] == '<'
        is_double_nl = text[index+1] == '\n'
        is_placeholder = text[index+1] == '~'

        is_target = not (is_tag or is_double_nl or is_placeholder)
        
        return is_target

def main():
    fileName = "../TextFiles/index.txt"

    h2 = h("<h2>", "</h2>", "~!")
    h3 = h("<h3>", "</h3>", '~@')
    p_ = p("<p>", "</p>", "")

    text = readFromFile(fileName)
    
    text = h2.insert_tag(text)
    text = h3.insert_tag(text)
    text = p_.insert_tag(text)

    print(text)

def readFromFile(fileName):
    file = open(fileName, 'r')

    text = file.read()

    return text

main()

