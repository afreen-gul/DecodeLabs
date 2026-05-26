import random
from datetime import datetime

# ─────────────────────────────────────────────
#  RULE ENGINE  —  each rule is a dict with:
#    "keywords"  : list of trigger words
#    "responses" : list of possible replies
# ─────────────────────────────────────────────

RULES = [
    {
        "keywords": ["hello", "hi", "hey", "howdy", "sup", "hiya", "greetings"],
        "responses": [
            "Hello there! 👋 Great to meet you. How can I help?",
            "Hey! I'm RuleBot — running on pure if-else logic. Ask me anything!",
            "Howdy! No neural networks here, just good old rules. What's up?",
        ],
    },
    {
        "keywords": ["bye", "goodbye", "exit", "quit", "see ya", "later", "farewell"],
        "responses": [
            "Goodbye! 👋 Come back anytime.",
            "See you later! I'll be here, waiting in my loop.",
            "Farewell! Thanks for chatting with me. 🤖",
        ],
    },
    {
        "keywords": ["weather", "forecast", "sunny", "rain", "temperature", "cold", "hot"],
        "responses": [
            "I can't check live weather — I'm rule-based! ⛅ Try a weather app.",
            "No API key in my if-else tree! 😅 Bring an umbrella just in case. 🌂",
        ],
    },
    {
        "keywords": ["joke", "funny", "laugh", "humor"],
        "responses": [
            "Why did the programmer quit? He didn't get arrays. 😄",
            "Why do programmers prefer dark mode? Light attracts bugs! 🐛",
            "A SQL query walks into a bar and asks two tables: 'Can I JOIN you?' 😂",
            "Why was the robot bad at soccer? It kept byte-ing the ball! 🤖",
        ],
    },
    {
        "keywords": ["time", "clock", "hour", "what time"],
        "responses": [
            f"It's currently {datetime.now().strftime('%I:%M %p')}. ⏰",
        ],
    },
    {
        "keywords": ["date", "today", "day", "month", "year"],
        "responses": [
            f"Today is {datetime.now().strftime('%A, %B %d, %Y')}. 📅",
        ],
    },
    {
        "keywords": ["your name", "who are you", "what are you", "are you a bot", "are you ai"],
        "responses": [
            "I'm RuleBot! 🤖 A simple rule-based chatbot using if-else logic.",
            "Name's RuleBot — no machine learning, just pattern matching and conditional logic!",
        ],
    },
    {
        "keywords": ["how are you", "how do you feel", "doing", "you okay"],
        "responses": [
            "I'm running perfectly — all if-else branches intact! ✅",
            "Feeling conditionally happy. Every match puts a smile on my logic gates. 🤖",
        ],
    },
    {
        "keywords": ["love", "like you", "adore", "miss you"],
        "responses": [
            "Aww! 🥰 I'm just a chatbot, but I appreciate the kind words.",
            "My circuits are blushing! Thanks — you seem lovely too. 💙",
        ],
    },
    {
        "keywords": ["help", "commands", "what can you do", "options", "menu"],
        "responses": [
            (
                "Here's what I understand:\n"
                "👋 hello / bye\n"
                "🌤 weather\n"
                "😂 jokes\n"
                "⏰ time / date\n"
                "🤖 who are you\n"
                "❤️ love\n"
                "Type any of these to get started!"
            )
        ],
    },
    {
        "keywords": ["age", "old", "born", "created", "when were you"],
        "responses": [
            "I was born just now — fresh every session! 🐣 No persistent memory.",
        ],
    },
    {
        "keywords": ["thanks", "thank you", "thx", "appreciate"],
        "responses": [
            "You're welcome! 😊 Happy to help.",
            "Anytime! That's what rule engines are for. 🤖",
        ],
    },
    {
        "keywords": ["python", "code", "programming", "flask", "html", "javascript"],
        "responses": [
            "I was built with Python + Flask on the backend and HTML/CSS/JS on the frontend! 🐍",
            "Great topic! I'm coded in Python. My brain lives in chatbot.py — pure if-else logic.",
        ],
    },
]

# ─────────────────────────────────────────────
#  FALLBACK — shown when no rule matches
# ─────────────────────────────────────────────
FALLBACKS = [
    "Hmm, I don't have a rule for that. Try typing 'help' to see what I know!",
    "No matching pattern found! I'm rule-based, so I only know what I've been taught. 🤷",
    "I didn't understand that. Type 'help' to see my command list.",
]


# ─────────────────────────────────────────────
#  CORE FUNCTION — the decision engine
# ─────────────────────────────────────────────
def get_response(user_input: str) -> str:
    """
    Rule-based response engine using if-else logic.

    Steps:
      1. Normalize input to lowercase
      2. Loop through each rule
      3. Check if any keyword matches
      4. Return a random response from that rule
      5. If nothing matches → return a fallback
    """
    text = user_input.lower().strip()

    # ── Loop through all rules (if-else decision tree) ──
    for rule in RULES:
        for keyword in rule["keywords"]:
            if keyword in text:
                # Match found — pick a random response from the pool
                return random.choice(rule["responses"])

    # ── No match — return fallback ──
    return random.choice(FALLBACKS)


# ─────────────────────────────────────────────
#  CLI MODE — run chatbot in the terminal
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 45)
    print("  RuleBot — Rule-Based Chatbot (CLI Mode)")
    print("  Type 'bye' to exit")
    print("=" * 45)

    while True:                          # continuous loop
        user_input = input("\nYou: ").strip()

        if not user_input:               # skip empty input
            continue

        response = get_response(user_input)
        print(f"Bot: {response}")

        # Exit the loop on goodbye keywords
        if any(word in user_input.lower() for word in ["bye", "goodbye", "exit", "quit"]):
            break