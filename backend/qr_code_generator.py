import qrcode


def qr_code_generator(url: str, filename: str):

    try:
        img = qrcode.make(url)
        img.save(filename)
        print(f"QR code saved successfully to '{filename}'")

    except Exception as e:
        print(f"Error: URL too large for QR code. {e}")

qr_code_generator("https://www.linkedin.com/in/maxim-vassilev-8b9a1721a/", "maxim-linkedin.png")