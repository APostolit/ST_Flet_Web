# Column_4
import flet as ft

@ft.control
class H_Alignment(ft.Column):
    alignment: ft.CrossAxisAlignment = ft.CrossAxisAlignment.START

    def init(self):
        self.controls = [
            ft.Text(str(self.alignment), size=16),
            ft.Container(
                bgcolor=ft.Colors.AMBER_100,
                width=100,
                content=ft.Column(
                    controls=self.generate_items(3),
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=self.alignment,),),]

    @staticmethod
    def generate_items(count: int):
        """Генерирует список пользовательских элементов с длиной `count`."""
        return [
            ft.Container(content=ft.Text(value=str(i)),
                         alignment=ft.Alignment.CENTER,
                         width=50, height=50, bgcolor=ft.Colors.AMBER_500,)
            for i in range(1, count + 1)]

def main(page: ft.Page):
    page.title = "Контейнер колонки - Column"
    page.add(
        ft.SafeArea(
            content=ft.Row(
                spacing=30,
                alignment=ft.MainAxisAlignment.START,
                controls=[
                    H_Alignment(alignment=ft.CrossAxisAlignment.START),
                    H_Alignment(alignment=ft.CrossAxisAlignment.CENTER),
                    H_Alignment(alignment=ft.CrossAxisAlignment.END),],)
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)