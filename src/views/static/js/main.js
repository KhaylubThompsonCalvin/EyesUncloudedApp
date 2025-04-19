/*
 Author: Khaylub Thompson-Calvin
 Date: 04/16/2025 (updated 04/18/2025)
 File Name: main.js
 Description:
   Enhanced JavaScript for the Eyes Unclouded App.
   Includes:
     - Animated flash fade-outs
     - Character counters
     - Live form validation
     - Splash-screen fade logic on audio end
     - Audio onboarding controls for register.html and role_select.html
*/

document.addEventListener('DOMContentLoaded', () => {
  // Auto-hide flash messages
  document.querySelectorAll('.flash-message').forEach(msg => {
    setTimeout(() => {
      msg.style.transition = 'opacity 1s ease, transform 0.5s ease';
      msg.style.opacity = 0;
      msg.style.transform = 'translateY(-10px)';
      setTimeout(() => msg.remove(), 1000);
    }, 4000);
  });

  // Character counter for textareas
  const textarea = document.querySelector('#template_body, #message');
  if (textarea) {
    const counter = document.createElement('small');
    counter.classList.add('char-counter');
    textarea.after(counter);
    const update = () => counter.textContent = `${textarea.value.length} characters`;
    textarea.addEventListener('input', update);
    update();
  }

  // Live form validation
  const form = document.querySelector('form');
  if (form) {
    form.addEventListener('submit', e => {
      let hasError = false;
      form.querySelectorAll('[required]').forEach(field => {
        if (!field.value.trim()) {
          field.style.borderColor = '#ff5252';
          hasError = true;
        } else {
          field.style.borderColor = '#00ffc3';
        }
      });
      if (hasError) {
        e.preventDefault();
        alert('Please fill out all required fields to continue your path.');
      }
    });
  }

  // Fade-out splash text when intro audio ends
  const introAudio = document.getElementById('introAudio');
  if (introAudio) {
    introAudio.addEventListener('ended', () => {
      document.querySelectorAll('.fade-on-audio').forEach(el => el.classList.add('fade-out'));
    });
  }

  // Audio onboarding for register.html
  const overviewAudio = document.getElementById('overviewAudio');
  const playOverviewBtn = document.getElementById('playOverviewBtn');
  const roleSelect = document.getElementById('role');
  const roleAudio = document.getElementById('roleAudio');
  const playRoleBtn = document.getElementById('playRoleBtn');

  if (overviewAudio && playOverviewBtn) {
    playOverviewBtn.addEventListener('click', () => {
      overviewAudio.load();
      overviewAudio.play();
    });
  }

  if (roleSelect && roleAudio && playRoleBtn) {
    // Update role audio source on change
    roleSelect.addEventListener('change', () => {
      const filename = 'Role_' + roleSelect.value + '.mp3';
      roleAudio.src = `${window.location.origin}/audio/${filename}`;
      playRoleBtn.disabled = false;
    });
    // Play selected role preview
    playRoleBtn.addEventListener('click', () => {
      roleAudio.load();
      roleAudio.play();
    });
  }

  // Audio previews for role_select.html
  document.querySelectorAll('.roles-container audio').forEach(audioEl => {
    // Unmute on first user interaction
    document.addEventListener('click', () => { audioEl.muted = false; }, { once: true });
  });
});

  