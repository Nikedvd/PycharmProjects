document.getElementById('getJoke').addEventListener('click', function() {
    const apiUrl = "https://api.chucknorris.io/jokes/random";
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            console.log(data.value);
        })
        .catch(error => console.error("Error:", error));
});