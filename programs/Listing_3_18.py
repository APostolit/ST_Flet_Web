# FilledTonalButton_1
import flet as ft

def main(page: ft.Page):
    page.title = "Кнопка FilledTonalButton"

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.FilledTonalButton(content="Активная кнопка"),
                    ft.FilledTonalButton(content="Пассивная кнопка", disabled=True),
                    ft.FilledTonalButton(content="Кнопка с иконкой",
                        icon=ft.Icons.BRUSH,),],
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)