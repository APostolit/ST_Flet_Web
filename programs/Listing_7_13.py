# Image_3
import base64
import flet as ft

def main(page: ft.Page):
    page.title = "Image"
    # Открываем файл изображения в бинарном режиме чтения
    with open('fox.jpg', 'rb') as img_file:
        # Считываем всё содержимое файла и кодируем его в Base64
        base64_src = base64.b64encode(img_file.read())
    # Изображение в виде байтовых данных
    bytes_src = base64.b64decode(base64_src)

    page.add(
        ft.SafeArea(
            content=ft.Row(
                controls=[
                    ft.Image(
                        src=bytes_src,
                        width=300,
                        height=300,
                    ),
                ],
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)