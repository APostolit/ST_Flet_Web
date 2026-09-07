# ReorderableDragHandle_1
import flet as ft

def main(page: ft.Page):
    page.title = "ReorderableDragHandle"
    def on_reorder(e: ft.OnReorderEvent):
        e.control.controls.insert(e.new_index, e.control.controls.pop(e.old_index))

    page.add(
        ft.SafeArea(
            content=ft.ReorderableListView(
                expand=True,
                show_default_drag_handles=False,
                on_reorder=on_reorder,
                controls=[
                    ft.ListTile(
                        title=ft.Text(f"Перетаскиваемый элемент {i}",
                                      color=ft.Colors.BLACK),
                        leading=ft.ReorderableDragHandle(
                            key=f"drag_handle_{i}",
                            content=ft.Icon(ft.Icons.DRAG_INDICATOR,
                                            color=ft.Colors.RED),
                            mouse_cursor=ft.MouseCursor.GRAB,),
                        bgcolor=ft.Colors.BLUE_100
                        if i % 2 == 0
                        else ft.Colors.BLUE_50,
                    )
                    for i in range(10)
                ],
            )
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)