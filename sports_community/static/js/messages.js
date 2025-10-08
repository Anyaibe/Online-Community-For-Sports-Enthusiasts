// Auto-dismiss messages after 5 seconds
document.addEventListener('DOMContentLoaded', function() {
    const messages = document.querySelectorAll('.message-alert');
    
    messages.forEach(function(message) {
        // Add fade-out animation after 5 seconds
        setTimeout(function() {
            message.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            message.style.opacity = '0';
            message.style.transform = 'translateY(-20px)';
            
            // Remove from DOM after animation completes
            setTimeout(function() {
                message.remove();
                
                // Check if messages container is empty, remove it
                const container = document.querySelector('.messages-container');
                if (container && container.children.length === 0) {
                    container.remove();
                }
            }, 500);
        }, 5000); // 5 seconds
        
        // Also allow manual close on click
        message.style.cursor = 'pointer';
        message.addEventListener('click', function() {
            message.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
            message.style.opacity = '0';
            message.style.transform = 'translateY(-20px)';
            
            setTimeout(function() {
                message.remove();
                
                const container = document.querySelector('.messages-container');
                if (container && container.children.length === 0) {
                    container.remove();
                }
            }, 300);
        });
    });
});