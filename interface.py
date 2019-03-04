# Lubeck Abraham Huaman Ponce

import sys
sys.dont_write_bytecode = True

#from __future__ import division
from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.image import Image as CoreImage
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput 
from kivy.uix.boxlayout import BoxLayout 
#mport sys
#sys.path.insert(0,"/etc/dhcp")
#import libcore
import libcorex
#import demo_class

import serial
import mongoapi
import cv2
#import schedule
import time
#Window.size = (1080, 720)

#todo ...
#import sim908 


from kivy.config import Config
Window.bordeless = 'False'

Config.set('graphics', 'borderless', 'False')
Config.set('graphics', 'width', '1280')
Config.set('graphics', 'height', '700')
Config.write()

Builder.load_string("""

<Test>:
    size_hint: 0.98,0.95
    pos_hint: {'center_x': .5, 'center_y': .5}
    do_default_tab: False
    tab_width:200
    border:(16,16,16,16)
    strip_border: (16,16,16,16)
    background_color: (80, 80, 80, 0.07)
    TabbedPanelItem:
        text: '   REAL TIME   '
        FloatLayout:
            Label:
                text: 'VERSION : beta 0.55 '
                pos: (740,600)
                weight: 50
                height: 30
                font_size: 17
                size_hint: (.2, None)
                multiline: False
            Label:
                text:' L. Abraham H.P.'
                pos: (730,560)
                weight: 50
                height: 30
                size_hint: (.2,None)
                font_size: 17
                multiline: False
            Label:
                text : 'ING. Electronica UNSAAAC procesamiento de imagenes.'
                pos: (880,520)
                weight: 50
                font_size: 17
                height: 30
                size_hint: (.2, None)
                multiline: False   
            Image:
                id:streaming_chanel
                pos: (80,110)
                size_hint: 2.2,0
                allow_stretch: True
                keep_ratio: False
            Button:
                id: streaming
                text: 'Pulse para iniciar streaming'
                font_size: 29
                pos : 800,450
                size_hint: 0.3, 0.1
                on_release: root.inicia_streaming()
            Button:
                id: reconocimiento
                text: 'xxxxxx'
                pos : 800,350
                size_hint: 0.1, 0.1
                
            Button:
                id: reconocimiento
                text: 'placa X2N206'
                pos : 950,350
                size_hint: 0.1, 0.1
                on_release: root.inicia_simulacro()
            
            Label:
                text: 'PLACA CAPTURADA :'
                pos: (870,300)
                font_size: 35
                weight: 50
                height: 30
                size_hint: (.2, None)
                multiline: False
                
                
    TabbedPanelItem:
        text: '    BASE DE DATOS    '
        FloatLayout:
            Label:
                text: 'Consulta Base de datos'
                pos: (150,600)
                size_hint:(.2, None)
                font_size: 35
                multiline: False
            TextInput:
                id:placa_cont
                pos: 200,580
                size_hint: (.2 , None)
                height: 30
                multiline: False
                
            Label:
                text: 'Placa ' 
                font_size: 20
                pos: 60,580
                size_hint: (.1, None)
                height: 15
                multiline: False

            TextInput:
                pos: 200,540
                size_hint: (.035 , None)
                height: 30
                multiline: False
                
            TextInput:
                pos: 255,540
                size_hint: (.035, None)
                height: 30
                multiline: False 
            TextInput:
                pos: 310,540
                size_hint: (.035, None)
                height: 30
                multiline: False 
            Label:
                text: 'Desde '
                font_size: 20
                pos: 60,540
                size_hint: (.1, None)
                height: 15
                multiline: False
            TextInput:
                pos: 200,500
                size_hint: (.035 , None)
                height: 30
                multiline: False
                id:year
            TextInput:
                pos: 255,500
                size_hint: (.035, None)
                height: 30
                multiline:False
                id:month
            TextInput:
                pos: 310,500
                size_hint: (.035, None)
                height:30
                multiline: False
                id:day
            Label:
                text: 'Hasta '
                font_size: 20
                pos: 60,500
                size_hint: (.1, None)
                height: 15
                multiline: False
            Label:
                text: 'FORMATO: YYYY--MM--DD'
                font_size:18
                pos: 200,470
                size_hint: (.1, None)
                height: 15
                multiline: False
            Button:
                id:botonbuscaplacas
                text: 'BUSCAR PLACA'
                pos : 550,550
                size_hint: 0.1, 0.1
                on_release: root.consulta_base_datos()
            ScrollView:
                size_hint: (0.9, 0.6)
                pos: 80,40
                weight: 10
                height: 30
                BoxLayout:
                    id:caja_respuesta
                    size_hint_y:None
                    height: sum(x.height for x in self.children)
                    orientation: 'vertical'
    TabbedPanelItem:
        text: 'AVISO DE PLACAS'
        FloatLayout:
            rows : 20
            cols : 2
            padding: 100
            spacing: 5
            Label: 
                text: 'placa1'
                size_hint: (.2, None)
                height: 30
                multiline: False
                pos: (5,530)

            TextInput: 
                id:placa_buscada
                size_hint: (.2, None)
                height: 30
                multiline: False
                pos: (180,530)
            
            Button:
                text: 'agregar placa. '
                pos: 180,430
                size_hint: 0.1 , 0.1
                on_release: root.agrega_a_buscados()
            ScrollView:
                size_hint: (0.4, 0.6)
                pos: 500, 170
                weight: 10
                height: 30
                BoxLayout:
                    id:caja_placas_buscadas
                    size_hint_y:None
                    height: sum(x.height for x in self.children)
                    orientation: 'vertical'
            TextInput:
                id:placa_a_borrar
                size_hint: (.2, None)
                height:30
                multiline: False
                pos:(180,230)
            Button:
                text: 'borrar placa.'
                size_hint: (.1, .1)
                pos : (180, 100)
                on_release:root.borra_placa_buscada()
    TabbedPanelItem:
        text: 'NUMEROS ANEXADOS.'
        FloatLayout:
            rows:20
            cols:2
            padding:100
            spacing:5
            Label:
                text: 'anexar numero'
                size_hint: (.2, None)
                height: 30
                multiline: False
                pos: (5,530)
            TextInput:
                id:anexado
                size_hint: (.2, None)
                height: 30
                multiline: False
                pos: (180,530)
            Button:
                text: 'anexar'
                pos: 180,430
                size_hint: 0.1, 0.1
                on_release: root.anexa_numero()
            ScrollView:
                size_hint: (0.4, 0.6)
                pos: 500, 170
                weight: 10
                height: 30
                BoxLayout:
                    id:caja_numeros_anexados 
                    size_hint_y: None
                    height: sum(x.height for x in self.children)
                    orientation: 'vertical'

        

 """)
