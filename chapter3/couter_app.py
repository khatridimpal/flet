import flet as ft

def main(page: ft.Page):
    page.title = "Counter App"
    page.vertical_alignment="center"
    text_number =ft.TextField(value="0",text_align="center",width=100)

    def minus_click(e):
        text_number.value = str(int(text_number.value)-1)
        page.update()

    def plus_click(e):
        text_number.value = str(int(text_number.value)+1)
        page.update()

    page.add(
        ft.Row(
            controls=[
                ft.IconButton(ft.icons.REMOVE,on_click=minus_click),
                text_number,
                ft.IconButton(ft.icons.ADD,on_click=plus_click),
            ],
            alignment="center"
        )
    )

ft.app(target=main)