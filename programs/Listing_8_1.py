# Column_1
import flet as ft

def main(page: ft.Page):
    page.title = "Контейнер колонки - Column"
    def generate_items(count: int):
        """Генерирует список пользовательских элементов с длиной `count`."""
        return [
            ft.Container(
                content=ft.Text(value="Строка - " + str(i)),
                alignment=ft.Alignment.CENTER,
                width=100,
                height=50,
                bgcolor=ft.Colors.AMBER,
                border_radius=ft.BorderRadius.all(5),
            )
            for i in range(1, count + 1)
        ]

    def handle_slider_change(e: ft.Event[ft.Slider]):
        """Обновляет интервал между элементами на основе значения ползунка."""
        column.spacing = int(e.control.value)
        column.update()

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Column(
                        controls=[
                            ft.Text("Расстояние между элементами"),
                            ft.Slider(min=0, max=100, divisions=10, value=0,
                                      label="Расстояние - {value}",
                                      width=500,
                                      on_change=handle_slider_change,),]
                    ),
                    column := ft.Column(spacing=0, controls=generate_items(5)),
                ]
            )
        ),
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)