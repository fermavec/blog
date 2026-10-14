document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');

    if (hamburger && navLinks) {
        hamburger.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            hamburger.innerHTML = navLinks.classList.contains('active')
                ? '<i class="fas fa-times"></i>' : '<i class="fas fa-bars"></i>';
        });
    }

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', event => {
            const targetId = anchor.getAttribute('href');
            const target = targetId && targetId !== '#' ? document.querySelector(targetId) : null;
            if (!target) return;
            event.preventDefault();
            target.scrollIntoView({ behavior: 'smooth' });
            if (navLinks?.classList.contains('active')) {
                navLinks.classList.remove('active');
                hamburger.innerHTML = '<i class="fas fa-bars"></i>';
            }
        });
    });

    document.querySelectorAll('.fade-in, section, .project-card, .blog-post, .blog-post-card').forEach(el => {
        el.style.opacity = '1';
        el.style.transform = 'none';
    });

    const filterBtns = document.querySelectorAll('.filter-btn');
    const postsContainer = document.getElementById('posts-container');
    if (filterBtns.length && postsContainer) {
        const originalContent = postsContainer.innerHTML;
        filterBtns.forEach(button => button.addEventListener('click', () => {
            filterBtns.forEach(item => item.classList.remove('active'));
            button.classList.add('active');
            if (button.dataset.filter === 'date') {
                postsContainer.innerHTML = originalContent;
                return;
            }
            const articles = [...new DOMParser().parseFromString(originalContent, 'text/html').querySelectorAll('article')];
            const tags = new Map();
            articles.forEach(article => (article.dataset.tags || 'Sin tema').split(' ').forEach(tag => {
                tags.set(tag, [...(tags.get(tag) || []), article.outerHTML]);
            }));
            postsContainer.innerHTML = [...tags].map(([tag, posts]) =>
                `<div class="posts-group topic-group"><h2 class="group-title">#${tag}</h2>${posts.join('')}</div>`
            ).join('');
        }));
    }

    addAccessibilityControls();
});

function addAccessibilityControls() {
    if (document.getElementById('accessibility-controls')) return;

    const style = document.createElement('style');
    style.textContent = `
      .accessibility-widget { position: fixed; right: 1rem; bottom: 1rem; z-index: 9999; display: flex; gap: .35rem; padding: .45rem; background: #111827; border: 1px solid #94a3b8; border-radius: .6rem; box-shadow: 0 4px 14px rgba(0,0,0,.35); }
      .accessibility-btn { min-width: 2.7rem; min-height: 2.7rem; padding: .35rem .55rem; background: #fff; color: #111827; border: 2px solid transparent; border-radius: .35rem; cursor: pointer; font: 700 1rem/1 sans-serif; }
      .accessibility-btn:hover, .accessibility-btn:focus-visible { background: #e0f2fe; border-color: #38bdf8; outline: 3px solid #facc15; outline-offset: 2px; }
      @media (max-width: 480px) { .accessibility-widget { right: .5rem; bottom: .5rem; } }
    `;
    document.head.appendChild(style);

    const isSpanish = document.documentElement.lang.toLowerCase().startsWith('es');
    const labels = isSpanish
        ? { read: 'Leer contenido', stop: 'Detener lectura', decrease: 'Reducir tamaño del texto', increase: 'Aumentar tamaño del texto', reset: 'Restablecer tamaño del texto' }
        : { read: 'Read content', stop: 'Stop reading', decrease: 'Decrease text size', increase: 'Increase text size', reset: 'Reset text size' };
    const widget = document.createElement('div');
    widget.id = 'accessibility-controls';
    widget.className = 'accessibility-widget';
    widget.setAttribute('role', 'group');
    widget.setAttribute('aria-label', isSpanish ? 'Controles de accesibilidad' : 'Accessibility controls');
    widget.innerHTML = `
      <button class="accessibility-btn" id="readContentBtn" type="button" aria-label="${labels.read}" title="${labels.read}">🔊</button>
      <button class="accessibility-btn" id="decreaseTextBtn" type="button" aria-label="${labels.decrease}" title="${labels.decrease}">A−</button>
      <button class="accessibility-btn" id="increaseTextBtn" type="button" aria-label="${labels.increase}" title="${labels.increase}">A+</button>
      <button class="accessibility-btn" id="resetTextBtn" type="button" aria-label="${labels.reset}" title="${labels.reset}">A</button>`;
    document.body.appendChild(widget);

    const root = document.documentElement;
    const storedScale = Number(localStorage.getItem('ferMavecTextScale'));
    let scale = Number.isFinite(storedScale) && storedScale >= 80 && storedScale <= 150 ? storedScale : 100;
    const applyScale = () => {
        root.style.fontSize = `${scale}%`;
        localStorage.setItem('ferMavecTextScale', String(scale));
    };
    applyScale();
    document.getElementById('increaseTextBtn').addEventListener('click', () => { scale = Math.min(150, scale + 10); applyScale(); });
    document.getElementById('decreaseTextBtn').addEventListener('click', () => { scale = Math.max(80, scale - 10); applyScale(); });
    document.getElementById('resetTextBtn').addEventListener('click', () => { scale = 100; applyScale(); });

    const readButton = document.getElementById('readContentBtn');
    let utterance;
    const stopReading = () => {
        window.speechSynthesis?.cancel();
        readButton.setAttribute('aria-label', labels.read);
        readButton.title = labels.read;
        readButton.textContent = '🔊';
        readButton.setAttribute('aria-pressed', 'false');
    };
    readButton.addEventListener('click', () => {
        if (!('speechSynthesis' in window)) return;
        if (window.speechSynthesis.speaking) { stopReading(); return; }
        const content = document.querySelector('main') || document.body;
        const text = content.innerText.trim();
        if (!text) return;
        utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = isSpanish ? 'es-ES' : 'en-US';
        utterance.onend = stopReading;
        utterance.onerror = stopReading;
        readButton.setAttribute('aria-label', labels.stop);
        readButton.title = labels.stop;
        readButton.textContent = '■';
        readButton.setAttribute('aria-pressed', 'true');
        window.speechSynthesis.speak(utterance);
    });
    window.addEventListener('pagehide', stopReading);
}
