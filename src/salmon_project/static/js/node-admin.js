document.addEventListener('DOMContentLoaded', function() {
    setInfoForm = document.getElementById("set-info");
    addNodeForm = document.getElementById("add-node");

    setInfoMessage = document.getElementById("set-info-message");
    addNodeMessage = document.getElementById("add-node-message");

    setInfoForm.addEventListener("submit", function(event) {
        event.preventDefault();
        fetch(this.action, {
            method: "POST",
            body: new FormData(this),
            headers: {
                'X-CSRFToken': new FormData(this).get('csrfmiddlewaretoken')
            }
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            location.reload();
            setInfoMessage.textContent = "Information updated successfully.";
            setInfoMessage.style.color = "green";
        })
        .catch(error => {
            console.error("Error:", error);
            setInfoMessage.textContent = "Error updating information.";
            setInfoMessage.style.color = "red";
        });
    });

    addNodeForm.addEventListener("submit", function(event) {
        event.preventDefault();
        let address = document.getElementById("node_address").value;
        let fetch_url = address + "/api/connect/";

        let external = document.getElementById("external").checked;

        if (external) {
            fetch_url = "/api/connect_external/";
            fetch(fetch_url, {
                method: "POST",
                body: new FormData(this),
                headers: {
                    'X-CSRFToken': new FormData(this).get('csrfmiddlewaretoken')
                }
            })
            .then(response => {
                if (response.ok) {
                    location.reload();
                    addNodeMessage.textContent = "Node added successfully.";
                    addNodeMessage.style.color = "green";
                    return response.json();
                }
                throw new Error("Network response was not ok.");
            })
            return;
        }
        
        fetch(fetch_url, {
            method: "POST",
            body: new FormData(this),
            headers: {
                'X-CSRFToken': new FormData(this).get('csrfmiddlewaretoken')
            }
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            }
            throw new Error("Network response was not ok.");
        })
        .then(data => {
            fetch(this.action, {
                method: "POST",
                body: new FormData(this),
                headers: {
                    'X-CSRFToken': new FormData(this).get('csrfmiddlewaretoken')
                }
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                location.reload();
                addNodeMessage.textContent = "Node added successfully.";
                addNodeMessage.style.color = "green";
            })
            .catch(error => {
                console.error("Error:", error);
                addNodeMessage.textContent = "Error adding node.";
                addNodeMessage.style.color = "red";
            });
        })
        .catch(error => {
            console.error("Error:", error);
        });
    });

    document.querySelectorAll(".remove-node").forEach(form => {
        form.addEventListener("submit", function(event) {
            event.preventDefault();
            fetch(this.action, {
                method: "POST",
                body: new FormData(this),
                headers: {
                    'X-CSRFToken': new FormData(this).get('csrfmiddlewaretoken')
                }
            })
            .then(response => {
                if (response.ok) {
                    return response.json();
                }
                throw new Error("Network response was not ok.");
            })
            .then(data => {
                console.log(data);
                location.reload();
            })
            .catch(error => {
                console.error("Error:", error);
            });
        });
    });
});
        