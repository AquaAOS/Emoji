import random

emoji_dict = {
    "happy": "😃",
    "sad": "😢",
    "angry": "😡",
    "mad": "😠",
    "finger": "🖕",
    "nice": "👍",
    "love": "❤️",
    "laugh": "😂",
    "cry": "😭",
    "confused": "😕",
    "heart": "💖",
    "fire": "🔥",
    "star": "⭐",
    "thumbs up": "👍",
    "thumbs down": "👎",
    "cool": "😎",
    "money": "💰",
    "shush": "🤫",
    "ghost": "👻",
    "alien": "👽",
    "unicorn": "🦄",
    "pizza": "🍕",
    "rocket": "🚀",
    "sun": "☀️",
    "moon": "🌙",
    "rose": "🌹"
    # Add more emojis and their corresponding words here
}

def add_to_dictionary():
    new_word = input("Enter a new word or phrase: ")
    emoji = input("Enter the corresponding emoji: ")
    emoji_dict[new_word] = emoji

def customize_emoji_mapping():
    print("Current Emoji Mapping:")
    for word, emoji in emoji_dict.items():
        print(f"{word}: {emoji}")

    while True:
        choice = input("Do you want to add a new mapping (1) or update an existing one (2)? (Enter 'exit' to quit): ")

        if choice == "1":
            add_to_dictionary()
        elif choice == "2":
            word_to_update = input("Enter the word or phrase you want to update: ")
            if word_to_update in emoji_dict:
                new_emoji = input(f"Enter the new emoji for '{word_to_update}': ")
                emoji_dict[word_to_update] = new_emoji
            else:
                print(f"'{word_to_update}' is not in the dictionary.")
        elif choice.lower() == "exit":
            break
        else:
            print("Invalid choice. Please enter '1' or '2.")

while True:
    user_input = input("Enter a text message to translate into emojis (or type 'exit' to quit): ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    input_words = user_input.split()

    translated_message = []
    for word in input_words:
        if word in emoji_dict:
            translated_message.append(emoji_dict[word])
        else:
            translated_message.append(word)
    
    translated_message = " ".join(translated_message)

    if user_input.lower() == "customize":
        customize_emoji_mapping()
    elif user_input.lower() == "test":
        test_sentence = " ".join(random.choice(list(emoji_dict.keys())) for _ in range(5))
        print(f"Test sentence: {test_sentence}")
        print("Translated message: ", " ".join(emoji_dict[word] for word in test_sentence.split() if word in emoji_dict))
