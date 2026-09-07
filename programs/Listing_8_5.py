# Column_5
import flet as ft

def main(page: ft.Page):
    page.title = "Контейнер бесконечная прокрутка"

    cl = ft.Column(
        spacing=10,
        height=200,
        width=200,
        scroll=ft.ScrollMode.ALWAYS,
        scroll_interval=0,)

    for i in range(0, 50):
        cl.controls.append(ft.Text(f"Текст строки {i}", key=str(i)))
        i += 1

    page.add(ft.SafeArea(content=ft.Container(cl, border=ft.Border.all(1))))

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)