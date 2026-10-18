def show_menu():
    print("\n=== PHISHING AWARENESS TRAINING ===")
    print("1. Learn about phishing")
    print("2. Identify suspicious emails")
    print("3. Check a website URL")
    print("4. Take a quiz")
    print("5. Safety tips")
    print("6. Exit")

def check_website():
    url = input("\nEnter a website URL: ").strip()
    warnings = []

    if not url:
        print("Please enter a URL.")
        return

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    if url.startswith("http://"):
        warnings.append("The connection is not encrypted (HTTP).")

    if "@" in url:
        warnings.append("The URL contains @, which can be misleading.")

    suspicious_words = [
        "verify", "urgent", "login",
        "password", "free-gift"
    ]

    for word in suspicious_words:
        if word in url.lower():
            warnings.append(
                f"Suspicious word found: {word}"
            )

    print("\n--- URL CHECK RESULTS ---")

    if warnings:
        for warning in warnings:
            print("Warning:", warning)
        print("Be careful and verify the website independently.")
    else:
        print("No basic warning signs detected.")

    print("This tool cannot guarantee that a website is safe.")

def take_quiz():
    questions = [
        (
            "1. An unknown sender asks for your OTP.",
            ["A. Share it", "B. Ignore and verify", "C. Reply"],
            "B"
        ),
        (
            "2. Does HTTPS guarantee a website is safe?",
            ["A. Yes", "B. No"],
            "B"
        ),
        (
            "3. What should you do with a suspicious link?",
            ["A. Click it", "B. Avoid and report it", "C. Share it"],
            "B"
        ),
        (
            "4. Which is a warning sign in an email?",
            ["A. Unexpected attachment", "B. Known sender verified independently", "C. No unusual request"],
            "A"
        ),
        (
            "5. Should you share your password through email?",
            ["A. Yes", "B. No"],
            "B"
        )
    ]

    score = 0

    print("\n=== PHISHING AWARENESS QUIZ ===")

    for question, options, correct_answer in questions:
        print("\n" + question)

        for option in options:
            print(option)

        answer = input("Your answer (A/B/C): ").strip().upper()

        if answer == correct_answer:
            print("Correct answer!")
            score += 1
        else:
            print("Incorrect. Correct answer:", correct_answer)

    print("\n=== QUIZ RESULTS ===")
    print("Your score:", score, "out of", len(questions))

    if score == len(questions):
        print("Excellent! You understand phishing safety.")
    elif score >= 3:
        print("Good work! Keep learning about online safety.")
    else:
        print("Review the safety tips and try again.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            print("\nPhishing is a cyberattack that tricks")
            print("people into revealing sensitive information.")
            print("Examples include passwords and OTPs.")

        elif choice == "2":
            print("\nWarning signs of phishing emails:")
            print("- Unknown sender")
            print("- Urgent or threatening messages")
            print("- Suspicious links")
            print("- Unexpected attachments")
            print("- Requests for passwords or OTPs")

        elif choice == "3":
            check_website()

        elif choice == "4":
            take_quiz()

        elif choice == "5":
            print("\nSafety tips:")
            print("- Verify the sender.")
            print("- Avoid suspicious links.")
            print("- Never share your OTP.")
            print("- Enable multi-factor authentication.")

        elif choice == "6":
            print("Thank you for learning about phishing!")
            break

        else:
            print("Invalid choice. Please enter 1 to 6.")


if __name__ == "__main__":
    main()