function sideBar() {

    let sideBar = document.getElementById("sideBar");

    let html = "";

    html += `<h1 style="margin-bottom: 0;">`
    + `<a href="index.html">`
    + `Zanes Fitness Guide</a></h1>`

    html += `<div style="padding: 10px; padding-top: 0;">`

    html += `<h2 class='sideBarTitle'>Contents</h2>`

    html += getHeadings();

    html += getLinksToOtherPages();

    html += `</div>`

    sideBar.innerHTML = html;
    
}

function getHeadings() {
/*
    This function will get a list of objects that have the headings in them. The list obj's are
    pretty comprenhsive so we index the innerText and return that to make the sideBars navigation

       args: None
    reuturn: HTML that will be used to make the naviagtion part of side bar
*/
    
    let headings = document.getElementsByName("heading");

/*
    console.log(headings[0].innerText);     // gives inner text
    console.log(headings);                  // gives list of "heading" objs
    console.log(headings[0].localName);     // gives tag
*/

    let html = "";

    let currentHeading = "";
    let headingText = "";
    let headingTag = "";

    for (let i = 0; i < headings.length; i++) {

        currentHeading = headings[i]

        headingText = currentHeading.innerText;
        headingTag = currentHeading.localName;

        if (headingTag == 'p')
            headingTag = 'h2'

        html
        += '<' + headingTag + ' class="sideBarPageIndex">'
            + `<a href='#` + i + `'>- ` + headingText + `</a>`
        + '</' + headingTag + '>';
    
    }

    return html;
}

function getLinksToOtherPages() {

    links = {
        'Pull': 'pull.html', 
        'Push': 'push.html', 
        'Legs': 'legs.html', 
        'Diet': 'diet.html'
    }

    html = ""

    html += `<h2 class="sideBarTitle";">Links</h2>`

    html += '<ul class="sideBarLink">'

    for (let catagory in links) {

        html += `<li><a href="${links[catagory]}">${catagory}</a></li>`
    }

    html += '</ul>'

    return html
}
