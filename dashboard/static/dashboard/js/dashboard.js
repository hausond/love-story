document.addEventListener("DOMContentLoaded", () => {
    // Fade-up observer
    const fadeEls = document.querySelectorAll(".fade-up");
    if ("IntersectionObserver" in window) {
        const obs = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("show");
                    obs.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });
        fadeEls.forEach((el) => obs.observe(el));
    } else {
        fadeEls.forEach((el) => el.classList.add("show"));
    }

    // Mobile nav
    const mobileToggle = document.getElementById("mobileNavToggle");
    const mobileNav = document.getElementById("mobileNav");
    if (mobileToggle && mobileNav) {
        mobileToggle.addEventListener("click", () => {
            mobileNav.classList.toggle("hidden");
        });
    }

    // Cropper integration
    let activeCropper = null;
    const destroyCropper = () => {
        if (activeCropper) {
            activeCropper.destroy();
            activeCropper = null;
        }
    };

    const initCropperForInput = (input) => {
        const container = input.closest("form") || document;
        const preview = container.querySelector("[data-crop-preview]");
        const trigger = container.querySelector(".js-crop-trigger");
        if (!preview || !trigger) {
            return;
        }

        input.addEventListener("change", (event) => {
            const file = event.target.files?.[0];
            if (!file) {
                destroyCropper();
                preview.classList.add("hidden");
                preview.removeAttribute("src");
                return;
            }
            const reader = new FileReader();
            reader.onload = () => {
                preview.src = reader.result;
                preview.classList.remove("hidden");
                destroyCropper();
                activeCropper = new Cropper(preview, {
                    aspectRatio: 4 / 3,
                    viewMode: 1,
                    autoCropArea: 1,
                    background: false,
                });
            };
            reader.readAsDataURL(file);
        });

        trigger.addEventListener("click", (event) => {
            event.preventDefault();
            if (!activeCropper) return;
            const canvas = activeCropper.getCroppedCanvas({ width: 800, height: 600 });
            canvas.toBlob((blob) => {
                if (!blob) return;
                const fileName = input.files?.[0]?.name || "cropped.jpg";
                const file = new File([blob], fileName, { type: "image/jpeg" });
                const dataTransfer = new DataTransfer();
                dataTransfer.items.add(file);
                input.files = dataTransfer.files;
                destroyCropper();
                preview.src = URL.createObjectURL(file);
                preview.classList.remove("hidden");
            }, "image/jpeg", 0.92);
        });
    };

    document.querySelectorAll("input.js-crop-input").forEach((input) => {
        initCropperForInput(input);
    });
});
