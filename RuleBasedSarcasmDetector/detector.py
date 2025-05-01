import re

# 🎭 Sarcasm Patterns 
sarcasm_patterns = [
    r"\boh (great|wow)\b",
    r"\byeah right\b",
    r"\bsure(eee+)?\b",
    r"\bloved it.*not\b",
    r"\bas if\b",
    r"\bthanks a lot\b",
    r"\btotally\b",
    r"\bamazing\.$", r"\bgreat\.$", r"\bfantastic\.$",
    r"\w+…+\s*not",         # Cool… not.
    r"\b(not)+!*$",         # NOT!!!
    r"\bbest.*ever.*not\b",
    r"\bsooo+.*\b",
    r"\bcan't wait\b",
    r"\bsuper fun\b",
    r"\bwhat a surprise\b",
    r"\blucky me\b",
    r"\blucky us\b",
    r"\bloved every second.*not\b",
    r"🙄|😒|🤦|🫠|🤷|😑|😬|😐|😏"
]

# 🌞 Positive Keywords 
positive_keywords = {
    "amazing", "awesome", "fantastic", "great", "excellent", "beautiful", "mind-blowing",
    "wonderful", "genius", "touching", "uplifting", "incredible", "smiling", "brilliant",
    "superb", "stunning", "perfect", "emotional", "charming", "heartfelt", "well-made",
    "entertaining", "moving", "inspiring", "enjoyed", "loved", "best", "masterpiece",
    "funny", "delightful", "engaging", "satisfying", "lovely", "hilarious"
}

# 🌧 Negative Keywords 
negative_keywords = {
    "boring", "disappointment", "disappointing", "predictable", "dull", "waste",
    "slow", "terrible", "forgettable", "weak", "forced", "dragged", "awful",
    "mediocre", "cringe", "cheesy", "poor", "annoying", "overrated", "underwhelming",
    "flat", "stupid", "horrible", "nonsense", "nonsensical", "lame", "ridiculous",
    "bad", "unwatchable", "poorly", "unoriginal", "pathetic", "tiresome", "painful",
    "laughable", "incoherent"
}

def detect_sarcasm(text):
    """Returns True if sarcasm is detected in the text."""
    text = text.lower()
    for pattern in sarcasm_patterns:
        if re.search(pattern, text):
            return True
    return False

def classify_sentiment(text):
    """Classifies the sentiment as Positive, Negative, or Neutral based on keyword frequency."""
    words = text.lower().split()
    pos_count = sum(1 for word in words if word in positive_keywords)
    neg_count = sum(1 for word in words if word in negative_keywords)

    if pos_count > neg_count:
        return "Positive 🙂"
    elif neg_count > pos_count:
        return "Negative 🙁"
    else:
        return "Neutral 😐"
