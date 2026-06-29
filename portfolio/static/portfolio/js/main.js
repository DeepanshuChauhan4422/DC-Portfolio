document.addEventListener('DOMContentLoaded', () => {
    
    // ==========================================================================
    // 1. CUSTOM CURSOR MOUSE GLOW TRACKER
    // ==========================================================================
    const cursorGlow = document.getElementById('cursor-glow');
    if (cursorGlow) {
        document.addEventListener('mousemove', (e) => {
            cursorGlow.style.left = `${e.clientX}px`;
            cursorGlow.style.top = `${e.clientY}px`;
        });
    }

    // ==========================================================================
    // THEME TOGGLE (LIGHT / DARK MODE)
    // ==========================================================================
    const themeToggle = document.getElementById('theme-toggle');
    const themeIcon = themeToggle ? themeToggle.querySelector('i') : null;
    
    console.log("Theme Toggle script initialized. Element:", themeToggle, "Icon:", themeIcon);
    
    // Sync toggle button icon with active theme
    if (document.body.classList.contains('light-theme')) {
        console.log("Initial theme: light");
        if (themeIcon) {
            themeIcon.className = 'fas fa-sun';
        }
    } else {
        console.log("Initial theme: dark");
        if (themeIcon) {
            themeIcon.className = 'fas fa-moon';
        }
    }
    
    if (themeToggle) {
        themeToggle.addEventListener('click', () => {
            document.body.classList.toggle('light-theme');
            let theme = 'dark';
            if (document.body.classList.contains('light-theme')) {
                theme = 'light';
                if (themeIcon) themeIcon.className = 'fas fa-sun';
            } else {
                if (themeIcon) themeIcon.className = 'fas fa-moon';
            }
            console.log("Theme toggled to:", theme);
            localStorage.setItem('theme', theme);
        });
    }

    // ==========================================================================
    // 2. NAVBAR SCROLL EFFECT & MOBILE MENU TOGGLE
    // ==========================================================================
    const navbar = document.getElementById('navbar');
    const navToggle = document.getElementById('nav-toggle');
    const navMenu = document.getElementById('nav-menu');
    const navLinks = document.querySelectorAll('.nav-link');

    // Change style on scroll
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
        
        // Scrollspy: Activate corresponding menu item
        let currentSection = '';
        const sections = document.querySelectorAll('section');
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 120;
            if (window.scrollY >= sectionTop) {
                currentSection = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${currentSection}`) {
                link.classList.add('active');
            }
        });
    });

    // Mobile nav toggle
    if (navToggle) {
        navToggle.addEventListener('click', () => {
            navMenu.classList.toggle('active');
            navToggle.classList.toggle('active');
        });
    }

    // Close mobile nav on link click
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            navMenu.classList.remove('active');
            navToggle.classList.remove('active');
        });
    });

    // ==========================================================================
    // 3. TYPEWRITER EFFECT (HERO SECTION)
    // ==========================================================================
    const typewriter = document.getElementById('typewriter');
    if (typewriter) {
        const words = JSON.parse(typewriter.getAttribute('data-words'));
        let wordIndex = 0;
        let charIndex = 0;
        let isDeleting = false;
        let typingSpeed = 100;

        function type() {
            const currentWord = words[wordIndex];
            
            if (isDeleting) {
                typewriter.textContent = currentWord.substring(0, charIndex - 1);
                charIndex--;
                typingSpeed = 50; // Delete faster
            } else {
                typewriter.textContent = currentWord.substring(0, charIndex + 1);
                charIndex++;
                typingSpeed = 120; // Normal typing speed
            }

            if (!isDeleting && charIndex === currentWord.length) {
                isDeleting = true;
                typingSpeed = 2000; // Pause at full word
            } else if (isDeleting && charIndex === 0) {
                isDeleting = false;
                wordIndex = (wordIndex + 1) % words.length;
                typingSpeed = 500; // Pause before typing next word
            }

            setTimeout(type, typingSpeed);
        }
        
        // Start typing
        setTimeout(type, 1000);
    }

    // ==========================================================================
    // 4. STATS COUNTER ANIMATION
    // ==========================================================================
    const statNumbers = document.querySelectorAll('.stat-number');
    let counted = false;

    const countStats = () => {
        statNumbers.forEach(stat => {
            const target = parseInt(stat.getAttribute('data-target'));
            let current = 0;
            const duration = 2000; // ms
            const increment = target / (duration / 16); // 60fps refresh rate

            const updateCount = () => {
                current += increment;
                if (current < target) {
                    stat.textContent = Math.ceil(current);
                    requestAnimationFrame(updateCount);
                } else {
                    stat.textContent = target;
                }
            };
            updateCount();
        });
        counted = true;
    };

    // Intersection observer for statistics counting
    const aboutSection = document.getElementById('about');
    if (aboutSection && statNumbers.length > 0) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting && !counted) {
                    countStats();
                }
            });
        }, { threshold: 0.2 });

        observer.observe(aboutSection);
    }

    // ==========================================================================
    // 5. SKILLS FILTERING SYSTEM
    // ==========================================================================
    const skillsNavButtons = document.querySelectorAll('.skills-nav-btn');
    const skillCards = document.querySelectorAll('.skill-card');

    skillsNavButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remove active from all nav items
            skillsNavButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const category = btn.getAttribute('data-category');

            skillCards.forEach(card => {
                const cardCategory = card.getAttribute('data-category');
                
                if (category === 'all' || cardCategory === category) {
                    card.style.display = 'flex';
                    // Trigger reflow for animations
                    setTimeout(() => card.style.opacity = '1', 50);
                } else {
                    card.style.opacity = '0';
                    card.style.display = 'none';
                }
            });
        });
    });

    // ==========================================================================
    // 6. PROJECT DETAIL MODALS
    // ==========================================================================
    const openModalButtons = document.querySelectorAll('.open-modal-btn');
    const closeModalTriggers = document.querySelectorAll('.close-modal-trigger');

    openModalButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const projectId = btn.getAttribute('data-project-id');
            const modal = document.getElementById(`modal-${projectId}`);
            if (modal) {
                modal.classList.add('active');
                modal.setAttribute('aria-hidden', 'false');
                document.body.style.overflow = 'hidden'; // Stop page background scroll
            }
        });
    });

    closeModalTriggers.forEach(trigger => {
        trigger.addEventListener('click', () => {
            const projectId = trigger.getAttribute('data-project-id');
            const modal = document.getElementById(`modal-${projectId}`);
            if (modal) {
                modal.classList.remove('active');
                modal.setAttribute('aria-hidden', 'true');
                document.body.style.overflow = 'auto'; // Restore page scroll
            }
        });
    });

    // Close modal on Escape key press
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            const activeModal = document.querySelector('.project-modal.active');
            if (activeModal) {
                activeModal.classList.remove('active');
                activeModal.setAttribute('aria-hidden', 'true');
                document.body.style.overflow = 'auto';
            }
        }
    });

    // ==========================================================================
    // 7. TOAST NOTIFICATION HELPERS
    // ==========================================================================
    const toastContainer = document.getElementById('toast-container');

    function showToast(message, type = 'success') {
        if (!toastContainer) return;
        
        const toast = document.createElement('div');
        toast.className = `toast ${type}`;
        
        const icon = document.createElement('i');
        icon.className = type === 'success' ? 'fas fa-check-circle toast-icon' : 'fas fa-exclamation-circle toast-icon';
        
        const text = document.createElement('span');
        text.textContent = message;

        toast.appendChild(icon);
        toast.appendChild(text);
        toastContainer.appendChild(toast);

        // Trigger transition
        setTimeout(() => toast.classList.add('active'), 50);

        // Remove toast
        setTimeout(() => {
            toast.classList.remove('active');
            setTimeout(() => toast.remove(), 400);
        }, 4000);
    }

    // ==========================================================================
    // 8. CONTACT FORM AJAX SUBMISSION
    // ==========================================================================
    const contactForm = document.getElementById('contact-form');
    const submitBtn = document.getElementById('form-submit-btn');

    if (contactForm) {
        contactForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            // Set loading state
            const originalBtnHtml = submitBtn.innerHTML;
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<span>Sending...</span> <i class="fas fa-circle-notch fa-spin"></i>';

            const formData = new FormData(contactForm);
            const formObject = {};
            formData.forEach((value, key) => formObject[key] = value);

            try {
                const response = await fetch(CONFIG.contactUrl, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': CONFIG.csrfToken
                    },
                    body: JSON.stringify(formObject)
                });

                const result = await response.json();

                if (response.ok && result.status === 'success') {
                    showToast(result.message, 'success');
                    contactForm.reset();
                } else {
                    showToast(result.message || 'Error sending message. Please check inputs.', 'error');
                }
            } catch (error) {
                showToast('Unable to connect to server. Please try again later.', 'error');
            } finally {
                // Restore button
                submitBtn.disabled = false;
                submitBtn.innerHTML = originalBtnHtml;
            }
        });
    }

    // ==========================================================================
    // 9. GITHUB API INTEGRATION
    // ==========================================================================
    const githubProfileHeader = document.getElementById('github-profile-header');
    const githubReposContainer = document.getElementById('github-repos-container');

    async function fetchGitHubData() {
        if (!CONFIG.githubUsername) return;

        try {
            // 1. Fetch Profile
            const profileRes = await fetch(`https://api.github.com/users/${CONFIG.githubUsername}`);
            if (profileRes.ok) {
                const profile = await profileRes.json();
                renderGitHubProfile(profile);
            } else {
                throw new Error("GitHub profile fetch failed");
            }

            // 2. Fetch Repos
            const reposRes = await fetch(`https://api.github.com/users/${CONFIG.githubUsername}/repos?sort=updated&per_page=6`);
            if (reposRes.ok) {
                const repos = await reposRes.json();
                renderGitHubRepos(repos);
            } else {
                throw new Error("GitHub repos fetch failed");
            }

        } catch (error) {
            console.error("GitHub API error: ", error);
            if (githubProfileHeader) {
                githubProfileHeader.innerHTML = `
                    <div class="github-meta">
                        <h3>Deepanshu Chauhan</h3>
                        <a href="https://github.com/${CONFIG.githubUsername}" target="_blank" class="github-username-link">
                            <i class="fab fa-github"></i> github.com/${CONFIG.githubUsername}
                        </a>
                        <p class="github-bio">Check out my active open source projects directly on my profile!</p>
                    </div>
                `;
            }
            if (githubReposContainer) {
                githubReposContainer.innerHTML = `
                    <div class="github-profile-loading text-center" style="grid-column: 1 / -1;">
                        <p><i class="fas fa-exclamation-triangle"></i> GitHub API rate limit hit or offline. You can review Deepanshu's codebases directly on GitHub.</p>
                        <a href="https://github.com/${CONFIG.githubUsername}" target="_blank" class="btn btn-secondary" style="margin-top: 15px;">
                            Visit GitHub Profile
                        </a>
                    </div>
                `;
            }
        }
    }

    function renderGitHubProfile(profile) {
        if (!githubProfileHeader) return;
        
        githubProfileHeader.innerHTML = `
            <img src="${profile.avatar_url}" alt="Deepanshu Chauhan" class="github-avatar">
            <div class="github-meta">
                <h3>${profile.name || 'Deepanshu Chauhan'}</h3>
                <a href="${profile.html_url}" target="_blank" rel="noopener noreferrer" class="github-username-link">
                    <i class="fab fa-github"></i> @${profile.login}
                </a>
                <p class="github-bio">${profile.bio || 'AI Application Developer &amp; Full Stack Software Engineer'}</p>
                <div class="github-stats-row">
                    <span class="github-stat"><strong>${profile.public_repos}</strong> repositories</span>
                    <span class="github-stat"><strong>${profile.followers}</strong> followers</span>
                </div>
            </div>
        `;
    }

    function renderGitHubRepos(repos) {
        if (!githubReposContainer) return;
        
        githubReposContainer.innerHTML = '';
        
        // Filter out forks or take top repos
        const displayRepos = repos.slice(0, 6);

        if (displayRepos.length === 0) {
            githubReposContainer.innerHTML = '<p class="github-profile-loading">No repositories available.</p>';
            return;
        }

        displayRepos.forEach(repo => {
            const langColors = {
                Python: '#3572A5',
                JavaScript: '#f1e05a',
                HTML: '#e34c26',
                CSS: '#563d7c',
                C: '#555555',
                'C++': '#f34b7d',
            };

            const langColor = langColors[repo.language] || '#888';
            const langText = repo.language || 'Code';

            const card = document.createElement('div');
            card.className = 'glass-card github-repo-card';
            card.innerHTML = `
                <div>
                    <h4 class="github-repo-title">
                        <i class="far fa-folder"></i> <a href="${repo.html_url}" target="_blank" rel="noopener noreferrer">${repo.name}</a>
                    </h4>
                    <p class="github-repo-desc">${repo.description || 'No description provided.'}</p>
                </div>
                <div class="github-repo-footer">
                    <span class="github-repo-lang">
                        <span class="github-lang-dot" style="background-color: ${langColor}"></span>
                        <span>${langText}</span>
                    </span>
                    <span class="github-repo-stars">
                        <i class="far fa-star"></i> ${repo.stargazers_count}
                    </span>
                </div>
            `;
            githubReposContainer.appendChild(card);
        });
    }

    // Call GitHub API on load
    if (githubProfileHeader || githubReposContainer) {
        fetchGitHubData();
    }

    // ==========================================================================
    // 10. AI ASSISTANT CHAT WIDGET
    // ==========================================================================
    const aiChatBubble = document.getElementById('ai-chat-bubble');
    const aiChatWidget = document.getElementById('ai-chat-widget');
    const aiChatClose = document.getElementById('ai-chat-close');
    const aiChatInput = document.getElementById('ai-chat-input');
    const aiChatSend = document.getElementById('ai-chat-send');
    const aiChatMessages = document.getElementById('ai-chat-messages');

    // Toggle Chat Window
    if (aiChatBubble) {
        aiChatBubble.addEventListener('click', () => {
            aiChatWidget.classList.add('active');
            aiChatInput.focus();
        });
    }

    if (aiChatClose) {
        aiChatClose.addEventListener('click', () => {
            aiChatWidget.classList.remove('active');
        });
    }

    // Send AI message helper
    async function sendAiMessage() {
        const query = aiChatInput.value.trim();
        if (!query) return;

        // Clear input field
        aiChatInput.value = '';

        // Append User bubble
        appendChatBubble(query, 'user');

        // Append temporary Bot Loading bubble
        const loadingId = 'bot-loading-' + Date.now();
        appendChatBubble('<i class="fas fa-circle-notch fa-spin"></i> Writing response...', 'bot', loadingId);

        try {
            const response = await fetch(CONFIG.aiAssistantUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': CONFIG.csrfToken
                },
                body: JSON.stringify({ message: query })
            });

            const result = await response.json();
            
            // Remove loading bubble
            const loadingBubble = document.getElementById(loadingId);
            if (loadingBubble) loadingBubble.remove();

            if (response.ok && result.status === 'success') {
                appendChatBubble(result.response, 'bot');
            } else {
                appendChatBubble("I'm sorry, I encountered a database connection issue or API outage. Please try again shortly or fill out the contact form below to email Deepanshu directly!", 'bot');
            }
        } catch (error) {
            // Remove loading bubble
            const loadingBubble = document.getElementById(loadingId);
            if (loadingBubble) loadingBubble.remove();
            
            appendChatBubble("Offline/Connection failure. Please ensure the server is fully running and try again.", 'bot');
        }
    }

    function appendChatBubble(text, sender, id = null) {
        if (!aiChatMessages) return;

        const bubble = document.createElement('div');
        bubble.className = `chat-message ${sender}`;
        if (id) bubble.id = id;

        const content = document.createElement('div');
        content.className = 'message-content';
        content.innerHTML = text; // Assumes formatted HTML/markdown response

        const time = document.createElement('span');
        time.className = 'message-time';
        time.textContent = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

        bubble.appendChild(content);
        bubble.appendChild(time);
        aiChatMessages.appendChild(bubble);

        // Scroll to bottom
        aiChatMessages.scrollTop = aiChatMessages.scrollHeight;
    }

    // Trigger AI send
    if (aiChatSend) {
        aiChatSend.addEventListener('click', sendAiMessage);
    }

    if (aiChatInput) {
        aiChatInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                sendAiMessage();
            }
        });
    }
});
