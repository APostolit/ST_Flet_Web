# ResponsiveRow_3
import flet as ft

def build_card(index: int, color: ft.Colors) -> ft.Container:
    return ft.Container(
        bgcolor=color,
        border_radius=8,
        padding=16,
        content=ft.Column(spacing=10,
            controls=[
                ft.Text(f"Карточка {index}", size=22, weight=ft.FontWeight.BOLD),
                ft.Text("Строка 1"),
                ft.Text("Строка 2"),
                ft.Text("Строка 3"),
                ft.Text("Строка 4"),
                ft.Text("Строка 5"),],
        ),
    )

def main(page: ft.Page):
    page.title = "ResponsiveRow прокручивание"
    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Column(
                expand=True,
                spacing=12,
                controls=[
                    ft.Text(
                        "Измените высоту окна. Заголовок остается видимым, пока "
                        "адаптивный контент прокручивается."
                    ),
                    ft.ResponsiveRow(
                        expand=True,
                        scroll=ft.ScrollMode.AUTO,
                        spacing=16,
                        run_spacing=16,
                        controls=[
                            ft.Container(
                                col={ft.ResponsiveRowBreakpoint.XS: 12,
                                     ft.ResponsiveRowBreakpoint.MD: 6,
                                     ft.ResponsiveRowBreakpoint.LG: 4,},
                                content=build_card(i,
                                                   [ft.Colors.BLUE_50,
                                                    ft.Colors.GREEN_50,
                                                    ft.Colors.AMBER_50,][i % 3],
                                ),
                            )
                            for i in range(1, 11)
                        ],
                    ),
                ],
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)