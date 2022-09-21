function loadContent() {

    rawText = readFromFile('TextFiles/index.txt')

    text = parseToHtml(rawText)

    main = document.getElementById("main")

    main.innerHtml = text
}