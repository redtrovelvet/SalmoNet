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
        likeCount.textContent = data.like_count;
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
        likeCount.textContent = data.like_count;
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
        author_id = data.author.id.split("/").slice(-1)[0];
        comment_id = data.id.split("/").slice(-1)[0];
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

        const type = document.createElement("input");
        type.type = "hidden";
        type.name = "type";
        type.value = "like";
        likeForm.appendChild(type);

        const likeButton = document.createElement("button");
        likeButton.type = "submit";
        likeButton.classList.add("btn");
        likeButton.classList.add("btn-primary");
        likeButton.innerText = "Like: ";
        
        const likeSpan = document.createElement("span");
        likeSpan.classList.add("like-count");
        likeSpan.innerText = "0";
        likeButton.appendChild(likeSpan);
        likeForm.appendChild(likeButton);
        likeForm.addEventListener("submit", send_comment_like);

        newComment.appendChild(likeForm);
        
        commentList.appendChild(newComment);
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
