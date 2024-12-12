function getNumbers() {
    let numbers = [];
    let input;
    while (true) {
        input = prompt("Enter a number (when you enter 0 it will stop):");
        if (input === null || input === "0") break;
        numbers.push(Number(input));
    }
    numbers.sort((a, b) => b - a);
    console.log(numbers);
}