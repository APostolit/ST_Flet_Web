# Color_BlockPicker
import flet as ft
from flet_color_pickers import BlockPicker

def main(page: ft.Page):
    page.title = "BlockPicker"
    page.padding = 20

    def on_color_change(e: ft.ControlEvent):
        print(f"Выбран цвет: {e.data}")

    picker = BlockPicker(
        color="#9c27b0",
        available_colors=["#f44336", "#e91e63", "#9c27b0", "#3f51b5",
                          "#2196f3", "#009688", "#4caf50", "#795548",],
        on_color_change=on_color_change,)

    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Pick a color"),
        content=picker,
        actions=[ft.TextButton("Закрыть", on_click=lambda e: page.pop_dialog()),],)

    page.add(
        ft.SafeArea(
            content=ft.IconButton(icon=ft.Icons.BRUSH,
                                  on_click=lambda e: page.show_dialog(dialog),)
            ),
        )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)