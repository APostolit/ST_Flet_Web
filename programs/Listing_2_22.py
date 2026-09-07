# Screenshot_1
from pathlib import Path
import flet as ft
from flet.utils.files import get_current_script_dir

def main(page: ft.Page):
    page.title = "Screenshot"
    async def take_screenshot(e: ft.Event[ft.Button]):
        image = await scr.capture()
        with open(Path(get_current_script_dir(), "Screenshot.png"), "wb") as f:
            f.write(image)

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    scr := ft.Screenshot(
                        content=ft.Container(
                            padding=10,
                            content=ft.Button(
                                "Элемент приложения",
                                bgcolor=ft.Colors.BLUE,
                                elevation=10,
                            ),
                        )
                    ),
                    ft.Button("Сделать снимок экрана", on_click=take_screenshot),
                ]
            )
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)