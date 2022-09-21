#include <fstream>
#include <iostream>
#include <string>
 
using namespace std;

string readFormFile(string);
string addTags(string);
void addToIndexPage(string);

class Tag {
    public:
        string tag_open;
        string tag_close;
        string placeholder;

        Tag(string tag_open_set, string tag_close_set, string placeholder_set) {
            tag_open = tag_open_set;
            tag_close = tag_close_set;
            placeholder = placeholder_set;
        }

};
 
int main()
{
    string* fileNames = {
        new string("../TextFiles/index.txt")
        };
    
    for (long unsigned int i = 0; i < sizeof(fileNames)/sizeof(string*); i++) {

        string fileName = fileNames[i];

        string rawText = readFormFile(fileName);

        string parsedText = addTags(rawText);

        addToIndexPage(parsedText);
    }

    return 0;
}

string addTags(string rawText) {

    Tag h2 = new Tag("<h2>", "</h2>", "!#")
    Tag h3 = new Tag("<h3>", "</h3>", "!@")

    return ;
}

void addToIndexPage(string parsedText) {
    return;
}

void writeToFile(string fileName, string textToWrite) {
    return;
}

string readFormFile(string fileName) {

    string line;
    string text;

    ifstream myfile (fileName);

    if (myfile.is_open()) {

        while ( getline (myfile,line) ) {
            text += line + '\n';
        }

        myfile.close();
    } else 
        cout << "Unable to open file"; 

    return text;
}