#img = cv2.imread('test.jpg', 0)
#im = Image("test.jpg")

#class KivyCamera(Image):
#    def __init__(self, capture, fps, **kwargs):
#        super(KivyCamera, self).__init__(**kwargs)
#        self.capture = capture
#        Clock.schedule_interval(self.update, 1.0 / fps)
#
#    def update(self, dt):
#        ret, frame = self.capture.read()
#        if ret:
#            # convert it to texture
#            buf1 = cv2.flip(frame, 0)
#            buf = buf1.tostring()
#            image_texture = Texture.create(
#                size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
#            image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
#            # display image from the texture
#            self.texture = image_texture


class Test(TabbedPanel):
    
    def __init__(self,**kwargs):
        super(Test, self).__init__(**kwargs)
        self.object_element = 0
        self.path_ultimo_detectado = ''
        self.placa = ''
        self.placas = mongoapi.database()
#        Image(source='/home/lubeck/Documents/proyectospython2/opencv/1plate_car.jpg',pos = (750,20),size=(50,500))
        self.container_placa = self.ids.placa_cont
#        self.presentador = Image(pos =(100,100), size(300,300))
        # todo : modificar el api de mongodb para una nueva coleccion 
        # de placas buscadas.
        self.placas_buscadas = mongoapi.database()
        self.carga_placas_buscadas()
        # para archivo texto de placas buscadas
        # self.placas_buscadas_text = file()

        self.my_camera = None 
        #self.anexados = open("anexados.txt", 'r+')
    def hulk_smash(self):
        self.ids.hulk.text = "hulk: puny god!"
        self.ids.hulk.pos = (200, 200)
        pass
    def inicia_simulacro(self):
        try:
            ser= serial.Serial('/dev/ttyUSB0',9600)
        except serial.serialutil.SerialException:
            return 
        lista = self.get_lista_anexados_txt()
        for e in lista: 
            sim908.iniciaModulo(ser)
            time.sleep(0.3)
            sim908.setNumber(ser,e[:8])
            time.sleep(0.3)
            sim908.enviaSMS(ser, "placa X2N206, en calle luis vallejos.")
        pass 
