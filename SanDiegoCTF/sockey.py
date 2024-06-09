from pwn import *

# Define the WebSocket URL
ws_url = "wss://ctf.sdc.tf/api/proxy/ff53a15a-86f7-400c-9656-ec5d82a17b38"

# Connect to the WebSocket server
io = process(["websocat", ws_url], level='error')

# Interact with the WebSocket server
io.interactive()

