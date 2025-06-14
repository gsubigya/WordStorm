# ⚡ WordStorm – Custom Wordlist Generator in Python

**WordStorm** is a lightweight yet powerful Python script that creates highly customizable password wordlists from base words, numbers, and symbols. Whether you're learning password attacks, performing ethical pentesting, or building CTF resources this tool is for you.

1) Built from scratch as a personal challenge to learn WiFi security and custom wordlist generation.
2) Generates up to **12 million** unique combinations (scalable).
3) Tailored for **targeted OSINT-based wordlist creation**.

---

## 🔧 How It Works

1. **Base Words Input**  
   You manually define a list of base words in the script: names, nicknames, birthdays, email handles, etc.

2. **Numbers & Symbols**  
   Add common or target-specific numbers and special characters to enhance combinations.

3. **Smart Combinations**  
   The script generates combinations like:
   - `base + number` → john123
   - `symbol + base` → @john
   - `base + symbol + number` → john@007
   - Variants with capitalizations

4. **Output**  
   The final wordlist is written to a `.txt` file containing potentially **millions** of custom combinations.

---

## 🚀 Getting Started

```bash
git clone https://github.com/gsubigya/WordStorm.git
cd WordStorm
python wordstorm.py
