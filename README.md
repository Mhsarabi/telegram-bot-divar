# Divar Telegram Bot

A Python-based Telegram bot designed to connect Telegram with **Divar**, an Iranian online classifieds platform.

## Overview

This project explores the integration of web scraping and Telegram bot development to provide a Telegram-based interface for interacting with Divar.

It uses HTTP requests and HTML parsing to communicate with web content, while the Telegram bot provides the user interaction layer.

## Tech Stack

- **Python** – Core programming language
- **pyTelegramBotAPI** – Telegram bot development
- **Requests** – HTTP communication
- **BeautifulSoup4** – HTML parsing

## Project Structure

```text
telegram-bot-divar/
│
├── core/             # Core application logic
├── requirements.txt  # Project dependencies
├── LICENSE           # MIT License
└── .gitignore
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Mhsarabi/telegram-bot-divar.git
cd telegram-bot-divar
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the bot

Create a Telegram bot using [@BotFather](https://t.me/BotFather) and obtain its API token.

Configure the token according to the application's configuration in the `core` directory.

### 5. Run the application

Run the project's main Python entry point from the repository root.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
