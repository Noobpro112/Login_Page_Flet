import flet as ft


def main(page: ft.Page):
    page.clean()
    page.add(ft.AppBar(title=ft.Text('Login!'), center_title=True,))

    def on_click(event):
        name_insert = username.value
        password_insert = password.value
        if name_insert == '' and password_insert == '':
            # sql inner join
            segunda_pagina(page)
            page.update()
        else:
            page.add(ft.Text(f'Senha ou Usuario incorretos.'))

    username = ft.TextField(hint_text="Username: ")
    password = ft.TextField(hint_text="Password: ")

    page.add(username)
    page.add(password)
    page.add(ft.FloatingActionButton(
        icon=ft.icons.PASSWORD_OUTLINED, on_click=on_click))
    page.add(ft.FilledButton(text='Registre-se',
             on_click=lambda event: registro(page)))


def segunda_pagina(page):
    page.clean()
    page.add(
        ft.AppBar(
            leading=ft.FilledTonalButton(
                "Login", icon='keyboard_backspace', on_click=lambda event: main(page)),
            leading_width=150,
            title=ft.Text('Banco Pig. Oink Oink!'),
            center_title=True,
        ),
        ft.Column(
            [
                ft.Row(
                    [
                        ft.Container(
                            bgcolor=ft.colors.AMBER,
                            alignment=ft.alignment.center,
                            expand=False,
                            height=100,
                            padding=2,
                            width=300,
                            ink=True,
                            content=ft.Text('Digitado algo'),
                            on_click=lambda e: print('Click'),
                        ),
                        ft.Container(
                            bgcolor=ft.colors.AMBER,
                            alignment=ft.alignment.center,
                            expand=False,
                            height=100,
                            padding=2,
                            width=300,
                            ink=True,
                            on_click=lambda e: print('Click')
                        ),
                    ],
                    alignment=ft.alignment.center,  # Centraliza a linha na página
                ),
                # Adicione mais linhas aqui para cada linha de produtos
            ],
            spacing=4,
            expand=False,
        ),
    )


def registro(page):
    page.clean()
    page.add(ft.AppBar(title=ft.Text('Registro!'), center_title=True,))

    def on_click(event):
        name_insert = username.value
        password_insert = password.value
        email_insert = email.value
        if name_insert == '' and password_insert == '' and email_insert == '':
            # SQL Insert
            segunda_pagina(page)
            page.update()
        else:
            page.add(ft.Text(f'Algo deu errado!'))
            page.update()

    username = ft.TextField(hint_text="Username: ")
    password = ft.TextField(hint_text="Password: ")
    reconfirm_password = ft.TextField(hint_text="Digite sua senha novamente:")
    email = ft.TextField(hint_text='Digite o seu email: ')

    page.add(username)
    page.add(password)
    page.add(reconfirm_password)
    page.add(email)
    page.add(ft.FloatingActionButton(
        icon=ft.icons.PASSWORD_OUTLINED, on_click=on_click))
    page.add(ft.FilledButton(text='Login', on_click=lambda event: main(page)))


ft.app(target=main)
