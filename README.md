# Tour Bot

Tour Bot is a Telegram bot that acts as a virtual tour guide for the city of Kaliningrad. Built with Python and the [pyTelegramBotAPI (telebot)](https://github.com/eternnoir/pyTelegramBotAPI) library, this project provides users with an interactive way to explore local attractions, learn about the city's history, and view photos of key sights—all within a conversational Telegram experience.

## Features

- **Interactive Menus**: Upon starting, users are greeted and presented with a main menu to select different days of their Kaliningrad tour.
- **Attraction Guides**: Each day contains a list of popular attractions. Selecting an attraction sends the user a photo and a detailed description (in Russian), helping them discover the story and significance of each site.
- **Rich Media**: The bot uses local image files (`amber.png`, `castle.png`, `beer.jpg`, etc.) to visually enhance the experience.
- **Russian Localization**: All interactions and descriptions are provided in Russian, making the bot ideal for Russian-speaking tourists or locals.

## How It Works

- The bot responds to the `/start` command, initiating the main menu.
- Users choose either "Day 1" or "Day 2" for different sightseeing routes.
- Each menu selection corresponds to a Kaliningrad landmark (e.g., Kant Island, Amber Museum, Victory Park, and more).
- Upon selection, the bot sends relevant images and descriptions directly in the chat.

## Technologies Used

- Python 3
- [pyTelegramBotAPI (telebot)](https://github.com/eternnoir/pyTelegramBotAPI)

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/Suvorov-Kirill/Tour_bot.git
   cd Tour_bot
   ```

2. **Install dependencies**
   ```bash
   pip install pyTelegramBotAPI
   ```

3. **Set up your Telegram Bot**
   - Create a new bot via [BotFather](https://t.me/botfather) on Telegram and obtain your API token.
   - Replace `'TOKEN'` in `bot.py` with your actual token.

4. **Run the bot**
   ```bash
   python bot.py
   ```

## Project Structure

- `bot.py` – Main logic for the Telegram bot.
- Image files (`amber.png`, `castle.png`, `beer.jpg`, etc.) – Used for sending photos of attractions to users.
- (Other files may be present; see the [repository](https://github.com/Suvorov-Kirill/Tour_bot/tree/main) for the complete list.)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

> _Tour Bot: Your virtual guide to Kaliningrad!_
