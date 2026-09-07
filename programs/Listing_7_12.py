# Image_2
import time
import flet as ft

def main(page: ft.Page):
    page.title = "Image"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def show_random(e: ft.Event[ft.Button]):
        image.src = f"https://picsum.photos/320/200?random={time.time()}"  # random
        image.update()

    page.add(
        ft.SafeArea(
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    image := ft.Image(
                        src="https://picsum.photos/320/200?random=1",
                        width=360,
                        height=220,
                        fit=ft.BoxFit.COVER,
                        placeholder_fade_out_animation=ft.Animation(
                            duration=ft.Duration(milliseconds=900),
                            curve=ft.AnimationCurve.EASE_OUT,),
                        fade_in_animation=ft.Animation(
                            duration=ft.Duration(milliseconds=700),
                            curve=ft.AnimationCurve.EASE_IN_OUT,),),
                    ft.Button("Показать случайное изображение", on_click=show_random),
                ],
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)