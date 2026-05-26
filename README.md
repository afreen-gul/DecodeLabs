# 🤖 RuleBot — Rule-Based AI Chatbot

A beginner-friendly chatbot built with **Python + Flask** that uses
pure **if-else logic** (no AI/ML libraries required).

---

## 📁 Folder Structure

```
rulebot/
├── app.py              ← Flask server (routes)
├── chatbot.py          ← Rule engine (if-else brain)
├── requirements.txt    ← Python dependencies
├── templates/
│   └── index.html      ← Chat UI (HTML)
└── static/
    ├── css/
    │   └── style.css   ← Styling
    └── js/
        └── chat.js     ← Frontend logic (fetch API)
```

---

## 🚀 Setup & Run (Step by Step)

### Step 1 — Make sure Python is installed
```bash
python --version    # should be 3.8 or higher
```

### Step 2 — Create a virtual environment (recommended)
```bash
python -m venv venv

# Activate it:
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### Step 3 — Install Flask
```bash
pip install -r requirements.txt
```

### Step 4 — Run the Flask server
```bash
python app.py
```

### Step 5 — Open in browser
```
http://127.0.0.1:5000
```

---

## 💻 Run in Terminal (No Browser Needed)

You can also run the chatbot directly in your terminal:
```bash
python chatbot.py
```

---

## 🧠 How the Rule Engine Works

```python
# chatbot.py — simplified view

RULES = [
    { "keywords": ["hello", "hi"],  "responses": ["Hello! 👋"] },
    { "keywords": ["joke"],         "responses": ["Why did the programmer quit? No arrays!"] },
    # ... more rules
]

def get_response(user_input):
    text = user_input.lower()

    for rule in RULES:               # loop through rules
        for keyword in rule["keywords"]:
            if keyword in text:      # if-else decision
                return random.choice(rule["responses"])

    return "I don't understand that!"   # fallback
```

---

## ➕ How to Add New Rules

Open `chatbot.py` and add a new entry to the `RULES` list:

```python
{
    "keywords": ["pizza", "food", "hungry"],
    "responses": [
        "I love pizza! 🍕 Pepperoni is the best.",
        "Food? I can't eat, but I hear pizza is amazing!",
    ],
},
```

Save the file and restart Flask — that's it!

---

## 🔌 API Endpoint

| Method | URL     | Body                      | Response                   |
|--------|---------|---------------------------|----------------------------|
| POST   | `/chat` | `{ "message": "hello" }` | `{ "response": "Hello! 👋" }` |

---

## 🛠 Key Concepts Demonstrated

| Concept            | Where                    |
|--------------------|--------------------------|
| if-else logic      | `chatbot.py` → `get_response()` |
| Continuous loop    | `chatbot.py` → CLI `while True` |
| Control flow       | Rule matching, fallback  |
| Functions          | `get_response()`, Flask routes |
| Lists & dicts      | `RULES` data structure   |
| REST API           | Flask `/chat` POST route |
| DOM manipulation   | `chat.js`                |
| Fetch API          | `chat.js` → POST to Flask |
