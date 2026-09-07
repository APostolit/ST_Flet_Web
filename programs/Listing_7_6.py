# ProgressBar_1
import asyncio
import flet as ft

async def main(page: ft.Page):
    page.title = "ProgressBar"
    determinate_bar = ft.ProgressBar(width=400)
    determinate_message = ft.Text("Ждите, идет загрузка...")

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Text(value="Линейный индикатор",
                        theme_style=ft.TextThemeStyle.HEADLINE_SMALL,),
                    ft.Column(controls=[determinate_message, determinate_bar]),
                    ft.Text(value="Индикатор с неопределенным значением",
                        theme_style=ft.TextThemeStyle.HEADLINE_SMALL,),
                    ft.ProgressBar(width=400, color=ft.Colors.AMBER),
                ]
            )
        )
    )

    for i in range(0, 101):
        determinate_bar.value = i * 0.01
        await asyncio.sleep(0.1)
        if i == 100:
            determinate_message.value = "Процесс завершен!"
        page.update()

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)