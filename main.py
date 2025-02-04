#Fairus Simple Morse Code Translator


#morse and alphabet
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
MORSE_CODE = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---',
              '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-',
              '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--',
              '....-', '.....', '-....', '--...', '---..', '----.']

# Create dictionaries for quick lookups
ENG_TO_MORSE = {letter: code for letter, code in zip(ALPHABET, MORSE_CODE)}
MORSE_TO_ENG = {code: letter for letter, code in zip(MORSE_CODE, ALPHABET)}

#functions to turn english to morsecode
def english_to_morse(text):
    """Convert English text to Morse Code."""
    text = text.upper()  # Convert to uppercase for consistency
    morse_translation = []
    
    for char in text:
        if char in ENG_TO_MORSE:
            morse_translation.append(ENG_TO_MORSE[char])
        elif char == ' ':
            morse_translation.append('/')  # Represent spaces as '/'
        else:
            print(f"Warning: '{char}' cannot be translated to Morse Code.")
    
    return ' '.join(morse_translation)

#function to turn morse to english
def morse_to_english(morse_code):
    """Convert Morse Code to English text."""
    words = morse_code.strip().split(' / ')  # Words are separated by '/'
    translated_text = []
    
    for word in words:
        letters = word.split()
        translated_word = ''.join(MORSE_TO_ENG.get(letter, '?') for letter in letters)  # '?' for unknown symbols
        translated_text.append(translated_word)
    
    return ' '.join(translated_text)

#the main function
def main():
    """Main function to interact with the user."""
    try:
        while True:
            print("\nMorse Code Translator")
            print("1. English to Morse Code")
            print("2. Morse Code to English")
            print("3. Exit")
            
            try:
                choice = input("Choose an option (1/2/3): ").strip()
            except EOFError:
                print("\nInput error detected. Exiting program.")
                break
            
            if choice == '1':
                text = input("Enter text to convert to Morse Code: ")
                print("Morse Code:", english_to_morse(text))
            elif choice == '2':
                morse = input("Enter Morse Code to convert to English (use '/' for spaces): ")
                print("English Text:", morse_to_english(morse))
            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please choose 1, 2, or 3.")
    except OSError as e:
        print(f"An OS error occurred: {e}")
        print("Exiting program.")

if __name__ == "__main__":
    main()