#        self.my_camera = None
        
#    def actualiza_presentador(self, my_camera):
#        lol = Image(size=(400,400))
#        while True :
#            lol.source = my_camera.get_path_last_detected()
#    def on_pause(self):
#      # Here you can save data if needed
#        self.
#        return True

    def on_pause(self):
        super(self.on_pause())
        # Here you can check if any data needs replacing (usually nothing)
        return True
    
    def inicia_streaming(self):
        self.object_element = self.object_element + 1
        if(self.object_element == 1):
            self.ids.streaming.text = "streaming iniciado"
            print ('streaming iniciado ... ')
#            widget = Widget()
#            img = cv2.imread('test.png', 1)
#            buf1 = cv2.flip(img, 0)
#            buf = buf1.tostring()
#            image_texture = Texture.create(size=(img.shape[1], img.shape[0]), colorfmt='bgr')
#            image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            # display image from the texture
    #        self.texture = image_texture
#            self.capture = cv2.VideoCapture('test2.avi')
            #rtsp = 'rtsp://admin:admin@172.17.33.85/defaultPrimary?streamType=m'
            #http = 'http://admin:admin@172.17.33.85/media/cam0/still.jpg'
            #self.capture = cv2.VideoCapture("test.avi")
            #self.capture = cv2.VideoCapture(rtsp) 
            #self.capture = cv2.VideoCapture(http)
            self.capture = 35
            with self.ids.streaming_chanel.canvas:
    #        with self.canvas:
    ##                Rectangle(texture=image_texture ,pos=(80, 80), size = (480,480))        
    #            KivyCamera(capture=self.capture, fps=25, size = (480,480), pos=(80, 0))
    #coneccion con nucleo de sistema
                self.my_camera = libcorex.KivyCamera(capture=self.capture,nombre_calle="AV Luis Vallejos.", fps=27.0, pos = (40,0.1), size=(650, 750))
