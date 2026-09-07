# Router_3
"""Динамические сегменты — :пути параметров с помощью use_route_params()."""
import flet as ft

@ft.component
def UserProfile():
    params = ft.use_route_params()
    return ft.Column(
        [ft.Text(f"Пользователи: {params['userId']}", size=24),
         ft.Text(f"Все параметры: {params}"),
         ft.Button("Просмотреть сообщение #10->",
                   on_click=lambda: ft.context.page.navigate(
                       f"/users/{params['userId']}/posts/10"),),
         ft.Button("<-Назад к пользователям",
                   on_click=lambda: ft.context.page.navigate("/"),),
         ])

@ft.component
def UserPost():
    params = ft.use_route_params()
    return ft.Column(
        [ft.Text(f"Пользователь: {params['userId']},"
                 f" Post: {params['postId']}", size=24),
         ft.Text(f"Все параметры: {params}"),
         ft.Button("<-Назад",
                   on_click=lambda:
                   ft.context.page.navigate(f"/users/{params['userId']}"),),
         ]
    )

@ft.component
def UserList():
    return ft.Column(
        [ft.Text("Пользователи:", size=24),
         ft.Button("Пользователь Alice->",
                   on_click=lambda: ft.context.page.navigate("/users/alice"),),
         ft.Button("Пользователь Bob->",
                   on_click=lambda: ft.context.page.navigate("/users/bob"), ),
        ])

@ft.component
def App():
    return ft.SafeArea(
        content=ft.Router(
            [ft.Route(index=True, component=UserList),
             ft.Route(path="users/:userId",
                      children=[ft.Route(index=True, component=UserProfile),
                                ft.Route(path="posts/:postId", component=UserPost),],
                ),
            ]
        )
    )

if __name__ == "__main__":
    ft.run(lambda page: page.render(App))