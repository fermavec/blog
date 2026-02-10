document.addEventListener('DOMContentLoaded', () => {
    // Mobile Menu Toggle
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');

    if (hamburger) {
        hamburger.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            hamburger.innerHTML = navLinks.classList.contains('active')
                ? '<i class="fas fa-times"></i>'
                : '<i class="fas fa-bars"></i>';
        });
    }

    // Smooth Scrolling for Anchor Links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            // Close mobile menu if open
            if (navLinks.classList.contains('active')) {
                navLinks.classList.remove('active');
                hamburger.innerHTML = '<i class="fas fa-bars"></i>';
            }

            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Simple Intersection Observer for Fade-in animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe all sections and project cards
    document.querySelectorAll('section, .project-card, .blog-post').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
        observer.observe(el);
    });

    // Add CSS class for animation via JS
    const style = document.createElement('style');
    style.innerHTML = `
        .fade-in {
            opacity: 1 !important;
            transform: translateY(0) !important;
        }
    `;
    document.head.appendChild(style);

    // Hero abstract shape slight parallax
    const heroShape = document.querySelector('.abstract-shape');
    if (heroShape) {
        window.addEventListener('mousemove', (e) => {
            const x = e.clientX / window.innerWidth;
            const y = e.clientY / window.innerHeight;

            heroShape.style.transform = `translate(${x * 30}px, ${y * 30}px) scale(1.05)`;
        });
    }
    // Blog Filtering Logic
    const filterBtns = document.querySelectorAll('.filter-btn');
    const postsContainer = document.getElementById('posts-container');

    if (filterBtns.length > 0 && postsContainer) {
        // Store original content to restore 'date' view easily
        const originalContent = postsContainer.innerHTML;

        filterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                // Update active button state
                filterBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');

                const filterType = btn.getAttribute('data-filter');

                if (filterType === 'date') {
                    // Restore original HTML (which is grouped by date)
                    postsContainer.innerHTML = originalContent;

                    // Re-attach observers for animation
                    document.querySelectorAll('.blog-post-card').forEach(el => {
                        el.style.opacity = '0';
                        el.style.transform = 'translateY(20px)';
                        observer.observe(el);
                    });

                } else if (filterType === 'topic') {
                    // Group by tags
                    const articles = Array.from(new DOMParser().parseFromString(originalContent, 'text/html').querySelectorAll('article'));
                    const tagsMap = {};

                    articles.forEach(article => {
                        const tags = article.getAttribute('data-tags') ? article.getAttribute('data-tags').split(' ') : ['Uncategorized'];
                        tags.forEach(tag => {
                            if (!tagsMap[tag]) {
                                tagsMap[tag] = [];
                            }
                            tagsMap[tag].push(article.outerHTML);
                        });
                    });

                    let newContent = '';
                    for (const [tag, posts] of Object.entries(tagsMap)) {
                        newContent += `
                            <div class="posts-group topic-group">
                                <h3 class="group-title">#${tag}</h3>
                                ${posts.join('')}
                            </div>
                        `;
                    }
                    postsContainer.innerHTML = newContent;

                    // Re-attach observers for animation
                    document.querySelectorAll('.blog-post-card').forEach(el => {
                        el.style.opacity = '0';
                        el.style.transform = 'translateY(20px)';
                        observer.observe(el);
                    });
                }
            });
        });
    }
});