#            with self.ids.placa_capturada.canvas:                
#            Clock.schedule_interval(Image(source=my_camera.get_path_last_detected()) , 1.0 / 7.0 )
#                presentador = core_module.presentador(5,pos = (680,12), size=(200, 200))
#                presentador.setpath(my_camera.get_path_placasython2/kivy/placas/X2K298.jpg')
#                Image(source=my_camera.get_path_last_detected())
    
    def simulacro(self):
        #self.my_camera
        #todo ... 
        pass

    def consulta_base_datos(self):
        #TODO
        self.ids.caja_respuesta.clear_widgets()
        lista = []
        f = self.ids.placa_cont   
        #print "[BD] PLACA .... "+ str(f.text) 
        temp = self.placas.get_placa(f.text)
        #print temp[0]
        for e in temp:
            #temp2 = TextInput(text = str(e), size_hint=[.2,None],multiline=False,height=30)
            lista.append(e)
        #print lista
        for e in lista:
            b = BoxLayout(orientation='horizontal',size_hint_y=0.1,height=15)
            rp = TextInput(text="PLACA: "+ str(e["placa"])+" | FECHA: "+str(e["tiempo"])[0:16] + " | LUGAR: ****",multiline=False,size_hint=[1,None],height=30,readonly=True)
            self.ids.caja_respuesta.add_widget(rp)
        pass

    def agrega_a_buscados(self):
        if len(self.ids.placa_buscada.text)==6:
            self.placas_buscadas.inserta_placa_buscada(self.ids.placa_buscada.text)
            self.carga_placas_buscadas()
        self.ids.placa_buscada.text=''
        pass
    #carga desde la base de datos para poder mostrar en el gui
    #se usa de nuevo para recargar al usar el boton de recarga
    def carga_placas_buscadas(self):
        self.ids.caja_placas_buscadas.clear_widgets()
        t = self.ids.caja_placas_buscadas
        lista = []
        temp = self.placas_buscadas.get_todas_placas_buscadas()
        for e in temp:
            lista.append(e)
        for e in lista:
            b = BoxLayout(orientation='horizontal', size_hint_y=0.1, height=15)
            rp = TextInput(text="PLACA: "+str(e["placa"]) + " | FECHA DE AGREGADO: ***", multiline=False, size_hint_y=[1, None], height=30, readonly=True)
            self.ids.caja_placas_buscadas.add_widget(rp)
        pass

    def inicia_reconocimiento(self):
        self.ids.reconocimiento.text = "reconocimiento iniciado"
        print ('reconocimiento iniciado ... ')
        img = cv2.imread('test.png', 1)
        buf1 = cv2.flip(img, 0)
        buf = buf1.tostring()
        image_texture = Texture.create(size=(img.shape[1], img.shape[0]), colorfmt='bgr')
        image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        # display image from the texture
#        self.texture = image_texturet
#        with self.ids.placa_capturada.canvas:
#            my_camera = core_module.KivyCamera(capture=self.capture, fps=30, pos = (80,1), size=(580, 580))
#            self.ids.placa_capturada.texture =  self.my_camera.get_placa_capturada()
#            self.my_camera = core_module.KivyCamera(capture=self.capture, fps=30, pos = (80,1), size=(580, 580))
#            Rectangle(texture=self.my_camera.placa_texture ,pos=(80, 80), size = (480,480))
    def borra_placa_buscada(self):
        #if len(self.ids.placa_a_borrar.text)>=5:
        self.placas_buscadas.remove_placa_buscada(self.ids.placa_a_borrar.text)
        self.carga_placas_buscadas()
        pass
        #self.placas_buscadas.append( self.ids.placa_buscada_1.text )
    
    def anexa_numero(self):
        self.carga_numeros_anexados() 
        pass

    def get_lista_anexados_txt(self):
        # extrae todo de un txt :v
        t = open("anexados.txt", 'r+')
        lineas = t.readlines()
        t.close()
        return lineas 
    
    def carga_numeros_anexados(self):
        self.ids.caja_numeros_anexados.clear_widgets()
        t = self.ids.caja_numeros_anexados 
        lista = []
        temp = self.get_lista_anexados_txt()
        for e in temp:
            lista.append(e)
        an = open("anexados.txt", "r+")
        te = an.readlines()
        for e in lista:
            #print e
            b=BoxLayout(orientation='horizontal', size_hint_y=0.1, height=15)
            rp = TextInput(text='numero : '+ e[:8], size_hint_y=[1, None], height=30, readonly=True, multiline=False)
            self.ids.caja_numeros_anexados.add_widget(rp)
        an.close()
        pass

class TabbedPanelApp(App):
    
    def build(self):
        tp = TabbedPanel()
        tp.default_tab_text = 'beta v0.45'
        return Test()
    def on_stop(self):
        #without this, app will not exit even if the window is closed
        self.capture.release()

if __name__ == '__main__':
    
    TabbedPanelApp().run()
    

