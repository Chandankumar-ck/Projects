// Get references to the HTML elements for hours, minutes, and seconds
let hrs = document.getElementById("hrs"); // Element displaying hours
let min = document.getElementById("min"); // Element displaying minutes
let sec = document.getElementById("sec"); // Element displaying seconds

// Update the time displayed every second
setInterval(() => {
    // Create a new Date object to get the current time
    let presentTime = new Date();

    // Get hours, minutes, and seconds from the Date object
    // Add leading zero if the number is less than 10 for formatting
    let hours = (presentTime.getHours() < 10 ? "0" : "") + presentTime.getHours();
    let minutes = (presentTime.getMinutes() < 10 ? "0" : "") + presentTime.getMinutes();
    let seconds = (presentTime.getSeconds() < 10 ? "0" : "") + presentTime.getSeconds();

    // Update the innerHTML of the respective elements to display the current time
    hrs.innerHTML = hours;   // Update hours element
    min.innerHTML = minutes; // Update minutes element
    sec.innerHTML = seconds; // Update seconds element

}, 1000); // Interval set to 1000 milliseconds (1 second)
