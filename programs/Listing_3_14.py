# CupertinoSegmentedButton_2
import flet as ft

def main(page: ft.Page):
    page.title = "Сегментированная кнопка"
    page.theme_mode = ft.ThemeMode.LIGHT

    segmented_button = ft.CupertinoSegmentedButton(
        selected_index=1,
        selected_color=ft.Colors.RED_400,
        unselected_color=ft.Colors.GREY_400,
        on_change=lambda e: print(f"Выбран индекс: {e.data}"),
        controls=[
            ft.Text("Все"),
            ft.Container(padding=ft.Padding.symmetric(vertical=30, horizontal=0),
                         content=ft.Text("Никто"),),
            ft.Container(padding=ft.Padding.symmetric(vertical=0, horizontal=30),
                content=ft.Text("Некоторые"),),
        ],
    )

    def handle_vertical_change(e: ft.Event[ft.Slider]):
        segmented_button.controls[1].padding = ft.Padding.only(
            top=e.control.value,
            bottom=e.control.value,)

    def handle_horizontal_change(e: ft.Event[ft.Slider]):
        segmented_button.controls[2].padding = ft.Padding.only(
            left=e.control.value,
            right=e.control.value,)

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    segmented_button,
                    ft.Text("Вертикальное заполнение button 1:"),
                    ft.Slider(label="{value}",
                              min=0,
                              max=50,
                              divisions=50,
                              value=30,
                              on_change=handle_vertical_change,),
                    ft.Text("Горизонтальное заполнение button 2:"),
                    ft.Slider(label="{value}",
                              min=0,
                              max=50,
                              divisions=50,
                              value=30,
                              on_change=handle_horizontal_change,),
                    ft.Text(
                        value=(
                            "*Обратите внимание, что изменения в заполнении"
                            " одного сегмента может повлиять на "
                            "заполнение других сегментов*"
                        ),
                        theme_style=ft.TextThemeStyle.LABEL_MEDIUM,
                        color=ft.Colors.ORANGE_ACCENT,
                    ),
                ],
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)