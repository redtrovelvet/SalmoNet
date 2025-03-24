// post-intersection.js

document.addEventListener("DOMContentLoaded", function() {
    const posts = document.querySelectorAll('.post');
    
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          // Post is in view – add visible and remove exit classes.
          entry.target.classList.add('visible');
          entry.target.classList.remove('exit-top', 'exit-bottom');
        } else {
          // Remove visible class when not intersecting.
          entry.target.classList.remove('visible');
          
          // Determine whether the post is above or below the viewport.
          if (entry.boundingClientRect.top < 0) {
            // The post has scrolled off the top.
            entry.target.classList.add('exit-top');
            entry.target.classList.remove('exit-bottom');
          } else if (entry.boundingClientRect.bottom > window.innerHeight) {
            // The post is below the viewport.
            entry.target.classList.add('exit-bottom');
            entry.target.classList.remove('exit-top');
          } else {
            // Otherwise, remove any exit classes.
            entry.target.classList.remove('exit-top', 'exit-bottom');
          }
        }
      });
    }, { threshold: 0.1 });
    
    posts.forEach(post => observer.observe(post));
  });
  