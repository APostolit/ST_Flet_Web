# CupertinoListTile_1
import flet as ft

def main(page: ft.Page):
    page.title = "Плитка CupertinoListTile"
    def handle_tile_click(_: ft.Event[ft.CupertinoListTile]):
        print("Нажатие на плитку")

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.CupertinoListTile(
                        additional_info=ft.Text("Понедельник 10:30"),
                        bgcolor_activated=ft.Colors.AMBER_ACCENT,
                        leading=ft.Icon(ft.CupertinoIcons.GAME_CONTROLLER),
                        title=ft.Text("Заголовок плитки 1"),
                        subtitle=ft.Text("Подзаголовок"),
                        trailing=ft.Icon(ft.CupertinoIcons.ALARM),
                        on_click=handle_tile_click,
                    ),
                    ft.CupertinoListTile(
                        notched=True,
                        additional_info=ft.Text("Вторник 13:00"),
                        leading=ft.Icon(ft.CupertinoIcons.GAME_CONTROLLER),
                        title=ft.Text("Заголовок плитки 2"),
                        subtitle=ft.Text("Подзаголовок"),
                        trailing=ft.Icon(ft.CupertinoIcons.ALARM),
                        on_click=handle_tile_click,
                    ),
                ],
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)