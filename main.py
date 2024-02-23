import flet as ft

def main(page: ft.Page):
    def on_click(username):
        if username.control.value == 'Admin' and password.control.value == 'admin':
            page.add(ft.Text(value="Login Efetuado com sucesso!"))
            page.update()
        else:
            page.add(ft.Text(value="Você errou algo!"))
            page.update()

    username = ft.TextField(hint_text="Username: ")
    password = ft.TextField(hint_text="Password: ")

    page.add(username)
    page.add(password)
    page.add(ft.FloatingActionButton(icon=ft.icons.ADD, on_click=on_click))

ft.app(target=main)
