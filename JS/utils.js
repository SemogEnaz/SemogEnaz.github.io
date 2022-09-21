function readFromFile(inputFileName) {

    text = ""

    const fs = require('fs')
    
    fs.readFile(inputFileName, (err, data) => {
        if (err) throw err;
    
        text += data.toString();
    })

    return text
}

function parseToHtml(inputText){
    
}