# Color_MaterialPicker
import flet as ft
from flet_color_pickers import MaterialPicker

def main(page: ft.Page):
    page.title = "MaterialPicker"
    page.padding = 20

    def on_color_change(e: ft.ControlEvent):
        print(f"Оттенок цвета: {e.data}")

    def on_primary_change(e: ft.ControlEvent):
        print(f"Основной цвет: {e.data}")

    picker = MaterialPicker(
        color="#ff9800",
        on_color_change=on_color_change,
        on_primary_change=on_primary_change,
    )

    page.add(ft.SafeArea(content=picker))

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)