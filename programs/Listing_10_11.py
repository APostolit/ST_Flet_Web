# Router_4
"""Загрузчики — загрузка данных с помощью loader и use_route_loader_data()."""
import flet as ft

def home_loader(params):
    return {"title": "Домашняя", "message": "Добро пожаловать в приложение!"}

def products_loader(params):
    return {
        "products": [
            {"id": 1, "name": "Рубашка", "price": 150.99},
            {"id": 2, "name": "Свитер", "price": 580.99},
            {"id": 3, "name": "Носки", "price": 90.99},
        ]
    }

def product_detail_loader(params):
    pid = params.get("pid", "?")
    # В реальном приложении данные извлекаются из БД или API
    products = {
        "1": {"id": 1, "name": "Рубашка", "price": 150.99, "stock": 42},
        "2": {"id": 2, "name": "Свитер", "price": 580.99, "stock": 7},
        "3": {"id": 3, "name": "Носки", "price": 90.99, "stock": 100},
    }
    return products.get(pid, {"id": pid, "name": "Unknown", "price": 0, "stock": 0})

@ft.component
def Home():
    data = ft.use_route_loader_data()
    return ft.Column(
        [ft.Text(data["title"], size=24),
         ft.Text(data["message"]),])

@ft.component
def ProductsList():
    data = ft.use_route_loader_data()
    return ft.Column(
        [ft.Text("Продукты", size=24),
            *[ft.ListTile(
                title=ft.Text(p["name"]),
                subtitle=ft.Text(f"Цена ₽: {p['price']:.2f}"),
                on_click=lambda _, pid=p["id"]: ft.context.page.navigate(
                    f"/products/{pid}"),)
                for p in data["products"]
            ],
        ]
    )

@ft.component
def ProductDetails():
    data = ft.use_route_loader_data()
    params = ft.use_route_params()
    return ft.Column(
        [ft.Text(data["name"], size=24),
         ft.Text(f"Цена ₽: {data['price']:.2f}"),
         ft.Text(f"В наличии: {data['stock']}"),
         ft.Text(f"ID продукта (из параметров): {params['pid']}"),
         ft.Button("<-Назад к продуктам",
                   on_click=lambda: ft.context.page.navigate("/products"), ),]
    )

@ft.component
def App():
    return ft.SafeArea(
        content=ft.Column(
            [ft.Row(
                [ft.Image('SIS.jpg',  width=50, height=50),
                 ft.Button("Домашняя",
                           on_click=lambda: ft.context.page.navigate("/"),),
                 ft.Button("Продукты",
                           on_click=lambda: ft.context.page.navigate("/products"),),]),
                ft.Divider(),
                ft.Router(
                    [ft.Route(index=True, component=Home, loader=home_loader),
                     ft.Route(path="products",
                              children=[ft.Route(index=True,
                                                 component=ProductsList,
                                                 loader=products_loader,),
                                        ft.Route(path=":pid",
                                                 component=ProductDetails,
                                                 loader=product_detail_loader,),
                                        ],
                              ),
                     ]
                ),
                ft.Divider(),
            ]
        )
    )

if __name__ == "__main__":
    ft.run(lambda page: page.render(App))