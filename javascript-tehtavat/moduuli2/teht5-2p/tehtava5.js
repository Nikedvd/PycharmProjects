function getNumbers() {
    let numbers = [];
    let input;
    while (true) {
        input = prompt("Enter a number:");
        if (input === null) break;
        if (numbers.includes(Number(input))) {
            alert("The number " + input + " you gave has already been given.");
            break;
        }
        numbers.push(Number(input));
    }
    numbers.sort((a, b) => a - b);
    console.log(numbers);
}