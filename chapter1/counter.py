import flet as ft
from time import sleep

def main(page: ft.Page):
    page.title = "Counter App"
    text =ft.Text()
    page.add(text)

    for i in range(1,11):
        text.value = "Count " + str(i)
        page.update()
        sleep(1)

ft.app(target=main)