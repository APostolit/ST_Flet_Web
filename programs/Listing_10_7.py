# NavigationRail_1
import flet as ft

def main(page: ft.Page):
    page.title = "NavigationRail"
    body_text = ft.Text("Главная страница")

    async def handle_change(e: ft.Event[ft.NavigationRail]):
        if e.control.selected_index == 0:
            body_text.value = "Выбрано: Элемент 1"
        elif e.control.selected_index == 1:
            body_text.value = "Выбрано: Элемент 2"
        else:
            body_text.value = "Выбрано: Элемент 3"

    async def on_click(e: ft.Event[ft.FloatingActionButton]):
        body_text.value = "Выбрано: Add"

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        group_alignment=-0.9,
        on_change=handle_change,
        leading=ft.FloatingActionButton(
            icon=ft.Icons.CREATE,
            content="Add",
            on_click=on_click,),
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.FAVORITE_BORDER,
                selected_icon=ft.Icons.FAVORITE,
                label="Элемент 1",),
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.BOOKMARK_BORDER),
                selected_icon=ft.Icon(ft.Icons.BOOKMARK),
                label="Элемент 2",),
            ft.NavigationRailDestination(
                icon=ft.Icons.SETTINGS_OUTLINED,
                selected_icon=ft.Icon(ft.Icons.SETTINGS),
                label=ft.Text("Элемент 3"),),],)

    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Row(
                expand=True,
                controls=[
                    ft.SelectionArea(content=rail),
                    ft.VerticalDivider(width=1),
                    ft.Column(
                        alignment=ft.MainAxisAlignment.START,
                        expand=True,
                        controls=[body_text],
                    ),
                ],
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)