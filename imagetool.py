from PIL import Image
import numpy as np

def encrypt_image(image_path, key, swap):
    image = Image.open(image_path)
    pixels = np.array(image)

    # Add the key to each pixel value (simple mathematical operation)
    encrypted_pixels = (pixels + key) % 256

    if swap:
        # Swap pixel values in a deterministic manner
        flat_pixels = encrypted_pixels.flatten()
        flat_pixels[::2], flat_pixels[1::2] = flat_pixels[1::2], flat_pixels[::2]
        encrypted_pixels = flat_pixels.reshape(pixels.shape)
    
    encrypted_image = Image.fromarray(encrypted_pixels.astype('uint8'))
    encrypted_image.save('encrypted_image.png')

def decrypt_image(image_path, key, swap):
    image = Image.open(image_path)
    pixels = np.array(image)

    if swap:
        # Swap pixel values back to original positions
        flat_pixels = pixels.flatten()
        flat_pixels[::2], flat_pixels[1::2] = flat_pixels[1::2], flat_pixels[::2]
        pixels = flat_pixels.reshape(pixels.shape)

    # Subtract the key from each pixel value
    decrypted_pixels = (pixels - key) % 256

    decrypted_image = Image.fromarray(decrypted_pixels.astype('uint8'))
    decrypted_image.save('decrypted_image.png')

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Encrypt or decrypt an image.')
    parser.add_argument('action', choices=['encrypt', 'decrypt'], help='Action to perform')
    parser.add_argument('image_path', help='Path to the image file')
    parser.add_argument('key', type=int, help='Encryption/Decryption key')
    parser.add_argument('--swap', action='store_true', help='Whether to swap pixels')
    
    args = parser.parse_args()

    if args.action == 'encrypt':
        encrypt_image(args.image_path, args.key, args.swap)
    else:
        decrypt_image(args.image_path, args.key, args.swap)
