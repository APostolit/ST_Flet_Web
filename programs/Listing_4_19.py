# RangeSlider_2
import flet as ft

def main(page: ft.Page):
    page.title = "RangeSlider"
    page.scroll = ft.ScrollMode.AUTO

    def handle_slider_change_start(e: ft.Event[ft.RangeSlider]):
        print(f"Текущее начало: {e.control.start_value}, {e.control.end_value}")

    def handle_slider_change(e: ft.Event[ft.RangeSlider]):
        print(f"Текущее состояние: {e.control.start_value}, {e.control.end_value}")

    def handle_slider_change_end(e: ft.Event[ft.RangeSlider]):
        print(f"Текущий конец: {e.control.start_value}, {e.control.end_value}")
        message.value = f"Выбран диапазон: {e.control.start_value}, {e.control.end_value}"

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Text(value="Обработка событий слайдера диапазона",
                            size=20,
                            weight=ft.FontWeight.BOLD,),
                    ft.RangeSlider(divisions=100,
                                   min=0,
                                   max=100,
                                   start_value=10,
                                   end_value=20,
                                   on_change_start=handle_slider_change_start,
                                   on_change=handle_slider_change,
                                   on_change_end=handle_slider_change_end,
                                   label="{value}%",),
                    message := ft.Text(),
                    ]
                )
            )
        )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)