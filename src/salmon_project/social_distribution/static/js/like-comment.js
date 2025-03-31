function send_comment_like(event) {
    event.preventDefault();
    const url = this.action;
    const formData = new FormData(this);

    fetch(url, {
        method: "POST",
        body: formData,
        headers: {
            'X-CSRFToken': formData.get('csrfmiddlewaretoken')
        }
    })
    .then(response => response.json())
    .then(data => {
        const likeCount = this.closest(".comment").querySelector(".like-count");
        likeCount.textContent = parseInt(likeCount.textContent) + data.like_count;
        this.closest(".comment").querySelector("button").classList.toggle("btn-liked");
    })
    .catch(error => {
        console.error("Error:", error);
    });
}

function send_post_like(event) {
    event.preventDefault();
    const url = this.action;
    const formData = new FormData(this);

    fetch(url, {
        method: "POST",
        body: formData,
        headers: {
            'X-CSRFToken': formData.get('csrfmiddlewaretoken')
        }
    })
    .then(response => response.json())
    .then(data => {
        const likeCount = this.closest(".post").querySelector(".like-count");
        likeCount.textContent = parseInt(likeCount.textContent) + data.like_count;
        this.closest(".post").querySelector("button").classList.toggle("btn-liked");
    })
    .catch(error => {
        console.error("Error:", error);
    });
}

function create_comment(event) {
    event.preventDefault();
    const url = this.action;
    const formData = new FormData(this);

    fetch(url, {
        method: "POST",
        body: formData,
        headers: {
            'X-CSRFToken': formData.get('csrfmiddlewaretoken')
        }
    })
    .then(response => response.json())
    .then(data => {
        const author_id = data.author.id.split("/").slice(-1)[0];
        const comment_id = data.id.split("/").slice(-1)[0];
        const commentList = this.closest(".post").querySelector(".comments ul");
        
        const newComment = document.createElement("li");
        newComment.classList.add("comment");
        
        const commentSpan = document.createElement("span");
        commentSpan.innerText = `${data.author.displayName}: ${data.comment}`;
        newComment.appendChild(commentSpan);
        
        const likeForm = document.createElement("form");
        likeForm.method = "post";
        likeForm.action = `/api/authors/${author_id}/comments/${comment_id}/liked/`;
        likeForm.classList.add("like-comment");
        
        const csrfToken = document.createElement("input");
        csrfToken.type = "hidden";
        csrfToken.name = "csrfmiddlewaretoken";
        csrfToken.value = formData.get('csrfmiddlewaretoken');
        likeForm.appendChild(csrfToken);
        
        const typeInput = document.createElement("input");
        typeInput.type = "hidden";
        typeInput.name = "type";
        typeInput.value = "like";
        likeForm.appendChild(typeInput);
        
        // Create the icon button for liking
        const likeButton = document.createElement("button");
        likeButton.type = "submit";
        likeButton.classList.add("like-icon-btn");
        
        
        const likeIcon = document.createElement("img");
        // Use the static path for the heart icon:
        likeIcon.src = "/static/img/heart.png"; 
        likeIcon.alt = "Like";
        likeIcon.classList.add("like-icon");
        likeButton.appendChild(likeIcon);
        
        // Append the like button to the like form
        likeForm.appendChild(likeButton);
        
        // Create the span for the like text and count (non-clickable)
        const likeText = document.createElement("span");
        likeText.classList.add("like-text");
        // Set inner HTML to bold "Likes:" and the count
        likeText.innerHTML = ' <strong class="like-count">0</strong>';
        likeForm.appendChild(likeText);
        
        // Add event listener to the like form for the bubbly animation and like functionality
        likeForm.addEventListener("submit", send_comment_like);
        
        
        newComment.appendChild(likeForm);
        
        // Append the new comment to the comment list
        commentList.appendChild(newComment);
        
        // Clear the comment textarea
        this.querySelector("textarea").value = "";
    })
    .catch(error => {
        console.error("Error:", error);
    });
}


document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll(".like-comment").forEach(function(form) {
        let likes = form.getAttribute('likes');
        let author = form.getAttribute('author');
        
        if (likes.includes(author)) {
            form.querySelector("button").classList.add("btn-liked");
        }

        form.addEventListener("submit", send_comment_like);
    });

    document.querySelectorAll(".like-post").forEach(function(form) {
        let likes = form.getAttribute('likes');
        let author = form.getAttribute('author');
        
        if (likes.includes(author)) {
            form.querySelector("button").classList.add("btn-liked");
        }

        form.addEventListener("submit", send_post_like);
    });

    document.querySelectorAll(".comment-form").forEach(function(form) {
        form.addEventListener("submit", create_comment);
    });
});
