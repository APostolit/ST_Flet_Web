# MenuItemButton_2
import flet as ft

def main(page: ft.Page):
    page.title = "Кнопки меню"
    page.padding = 0
    page.spacing = 0
    page.theme_mode = ft.ThemeMode.LIGHT

    def handle_color_click(e: ft.Event[ft.MenuItemButton]):
        color = e.control.content.value
        background_container.content.value = f"Выбран цвет фона: {color}"
        background_container.bgcolor = color.lower()

    def handle_on_hover(e: ft.Event[ft.MenuItemButton]):
        print(e)

    menubar = ft.MenuBar(
        expand=True,
        controls=[
            ft.SubmenuButton(
                content=ft.Text("Цвет фона окна"),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Blue"),
                        leading=ft.Icon(ft.Icons.COLORIZE),
                        style=ft.ButtonStyle(
                            bgcolor={ft.ControlState.HOVERED: ft.Colors.BLUE}),
                        on_click=handle_color_click,
                        on_hover=handle_on_hover,),
                    ft.MenuItemButton(
                        content=ft.Text("Green"),
                        leading=ft.Icon(ft.Icons.COLORIZE),
                        style=ft.ButtonStyle(
                            bgcolor={ft.ControlState.HOVERED: ft.Colors.GREEN}),
                        on_click=handle_color_click,
                        on_hover=handle_on_hover,),
                    ft.MenuItemButton(
                        content=ft.Text("Red"),
                        leading=ft.Icon(ft.Icons.COLORIZE),
                        style=ft.ButtonStyle(
                            bgcolor={ft.ControlState.HOVERED: ft.Colors.RED}),
                        on_click=handle_color_click,
                        on_hover=handle_on_hover,),],),],)

    page.add(
        ft.SafeArea(
            expand=True,
            avoid_intrusions_left=False,
            avoid_intrusions_top=False,
            avoid_intrusions_right=False,
            avoid_intrusions_bottom=False,
            content=ft.Column(
                expand=True,
                spacing=0,
                controls=[
                    ft.Row(controls=[menubar]),
                    background_container := ft.Container(
                        expand=True,
                        bgcolor=ft.Colors.WHITE,
                        alignment=ft.Alignment.CENTER,
                        content=ft.Text(
                            value="Выберите цвет фона окна из меню",
                            style=ft.TextStyle(weight=ft.FontWeight.W_500),
                        ),
                    ),
                ],
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)