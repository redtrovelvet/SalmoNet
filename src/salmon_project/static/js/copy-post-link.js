// Script for copying "data-copy" content of "copy-post-link" buttons to clipboard

document.addEventListener("DOMContentLoaded", function () {
    // Listen for both the old and the new button classes
    let buttons = document.querySelectorAll(".copy-post-link, .share-icon-btn");
    buttons.forEach(button => {
        button.addEventListener("click", function () {
            let textToCopy = button.getAttribute("data-copy");
            const textArea = document.createElement("textarea")
            textArea.value = textToCopy
            textArea.style.position = "absolute";
            textArea.style.left = "-999999px";
            document.body.prepend(textArea);
            textArea.select()
            document.execCommand('copy')
            textArea.remove()
            alert("Link to post copied!");
        });
    });
});
