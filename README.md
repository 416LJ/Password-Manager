# Password Manager

A simple, local GUI-based password manager application build with Python and Tkinter. This application allows you to securely store your passwords, generate strong new passwords, and easily search for saved credentials.

## Features

- **Store Passwords**: Save your website credentials (website, email/username, password) locally.
- **Password Generator**: detailed, automatic generation of strong passwords containing a mix of letters, numbers, and symbols.
- **Clipboard Integration**: Automatically copies generated passwords to your clipboard for easy pasting.
- **Search Functionality**: Quickly retrieve saved password details by searching for the website name.
- **Local Storage**: All data is stored securely in a local `data.json` file.

## Prerequisites

- Python 3.x
- `pyperclip` library

## Installation

1.  **Clone the repository** or download the source code:

    ```sh
    git clone <repository-url>
    cd password-manager
    ```

2.  **Install dependencies**:
    The application requires `pyperclip` for clipboard functionality. Install it using pip:

    ```sh
    pip install pyperclip
    ```

    _Note: Tkinter is usually included with Python installations. If you encounter an error related to Tkinter, ensure it is installed on your system._

## Usage

1.  **Run the application**:

    ```sh
    python main.py
    ```

2.  **Using the App**:
    - **Add a Password**:
      - Enter the **Website** URL.
      - Enter your **Email/Username** (defaults to `laxsan.jeya@gmail.com` but performs as a normal entry field).
      - Enter a **Password** or click **Generate Password** to create a strong one automatically.
      - Click **Add** to save the entry.
    - **Search for a Password**:
      - Enter the **Website** name you want to find.
      - Click **Search**. A popup will display the email and password if the website is found.
    - **Generate Password**:
      - Click **Generate Password** to fill the password field with a random secure password and copy it to your clipboard.

## Project Structure

- `main.py`: The main script containing the application logic and GUI code.
- `data.json`: Stores the password data in JSON format (created automatically upon first save).
- `logo.png`: Image file used for the application logo.

## Dependencies

- **tkinter**: For the Graphical User Interface.
- **json**: For saving and retrieving data.
- **random**: For generating random password characters.
- **pyperclip**: For copying text to the clipboard.

## Notes

- The application creates a `data.json` file in the same directory to store your passwords. Keep this file secure.
- The default email in the UI is set to `laxsan.jeya@gmail.com`. You can change this in the source code (`main.py`) or overwrite it in the GUI.

## License

This project is open source and available for personal use.
