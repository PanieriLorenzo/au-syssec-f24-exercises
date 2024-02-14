from ppmcrypt import PPMImage
import subprocess
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


IN_FILE = "au"
OUT_FILE = "au_new"

key = get_random_bytes(16)


image = PPMImage.load_from_file(open(IN_FILE + ".ppm", "rb"))
image.encrypt(key, 'CBC')
image.data[100000] = 0xff
image.decrypt(key)
image.write_to_file(open(OUT_FILE + ".ppm", "wb"))

subprocess.run(["convert", OUT_FILE + ".ppm", OUT_FILE + ".png"])
