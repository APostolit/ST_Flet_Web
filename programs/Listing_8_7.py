# Container_1
import flet as ft

def main(page: ft.Page):
    page.title = "Элемент - Container"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    c1 = ft.Container(margin=10, padding=10, alignment=ft.Alignment.CENTER,
                      bgcolor=ft.Colors.AMBER,
                      width=150, height=150, border_radius=10,
                      content=ft.Text("Не кликабельный"),)
    c2 = ft.Container(margin=10, padding=10, alignment=ft.Alignment.CENTER,
                        bgcolor=ft.Colors.GREEN_200,
                        width=150, height=150, border_radius=10,
                        on_click=lambda e: print("Нажат кликабельный без анимации!"),
                        content=ft.Text("Кликабельный без анимации"),)
    c3 = ft.Container(margin=10, padding=10, alignment=ft.Alignment.CENTER,
                        bgcolor=ft.Colors.CYAN_200,
                        width=150, height=150,  border_radius=10, ink=True,
                        on_click=lambda e: print("Нажат кликабельный с анимацией!"),
                        content=ft.Text("Кликабельный с анимацией"),)
    c4 =  ft.Container(margin=10, padding=10, alignment=ft.Alignment.CENTER,
                        width=150, height=150, border_radius=10, ink=True,
                        on_click=lambda e: print(
                            "Нажат кликабельный прозрачный с анимацией!"),
                        content=ft.Text("Кликабельный прозрачный с анимацией"),)
    page.add(
        ft.SafeArea(
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[c1, c2, c3, c4],)
        ),
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)