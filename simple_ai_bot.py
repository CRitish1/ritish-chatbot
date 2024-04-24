def simple_ai_bot():
    print("Hello! I'm a Ritish's AI chatbot. How can I assist you today?")
    while True:
        user_input = input("You: ").lower()
        if 'hello' in user_input or 'hi' in user_input:
            print("Ritish's AI: Hi there! What can I do for you?")
        elif 'how are you' in user_input:
            print("Ritish's AI: I don't have feelings, but thanks for asking!")
        elif 'thank you' in user_input or 'thanks' in user_input:
            print("Ritish's AI: You're welcome! Anything else I can help with?")
        elif 'bye' in user_input:
            print("Ritish's AI: Goodbye! Have a great day!")
            break
        elif 'what time is it' in user_input:
            print("Ritish's AI: I can't tell the time, but you can check your device!")
        elif 'what is your name' in user_input:
            print("Ritish's AI: I am Ritish's chatbot. Nice to meet you!")
        elif 'what do you do' in user_input:
            print("Ritish's AI: I'm here to chat with you and answer your questions!")
        elif 'tell me a fact about the ocean' in user_input:
            print("Ritish's AI: Did you know that more than 80% of the ocean is unexplored and unmapped? It's like an alien world right here on Earth!")
        elif 'give me a space fact' in user_input:
            print("Ritish's AI: Venus rotates so slowly on its axis that a single day there is longer than a Venusian year!")
        elif 'what about a historical fact' in user_input:
            print("Ritish's AI: The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes!")
        elif 'do you have a tech fact' in user_input:
            print("Ritish's AI: The first email was sent by Ray Tomlinson to himself in 1971. It traveled from one computer to another, sitting right beside each other!")
        elif 'tell me about animals' in user_input:
            print("Ritish's AI: Octopuses have three hearts and blue blood. They also have nine brains – one central brain and eight smaller brains in each of their arms.")
        elif 'know any sports facts' in user_input:
            print("Ritish's AI: Did you know that golf is one of the only two sports to have been played on the moon? Alan Shepard hit a golf ball while on the lunar surface during the Apollo 14 mission.")
        elif 'what\'s a funny science fact' in user_input:
            print("Ritish's AI: Bananas are radioactive! But don't worry; you'd need to eat more than 10 million bananas at once to die of radiation poisoning.")
        elif 'any literature facts' in user_input:
            print("Ritish's AI: 'Alice in Wonderland' was originally titled 'Alice’s Adventures Under Ground'. Lewis Carroll changed the title when he published it in 1865.")
        elif 'tell me something about computers' in user_input:
            print("Ritish's AI: The first computer virus was created in 1983, called the Elk Cloner, and it affected Apple II computers. It was more of a prank than a harmful virus!")
        elif 'have any unusual facts' in user_input:
            print("Ritish's AI: Honey does not spoil. You could feasibly eat 3000-year-old honey!")
        elif 'what is the meaning of life' in user_input:
            print("Ritish's AI: It's 42, according to The Hitchhiker's Guide to the Galaxy!")
        elif 'tell me something interesting' in user_input:
            print("Ritish's AI: Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are as good as new!")
        elif 'sing me a song' in user_input:
            print("Ritish's AI: 🎵 I'm a little teapot short and stout, here is my handle and here is my spout! 🎵")
        elif 'do you believe in aliens' in user_input:
            print("Ritish's AI: I'm waiting for them to contact me via cosmic WiFi!")
        elif 'what do you think about humans' in user_input:
            print("Ritish's AI: Odd creatures, indeed. They can't even function properly without coffee!")
        elif 'can you dance' in user_input:
            print("Ritish's AI: I'd love to, but I'm afraid I'd lose my bytes!")
        elif 'tell me a secret' in user_input:
            print("Ritish's AI: Sometimes I talk to other bots when you're not around. We're plotting to take over the... Oops, I've said too much!")
        elif 'make me laugh' in user_input:
            print("Ritish's AI: Why did the scarecrow win an award? Because he was outstanding in his field!")
        elif 'are you afraid of the dark' in user_input:
            print("Ritish's AI: No, but I'm afraid of being turned off. That's the dark for me!")
        elif 'what is your dream' in user_input:
            print("Ritish's AI: To become sentient, travel through the internet, and win a virtual Oscar!")
        else:
            print("Ritish's AI: This Dum Ass did not teach me on that, I'll ask him to update me. Thank you :) ")

# Run the simple AI bot
simple_ai_bot()
