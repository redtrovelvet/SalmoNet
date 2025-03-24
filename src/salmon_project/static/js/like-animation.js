// Animation Script For like button.

document.addEventListener("DOMContentLoaded", function() {
    // Select all like icon buttons
    var likeButtons = document.querySelectorAll('.like-icon-btn');
    
    likeButtons.forEach(function(btn) {
      btn.addEventListener('click', function(e) {
        // adding the bubbly animation class on click
        this.classList.add('bubbly-animate');
        
        setTimeout(() => {
          this.classList.remove('bubbly-animate');
        }, 700);
      });
    });
  });
  