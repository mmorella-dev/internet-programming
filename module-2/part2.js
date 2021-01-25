// EVENT HANDLERS FOR ASSIGNMENT 2 PART 2

const tableEl = document.querySelector("[data-class~=sort-table]");

// Updates the length value
const handleCellInput = (el) => {
  const length = el.value.length;
  const lengthEl = el.closest("[data-class~=row]").querySelector("[data-class~=length]");
  lengthEl.innerText = length;
}

// Create a new cell, or unhide the most recently hidden one
const handleAddCell = () => {
  let hiddenRows = tableEl.querySelectorAll("[data-class~=row].hide");
  let visibleRows = tableEl.querySelectorAll("[data-class~=row]:not(.hide)");
  // if there is a hidden row,
  if (hiddenRows.length > 0) {
    // unhide the recently hidden row cell
    hiddenRows[0].classList.remove("hide");
  } else {
    // create a new row element.
    let index = visibleRows.length;
    let template = document.createElement('template');
    template.innerHTML = `<tr data-class="row">
    <td data-class="index">${index}</td>
    <td><input data-class="input" type="text" oninput="handleCellInput(this)"></td>
    <td><output data-class="length">0</output></td></tr>`
      .trim();
    let newRow = template.content.firstChild;
    tableEl.appendChild(newRow);
  }
}

// Hide the last row
const handleRemoveCell = () => {
  let rows = tableEl.querySelectorAll("[data-class~=row]:not(.hide)");
  if (rows.length > 1)
    rows[rows.length - 1].classList.add("hide");
}

// Reorder the table by string length
const handleSortTable = () => {
  const inputs = tableEl.querySelectorAll("[data-class~=row]:not(.hide) [data-class~=input]");
  let strings = [...inputs].map(el => el.value);
  strings = strings.sort((a, b) => b.length - a.length);
  inputs.forEach((el, i) => {
    el.value = strings[i];
    handleCellInput(el);
  });
}
// When the page loads, create one empty row.
if (tableEl) {
  handleAddCell();
}