

const api_url = f"https://geocode.search.hereapi.com/v1/geocode?q={qq}&apiKey=A1shZUUaf4D_WTo2UQCmZ4Ut5yezRhWnSDdJTY3qz3w";

async function getapi(url) {
    // Storing response
    const response = await fetch(url);
    
    // Storing data in form of JSON
    var data = await response.json();
    console.log(data);
    if (response) {
        hideloader();
    }
    show(data);
}