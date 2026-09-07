# Column_6
import flet as ft

def main(page: ft.Page):
    page.title = "Контейнер программная прокрутка"
    column = ft.Column(
        spacing=10,
        height=200,
        width=float("inf"),
        scroll=ft.ScrollMode.ALWAYS,
        controls=[
            ft.Text(f"Текстовая строка {i}", key=ft.ScrollKey(i)) for i in range(0, 100)
        ],
    )

    async def scroll_to_offset(e):
        await column.scroll_to(offset=500, duration=1000)

    async def scroll_to_start(e):
        await column.scroll_to(offset=0, duration=1000)

    async def scroll_to_end(e):
        await column.scroll_to(
            offset=-1, duration=2000, curve=ft.AnimationCurve.EASE_IN_OUT)

    async def scroll_to_key(e):
        await column.scroll_to(scroll_key="20", duration=1000)

    async def scroll_to_delta(e):
        await column.scroll_to(delta=100, duration=200)

    async def scroll_to_minus_delta(e):
        await column.scroll_to(delta=-100, duration=200)

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Container(content=column, border=ft.Border.all(1)),
                    ft.Button("Строго на 500", on_click=scroll_to_offset),
                    ft.Row(
                        controls=[
                            ft.Button("Назад -100", on_click=scroll_to_minus_delta),
                            ft.Button("Вперед +100", on_click=scroll_to_delta),]),
                    ft.Button("На элемент '20'", on_click=scroll_to_key),
                    ft.Row(
                        controls=[
                            ft.Button("На первый элемент", on_click=scroll_to_start),
                            ft.Button("на последний элемент", on_click=scroll_to_end),]),
                ]
            )
        ),
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)