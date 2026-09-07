# CupertinoSegmentedButton_1
import flet as ft

def main(page: ft.Page):
    page.title = "Сегментированная кнопка"
    page.theme_mode = ft.ThemeMode.LIGHT

    page.add(
        ft.SafeArea(
            content=ft.CupertinoSegmentedButton(
                selected_index=1,
                selected_color=ft.Colors.RED_400,
                on_change=lambda e: print(f"Выбран индекс: {e.data}"),
                padding=ft.Padding.symmetric(vertical=20, horizontal=50),
                controls=[
                    ft.Text("Кнопка 1"),
                    ft.Container(
                        padding=ft.Padding.symmetric(vertical=10, horizontal=30),
                        content=ft.Text("Кнопка 2"),),
                    ft.Container(
                        padding=ft.Padding.symmetric(vertical=5, horizontal=10),
                        content=ft.Text("Кнопка 3"),
                    ),
                ],
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)