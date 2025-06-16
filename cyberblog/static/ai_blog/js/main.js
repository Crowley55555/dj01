/**
 * Main JavaScript file for CyberBlog AI
 * Contains basic interactivity
 */

document.addEventListener('DOMContentLoaded', function() {
    // Add animation to article cards on hover
    const articles = document.querySelectorAll('.article-card');

    articles.forEach(article => {
        article.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
            this.style.transition = 'transform 0.3s ease';
        });

        article.addEventListener('mouseleave', function() {
            this.style.transform = '';
        });
    });
});