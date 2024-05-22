import random
def get_responses():

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

def magic_ball():
    print("Welcome to 8-Ball-Magic-Machine, We offer choices you're negligent or afraid to make")
    positive_responses, negative_responses, neutral_responses = get_responses()
    while True:
        question = input("Ask the machine a question of your desire or remain silent to exit: ")
        if question == "":
            break
        sort_of_responses = random.choice([positive_responses, negative_responses, neutral_responses])
        response = random.choice(sort_of_responses)
        print(f"The magic ball says: {response}\n")

if __name__ == "__main__":
    magic_ball()
