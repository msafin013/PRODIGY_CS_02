# Overview
  This Python script provides a basic image encryption tool using pixel manipulation. It offers two simple encryption methods: swapping pixel values and applying a basic mathematical operation.

# Functions

### Encrypt an Image

python image_encryption.py encrypt <image_path> <key> [--swap]

### Decrypt an Image

python image_encryption.py decrypt <image_path> <key> [--swap]


# Example of usage..

python image_encryption.py encrypt images/input_image.png 50 --swap

python image_encryption.py decrypt encrypted_image.png 50 --swap


# Limitations
This is a simple demonstration and not secure for sensitive data.
The encryption methods are basic and can be easily broken.
The key space is limited.
