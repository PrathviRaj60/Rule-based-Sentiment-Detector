from detector import detect_sarcasm, classify_sentiment

def main():
    print("Welcome to the Sentiment Detector 🎯")
    print("Type your sentence below (or type 'exit' to quit):\n")

    while True:
        review = input("📝 Your Sentence: ").strip()
        if review.lower() == "exit":
            print("Goodbye! 👋")
            break
        elif not review:
            print("⚠️ Please enter some text.\n")
            continue

        if detect_sarcasm(review):
            print("→ Detected: Sarcastic 😏\n")
        else:
            sentiment = classify_sentiment(review)
            print(f"→ Detected: {sentiment}\n")

if __name__ == "__main__":
    main()
