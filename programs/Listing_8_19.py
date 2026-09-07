# ExpansionPanelList_2
import flet as ft

def main(page: ft.Page):
    page.title = "ExpansionPanelList"
    page.theme_mode = ft.ThemeMode.LIGHT

    def handle_change(e: ft.Event[ft.ExpansionPanelList]):
        print(f"Изменение на панели с индексом {e.data}")

    def handle_delete(e: ft.Event[ft.IconButton]):
        icon_button = e.control
        tile = icon_button.parent
        panel = tile.parent
        panel_list.controls.remove(panel)
        panel_list.update()

    panel_list = ft.ExpansionPanelList(
        expand_icon_color=ft.Colors.AMBER,
        elevation=8,
        divider_color=ft.Colors.AMBER,
        on_change=handle_change,
        controls=[
            ft.ExpansionPanel(
                bgcolor=ft.Colors.BLUE_400,
                header=ft.ListTile(title=ft.Text("Заголовок главной панели")),
                content=ft.Text("Содержание главной панели"),
                expanded=True,),], )

    colors = [ft.Colors.GREEN_700, ft.Colors.GREEN_500, ft.Colors.GREEN_300,]

    for i, bgcolor in enumerate(colors):
        panel_list.controls.append(
            ft.ExpansionPanel(
                bgcolor=bgcolor,
                header=ft.ListTile(title=ft.Text(f"Панель {i}"), bgcolor=bgcolor),
                content=ft.ListTile(
                    bgcolor=bgcolor,
                    title=ft.Text(f"Это панель {i}"),
                    subtitle=ft.Text(f"Нажмите на иконку для удаления панели {i}"),
                    trailing=ft.IconButton(
                        icon=ft.Icons.DELETE,
                        on_click=handle_delete,),),))
    page.add(ft.SafeArea(content=panel_list,))

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)