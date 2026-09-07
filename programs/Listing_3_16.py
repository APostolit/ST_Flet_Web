# FilledButton_1
import flet as ft

def main(page: ft.Page):
    page.title = "Кнопка FilledButton"

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.FilledButton(content="Кнопка доступна"),
                    ft.FilledButton(content="Кнопка не доступна", disabled=True),
                    ft.FilledButton(content="Кнопка с иконкой",
                                    icon=ft.Icons.FIND_IN_PAGE,),],
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)