// JavaScript shakesspeare Demo
// Jim Skon, Kenyon College, 2021

console.log("Start!");
// Add a click event for the search button
document.querySelector("#search-btn").addEventListener("click", (e) => {
    getMatches();
});


function processResults(results) {
    document.querySelector('#searchresults').innerHTML = results;
}

function clearResults() {
    document.querySelector('#searchresults').innerHTML = "";
}

function getMatches(){
    console.log("getMatches!");
    var searchStr=document.querySelector('#search').value;
    console.log(searchStr);

    // Ignore short requests
    if (searchStr.length < 2) return;

    // Clear the previous results
    document.querySelector('#searchresults').innerHTML = "";

    fetch('/cgi-bin/skon_shakewebpy.py?word='+searchStr, {
	method: 'get'
    })
	.then (response => response.text() )
        .then (data => processResults(data))
	.catch(error => {
	    {alert("Error: Something went wrong:"+error);}
	})
}


