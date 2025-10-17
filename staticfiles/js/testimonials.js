// Testimonials Swiper Carousel - With performance optimization
document.addEventListener("DOMContentLoaded", function () {
  // Use requestIdleCallback for non-essential initialization if available
  const initSwiper = () => {
    // Check if Swiper is loaded before initializing
    if (typeof Swiper === "undefined") {
      console.error(
        "Swiper JS is not loaded! Please check your script includes."
      );
      return;
    }

    // Check if element exists
    if (!document.querySelector(".testimonials-swiper")) {
      return;
    }

    // Show preloader until swiper is ready
    const preloader = document.querySelector(".testimonials-preloader");
    const swiperContainer = document.querySelector(".testimonials-swiper");

    // Handle preloader and show swiper when ready
    function showSwiperContent() {
      if (preloader && swiperContainer) {
        setTimeout(() => {
          preloader.style.display = "none";
          swiperContainer.classList.add("opacity-100");
        }, 800);
      }
    }
    // Initialize Swiper with enhanced effects and interactions
    const testimonialsSwiper = new Swiper(".testimonials-swiper", {
      // Enable autoplay with smooth transitions
      autoplay: {
        delay: 5000,
        disableOnInteraction: false,
        pauseOnMouseEnter: true,
      },

      // Number of slides per view (responsive)
      slidesPerView: 1,
      spaceBetween: 30,

      // Enable loop and centered modes for better presentation
      loop: true,
      centeredSlides: true,

      // Use slide effect with easing
      effect: "slide",
      speed: 800,

      // Add gorgeous slide shadows for depth
      coverflowEffect: {
        rotate: 0,
        stretch: 0,
        depth: 100,
        modifier: 1,
        slideShadows: true,
      },

      // Enhanced pagination with dynamic bullets and accessibility
      pagination: {
        el: ".swiper-pagination",
        clickable: true,
        dynamicBullets: true,
        dynamicMainBullets: 3,
        bulletElement: "button",
        bulletClass: "swiper-pagination-bullet",
        bulletActiveClass: "swiper-pagination-bullet-active",
        renderBullet: function (index, className) {
          return (
            '<button class="' +
            className +
            '" aria-label="Go to testimonial ' +
            (index + 1) +
            '"></button>'
          );
        },
      },

      // Navigation arrows with hover effects
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
        disabledClass: "swiper-button-disabled",
      },

      // Keyboard accessibility
      keyboard: {
        enabled: true,
        onlyInViewport: true,
      },
      // Enhanced event handlers for better UX and performance
      on: {
        init: function () {
          setTimeout(() => {
            // Add initial animations when carousel loads
            document
              .querySelectorAll(".star-rating svg")
              .forEach((star, index) => {
                star.style.animationDelay = `${index * 0.1}s`;
              });
          }, 500);

          // Announce to screen readers that carousel is ready
          const srAnnouncement = document.createElement("div");
          srAnnouncement.className = "sr-only";
          srAnnouncement.setAttribute("aria-live", "polite");
          srAnnouncement.textContent =
            "Testimonials carousel is ready. Use arrow keys to navigate between slides.";
          document
            .querySelector(".testimonials-swiper")
            .appendChild(srAnnouncement);
          setTimeout(() => srAnnouncement.remove(), 3000);
        },

        slideChange: function () {
          // Update ARIA attributes for screen readers when slide changes
          const activeIndex = this.realIndex + 1;
          const totalSlides = document.querySelectorAll(
            ".swiper-slide:not(.swiper-slide-duplicate)"
          ).length;
          const srAnnouncement = document.createElement("div");
          srAnnouncement.className = "sr-only";
          srAnnouncement.setAttribute("aria-live", "polite");
          srAnnouncement.textContent = `Showing testimonial ${activeIndex} of ${totalSlides}`;
          document
            .querySelector(".testimonials-swiper")
            .appendChild(srAnnouncement);
          setTimeout(() => srAnnouncement.remove(), 1000);
        },

        // Pause autoplay when user interacts with keyboard
        keyPress: function () {
          if (this.autoplay.running) {
            this.autoplay.stop();
          }
        },
      },
      // Responsive breakpoints for different screen sizes
      breakpoints: {
        // when window width is >= 640px (sm)
        640: {
          slidesPerView: 1,
          spaceBetween: 20,
        },
        // when window width is >= 768px (md)
        768: {
          slidesPerView: 2,
          spaceBetween: 30,
        },
        // when window width is >= 1024px (lg)
        1024: {
          slidesPerView: 3,
          spaceBetween: 40,
        },
      },

      // Touch interaction settings for mobile
      touchRatio: 1,
      touchAngle: 45,
      grabCursor: true,
      freeMode: false,

      // Improve mobile experience
      touchStartPreventDefault: false,
      threshold: 5, // Minimum touch distance for swipe
      resistance: true,
      resistanceRatio: 0.85,

      // Accessibility features
      a11y: {
        prevSlideMessage: "Previous testimonial",
        nextSlideMessage: "Next testimonial",
        paginationBulletMessage: "Go to testimonial {{index}}",
      },
    });
    // Add hover effect for navigation arrows
    const addHoverEffects = () => {
      try {
        const navButtons = document.querySelectorAll(
          ".swiper-button-next, .swiper-button-prev"
        );

        if (navButtons.length === 0) {
          console.warn("Navigation buttons not found in testimonials carousel");
          return;
        }

        navButtons.forEach((button) => {
          button.addEventListener("mouseenter", () => {
            button.style.transform = "scale(1.15)";
            button.style.boxShadow = "0 4px 15px rgba(220, 38, 38, 0.25)";
          });

          button.addEventListener("mouseleave", () => {
            button.style.transform = "scale(1)";
            button.style.boxShadow = "0 2px 10px rgba(0, 0, 0, 0.1)";
          });
        });

        // Also add animations to testimonial cards for touch devices
        const testimonialCards = document.querySelectorAll(".testimonial-card");
        testimonialCards.forEach((card) => {
          card.addEventListener("touchstart", () => {
            card.classList.add("touch-active");
          });

          card.addEventListener("touchend", () => {
            setTimeout(() => {
              card.classList.remove("touch-active");
            }, 300);
          });
        });
      } catch (error) {
        console.error("Error adding hover effects to testimonials:", error);
      }
    };
    // Call function to add hover effects
    addHoverEffects();

    // Show swiper content after initialization
    showSwiperContent();
  };

  // Use requestIdleCallback for non-critical initialization if available
  if ("requestIdleCallback" in window) {
    requestIdleCallback(() => initSwiper(), { timeout: 2000 });
  } else {
    // Fallback to setTimeout for browsers without requestIdleCallback
    setTimeout(initSwiper, 100);
  }
});
