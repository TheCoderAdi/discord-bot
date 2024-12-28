# Sample Python Discord Bot

This repository contains a Python-based Discord bot that integrates with Daytona for development and testing. The bot uses the Discord API and is designed to demonstrate scalable and modular bot development practices.

---

## 🚀 Getting Started

### Open Using Daytona

1. **Install Daytona**: Follow the [Daytona installation guide](https://www.daytona.io/docs/installation/installation/).

2. **Create the Workspace**:

   ```bash
   daytona create https://github.com/TheCoderAdi/discord-bot
   ```

3. **Setup Environment**:  
   Ensure all dependencies are installed by running:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Bot**:

   - Create a `.env` file with your bot token and any other necessary credentials:
     ```
     DISCORD_TOKEN=your_discord_bot_token
     PRODIA_API_KEY=your_prodia_api_key
     ```

5. **Run the Bot**:  
   Start the bot by running:
   ```bash
   python bot.py
   ```

---

## ✨ Features

- **Integration with Daytona**: Standardized development environment with devcontainers.
- **Python Bot Framework**: Modular design to allow easy extension of commands and features.
- **Discord API**: Handles real-time communication on Discord servers.

---

## 🤝 Contributing

1. Fork the repository.
2. Create a new branch for your changes:
   ```bash
   git checkout -b feature-branch
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-branch
   ```
5. Open a pull request.

---

## 📜 License

This repository is licensed under the MIT License. See the `LICENSE` file for more details.

---

## 📚 Learn More

For more details on Daytona, visit the [official documentation](https://www.daytona.io/docs).
