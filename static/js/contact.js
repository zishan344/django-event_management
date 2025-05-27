// Contact Form Interactions
document.addEventListener("DOMContentLoaded", function () {
  // Get form elements
  const form = document.querySelector(".contact-form");
  const inputs = form.querySelectorAll("input, textarea");
  const submitBtn = form.querySelector('button[type="submit"]');

  // Add focus animations
  inputs.forEach((input) => {
    input.addEventListener("focus", function () {
      this.parentElement.classList.add("input-focused");
    });

    input.addEventListener("blur", function () {
      if (this.value === "") {
        this.parentElement.classList.remove("input-focused");
      }
    });
  });

  // Form submission animation
  form.addEventListener("submit", function (e) {
    // For demo purposes only - normally this would be handled by the backend
    e.preventDefault();

    // Add loading state
    submitBtn.disabled = true;
    submitBtn.innerHTML =
      '<div class="flex items-center justify-center"><svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg><span>Sending...</span></div>';

    // Simulate server response
    setTimeout(() => {
      // Show success message
      const successMessage = document.querySelector(".success-message");
      successMessage.classList.remove("hidden");

      // Reset form
      form.reset();

      // Reset button
      setTimeout(() => {
        submitBtn.disabled = false;
        submitBtn.innerHTML =
          '<div class="flex items-center justify-center"><span>Send Message</span><svg class="w-5 h-5 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg></div>';
      }, 1000);
    }, 2000);
  });
});
