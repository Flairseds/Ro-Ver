from resources.framework import client


@client.event
async def on_ready():
    print(f'Logged in as {client.user}', flush=True)
