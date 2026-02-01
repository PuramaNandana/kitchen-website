// Initialize ScrollReveal with custom settings
const sr = ScrollReveal({
    origin: 'bottom',
    distance: '80px',
    duration: 1200,
    delay: 200,
    reset: false,
    easing: 'cubic-bezier(0.165, 0.84, 0.44, 1)'
});

// Apply reveal animations to all major components
sr.reveal('.reveal-up');
sr.reveal('.reveal-left', { origin: 'left', distance: '100px' });
sr.reveal('.reveal-right', { origin: 'right', distance: '100px' });
sr.reveal('.design-card', { interval: 100 });
sr.reveal('.service-card', { interval: 100 });
sr.reveal('.stat-item', { interval: 150 });

// Navbar Scroll Logic
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
    if (window.scrollY > 100) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Pure JS Mobile Menu Logic (Simple version for demonstration)
const mobileMenuBtn = document.getElementById('mobile-menu-btn');
const navLinks = document.querySelector('.nav-links');

if (mobileMenuBtn) {
    mobileMenuBtn.addEventListener('click', () => {
        // Toggle logical mobile menu (UI could be expanded with a class)
        alert('Purama Nandana Lakshmi Studio: Mobile menu under construction. Navigate via sections!');
    });
}

// Handle Form Submission with local feedback (No Backend required)
const contactForm = document.getElementById('contactForm');
if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
        e.preventDefault();

        const status = document.getElementById('formStatus');
        const submitBtn = contactForm.querySelector('button');

        // Visual feedback
        submitBtn.innerHTML = 'Sending...';
        submitBtn.disabled = true;

        // Simulate a delay for premium feel
        setTimeout(() => {
            status.innerHTML = 'Message sent successfully! Purama Nandana Lakshmi will contact you soon.';
            status.style.color = '#2ecc71';
            status.style.fontWeight = 'bold';

            submitBtn.innerHTML = 'Message Sent!';
            contactForm.reset();

            // Revert button after few seconds
            setTimeout(() => {
                submitBtn.innerHTML = 'Send Message';
                submitBtn.disabled = false;
            }, 3000);

        }, 1500);
    });
}

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            window.scrollTo({
                top: target.offsetTop - 80,
                behavior: 'smooth'
            });
        }
    });
});

// Add subtle parallax to hero
window.addEventListener('scroll', () => {
    const scroll = window.pageYOffset;
    const heroBg = document.querySelector('.hero');
    if (heroBg) {
        heroBg.style.backgroundPositionY = (scroll * 0.5) + 'px';
    }
});

console.log('Purama Nandana Lakshmi Portfolio loaded successfully.');
