import time

def slow_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.01)
    print()

# Questions database
questions = {
    "Password & Authentication": [
        ("Do you use strong and complex passwords? (1: Yes, 2: Sometimes, 3: No)", 3),
        ("Do you use different passwords for different accounts? (1: Yes, 2: Sometimes, 3: No)", 3),
        ("Do you use a password manager? (1: Yes, 2: Planning to, 3: No)", 2),
        ("Do you enable Multi-Factor Authentication (MFA)? (1: Yes, 2: For some accounts, 3: No)", 3),
    ],
    "Device Security": [
        ("Is your antivirus software installed and regularly updated? (1: Yes, 2: Not sure, 3: No)", 2),
        ("Are your OS and apps regularly updated? (1: Yes, 2: Occasionally, 3: No)", 2),
        ("Do you use a firewall (built-in or 3rd party)? (1: Yes, 2: Not sure, 3: No)", 1),
    ],
    "Social Media Privacy": [
        ("Are your social media profiles set to private or limited visibility? (1: Yes, 2: Some, 3: No)", 2),
        ("Do you avoid oversharing personal data online? (1: Yes, 2: Sometimes, 3: No)", 1),
        ("Do you review your privacy settings regularly? (1: Yes, 2: Rarely, 3: Never)", 1),
    ],
    "Email & Phishing": [
        ("Can you confidently identify phishing emails? (1: Yes, 2: Sometimes, 3: No)", 3),
        ("Do you check sender email addresses and hover over links? (1: Always, 2: Sometimes, 3: Never)", 2),
        ("Do you report or delete suspicious emails? (1: Yes, 2: Sometimes, 3: No)", 1),
    ],
    "Data Backup": [
        ("Do you back up your data regularly? (1: Weekly, 2: Monthly, 3: Rarely/Never)", 2),
        ("Are your backups encrypted? (1: Yes, 2: Not sure, 3: No)", 2),
    ]
}

score = 0
max_score = 0
recommendations = []

slow_print("🔐 Welcome to the Enhanced Personal Cyber Hygiene Self-Audit Tool!\n")

for category, qs in questions.items():
    print(f"\n📂 {category}")
    for q_text, weight in qs:
        while True:
            try:
                ans = int(input(f"   {q_text} "))
                if ans not in [1, 2, 3]:
                    raise ValueError
                break
            except ValueError:
                print("   Please enter a valid number (1, 2, or 3).")

        # Calculate score (1 = best)
        if ans == 1:
            score += weight
        elif ans == 2:
            score += weight // 2
            recommendations.append(f"Consider improving: {q_text.split('?')[0]}.")
        else:
            recommendations.append(f"Urgent: {q_text.split('?')[0]} needs attention.")
        max_score += weight

# Final Score Evaluation
print("\n🧾 Audit Summary")
print(f"Your Score: {score} / {max_score}")

percentage = (score / max_score) * 100
if percentage >= 85:
    hygiene_level = "Excellent"
elif percentage >= 70:
    hygiene_level = "Good"
elif percentage >= 50:
    hygiene_level = "Fair"
else:
    hygiene_level = "Poor"

print(f"Cyber Hygiene Level: {hygiene_level} ({percentage:.1f}%)")

# Recommendations
if recommendations:
    print("\n📌 Recommendations:")
    for rec in recommendations:
        print(f"- {rec}")
else:
    print("\n✅ You're doing great! No critical recommendations at this time.")

# Save Results (Optional)
save = input("\nWould you like to save this report to a file? (yes/no): ").lower()
if save == "yes":
    with open("cyber_hygiene_report.txt", "w") as file:
        file.write(f"Cyber Hygiene Audit Report\n")
        file.write(f"Score: {score}/{max_score} ({percentage:.1f}%)\n")
        file.write(f"Level: {hygiene_level}\n\nRecommendations:\n")
        for rec in recommendations:
            file.write(f"- {rec}\n")
    print("📝 Report saved to 'cyber_hygiene_report.txt'")

print("\n🔁 Consider re-running this audit every 3 months for best results!")
