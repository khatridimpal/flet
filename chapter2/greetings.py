import flet as ft

def main(page: ft.Page):
    page.title= "Simple Greeting App!"
    first_name = ft.TextField(label="first name", autofocus=True)
    last_name = ft.TextField(label="last name")

    greeting = ft.Column()
    def btn_click(e):
        greeting.controls.append(ft.Text(f"Hello {first_name.value} {last_name.value}!"))
        first_name.value=""
        last_name.value=""
        first_name.focus()
        page.update()

    hello = ft.ElevatedButton("Say hello!", on_click = btn_click)
    page.add(
        first_name,
        last_name,
        hello,
        greeting,
    )

ft.app(target=main)