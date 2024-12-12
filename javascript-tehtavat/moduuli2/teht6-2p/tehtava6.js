function rollDie() {
    return Math.floor(Math.random() * 6) + 1;
}

function rollDice() {
    let results = [];
    let roll;
    do {
        roll = rollDie();
        results.push(roll);
    } while (roll !== 6);
    displayResults(results);
}

function displayResults(results) {
    let list = "<ul>";
    for (let result of results) {
        list += "<li>" + result + "</li>";
    }
    list += "</ul>";
    document.getElementById("results").innerHTML = list;
}