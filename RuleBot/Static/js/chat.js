// ─────────────────────────────────────────────
//  chat.js  —  Handles all UI interactions
// ─────────────────────────────────────────────

const messagesEl  = document.getElementById("messages");
const inputEl     = document.getElementById("userInput");
const sendBtn     = document.getElementById("sendBtn");
const typingEl    = document.getElementById("typing");

// ── Add a message bubble to the chat ──
function addMessage(text, sender) {
  const msg    = document.createElement("div");
  msg.className = `msg ${sender}`;

  const avatar = document.createElement("div");
  avatar.className = "avatar";
  avatar.textContent = sender === "bot" ? "🤖" : "U";

  const bubble = document.createElement("div");
  bubble.className = "bubble";
  bubble.textContent = text;           // safe — no innerHTML

  msg.appendChild(avatar);
  msg.appendChild(bubble);
  messagesEl.appendChild(msg);

  // Scroll to bottom
  messagesEl.scrollTop = messagesEl.scrollHeight;
}

// ── Show / hide typing indicator ──
function showTyping()  { typingEl.classList.add("show");    messagesEl.scrollTop = 99999; }
function hideTyping()  { typingEl.classList.remove("show"); }

// ── Disable/enable input while waiting ──
function setLoading(on) {
  sendBtn.disabled  = on;
  inputEl.disabled  = on;
  sendBtn.textContent = on ? "…" : "Send ➤";
}

// ── Main send function ──
async function sendMessage() {
  const text = inputEl.value.trim();
  if (!text) return;

  // 1. Show user message
  addMessage(text, "user");
  inputEl.value = "";
  setLoading(true);
  showTyping();

  try {
    // 2. Call Flask /chat endpoint
    const res  = await fetch("/chat", {
      method:  "POST",
      headers: { "Content-Type": "application/json" },
      body:    JSON.stringify({ message: text }),
    });

    const data = await res.json();

    // 3. Show bot response
    hideTyping();
    addMessage(data.response, "bot");

  } catch (err) {
    hideTyping();
    addMessage("⚠️ Could not reach the server. Is Flask running?", "bot");
    console.error("Fetch error:", err);
  }

  setLoading(false);
  inputEl.focus();
}

// ── Suggestion button handler ──
function sendSuggestion(text) {
  inputEl.value = text;
  sendMessage();
}

// ── Send on Enter key ──
inputEl.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
});

// ── Focus input on load ──
inputEl.focus();