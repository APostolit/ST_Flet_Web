# FloatingActionButton_1
import flet as ft

def main(page: ft.Page):
    page.title = "Кнопка FloatingActionButton"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 0
    page.scroll = ft.ScrollMode.HIDDEN

    count = 1

    def handle_fab_click(e: ft.Event[ft.FloatingActionButton]):
        nonlocal count
        page.add(
            ft.ListTile(
                title=ft.Text(f"Заголовок {count}"),
                bgcolor=ft.Colors.TEAL_300,
                leading=ft.Icon(
                    ft.Icons.CIRCLE_OUTLINED,
                    color=ft.Colors.DEEP_ORANGE_300,
                ),
                on_click=lambda x: print(x.control.title.value + " был нажат!"),
            )
        )
        page.show_dialog(ft.SnackBar(ft.Text("Заголовок был успешно добавлен!")))
        count += 1

    page.floating_action_button = ft.FloatingActionButton(
        key="handling_clicks_fab",
        icon=ft.Icons.ADD,
        on_click=handle_fab_click,
        bgcolor=ft.Colors.LIME_300,
    )

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Container(
                        bgcolor=ft.Colors.BLUE,
                        padding=ft.Padding.all(20),
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Text(
                                    value="Пример FloatingActionButton",
                                    style=ft.TextStyle(
                                        size=20,
                                        weight=ft.FontWeight.W_500,
                                    ),
                                )
                            ],
                        ),
                    ),
                    ft.Text("Нажмите на '+' для добавления заголовка"),
                ],
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)