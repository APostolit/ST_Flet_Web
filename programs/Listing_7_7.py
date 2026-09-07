# ProgressRing_1
import asyncio
import flet as ft

async def main(page: ft.Page):
    page.title = "ProgressRing"
    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Text(value="Круговой индикатор с известным временем завершения",
                            theme_style=ft.TextThemeStyle.HEADLINE_SMALL,),
                    ft.Row(
                        controls=[determinate_ring := ft.ProgressRing(
                            width=16, height=16, stroke_width=2),
                                  determinate_message := ft.Text(
                                      "Ждите окончания процесса..."),]),
                    ft.Text(
                        value="Круговой индикатор с не известным временем завершения",
                        theme_style=ft.TextThemeStyle.HEADLINE_SMALL,),
                    ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[ft.ProgressRing(),
                                  ft.Text("Ждите, длительный процесс..."),],
                        ),
                    ]
                )
            )
        )

    for i in range(0, 101):
        determinate_ring.value = i * 0.01
        await asyncio.sleep(0.1)
        if i == 100:
            determinate_message.value = "Процесс завершен!"
        page.update()

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)