from abc import ABC, abstractmethod

class Tag(ABC):

    def __init__(self, tag_open, tag_close, placeholder):
        self.tag_open = tag_open
        self.tag_close = tag_close
        self.placeholder = placeholder

    @abstractmethod
    def insert_tag(self, text):
        pass

class H(Tag):

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

class P(Tag):

    def __init__(self):
        tag_open = "<p>"
        tag_close = "</p>"
        placeholder = None
        super().__init__(tag_open, tag_close, placeholder)

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

class Ul(Tag):

    def __init__(self):
        tag_open = "<ul>"
        tag_close = "</ul>"
        placeholder = "~:"
        self.tag_inner_open = "<li>"
        self.tag_inner_closed = "</li>"
        super().__init__(tag_open, tag_close, placeholder)
        
    def insert_tag(self, text):
        index_start = 0
        index_end = 0
        
        while True:

            # Find the index of the first placeholder
            index_start = text.find(self.placeholder, index_end)

            # Find the index of the next place holder
            index_end = text.find(self.placeholder, index_start+1)

            # If you cant find a pair of placeholders, exit
            if (index_start + index_start == -2):
                break

            # Store the text of the main list and add the inner list tags to it
            inner_list = text[index_start+2: index_end]

            # Add <li></li> tags at the start and end of each line
            inner_list = self.addInnerTags(inner_list)

            # Replace old list with one with inner tags
            text = text[:index_start+2] + inner_list + text[index_end:]

            # Replace placeholder with tags 
            text = text.replace(self.placeholder, self.tag_open, 1)
            text = text.replace(self.placeholder, self.tag_close, 1)

        return text

    def addInnerTags(self, text):
        # Find next line characters and add a open inner tag before it and one after it
        # Add one before the first char and one after the last char
        
        text = self.tag_inner_open + text   # Add behind
        text += self.tag_inner_closed       # Add ahead

        index = 0

        while text.find('\n', index) != -1:
            
            index = text.find('\n', index)

            # Increment index to after double \n and spaces
            if (text[index+1] == '\n'):
                index += 1
                text_closed = text[:index] + self.tag_inner_closed + '<br>'
            else:
                text_closed = text[:index] + self.tag_inner_closed 

            space_count = 0

            while text[index+1] == ' ':
                index += 1
                space_count += 1

            text_open = '\n' + ' '*space_count + self.tag_inner_open + text[index+1:]
            text = text_closed + text_open

            # Increment index by '<\li>\n' string len
            index += 6

        return text
