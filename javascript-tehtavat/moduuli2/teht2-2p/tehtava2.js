function getParticipants() {
    let numParticipants = prompt("Enter the number of participants you want:");
    let participants = [];
    for (let i = 0; i < numParticipants; i++) {
        let name = prompt("Enter the name of participant " + (i + 1) + ":");
        participants.push(name);
    }
    participants.sort();
    displayParticipants(participants);
}

function displayParticipants(participants) {
    let list = "<ol>";
    for (let participant of participants) {
        list += "<li>" + participant + "</li>";
    }
    list += "</ol>";
    document.getElementById("participantsList").innerHTML = list;
}