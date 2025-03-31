// Script for hidden Comment Section Animation.

document.addEventListener("DOMContentLoaded", function() {
    const commentButtons = document.querySelectorAll('.comment-toggle-btn');
    
    commentButtons.forEach(function(button) {
      button.addEventListener('click', function() {
        const postContainer = this.closest('.post');
        if (postContainer) {
          postContainer.classList.toggle('show-comments');
        }
      });
    });
  });
  