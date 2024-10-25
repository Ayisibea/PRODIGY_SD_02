import random
import PySimpleGUI as sg

# Function to create the guessing game
def guessing_game():
    # Function to start/restart the game
    def start_new_game():
        return random.randint(1, 100), 0
    
    # Initialize the game with a random number and set attempts to 0
    number_to_guess, attempts = start_new_game()

    # Define the layout for the PySimpleGUI window
    layout = [
        [sg.Text("I'm thinking of a number between 1 and 100.")],
        [sg.Text("Enter your guess:"), sg.InputText(key='guess')],
        [sg.Button('Submit'), sg.Button('Quit')],
        [sg.Text(size=(40, 1), key='output')],
        [sg.Text("Attempts: 0", size=(40, 1), key='attempts_output')],
        [sg.Button('Play Again', visible=False, key='play_again')]
    ]
    
    # Create the window
    window = sg.Window('Guessing Game', layout)
    
    while True:
        # Read the window events and values
        event, values = window.read()
        
        # If the user wants to quit, break the loop
        if event == sg.WIN_CLOSED or event == 'Quit':
            break

        if event == 'Submit':
            # Increase the attempt count
            attempts += 1
            
            try:
                # Get the user's guess and compare with the number
                guess = int(values['guess'])
                
                if guess < number_to_guess:
                    window['output'].update('Too low! Try again.')
                elif guess > number_to_guess:
                    window['output'].update('Too high! Try again.')
                else:
                    window['output'].update(f"You've won! It took you {attempts} attempts.")
                    window['attempts_output'].update(f'Attempts: {attempts}')
                    # Show the Play Again button
                    window['play_again'].update(visible=True)

            except ValueError:
                window['output'].update('Please enter a valid number.')
            
            # Update the attempts display
            window['attempts_output'].update(f'Attempts: {attempts}')
        
        if event == 'Play Again':
            # Reset the game by starting a new one
            number_to_guess, attempts = start_new_game()
            # Reset the output messages and hide the Play Again button
            window['output'].update("")
            window['attempts_output'].update("Attempts: 0")
            window['play_again'].update(visible=False)
            window['guess'].update("")  # Clear the input field

    # Close the window after finishing the game
    window.close()

# Run the game
guessing_game()
