import flet as ft

def main(page: ft.Page):
    page.title = "Hello world"
    text = ft.Text(value="my flet app", color = "yellow")
    page.controls.append(text)
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER)