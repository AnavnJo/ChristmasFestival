- name: Run the bot
  env:
    DISCORD_TOKEN: ${{ secrets.DISCORD_TOKEN }}
  run: python src/my_bot.py
