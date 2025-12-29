import qrcode
from qrcode.constants import ERROR_CORRECT_H


def generar_qr(
    url,
    nombre_archivo="qr_menu.png"
):
    qr = qrcode.QRCode(
        version=4,
        error_correction=ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(nombre_archivo)

    print(f"QR generado correctamente: {nombre_archivo}")


if __name__ == "__main__":
    url_menu = "https://tusitio.com/menu/cafeteria-aroma"
    generar_qr(url_menu, "qr_cafeteria_aroma.png")
