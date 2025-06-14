import random
import sys

# ──────────────────────────────────────────────────────────────
# Attempt to print a fancy banner
# ──────────────────────────────────────────────────────────────
import banner
# ──────────────────────────────────────────────────────────────
# STATIC DATA SETUP
# ──────────────────────────────────────────────────────────────

BASE_WORDS: list[str] = [
    # Core identifiers
    "Rishi", "Krishna", "Yadav", "School",
    "Common", "CommonWebsurfer",
    # Geography & localities
    "Kathmandu", "Sundhara", "Nepal", "Bagmati",
    # Education themes & roles
    "Education", "Principal", "Teacher", "Students", "SchoolLife",
    # Awards & certifications
    "BritishCouncil", "Award2021", "BCISA2021", "ISA2020", "ISAaward",
    # Misc.
    "LearningCenter", "SmartSchool", "WomenPower", "Shikshya",
    "BalMandir", "BalBikash", "NepalMontessori", "NepalEdu", "NepalSchool",
    "BaniyatarTokha", "Montessori", "NepaliWomen", "WomenLeadership",
    # Lifestyle & branding words
    "SWS", "MontessoriLife", "ChildEdu", "EarlyLearning", "SmartLearning",
    "PreSchool", "LittleSteps", "HappyKids", "HappyZone", "HappyMontessori",
    "GlobalSchool", "ShikshaSanstha", "EnglishMedium", "LearningZone",
    "EducationHub", "ModernSchool", "JuniorKids", "ChildCare",
    # Year tags for realism
    "Nepal2020", "Nepal2021", "Nepal2022", "Nepal2023",
]

SYMBOLS: list[str] = list("!@#$%^&*()_+=-?;:[]{}\\|./,")
NUMERIC_SUFFIXES: list[str] = [str(n) for n in range(1, 1000)] + [str(year) for year in range(1990, 2031)]
SPECIAL_SUFFIXES: list[str] = ["2021", "2022", "2023", "Nepal"]

# Simple leet‑speak mapping (single substitute per char for performance)
LEET_MAP: dict[str, str] = {
    "a": "@", "A": "@",
    "s": "$", "S": "$",
    "i": "1", "I": "1",
    "o": "0", "O": "0",
    "e": "3", "E": "3",
    "t": "7", "T": "7",
}

TARGET_COUNT = 20_000_000  # ≈20 million unique lines
OUTPUT_FILE = "ultra_wordlist.txt"
MIN_LENGTH = 8  # passwords shorter than this are skipped

# ──────────────────────────────────────────────────────────────
# HELPER FUNCTIONS
# ──────────────────────────────────────────────────────────────

def to_leetspeak(text: str) -> str:
    """Return the text with basic leet substitutions applied."""
    return "".join(LEET_MAP.get(ch, ch) for ch in text)


def random_case_mix(text: str) -> str:
    """Randomly toggle the case of each character (e.g., abc → aBc)."""
    return "".join(ch.upper() if random.choice((0, 1)) else ch.lower() for ch in text)


def insert_random_symbol(text: str) -> str:
    """Insert one random symbol at a random position inside *text*."""
    if len(text) < 2:
        return text
    index = random.randint(1, len(text) - 1)
    return text[:index] + random.choice(SYMBOLS) + text[index:]

# ──────────────────────────────────────────────────────────────
# VARIANT GENERATORS (small, testable units)
# ──────────────────────────────────────────────────────────────

def numeric_variants(keyword: str):
    """Append numeric suffixes plus common transformations."""
    for num in NUMERIC_SUFFIXES:
        word_num = f"{keyword}{num}"
        yield word_num
        yield word_num.lower()
        yield word_num.upper()
        yield to_leetspeak(word_num)
        mixed = random_case_mix(word_num)
        yield mixed
        yield insert_random_symbol(word_num)
        yield insert_random_symbol(mixed)


def symbol_variants(keyword: str):
    """Add a single symbol before, after, or inside the keyword."""
    halfway = len(keyword) // 2
    for sym in SYMBOLS:
        yield f"{keyword}{sym}"
        yield f"{sym}{keyword}"
        yield f"{keyword[:halfway]}{sym}{keyword[halfway:]}"


def special_year_variants(keyword: str):
    """Combine keyword with (symbol + special year) permutations."""
    for sym in SYMBOLS:
        for suffix in SPECIAL_SUFFIXES:
            yield f"{keyword}{sym}{suffix}"
            yield f"{keyword}{suffix}{sym}"


def paired_word_variants():
    """Keyword1 + Keyword2 combos with extra permutations."""
    for first in BASE_WORDS:
        for second in BASE_WORDS:
            if first == second:
                continue  # skip identical pairs to reduce duplicates
            combo = first + second
            yield combo
            yield insert_random_symbol(combo)
            yield random_case_mix(combo)
            yield to_leetspeak(combo)
            for num in NUMERIC_SUFFIXES:
                yield combo + num
                yield insert_random_symbol(combo + num)


def common_weak_passwords():
    """Localised weak passwords grafted onto core keywords."""
    weak_roots = ["12345678", "password", "password1", "iloveyou", "Nepal123", "Nepal2021"]
    for base in ("Gorakhalaya", "School", "Montessori", "Nepal"):
        for weak in weak_roots:
            yield f"{base}{weak}"
            yield f"{weak}{base}"
            yield insert_random_symbol(f"{base}{weak}")

# ──────────────────────────────────────────────────────────────
# MASTER GENERATOR
# ──────────────────────────────────────────────────────────────

def generate_wordlist_lines():
    """Yield password candidates until exhaustion (millions of lines)."""
    for keyword in BASE_WORDS:
        yield from numeric_variants(keyword)
        yield from symbol_variants(keyword)
        yield from special_year_variants(keyword)
    # After single‑word passes, do paired‑word explosion
    yield from paired_word_variants()
    # Finally append weak patterns
    yield from common_weak_passwords()

# ──────────────────────────────────────────────────────────────
# MAIN DRIVER
# ──────────────────────────────────────────────────────────────

def main() -> None:
    """Generate the wordlist file up to TARGET_COUNT entries."""
    generated = 0
    try:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as outfile:
            for candidate in generate_wordlist_lines():
                if len(candidate) < MIN_LENGTH:
                    continue  # enforce minimum length
                outfile.write(candidate + "\n")
                generated += 1
                if generated >= TARGET_COUNT:
                    break

        print(f"✅ Successfully generated {generated:,} passwords → {OUTPUT_FILE}")

    except IOError as io_err:
        print(f"❌ I/O error: {io_err}", file=sys.stderr)
    except Exception as unexpected_err:
        print(f"❌ Unexpected error: {unexpected_err}", file=sys.stderr)


if __name__ == "__main__":
    main()
