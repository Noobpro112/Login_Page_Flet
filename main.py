import flet as ft

def main(page: ft.Page):
    def on_click(event):  
        name_insert = username.value
        password_insert = password.value
        if name_insert == 'ADMIN' and password_insert == 'ADMIN':
            page.add(ft.Text(f'Login Confirmed!'))
            page.update()
        else:
            page.add(ft.Text(f'Algo deu errado!'))

    username = ft.TextField(hint_text="Username: ")
    password = ft.TextField(hint_text="Password: ")

    page.add(username)
    page.add(password)
    page.add(ft.FloatingActionButton(icon=ft.icons.ADD, on_click=on_click))

ft.app(target=main)
