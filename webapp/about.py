import justpy as jp
class About:
    path="/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes=" bg-gray-200 h-screen ")
        jp.Div(a=div,text="About the Page" ,classes="text-4xl m-2")
        jp.Div(a=div, text="""
        This page will help find the meaning of
         any word that you want to know about.
        """, classes="text-lg")
        return wp

