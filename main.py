import discord

client = discord.Client()

@client.event
async def on_ready():
  print('Bejelentkeztem {0.user} -ként'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.author.id == 159985870458322944 and message.content.startswith('GG'):
    mention = message.mentions[0].id
    response = f"Én is gratulálok neked <@!{mention}>, ügyes vagy"
    await message.channel.send(response)

client.run(TOKEN)

