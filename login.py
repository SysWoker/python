from flet import *


body = Container(
    Container(
        Stack([
            Container(
                border_radius=11,
                width=360,
                height=560,
                bgcolor='#fff',
                rotate=Rotate(0.98*3.14),
            ),
            Container(
                Container(
                    Column([
                        Container(
                            Image(
                                src='logo2.png',
                                width=60,
                                scale=1,
                            ),padding=padding.only(105,20,20,40),
                        ),
                        Text(
                            'Login',
                            width=360,
                            size=30,
                            weight='w900',
                            text_align='center',
                        ),
                        Container(
                            TextField(
                                width=320,
                                height=55,
                                hint_text="Usuario",
                                border='underline',
                                color='#fdfdfd',
                                prefix_icon= icons.PERSON,
                                
                            ),padding=padding.only(25,20),
                            
                            
                        ),
                        Container(
                            TextField(
                                width=320,
                                height=55,
                                hint_text='Contraseña',
                                border='underline',
                                color='#fdfdfd',
                                prefix_icon= icons.LOCK_ROUNDED,
                                border_color="#009FE3",
                            ),padding=padding.only(25,20),
                        ),
                        Container(
                            TextButton(
                                '¿Olvidaste la contraseña?',
                                
                                
                            ),padding=padding.only(25),
                        ),
                        Container(
                            ElevatedButton(
                                content=Text(
                                    'Iniciar Secion',
                                    
                                ),bgcolor="#312783",color="#e9e9e9",width="250",
                            ),padding=padding.only(18),
                        ),
                    ]),
                    ),
                width=360,
                height=560,
                bgcolor='#35ffffff',
                border_radius=12,
            ),
        ]),
    ),
    padding=110,
    width=520,
    height=740,
    gradient=LinearGradient(['#312783','#009FE3']),
)



async def main(page: Page):
    page.window_width = 500
    page.window_height = 880
    page.window_resizable = False
    page.padding = 0
    
    #script para visualizar los pixel width en pantalla 
    def page_resize(e):
        
        pw.value = f"{page.width} px"
        pw.update()
    
    page.on_resize = page_resize
    
    pw = Text(bottom=50, right=50, style="displaySmall")
    page.overlay.append(pw)
    page.window_resizable = False
    
    
    await page.add_async(body)
    
    
app(target=main)