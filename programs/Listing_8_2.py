# Column_2
import flet as ft
HEIGHT = 400

def main(page: ft.Page):
    page.title = "Контейнер колонки - Column"
    def items(count: int):
        return [
            ft.Container(
                content=ft.Text(value="Э" + str(i)),
                alignment=ft.Alignment.CENTER,
                width=50,
                height=30,
                bgcolor=ft.Colors.AMBER,
                border_radius=ft.BorderRadius.all(5),
            )
            for i in range(1, count + 1)]

    def handle_slider_change(e: ft.Event[ft.Slider]):
        col.height = float(e.control.value)
        col.update()
    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Column(
                        controls=[
                            ft.Text(
                                "Измените высоту столбца, чтобы увидеть, как "
                                "переместятся дочерние элементы:"),
                            ft.Slider(min=0, max=HEIGHT, divisions=20, value=HEIGHT,
                                label="Высота - {value}", width=500,
                                on_change=handle_slider_change,),]),
                    ft.Container(
                        bgcolor=ft.Colors.TRANSPARENT,
                        content=(
                            col := ft.Column(wrap=True, spacing=10, run_spacing=10,
                                             controls=items(10), height=HEIGHT,)),),]
            )
        ),
    )
if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)