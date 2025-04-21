document.addEventListener("DOMContentLoaded", () => {
    const windowEl = document.getElementById("chat-window");
    const inputEl  = document.getElementById("chat-input");
    const btn      = document.getElementById("send-btn");
  
    function appendMessage(who, text) {
      const wrapper = document.createElement("div");
      wrapper.classList.add("chat-message", who === "AI" ? "from-ai" : "from-user");
      wrapper.innerHTML = `<strong>${who}</strong>: ${text}`;
      windowEl.append(wrapper);
      windowEl.scrollTop = windowEl.scrollHeight;
    }
  
    btn.addEventListener("click", async () => {
      const msg = inputEl.value.trim();
      if (!msg) return;
      appendMessage("You", msg);
      inputEl.value = "";
      btn.disabled = true;
  
      try {
        const res = await fetch("/chat/api", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ message: msg })
        });
        const data = await res.json();
        if (data.error) throw new Error(data.error);
        appendMessage("AI", data.reply);
      } catch (e) {
        appendMessage("AI", "⚠️ Error: " + e.message);
      } finally {
        btn.disabled = false;
        inputEl.focus();
      }
    });
  
    // allow Ctrl+Enter to send
    inputEl.addEventListener("keydown", e => {
      if (e.ctrlKey && e.key === "Enter") {
        btn.click();
      }
    });
  });
  