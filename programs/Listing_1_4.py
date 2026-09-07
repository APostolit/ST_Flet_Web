# base_container.py
import flet as ft

def main(page: ft.Page):
    # Строка
    row = ft.Row(controls=[ft.Text("Строка 1"),
                           ft.Text("Строка 2"),
                           ft.Text("Строка 3"),],)
    # Колонка
    column = ft.Column(width=220,
                       height=120,
                       controls=[ft.Text("Строка 1"),
                                 ft.Text("Строка 2"),
                                 ft.Text("Строка 3"),],)
    # Объединяющая колонка
    col = ft.Column(width=220, controls=[row, column])

    # Контейнер
    container = ft.Container(content=col,
                             bgcolor=ft.Colors.CYAN_200,
                             border_radius=10)
    page.add(container)

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)