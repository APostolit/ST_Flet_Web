# ExpansionTile_1
import flet as ft

def main(page: ft.Page):
    page.title = "ExpansionTile"
    pl = ft.ExpansionTile(
    width=400,
    title="Профиль.",
    subtitle="Параметры пользователя.",
    expanded=False,
    controls=[
        ft.ListTile(title=ft.Text("Входное имя: Anatolii")),
        ft.ListTile(title=ft.Text("Почта: anatolii@mail.ru")),],
        )

    page.add(pl)

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)