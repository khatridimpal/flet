import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Row(controls=[ft.Text("My favorite fruits:\n")]),
        ft.Row(
            controls=[
                ft.Text(value="Apple", color="red"),
                ft.Text(value="Orange", color="orange"),
                ft.Text(value="Banana", color="yellow"),
            ]
        ),
        ft.Column(controls=[ft.Text("My favorite fruits:\n")]),
        ft.Column(
            controls=[
                ft.Text(value="ms dhoni"),
                ft.Text(value="sachin"),
                ft.Text(value="virat"),
            ]
        )
    )

ft.app(target=main)