let numberOfDice = parseInt(prompt("Enter the number of times you want to roll the dice:"));
let sum = 0;
for (let i = 0; i < numberOfDice; i++) {
    sum += Math.floor(Math.random() * 6) + 1;
}
document.body.innerHTML = `The sum of the all your dice's is: ${sum}`;