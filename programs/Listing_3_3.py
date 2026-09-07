# Button_3.py
import flet as ft

def main(page: ft.Page):
    page.title = "Кнопки"
    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Button(content="Кнопка с иконкой",
                              icon=ft.Icons.WAVES_ROUNDED),
                    ft.Button(content="Кнопка с цветной иконкой",
                              icon=ft.Icons.PARK_ROUNDED,
                              icon_color=ft.Colors.GREEN_400,),
                ]
            )
        ),
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)