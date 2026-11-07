# ==========================================
# PROJECT: SCAMSHIELD
# Smart Phishing Message Detection System
# ==========================================


# 1. DEFINE SUSPICIOUS KEYWORDS

suspicious_words = [
    "urgent", "verify", "password", "otp",
    "blocked", "suspended", "winner",
    "prize", "free", "claim", "click here"
]


# 2. STORE ANALYSIS HISTORY

history = []


# 3. CREATE MESSAGE ANALYSIS FUNCTION

def analyze_message(message):

    score = 0
    indicators = []
    text = message.lower()

    # 4. CHECK SUSPICIOUS KEYWORDS

    for word in suspicious_words:
        if word in text:
            score += 10
            indicators.append("Suspicious word: " + word)

    # 5. CHECK SUSPICIOUS LINKS

    if "http" in text or "www." in text:
        score += 25
        indicators.append("Suspicious website link")

    # 6. CHECK URGENCY AND SENSITIVE WORDS

    if text.count("!") >= 3:
        score += 10
        indicators.append("Excessive exclamation marks")

    if "password" in text or "otp" in text:
        score += 20
        indicators.append("Sensitive information request")

    # 7. CALCULATE FINAL RISK SCORE

    score = min(score, 100)

    if score >= 60:
        result = "HIGH RISK"

    elif score >= 30:
        result = "SUSPICIOUS"

    else:
        result = "LOW RISK"

    if not indicators:
        indicators.append("No suspicious patterns found")

    return score, result, indicators


# 8. DISPLAY ANALYSIS RESULTS

def display_result(message, score, result, indicators):

    print("\n========== ANALYSIS REPORT ==========")

    print("Message:", message)
    print("Risk Score:", score, "/100")
    print("Risk Level:", result)

    print("\nSuspicious Indicators:")

    for item in indicators:
        print("-", item)

    print("=====================================")


# 9. ANALYZE USER MESSAGE

def check_message():

    message = input("\nEnter message for analysis: ")

    if message.strip() == "":
        print("Please enter a valid message!")
        return

    score, result, indicators = analyze_message(message)

    display_result(message, score, result, indicators)

    history.append((message, score, result))


# 10. DISPLAY PREVIOUS ANALYSIS HISTORY

def show_history():

    print("\n========== SCAN HISTORY ==========")

    if len(history) == 0:
        print("No previous scans available.")

    else:
        for number, item in enumerate(history, start=1):

            print("\nScan Number:", number)
            print("Message:", item[0])
            print("Score:", item[1])
            print("Result:", item[2])

    print("==================================")


# 11. MAIN MENU

while True:

    print("\n========== SCAMSHIELD ==========")
    print("1. Analyze a Message")
    print("2. View Scan History")
    print("3. Exit")
    print("================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        check_message()

    elif choice == "2":
        show_history()

    elif choice == "3":
        print("Thank you for using ScamShield!")
        break

    else:
        print("Invalid choice! Please select 1, 2 or 3.")