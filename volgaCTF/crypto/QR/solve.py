from PIL import Image
from secret import flag
from lfsr_parameters import register, branches
import qrcode

QR_FILE = 'qr_flag.png'

class LFSR:
    def __init__(self, register, branches):
        self.register = register
        self.branches = branches
        self.n = len(register)

    def next_bit(self):
        ret = self.register[self.n - 1]
        new = 0
        for i in self.branches:
            new ^= self.register[i - 1]
        self.register = [new] + self.register[:-1]

        return ret

def qr_text(text: bytes):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=2,
        border=0,
    )
    qr.add_data(text.decode())
    qr.make(fit=True)

    img = qr.make_image(fill_color='black', back_color='white')

    img.save(QR_FILE)

def decrypt_png(encrypted_path: str, result_path: str, register, branches):
    generator = LFSR(register, branches)

    encrypted_image = Image.open(encrypted_path)
    w = encrypted_image.width
    h = encrypted_image.height

    decrypted_image = Image.new(encrypted_image.mode, encrypted_image.size)
    encrypted_pixels = encrypted_image.load()
    decrypted_pixels = decrypted_image.load()

    for y in range(h):
        for x in range(w):
            encrypted_pixel = encrypted_pixels[x, y] // 255
            next_bit = generator.next_bit()
            decrypted_pixel = encrypted_pixel ^ next_bit

            decrypted_pixels[x, y] = decrypted_pixel * 255

    decrypted_image.save(result_path, encrypted_image.format)

if __name__ == '__main__':
    qr_text(flag)
    decrypt_png('qr.png', 'restored_qr.png', register, branches)
