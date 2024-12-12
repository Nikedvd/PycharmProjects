function getDogNames() {
    let dogNames = [];
    for (let i = 0; i < 6; i++) {
        let name = prompt("Enter the name of dog " + (i + 1) + ":");
        dogNames.push(name);
    }
    dogNames.sort().reverse();
    displayDogNames(dogNames);
}

function displayDogNames(dogNames) {
    let list = "<ul>";
    for (let name of dogNames) {
        list += "<li>" + name + "</li>";
    }
    list += "</ul>";
    document.getElementById("dogNamesList").innerHTML = list;
}