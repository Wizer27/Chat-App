# Chat Roulette App

This is a simple chat application created using the Kivy framework in Python. The application allows users to input their personal information and search for other users based on their country, city, age, and gender.

## Features

- User input for country, city, age, name, phone number, and gender.
- Toggle buttons to select gender.
- Checkboxes to specify whether to search for people in the same country and/or city.
- Random data generation for simulated users.
- Sorting of users based on their proximity to the user's location.
- Error handling for invalid inputs.
- Kivy GUI components for user interaction.

## Requirements

- Python 3.x
- Kivy

## Installation

1. Install Python 3.x from [python.org](https://www.python.org/).
2. Install Kivy using pip:
    ```sh
    pip install kivy
    ```

## Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/IvanVINOG/Chat-App
    cd Chat-App
    ```

2. Run the application:
    ```sh
    python main.py
    ```

3. In the application window, enter your personal information:
    - Country
    - City
    - Age
    - Name
    - Phone number
    - Gender (select using the toggle buttons)

4. Use the checkboxes to specify whether to search for people in the same country and/or city.

5. Click the "Find" button to search for matching users.

## File Descriptions

- `main.py`: The main script containing the application logic and GUI components.
- `111.txt`: A text file used to store user data. Each user's data is stored in a new line with the format: `name country city gender age phone_number`.

## Classes

### Human

A class to represent a human user with attributes for number, name, age, country, city, and gender. Provides methods for user input, data storage, random data generation, and compatibility checks with other users.

### MyApp

A Kivy App class to create and manage the GUI for the chat application. Includes methods for building the interface and handling button presses.

## Example

```python
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.togglebutton import ToggleButton
import random

# Define your data and classes here...

if __name__ == "__main__":
    MyApp().run()
