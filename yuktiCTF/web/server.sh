#!/bin/bash

# Server's IP address and port
HOST="10.11.18.50"
PORT=80

# Function to receive file
receive_file() {
    # Create a socket and listen for incoming connections
    while true; do
        # Accept a connection from a client
        client_socket=$(nc -l -p $PORT)
        echo "Connection from $client_socket"

        # Receive file data from the client
        while IFS= read -r line; do
            echo "$line" >> received_file.txt
        done < "$client_socket"

        echo "File received successfully"
    done
}

# Call the function
receive_file
