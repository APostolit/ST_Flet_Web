# Banner_2.py
import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "Banner"

    def handle_banner_close(e: ft.Event[ft.TextButton]):
        page.pop_dialog()
        page.add(ft.Text("Выбрано: " + e.control.content))
        # page.add(ft.Text("Выбрано: " + e.control.data))

    action_button_style = ft.ButtonStyle(color=ft.Colors.BLUE)
    banner = ft.Banner(
        bgcolor=ft.Colors.AMBER_100,
        leading=ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, color=ft.Colors.AMBER, size=40),
        content=ft.Text(value="К сожалению при сохранении файла произошла ошибка!"
                              "Ваши дальнейшие действия?",
                        color=ft.Colors.BLACK,),
        actions=[
            ft.TextButton(content="Повторить",
                          style=action_button_style,
                          on_click=handle_banner_close,
                          data="retry",),
            ft.TextButton(content="Игнорировать",
                          style=action_button_style,
                          on_click=handle_banner_close,
                          data="ignore",),
            ft.TextButton(content="Прервать",
                          style=action_button_style,
                          on_click=handle_banner_close,
                          data="cancel",),],)
    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Button(
                        "Показать Banner", on_click=lambda e: page.show_dialog(banner)
                    )
                ]
            )
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)