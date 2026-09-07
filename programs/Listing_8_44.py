# Tabs_5
import random
import flet as ft

def main(page: ft.Page):
    async def handle_move_to_random(e: ft.Event[ft.FloatingActionButton]):
        # формирование случайного индекса вкладки
        i = random.choice([i for i in range(tabs.length) if i != tabs.selected_index])
        await tabs.move_to(
            index=i,
            animation_curve=ft.AnimationCurve.FAST_OUT_SLOWIN,
            animation_duration=ft.Duration(seconds=3),)

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.MOVE_UP,
        content="Случайное переключение вкладок",
        on_click=handle_move_to_random,)

    tabs = ft.Tabs(
        length=6,
        selected_index=5,
        expand=True,
        content=ft.Column(
            expand=True,
            controls=[
                ft.TabBar(
                    tab_alignment=ft.TabAlignment.CENTER,
                    tabs=[ft.Tab(label=ft.Text("Вкладка 1")),
                          ft.Tab(label=ft.Text("Вкладка 2")),
                          ft.Tab(label=ft.Text("Вкладка 3")),
                          ft.Tab(label=ft.Text("Вкладка 4")),
                          ft.Tab(label=ft.Text("Вкладка 5")),
                          ft.Tab(label=ft.Text("Вкладка 6")),],),
                ft.TabBarView(
                    expand=True,
                    controls=[
                        ft.Container(
                            alignment=ft.Alignment.CENTER,
                            content=ft.Text("Содержимое вкладки 1"),),
                        ft.Container(
                            alignment=ft.Alignment.CENTER,
                            content=ft.Text("Содержимое вкладки 2"),),
                        ft.Container(
                            alignment=ft.Alignment.CENTER,
                            content=ft.Text("Содержимое вкладки 3"),),
                        ft.Container(
                            alignment=ft.Alignment.CENTER,
                            content=ft.Text("Содержимое вкладки 4"), ),
                        ft.Container(
                            alignment=ft.Alignment.CENTER,
                            content=ft.Text("Содержимое вкладки 5"),),
                        ft.Container(
                            alignment=ft.Alignment.CENTER,
                            content=ft.Text("Содержимое вкладки 6"),),
                    ],
                ),
            ],
        ),
    )

    page.add(ft.SafeArea(expand=True, content=tabs))

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)