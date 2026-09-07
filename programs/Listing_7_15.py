# Video_1
import flet as ft
import flet_video as ftv

def main(page: ft.Page):
    page.title = "Video"

    page.add(
        ft.SafeArea(
            expand=True,
            content=ftv.Video(
                expand=True,
                key='my_video',
                # autoplay=True,
                # configuration=ftv.VideoConfiguration(hardware_decoding_api="vaapi"),
                playlist=[
                    ftv.VideoMedia("Astana.mp4"),
                ],
            ),
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)