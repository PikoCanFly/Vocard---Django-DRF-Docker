

import './index.css';
const { ipcRenderer } = require('electron');

const goButton = document.getElementById("go");
const urlInputField = document.getElementById("url-input");
let url = ""
goButton.addEventListener("click", (event) => {
    event.preventDefault(); // Prevent the default form submission behavior
    url = "http://"+urlInputField.value;
    console.log("url: ", url);

            ipcRenderer.send('update-url', url);

});

console.log('👋 This message is being logged by "renderer.js", included via Vite');
console.log("url", url)