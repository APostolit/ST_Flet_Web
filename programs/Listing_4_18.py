# RangeSlider_1
import flet as ft

def main(page: ft.Page):
    page.title = "RangeSlider"
    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Text(value="Слайдер диапазона с делениями и надписями",
                            size=20,
                            weight=ft.FontWeight.BOLD,),
                    ft.RangeSlider(min=0,
                                   max=50,
                                   start_value=10,
                                   divisions=10,
                                   end_value=20,
                                   inactive_color=ft.Colors.GREEN_300,
                                   active_color=ft.Colors.GREEN_700,
                                   overlay_color=ft.Colors.GREEN_100,
                                   label="{value}",),
                    ]
               ),
           )
       )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)