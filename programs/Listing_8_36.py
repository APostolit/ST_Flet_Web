# SafeArea_1.py
import flet as ft

def main(page: ft.Page):
    page.title = "SafeArea"
    counter = 0
    message = ft.Text("0", size=50)

    def handle_button_click(e: ft.Event[ft.FloatingActionButton]):
        nonlocal counter
        counter += 1
        message.value = str(counter)
        message.update()

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD,
        on_click=handle_button_click,)

    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Container(
                alignment=ft.Alignment.CENTER,
                content=message,),
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)