# Tabs_3
from dataclasses import field
import flet as ft
from flet import Alignment

@ft.control
class MyContainer(ft.Container):
    text: str = ""
    height: int = 100
    alignment: Alignment = field(default_factory=lambda: Alignment.CENTER)

    def init(self):
        self.bgcolor = ft.Colors.random()
        self.content = ft.Text(self.text)

def main(page: ft.Page):
    page.title = "Tabs"
    def handle_new_tab(e: ft.Event[ft.CupertinoFilledButton]):
        tab_count = len(tab_bar.tabs) + 1
        tab_bar.tabs.append(ft.Tab(label=ft.Text(f"Вкладка {tab_count}")))
        tab_view.controls.append(MyContainer(text=f"Содержимое вкладки {tab_count}"))
        tabs.length = len(tab_bar.tabs)

    tabs = ft.Tabs(
        length=2,
        expand=True,
        content=ft.Column(
            expand=True,
            controls=[
                tab_bar := ft.TabBar(
                    tab_alignment=ft.TabAlignment.CENTER,
                    tabs=[
                        ft.Tab(label=ft.Text("Вкладка 1")),
                        ft.Tab(label=ft.Text("Вкладка 2")),],),
                ft.Row(alignment=ft.MainAxisAlignment.CENTER,
                       controls=[ft.CupertinoFilledButton(
                           content="Добавить вкладку",
                           icon=ft.Icons.ADD,
                           on_click=handle_new_tab,),],),
                tab_view := ft.TabBarView(
                    expand=True,
                    controls=[MyContainer(text="Содержимое вкладки 1"),
                              MyContainer(text="Содержимое вкладки 2"),],),
            ],
        ),
    )

    page.add(ft.SafeArea(expand=True,
                         content=tabs,))

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)