let year = parseInt(prompt("Enter a year:"));
let isLeapYear = (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
let result = isLeapYear ? `${year} is a leap year.` : `${year} is not a leap year.`;
document.body.innerHTML = result;