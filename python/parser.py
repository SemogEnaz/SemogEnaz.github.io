
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

    def __init__(self, tag_open, tag_close):
        super().__init__(tag_open, tag_close, None)

    def insert_tag(self, text):

        index = text.find('\n', 0)
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

        # text = self.insert_br(text)

        return text

    def check_if_target(self, index: int, text) -> bool:

        is_tag = text[index+1] == '<'
        is_double_nl = text[index+1] == '\n'
        is_placeholder = text[index+1] == '~'

        is_target = not (is_tag or is_double_nl or is_placeholder)
        
        return is_target

    def insert_br(self, text):
        # If a closing p tag is followed by an opening p tag after ' ' & '\n'
        # then insert a <br> right before the opening p tag

        # TODO: insert behind the closing p tag instead

        index = 0

        while index != -1:

            index = text.find("</p>", index)

            if index == -1:
                continue

            index += 4

            while text[index+1] == ' ' or text[index+1] == '\n':
                index += 1

            index += 1

            if text[index:index+3] == '<p>':
                text = text[:index] + "<br>" + text[index:]

        return text

def main():
    key = "<div id=\"main\">"

    htmlFile = "../index.html"

    clean_file(htmlFile, key)

    text = generate_html()

    insertHTML(htmlFile, text, key)

def clean_file(fileName, key) -> None:

    #end_string = "\n" + (" " * indentation of key)

    html = readFromFile(fileName)

    index_start = html.find(key)
    index = index_start
    
    if index == -1:
        return

    space_counter = 0

    while True:
        if index > 0:

            if html[index-1] == '\n':
                break
            elif html[index-1] == " ":
                space_counter += 1
                index -= 1
            else:
                print("ERROR, erronious use of parser.\nKey must be placed after newline!!!")
                return

    end_div = '\n' + " " * space_counter + "</div>"

    index_end = html.find(end_div, index_start)

    if index_end == -1:
        return

    # Removing html in main div
    html = html[:index_start + len(key)] + html[index_end:]

    writeToFile(fileName, html)

def generate_html():
    fileName = "../TextFiles/index.txt"

    h2 = h("<h2>", "</h2>", "~!")
    h3 = h("<h3>", "</h3>", '~@')
    p_ = p("<p>", "</p>")

    text = readFromFile(fileName)
    
    text = h2.insert_tag(text)
    text = h3.insert_tag(text)
    text = p_.insert_tag(text)
    
    text = insert_heading_name_and_id(text)

    return text

def readFromFile(fileName):
    file = open(fileName, 'r')

    text = file.read()

    file.close()

    return text

def writeToFile(fileName, text) -> None:
    file = open(fileName, "w")

    file.write(text)
    
    file.close()

def insertHTML(fileName, text, key) -> None:
    html = readFromFile(fileName)

    index = html.find(key)
    
    if index == -1:
        return

    index += len(key)

    # Adding the html we generated from the text file
    html = html[:index] + text + html[index:]

    writeToFile(fileName, html)

def insert_heading_name_and_id(text):

    heading_count = 0

    index = 0

    while index != -1:
        index = text.find("<h", index)

        if index == -1:
            continue
        
        index += 3

        text = text[:index] + " name=\"heading\" id=\"" + str(heading_count) + "\" " + text[index:]

        heading_count += 1

    return text

main()

