function sideBar() {

    let sideBar = document.getElementById("sideBar");

    let html = "";

    html += '<h1>Zanes Fitness Guide</h1>';
    html

    html += getHeadings()

    sideBar.innerHTML = html;
    
}

/*
    This function will get a list of objects that have the headings in them. The list obj's are
    pretty comprenhsive so we index the innerText and return that to make the sideBars navigation

       args: None
    reuturn: HTML that will be used to make the naviagtion part of side bar
*/
function getHeadings() {
    
    let headings = document.getElementsByName("heading");

/*
    console.log(headings[0].innerText);     // gives inner text
    console.log(headings);                  // gives list of "heading" objs
    console.log(headings[0].localName);     // gives tag
*/

    let html = "";

    let currentHeading = "";
    let text = "";
    let tag = "";

    for (let i = 0; i < headings.length; i++) {

        currentHeading = headings[i]

        text = currentHeading.innerText;
        tag = currentHeading.localName;

        if (currentHeading.localName == 'h1')
            continue;

        html += '<' + tag + ' class="sideBarHeading">'
                + '-' + text
                + '</' + tag + '>';
    }

    return html;
}