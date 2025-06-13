/**
 * Main JavaScript file for CyberBlog AI
 * Contains basic interactivity and analytics
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

    // Simple analytics - track page visits
    if (typeof navigator.sendBeacon === 'function') {
        const page = window.location.pathname;
        const data = new FormData();
        data.append('page', page);
        data.append('time', new Date().toISOString());

        // Используем абсолютный путь
        const analyticsUrl = window.location.origin + '/analytics/';
        navigator.sendBeacon(analyticsUrl, data);
    }
});