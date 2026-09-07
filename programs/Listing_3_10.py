# Chip_2
import flet as ft

def main(page: ft.Page):
    page.title = "Чипы"
    def handle_amenity_selection(e: ft.Event[ft.Chip]):
        print("Сделан выбор:", e.control.label.value)

    amenities = ["Холодильники", "Телевизоры", "Пылесосы",
                 "Корм для собак", "Корм для кошек"]

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.HOTEL_CLASS),
                            ft.Text("Товары"),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.Chip(
                                label=ft.Text(amenity),
                                bgcolor=ft.Colors.GREEN_200,
                                disabled_color=ft.Colors.GREEN_100,
                                autofocus=True,
                                on_select=handle_amenity_selection,
                            )
                            for amenity in amenities
                        ]
                    ),
                ]
            )
        )
    )


if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)