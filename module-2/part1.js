// STRING PROGRAMS

/**
* Verbosely squares a number.
* As a side effect, logs "The square of N is N^2."
* @param {Number} n a number to square.
* @returns {Number} the square of n.
*/
const squareNumber = (n) => {
  const square = Math.pow(n, 2);
  console.log(`The square of ${n} is ${square}.`);
  return square;
}

/**
* @param {String} str A string with at least one character.
* @returns {String} the input string, but all succeeding occurrences of
* its first character have been replaced with '*'
*/
const fixStart = (str) => {
  const  first = str.charAt(0);
  return first + str.slice(1).replaceAll(first, '*');
}


/**
* Finds the first appearance of the substring 'not' and 'bad'.
* If the 'bad' follows the 'not', then it should replace the whole 'not'...'bad'
* @params {String} str
* @returns {String}
*/
const notBad = (str) => str.replace(/not.*bad/g, "good");


// EVENT HANDLER

/**
 * Execute a function using the `value` attribute of `<input id="elementId">`.
 * The result is stored in `<output for="elementId">`
 * @param {String} elementId The ID of an input element
 * @param {(val: String) => String} func The function to execute
 */
const handleStringOperation = (elementId, func) => {
  const inputEl = document.getElementById(elementId);
  const outputEl = document.querySelector(`output[for=${elementId}]`);
  if (inputEl.value && outputEl) {
    outputEl.innerText = func(inputEl.value);
  }
}