import random

positive_responses = [
    "It is certain.", "It is decidedly so.", "Without a doubt.", "Yes, definitely.",
    "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.",
    "Yes.", "Signs point to yes.", "Absolutely!", "Certainly!", "The stars say yes.",
    "Positive vibes only.", "All signs point to yes.", "Count on it.", "No doubt about it.",
    "You got it!", "For sure.", "The answer is yes."
]

negative_responses = [
    "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.",
    "Very doubtful.", "No.", "Absolutely not.", "Definitely not.", "Not in a million years.",
    "Chances aren't good.", "I don't think so.", "Unlikely.", "The answer is no.",
    "Not a chance.", "No way.", "Negative.", "Don't bet on it.", "Nope.", "Try again later.",
    "It's not looking good."
]

neutral_responses = [
    "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.",
    "Concentrate and ask again.", "Maybe.", "It's possible.", "Hard to say.", "Not sure.",
    "Can't tell right now.", "Unclear, ask again.", "Indeterminate.", "Ask again soon.",
    "Focus and ask again.", "Wait and see.", "Time will tell.", "Uncertain.", "Ask again in a bit.",
    "The answer is unclear.", "Think about it and ask again."
]

question_count = 0

print("Welcome to the Dark Alleys of Magic-8 Ball Arcade")
while True:
    question = input("Ask me a question Confused one or remain silent to teleport back\n")
    if question.strip() == "":
        print("Farewell, Then")
        print("You've Been Granted " + str(question_count) + " answers till now!")
        break

    question_count += 1

    if question_count > 5:
        response_type = random.choices(
            ['positive', 'neutral', 'negative'],
            weights=[1, 3, 1],
            k=1
        )[0]
    else:
        response_type = random.choice(['positive', 'neutral', 'negative'])

    if response_type == "positive":
        answer = random.choice(positive_responses)
    elif response_type == "negative":
        answer = random.choice(negative_responses)
    else:
        answer = random.choice(neutral_responses)

    print("Fetching your Fate. . . .")
    print("The almighty Magic 8 Ball says: " + answer)
