# Text_4
import flet as ft

def main(page: ft.Page):
    page.title = "Text theme styles"
    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Text("Обычный текст со стилем по умолчанию"),
                    ft.Text("Выбираемый обычный текст со стилем по умолчанию",
                        selectable=True,
                    ),
                    ft.Text(
                        value="Это простой текст, ",
                        selectable=True,
                        size=30,
                        spans=[
                            ft.TextSpan(
                                text="это наклонный italic, ",
                                style=ft.TextStyle(
                                    italic=True,
                                    size=20,
                                    color=ft.Colors.GREEN,
                                ),
                                spans=[
                                    ft.TextSpan(
                                        text="Это жирный bold и наклонный italic, ",
                                        style=ft.TextStyle(weight=ft.FontWeight.BOLD),
                                    ),
                                    ft.TextSpan(
                                        text="только наклонный italic, ",
                                        spans=[
                                            ft.TextSpan(
                                                "уменьшенный наклонный italic",
                                                ft.TextStyle(size=15),
                                            )
                                        ],
                                    ),
                                ],
                            )
                        ],
                    ),
                    ft.Text(
                        disabled=False,
                        spans=[
                            ft.TextSpan(
                                text="подчеркнутый и кликабельный (clickable), ",
                                style=ft.TextStyle(
                                    decoration=ft.TextDecoration.UNDERLINE
                                ),
                                on_click=lambda e: print(f"Clicked span: {e.control}"),
                                on_enter=lambda e: print(f"Entered span: {e.control}"),
                                on_exit=lambda e: print(f"Exited span: {e.control}"),
                            ),
                            ft.TextSpan(text=" "),
                            ft.TextSpan(
                                text="подчеркнутый красной волнистой линией, ",
                                style=ft.TextStyle(
                                    decoration=ft.TextDecoration.UNDERLINE,
                                    decoration_color=ft.Colors.RED,
                                    decoration_style=ft.TextDecorationStyle.WAVY,
                                ),
                                on_enter=lambda e: print(f"Entered span: {e.control}"),
                                on_exit=lambda e: print(f"Exited span: {e.control}"),
                            ),
                            ft.TextSpan(text=" "),
                            ft.TextSpan(
                                text="верхнее подчеркивание -синим цветом blue",
                                style=ft.TextStyle(
                                    decoration=ft.TextDecoration.OVERLINE,
                                    decoration_color="blue",
                                ),
                            ),
                            ft.TextSpan(text=" "),
                            ft.TextSpan(
                                text="верхнее и нижнее подчеркивание, ",
                                style=ft.TextStyle(
                                    decoration=ft.TextDecoration.OVERLINE
                                    | ft.TextDecoration.UNDERLINE
                                ),
                            ),
                            ft.TextSpan(text=" "),
                            ft.TextSpan(
                                text="зачеркнутый текст",
                                style=ft.TextStyle(
                                    decoration=ft.TextDecoration.LINE_THROUGH,
                                    decoration_thickness=3,
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        ),
    )

    def handle_link_highlight(e: ft.Event[ft.TextSpan]):
        e.control.style.color = ft.Colors.BLUE
        e.control.update()

    def handle_link_unhighlight(e: ft.Event[ft.TextSpan]):
        e.control.style.color = None
        e.control.update()

    page.add(
        ft.Text(
            disabled=False,
            spans=[
                ft.TextSpan(
                    text="текст - ссылка на Google",
                    style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
                    url="https://google.com",
                    on_enter=handle_link_highlight,
                    on_exit=handle_link_unhighlight,
                )
            ],
        ),
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)