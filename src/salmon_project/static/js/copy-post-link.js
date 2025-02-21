// Script for copying "data-copy" content of "copy-post-link" buttons to clipboard

document.addEventListener("DOMContentLoaded", function () {
    let buttons = document.querySelectorAll(".copy-post-link");
    buttons.forEach(button => {
        button.addEventListener("click", function () {
            let textToCopy =  button.getAttribute("data-copy");
            navigator.clipboard.writeText(textToCopy).then(() => {
                alert("Link to post copied!");
            });
        });
    });
});