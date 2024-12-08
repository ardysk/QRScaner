import qrcode

def generate_qr_code(data, file_path):
    """
    Generuje kod QR
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Tworzenie obrazu QR
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)
