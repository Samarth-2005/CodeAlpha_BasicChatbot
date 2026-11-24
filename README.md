# CodeAlpha_BasicChatbot

A rule-based **Basic Chatbot** built in Python for the **CodeAlpha Python Programming Internship (Task 4)**.

## Project Overview

This console-based chatbot responds to user inputs such as `"hello"`, `"how are you"`, `"what is your name"`, `"help"`, and `"bye"` with predefined replies using `if-elif-else` conditional logic, modular functions, and an interactive `while` loop.

## Features

- **Rule-Based Conversation**: Matches common greetings, questions, and keywords using normalized `if-elif-else` conditions.
- **Modular Function Design**: Separates response logic (`get_bot_response`) from the interactive console loop (`run_chatbot`).
- **Clean Exit Handling**: Continues chatting in a loop until the user types `"bye"`, `"goodbye"`, `"exit"`, or `"quit"`.

## Key Concepts Used

- `if-elif-else` statements
- Functions (`get_bot_response()`, `run_chatbot()`)
- `while` loops
- Console input/output (`input()`, `print()`, string normalization with `.strip()`, `.lower()`, `.rstrip()`)

## How to Run

1. Open a terminal in the project folder (`CodeAlpha_BasicChatbot`).
2. Run the script:
   ```bash
   python basic_chatbot.py
   ```
