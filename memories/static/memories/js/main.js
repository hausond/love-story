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

    // Ensure fade-up sections display if IntersectionObserver not supported.
    if (!("IntersectionObserver" in window)) {
        document.querySelectorAll(".fade-up").forEach((section) => section.classList.add("show"));
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