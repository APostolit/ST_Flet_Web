# Audio_1
import flet as ft
import flet_audio as fta

def main(page: ft.Page):
    url = "gaiti.mp3"

    async def play():
        await audio.play()

    audio = fta.Audio(
        src=url,
        autoplay=False,
        volume=1,
        balance=0,)
    page.services.append(audio)

    page.add(
        ft.SafeArea(ft.Button("Play", on_click=play),)
        )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)