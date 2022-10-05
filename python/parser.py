from editHTML import *

def main():
    key = "<div id=\"main\">"

    htmlFile = "../index.html"

    clean_file(htmlFile, key)

    text = generate_html()

    insertHTML(htmlFile, text, key)

main()