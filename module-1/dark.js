// "Dark/Light Mode Switch with CSS Variables" by Ananya Neogi
// https://dev.to/ananyaneogi/create-a-dark-light-mode-switch-with-css-variables-34l8

//determines if the user has a set theme
function detectColorScheme() {
  var theme = "light"; //default to light

  //local storage is used to override OS theme settings
  if (localStorage.getItem("theme")) {
    if (localStorage.getItem("theme") == "dark") {
      var theme = "dark";
    }
  } else if (!window.matchMedia) {
    //matchMedia method not supported
    return false;
  } else if (window.matchMedia("(prefers-color-scheme: dark)").matches) {
    //OS theme setting detected as dark
    var theme = "dark";
  }

  //dark theme preferred, set document with a `data-theme` attribute
  if (theme == "dark") {
    document.documentElement.setAttribute("data-theme", "dark");
  }
}
detectColorScheme();

const toggleSwitchLabel = document.createElement("label");
toggleSwitchLabel.id = "theme-switch"
toggleSwitchLabel.className = "theme-switch"
toggleSwitchLabel.setAttribute("for", "checkbox_theme")
toggleSwitchLabel.innerHTML = `<input type="checkbox" id="checkbox_theme"> Toggle dark mode`
document.body.prepend(toggleSwitchLabel);

//identify the toggle switch HTML element
const toggleSwitch = document.querySelector('#theme-switch input[type="checkbox"]');

//function that changes the theme, and sets a localStorage variable to track the theme between page loads
function switchTheme(e) {
  document.body.classList.add("color-fade");
  // toggleSwitch.disabled = true;
  // setTimeout(() => { toggleSwitch.disabled = false }, 250)
  if (e.target.checked) {
    localStorage.setItem('theme', 'dark');
    document.documentElement.setAttribute('data-theme', 'dark');
    e.target.checked = true;
  } else {
    localStorage.setItem('theme', 'light');
    document.documentElement.setAttribute('data-theme', 'light');
    e.target.checked = false;
  }
}

//listener for changing themes
toggleSwitch.addEventListener('change', switchTheme, false);

//pre-check the dark-theme checkbox if dark-theme is set
if (document.documentElement.getAttribute("data-theme") == "dark") {
  toggleSwitch.checked = true;
}