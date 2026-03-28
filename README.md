# Random Image Bot 🖼️

A discord bot that returns a random image when you ping it.

## Running the Bot

Ensure that you have a recent version of Python and you have created a Discord bot on their developer portal. Then you can run these commands:

For Linux:

```bash
git clone https://github.com/ReedGraf/random-image-discord-bot.git
cd random-image-discord-bot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

> Sorry windows users, you're on your own.

Once you've done that, you'll want to create a `images` folder and a `.env` file. Fill the `images` folder with all the images you want it to pull from. Then add in your `.env` file: `TOKEN=<insert bot token here>`.

After all of that setup you should be all set to run the bot with, `python3 app.py` in your terminal.
