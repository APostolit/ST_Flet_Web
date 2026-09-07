# Tabs_1
import flet as ft

def main(page: ft.Page):
    page.title = "Tabs"
    t_bar = ft.TabBar(
        tabs=[ft.Tab(label="Вкладка 1", icon=ft.Icons.SETTINGS_PHONE),
              ft.Tab(label="Вкладка 2", icon=ft.Icons.SETTINGS),
              ft.Tab(label=ft.CircleAvatar(
                  foreground_image_src="images/fl.png",),),]
        )
    t_view = ft.TabBarView(
        expand=True,
        controls=[ft.Container(alignment=ft.Alignment.CENTER,
                               content=ft.Text("Это содержимое вкладки 1"),),
                  ft.Container(alignment=ft.Alignment.CENTER,
                               content=ft.Text("Это содержимое вкладки 2"),),
                  ft.Container(alignment=ft.Alignment.CENTER,
                               content=ft.Text("Это содержимое вкладки 3"),),],)
    page.add(ft.SafeArea(expand=True,
                         content=ft.Tabs(selected_index=1, length=3, expand=True,
                                         content=ft.Column(
                                             expand=True,
                                             controls=[t_bar, t_view,],),),
                         )
             )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)