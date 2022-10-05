from Tags import H, P, Ul
from fileIO import *

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

    h2 = H("<h2>", "</h2>", "~!")
    h3 = H("<h3>", "</h3>", '~@')
    p  = P()
    ul = Ul()

    text = readFromFile(fileName)
    
    text = h2.insert_tag(text)
    text = h3.insert_tag(text)
    text = ul.insert_tag(text)
    text = p.insert_tag(text)
    
    text = insert_heading_name_and_id(text)

    text = insert_sub_heading(text)

    return text

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

def insert_sub_heading(text, start_index):
    # if encounter heading with the same number, do the open closing div thing
    # otherwise recursive call the function recursively.

    opening_div = '<div class="heading">'
    closing_div = '</div>'

    insertion_count = 0
    while True:
        start_index = text.find("<h", index)

        if start_index == -1:
            text += closing_div
            break

        if (insertion_count == 0):
            text = text[:start_index] + opening_div + text[start_index:]
            start_index += len(opening_div) + 4
        else:
            text = text[:start_index] + closing_div + opening_div + text[start_index:] 
            start_index += len(closing_div) + len(opening_div) + 4

        insertion_count += 1

    return text