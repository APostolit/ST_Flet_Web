# ShaderMask_3
import flet as ft
import base64
import os

def main(page: ft.Page):
    page.title = "ShaderMask"
    # Получаем текущую рабочую директорию
    current_dir = os.getcwd()
    # Изображение должно лежать в папке current_dir
    # Открываем файл изображения в бинарном режиме чтения
    with open('fox.jpg', 'rb') as img_file:
        # Считываем всё содержимое файла и кодируем его в Base64
        base64_src = base64.b64encode(img_file.read())
    # image as bytes
    bytes_src = base64.b64decode(base64_src)

    page.add(
        ft.SafeArea(
            content=ft.Row(
                controls=[
                    ft.Image(
                        src=bytes_src,
                        width=300,
                        height=300,
                        fit=ft.BoxFit.FILL,),
                    ft.ShaderMask(
                        blend_mode=ft.BlendMode.COLOR_BURN,
                        shader=ft.RadialGradient(
                            center=ft.Alignment.TOP_LEFT,
                            radius=1.0,
                            colors=[ft.Colors.YELLOW, ft.Colors.DEEP_ORANGE_900],
                            tile_mode=ft.GradientTileMode.CLAMP,),
                        content=ft.Image(
                            src=bytes_src,
                            width=300,
                            height=300,
                            fit=ft.BoxFit.FILL,),),
                    ft.ShaderMask(
                        blend_mode=ft.BlendMode.DST_IN,
                        shader=ft.LinearGradient(
                            begin=ft.Alignment.TOP_CENTER,
                            end=ft.Alignment.BOTTOM_CENTER,
                            colors=[ft.Colors.BLACK, ft.Colors.TRANSPARENT],
                            stops=[0.5, 1.0],),
                        content=ft.Image(
                            src=bytes_src,
                            width=300,
                            height=300,),),
                ]
            )
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)