# NavigationBar_1
import flet as ft

def main(page: ft.Page):
    page.title = "NavigationBar"
    body_text = ft.Text("Страница приложения - Поиск")
    def change(e: ft.Event[ft.NavigationBar]):
        if e.control.selected_index == 0:
            body_text.value = "Страница приложения - Поиск"
        elif e.control.selected_index == 1:
            body_text.value = "Страница приложения - Доставка"
        else:
            body_text.value = "Страница приложения - Получено"

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.EXPLORE, label="Поиск"),
            ft.NavigationBarDestination(icon=ft.Icons.COMMUTE, label="Доставка"),
            ft.NavigationBarDestination(icon=ft.Icons.BOOKMARK_BORDER,
                                        label="Получено",
                                        selected_icon=ft.Icons.BOOKMARK,),],
        on_change=change,)

    page.add(ft.SafeArea(content=body_text, ))

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)