function sideBar() {

    let sideBar = document.getElementById("sideBar");

    let html = "";

    html += `<h1 style="margin-bottom: 0;">`
    + `<a href="index.html">`
    + `Zanes Fitness Guide</a></h1>`

    html += `<div style="padding: 10px; padding-top: 0;">`

    html += `<h2 style='text-align: center; text-decoration: underline'>Contents</h2>`

    // Adding the headings to the side bar to make it an effective page index.
    // ADD LINKS LATER
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

        /*
        // the h1 is reserved for the title of the welcome message
        if (currentHeading.localName == 'h1')
            continue;
        */

        html 
        += '<' + headingTag + ' class="sideBarHeading">'
        + '-' + headingText
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

    console.log(links[0])

    html = '<ul class="sideBarLink">'

    for (let catagory in links) {

        html += `<li><a href="${links[catagory]}">${catagory}</a></li>`
    }

    html += '</ul>'

    return html
}