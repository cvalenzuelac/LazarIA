import RPi.GPIO as pin
import time
from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput
import pygame


picam2 = Picamera2()#Inicializar camara
pygame.mixer.init()#Inicializar salida audio

def playwav(wav):
    sound = pygame.mixer.Sound(wav)
    playing = sound.play()
    while playing.get_busy():
        pygame.time.delay(100)

#Para trabajar con la numeración fisica de la tarjeta
pin.setmode(pin.BOARD)

def enbutton(board_number):
    pin.setup(board_number, pin.IN, pull_up_down = pin.PUD_DOWN)
    
enbutton(11)
enbutton(13)
enbutton(15)
enbutton(37) #boton para modo Cloud
modoCloud = False
pushArray = [False, False, False, False]
playwav('/home/lazaria/Desktop/Reto3/audiosr3/starting.wav')
playwav('/home/lazaria/Desktop/Reto3/audiosr3/liasaludo.wav')

while True:
    if pin.input(11) == pin.HIGH:
        playwav('/home/lazaria/Desktop/Reto3/audiosr3/press.wav')
        pushArray[0] = True
    else:
        pushArray[0] = False
        
    if pin.input(13) == pin.HIGH:
        playwav('/home/lazaria/Desktop/Reto3/audiosr3/press.wav')
        pushArray[1] = True
    else:
        pushArray[1] = False
        
    if pin.input(15) == pin.HIGH:
        playwav('/home/lazaria/Desktop/Reto3/audiosr3/press.wav')
        pushArray[2] = True
    else:
        pushArray[2] = False
        
    if pin.input(37) == pin.HIGH:
        playwav('/home/lazaria/Desktop/Reto3/audiosr3/press.wav')
        into = True
        pushArray[3] = True
        modoCloud = not modoCloud
        #import cloudMode
        if modoCloud:
            playwav('/home/lazaria/Desktop/Reto3/audiosr3/liacloudon.wav')
            print("Entraste en modo Cloud")
        while modoCloud:
            if pin.input(11) == pin.HIGH:
                playwav('/home/lazaria/Desktop/Reto3/audiosr3/press.wav')
                picam2.start(show_preview=False)
                time.sleep(3) #Timer de 3 segundos
                picam2.capture_file("Foto1.jpeg")
                playwav('/home/lazaria/Desktop/Reto3/audiosr3/liacapture.wav')
                print('foto tomada')
                picam2.stop()
                pushArray[0] = True
            else:
                pushArray[0] = False
                
            if pin.input(13) == pin.HIGH:
                playwav('/home/lazaria/Desktop/Reto3/audiosr3/press.wav')
                print("inicio video")
                #picam2.start_and_record_video("test.mp4", duration=5)
                encoder = H264Encoder(10000000)
                output = FfmpegOutput('test.mp4')
                playwav('/home/lazaria/Desktop/Reto3/audiosr3/liarecstart.wav')
                picam2.start_recording(encoder, output)
                time.sleep(5)#clip de 5 segundos
                picam2.stop_recording()
                playwav('/home/lazaria/Desktop/Reto3/audiosr3/liarecstop.wav')
                print("fin de video")
                pushArray[1] = True
            else:
                pushArray[1] = False
                
            if pin.input(15) == pin.HIGH:
                playwav('/home/lazaria/Desktop/Reto3/audiosr3/press.wav')
                pushArray[2] = True
            else:
                pushArray[2] = False
            if pin.input(37) == pin.HIGH:
                playwav('/home/lazaria/Desktop/Reto3/audiosr3/press.wav')
                if into:
                    into = not into #para evitar que el click de acceso se cuente
                else:
                    modoCloud = not modoCloud
                    print('Saliste de modo Cloud')
                    playwav('/home/lazaria/Desktop/Reto3/audiosr3/liacloudoff.wav')
                pushArray[3] = True
            else:
                pushArray[3] = False
                
            hubotrue = False
            for i in range(len(pushArray)):
                if pushArray[i]:
                    hubotrue = True
                    print('Cloud Push button'+str(i+1), end=' ')
            if hubotrue:
                print('')
            time.sleep(0.2)
                
    else:
        pushArray[3] = False
        
    hubotrue = False
    for i in range(len(pushArray)):
        if pushArray[i]:
            hubotrue = True
            print('Push button'+str(i+1), end=' ')
    if hubotrue:
        print('')
    time.sleep(0.15)
