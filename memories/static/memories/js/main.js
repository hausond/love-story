document.addEventListener("DOMContentLoaded", () => {
    const body = document.body;
    requestAnimationFrame(() => body.classList.add("ready"));

    // Smooth fade transitions between pages.
    document.querySelectorAll("a[href]").forEach((link) => {
        const href = link.getAttribute("href");
        if (
            !href ||
            href.startsWith("#") ||
            link.target === "_blank" ||
            link.hasAttribute("download") ||
            href.startsWith("mailto:") ||
            href.startsWith("tel:") ||
            link.dataset.transition === "false"
        ) {
            return;
        }
        link.addEventListener("click", (event) => {
            if (event.metaKey || event.ctrlKey) return;
            event.preventDefault();
            body.classList.remove("ready");
            setTimeout(() => {
                window.location.href = link.href;
            }, 220);
        });
    });

    const fadeUpElements = document.querySelectorAll(".fade-up");
    const revealAll = () => fadeUpElements.forEach((section) => section.classList.add("show"));

    if ("IntersectionObserver" in window) {
        const observer = new IntersectionObserver(
            (entries) => {
                entries.forEach((entry) => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add("show");
                        observer.unobserve(entry.target);
                    }
                });
            },
            { threshold: 0.1 }
        );
        fadeUpElements.forEach((section) => observer.observe(section));

        // Fallback: ensure sections become visible if observer never fires.
        setTimeout(() => {
            fadeUpElements.forEach((section) => {
                if (!section.classList.contains("show")) {
                    section.classList.add("show");
                }
            });
        }, 1200);
    } else {
        revealAll();
    }

    // Mobile menu toggle.
    const toggleButton = document.getElementById("mobile-menu-toggle");
    const mobileMenu = document.getElementById("mobile-menu");
    if (toggleButton && mobileMenu) {
        toggleButton.addEventListener("click", () => {
            mobileMenu.classList.toggle("hidden");
        });
    }

    // Lightbox for gallery.
    const overlay = document.getElementById("lightbox-overlay");
    const overlayImage = document.getElementById("lightbox-image");
    const overlayCaption = document.getElementById("lightbox-caption");
    const overlayClose = document.getElementById("lightbox-close");
    const openLightbox = (src, caption) => {
        if (!overlay || !overlayImage) return;
        overlayImage.src = src;
        overlayImage.alt = caption || "";
        if (overlayCaption) {
            overlayCaption.textContent = caption || "";
        }
        overlay.classList.remove("hidden");
        overlay.classList.add("flex");
        body.classList.add("overflow-hidden");
    };
    const closeLightbox = () => {
        if (!overlay) return;
        overlay.classList.add("hidden");
        overlay.classList.remove("flex");
        body.classList.remove("overflow-hidden");
        if (overlayImage) {
            overlayImage.src = "";
            overlayImage.alt = "";
        }
    };

    if (overlay && overlayClose) {
        overlayClose.addEventListener("click", closeLightbox);
        overlay.addEventListener("click", (event) => {
            if (event.target === overlay) closeLightbox();
        });
        document.addEventListener("keyup", (event) => {
            if (event.key === "Escape") {
                closeLightbox();
            }
        });
    }

    document.querySelectorAll("[data-lightbox-item]").forEach((item) => {
        item.addEventListener("click", () => {
            const src = item.getAttribute("data-lightbox-src");
            const caption = item.getAttribute("data-lightbox-caption");
            if (src) {
                openLightbox(src, caption);
            }
        });
    });
});

// 9*PTWheFv&2m
