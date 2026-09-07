# View_1
import flet as ft

def main(page: ft.Page):
    page.title = "Элемент View"

    # Создаём несколько виджетов
    text_widget = ft.Text(value="Привет, Flet!", size=30)
    button = ft.Button(content="Кнопка")
    appbar = ft.AppBar(leading=ft.Icon(ft.Icons.MENU),
                       title=ft.Text("Верхняя панель"),
                       color = ft.Colors.WHITE,
                       bgcolor=ft.Colors.BLUE_500,
                       actions=[ft.IconButton(ft.Icons.SEARCH),
                                ft.IconButton(ft.Icons.MORE_VERT),],)

    # View выступает контейнером для этих виджетов
    view = ft.View(controls=[appbar, text_widget, button],
                   bgcolor=ft.Colors.BLUE_200)

    # Добавляем View на страницу
    page.views.append(view)

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)