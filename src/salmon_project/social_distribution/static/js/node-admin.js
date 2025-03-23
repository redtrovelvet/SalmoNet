document.addEventListener('DOMContentLoaded', function() {
    setInfoForm = document.getElementById("set-info");
    addNodeForm = document.getElementById("add-node");


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
        })
        .catch(error => {
            console.error("Error:", error);
        });
    });

    addNodeForm.addEventListener("submit", function(event) {
        event.preventDefault();
        let address = document.getElementById("node_address").value;
        if (!address.startsWith("http://") && !address.startsWith("https://")) {
            address = "http://" + address;
            this.querySelector("#node_address").value = address;
        }

        // TODO: make sure the port is included in the address
        let fetch_url = address + ":8000/api/connect/";
        
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
            })
            .catch(error => {
                console.error("Error:", error);
            });
        })
        .catch(error => {
            console.error("Error:", error);
        });
    });
});
        