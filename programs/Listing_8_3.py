# Column_3
import flet as ft

@ft.control
class V_Alignment(ft.Column):
    alignment: ft.MainAxisAlignment = ft.MainAxisAlignment.START

    def init(self):
        self.controls = [
            ft.Text(str(self.alignment), size=10),
            ft.Container(
                content=ft.Column(self.generate_items(3), alignment=self.alignment),
                bgcolor=ft.Colors.AMBER_100, height=400,),]

    @staticmethod
    def generate_items(count: int):
        """Генерирует список пользовательских элементов с длиной `count`."""
        return [
            ft.Container(content=ft.Text(value=str(i)),
                         alignment=ft.Alignment.CENTER,
                         width=50, height=50,
                bgcolor=ft.Colors.AMBER_500,)
            for i in range(1, count + 1)]

def main(page: ft.Page):
    page.title = "Контейнер колонки - Column"
    page.add(
        ft.SafeArea(
            content=ft.Row(
                spacing=30,
                alignment=ft.MainAxisAlignment.START,
                scroll=ft.ScrollMode.AUTO,
                controls=[
                    V_Alignment(alignment=ft.MainAxisAlignment.START),
                    V_Alignment(alignment=ft.MainAxisAlignment.CENTER),
                    V_Alignment(alignment=ft.MainAxisAlignment.END),
                    V_Alignment(alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    V_Alignment(alignment=ft.MainAxisAlignment.SPACE_AROUND),
                    V_Alignment(alignment=ft.MainAxisAlignment.SPACE_EVENLY),],)))
if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)