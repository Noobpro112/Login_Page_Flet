import flet as ft

def main(page: ft.Page):
    page.clean()
    page.add(ft.AppBar(title=ft.Text('Login!'), center_title=True,))

    def on_click(event):  
        name_insert = username.value
        password_insert = password.value
        if name_insert == '' and password_insert == '':
            segunda_pagina(page)
            page.update()
        else:
            page.add(ft.Text(f'Algo deu errado!'))

    username = ft.TextField(hint_text="Username: ")
    password = ft.TextField(hint_text="Password: ")

    page.add(username)
    page.add(password)
    page.add(ft.FloatingActionButton(icon=ft.icons.PASSWORD_OUTLINED, on_click=on_click))


def segunda_pagina(page):
    page.clean()
    page.add(
        ft.AppBar(
            leading=ft.FilledTonalButton("Login", icon='add_shopping_cart', on_click=lambda event: main(page)),
            leading_width=150,
            title=ft.Text('Mercado Online!'),
            center_title=True,
        ),
        ft.Column(
            [
                ft.Container(
                    bgcolor=ft.colors.AMBER,
                    alignment=ft.alignment.center,
                    expand=True,
                ),
                ft.Divider(),
                ft.Container(bgcolor=ft.colors.PINK, alignment=ft.alignment.center, expand=True),
                ft.Divider(height=1, color="white"),
                ft.Container(
                    bgcolor=ft.colors.BLUE_300,
                    alignment=ft.alignment.center,
                    expand=True,
                ),
                ft.Divider(height=9, thickness=3),
                ft.Container(
                    bgcolor=ft.colors.DEEP_PURPLE_200,
                    alignment=ft.alignment.center,
                    expand=True,
                ),
            ],
            spacing=0,
            expand=True,
        ),
    )
ft.app(target=main)
