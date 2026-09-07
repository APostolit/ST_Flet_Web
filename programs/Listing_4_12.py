# Dropdown_0
import flet as ft

def main(page: ft.Page):
    select_key = ft.Text('')

    def select(e: ft.Event[ft.Dropdown]):
        select_key.value = e.control.value

    options = [ft.DropdownOption(key="red", text="Красный"),
               ft.DropdownOption(key="green", text="Зеленый"),
               ft.DropdownOption(key="blue", text="Синий"),]

    page.add(
        ft.SafeArea(content=ft.Column(
            controls=[
                select_key,
                ft.Dropdown(key="color_dropdown",
                            editable=True,
                            label="Цвет",
                            options=options,
                            on_select=select,),
                ]
            )
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)