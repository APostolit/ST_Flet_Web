# CircleAvatar_1
import flet as ft

def main(page: ft.Page):
    page.title = "Аватар пользователя"
    img_1 = "https://avatars.githubusercontent.com/u/5041459?s=88&v=4"
    img_2 = "https://avatars.githubusercontent.com/u/_5041459?s=88&v=4"

    page.add(
        ft.SafeArea(
            content=ft.Row(
                controls=[
                    # «обычный» аватар с фоновым изображением
                    ft.CircleAvatar(foreground_image_src=img_1,
                                    content=ft.Text("FF"),),
                    # аватар с резервным текстом (если изображение не подгрузилось)
                    ft.CircleAvatar(foreground_image_src=img_2,
                                    content=ft.Text("AV"),),
                    # аватар с иконкой
                    ft.CircleAvatar(content=ft.Icon(ft.Icons.ABC)),
                    # аватар с иконкой и пользовательскими цветами
                    ft.CircleAvatar(content=ft.Icon(ft.Icons.WARNING_ROUNDED),
                                    color=ft.Colors.YELLOW_200,
                                    bgcolor=ft.Colors.AMBER_700,),
                    # аватар с онлайн-статусом
                    ft.Stack(
                        width=40,
                        height=40,
                        controls=[
                            ft.CircleAvatar(foreground_image_src=img_1),
                            ft.Container(alignment=ft.Alignment.BOTTOM_LEFT,
                                         content=ft.CircleAvatar(
                                             bgcolor=ft.Colors.GREEN, radius=5),
                                         ),
                            ],
                        ),
                    ]
                ),
            ),
        )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)