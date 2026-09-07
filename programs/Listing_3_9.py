# Chip_1
import flet as ft

def main(page: ft.Page):
    page.title = "Чипы"
    url_launcher = ft.UrlLauncher()
    page.services.append(url_launcher)

    def handle_chip1_click(e: ft.Event[ft.Chip]):
        e.control.label.value = "Сохранить в избранное"
        e.control.leading = ft.Icon(ft.Icons.FAVORITE_OUTLINED)
        e.control.disabled = True

    async def handle_chip2_click(e: ft.Event[ft.Chip]):
        await url_launcher.launch_url("https://maps.google.com")

    page.add(
        ft.SafeArea(
            content=ft.Row(
                controls=[
                    ft.Chip(
                        label=ft.Text("Сохранить в избранное"),
                        leading=ft.Icon(ft.Icons.FAVORITE_BORDER_OUTLINED),
                        bgcolor=ft.Colors.GREEN_200,
                        disabled_color=ft.Colors.GREEN_100,
                        autofocus=True,
                        on_click=handle_chip1_click,
                    ),
                    ft.Chip(
                        label=ft.Text("Карта Google"),
                        leading=ft.Icon(ft.Icons.MAP_SHARP),
                        bgcolor=ft.Colors.GREEN_200,
                        on_click=handle_chip2_click,
                    ),
                ]
            )
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)