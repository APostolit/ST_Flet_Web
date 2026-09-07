# Dropdown_2
import flet as ft

def main(page: ft.Page):
    page.title = "Элемент Dropdown"
    def get_options() -> list[ft.DropdownOption]:
        icons = [
            {"name": "Улыбка", "icon": ft.Icons.SENTIMENT_SATISFIED_OUTLINED},
            {"name": "Облако", "icon": ft.Icons.CLOUD_OUTLINED},
            {"name": "Кисть", "icon": ft.Icons.BRUSH_OUTLINED},
            {"name": "Сердце", "icon": ft.Icons.FAVORITE},]
        return [
            ft.DropdownOption(key=icon["name"], leading_icon=icon["icon"])
            for icon in icons
        ]

    page.add(
        ft.SafeArea(
            content=ft.Dropdown(
                key="icon_dropdown",
                border=ft.InputBorder.UNDERLINE,
                enable_filter=True,
                editable=True,
                leading_icon=ft.Icons.SEARCH,
                label="Icon",
                options=get_options(),
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)