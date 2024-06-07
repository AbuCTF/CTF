#!/bin/bash

# Server's IP address and port
SERVER_HOST="10.11.18.50"
SERVER_PORT=80

# Path to the file to send
FILE_PATH="server.sh"

# Function to send file
send_file() {
    # Connect to the server
    echo "Sending file to server..."
    cat "$FILE_PATH" | nc $SERVER_HOST $SERVER_PORT
    echo "File sent successfully"
}

# Call the function
send_file
