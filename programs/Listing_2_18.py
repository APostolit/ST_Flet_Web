# ListView_1
import flet as ft

def main(page: ft.Page):
    page.title = "ListView"
    # Создаём контейнер с заданной высотой
    container = ft.Container(
        content=ft.ListView(
            controls=[ft.Text(f"Элемент списка {i}") for i in range(1, 31)],
            expand=1,
            spacing=10,
            auto_scroll=True),
        height=300,  # Я явно задаём высоту контейнера
    )
    page.add(container)

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)