# Secure Chat Application

Python-based secure chat application implementing RSA and AES encryption for secure client-server communication.

## Overview

This project demonstrates secure messaging concepts using modern encryption techniques. The application establishes encrypted communication between two users through a client-server architecture.

The system uses:
- RSA encryption for secure key exchange
- AES encryption for encrypted message transmission
- Socket programming for network communication

## Features

- Secure encrypted messaging
- RSA public/private key exchange
- AES symmetric encryption
- Client-server communication
- Python socket programming
- Real-time message transfer

## Technologies Used

- Python
- Socket Programming
- RSA Encryption
- AES Encryption
- Cryptography Libraries

## Project Structure

```text
client.py
server.py
```

- `server.py` handles incoming connections and encrypted communication
- `client.py` connects to the server and sends encrypted messages

## How to Run

### Start the Server

```bash
python server.py
```

### Start the Client

Open a second terminal window:

```bash
python client.py
```

## Concepts Demonstrated

- Network programming
- Cryptography fundamentals
- Public/private key encryption
- Secure communication protocols
- Client-server architecture

## Future Improvements

Potential future improvements include:
- GUI interface
- Multi-user chat support
- Message authentication
- Secure file transfer
- Database integration

## Author

Ellie Storms
