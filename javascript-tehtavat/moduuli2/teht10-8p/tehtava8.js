function startVoting() {
    let candidatesCount = parseInt(prompt("Enter the number of candidates:"));
    let candidates = [];
    for (let i = 0; i < candidatesCount; i++) {
        let name = prompt("Name for candidate " + (i + 1) + ":");
        candidates.push({ name: name, votes: 0 });
    }
    let votersCount = parseInt(prompt("Enter the number of voters:"));
    for (let i = 0; i < votersCount; i++) {
        let vote = prompt("Voter " + (i + 1) + ", enter the name of the candidate you vote for:");
        if (vote) {
            let candidate = candidates.find(c => c.name.toLowerCase() === vote.toLowerCase());
            if (candidate) {
                candidate.votes++;
            }
        }
    }
    let winner = candidates.reduce((prev, current) => (prev.votes > current.votes) ? prev : current);
    console.log("The winner is " + winner.name + " with " + winner.votes + " votes.");
    console.log("Results:");
    candidates.forEach(c => console.log(c.name + ": " + c.votes + " votes"));
}