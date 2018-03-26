# Trabalho de CG Quarto
from math import cos
from math import sin
from sys import argv
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from abajur import Abajur
from mesinha import Mesinha
from assets import *
from wardrobe import Wardrobe
from walls import Walls
from cama import Cama


global esqdir
global cimabaixo
global aux1
global aux2
global angulo
global distanciamax
global estadoluz0
global estadoluz1
global estadoluz2

esqdir = 0
cimabaixo = 0
aux1 = 0
aux2 = 0
aux3 = 0
aux4 = 0
angulo = 45
distanciamax = 500
estadoluz0 = 1
estadoluz1 = 0
estadoluz2 = 0


def desenho():
    global aux1
    global aux2

    Cama().draw(2,{"x":0,"y":-1.8,"z":3.3})
    Abajur().draw(1,{"x":1.4,"y":2,"z":-0.17})    
    Window().draw(2.5,{"x":0,"y":1,"z":-1.79})
    Flower().draw(1,{"x":-1.4,"y":-0.90,"z":-2})
    Wardrobe().draw(1,{"x":3.5,"y":-1.65,"z":-4})
    Walls().draw(1,{"x":5,"y":0,"z":0})
    Mesinha().draw(1,{"x":0,"y":-1,"z":-2})


def iluminacao_da_cena():
    
    luzAmbiente0=[0.2,0.2,0.2,1.0]
    luzDifusa0=[0.7,0.7,0.7,1.0]  # ; // "cor"
    luzEspecular0 = [0.01, 0.01, 0.01, 0.01]  #;// "brilho"
    posicaoLuz0=[0.0, 50.0, 50.0, 1.0]

    luzAmbiente1=[0.0,0.0,0.0,1.0]
    luzDifusa1=[0.0,0.0,1.0,1.0]  # ; // "cor"
    luzEspecular1 = [0.0, 0.0, 0.01, 0.01]  #;// "brilho"
    posicaoLuz1=[0.0, 50.0, -50.0, 1.0]

    luzAmbiente2=[0.0,0.0,0.0,1.0]
    luzDifusa2=[1.0,0.0,0.0,1.0]  # ; // "cor"
    luzEspecular2 = [0.01, 0.0, 0.0, 0.01]  #;// "brilho"
    posicaoLuz2=[0.0, 5.0, 0.0, 0.0]  # última coord como 0 pra funcionar como vetor da luz direcional
    direcao2 = [0.0, -1,0, 0,0]  # direção do vetor do spot

    #Capacidade de brilho do material
    especularidade=[1.0,1.0,1.0,1.0]
    especMaterial = 20

    # Especifica que a cor de fundo da janela será branca
    glClearColor(1.0, 1.0, 1.0, 1.0)

    # Habilita o modelo de colorização
    glShadeModel(GL_SMOOTH)   # GL_SMOOTH ou GL_FLAT

    #  Define a refletância do material
    glMaterialfv(GL_FRONT,GL_SPECULAR, especularidade)
    #  Define a concentração do brilho
    glMateriali(GL_FRONT,GL_SHININESS,especMaterial)

    # Ativa o uso da luz ambiente
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luzAmbiente0)

    # Define os parametros da luz de número 0
    glLightfv(GL_LIGHT0, GL_AMBIENT, luzAmbiente0)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luzDifusa0 )
    glLightfv(GL_LIGHT0, GL_SPECULAR, luzEspecular0 )
    glLightfv(GL_LIGHT0, GL_POSITION, posicaoLuz0 )

    # Define os parametros da luz de número 1
    glLightfv(GL_LIGHT1, GL_AMBIENT, luzAmbiente1)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, luzDifusa1 )
    glLightfv(GL_LIGHT1, GL_SPECULAR, luzEspecular1 )
    glLightfv(GL_LIGHT1, GL_POSITION, posicaoLuz1 )
    
    # Define os parametros da luz de número 2
    glLightfv(GL_LIGHT2, GL_AMBIENT, luzAmbiente2)
    glLightfv(GL_LIGHT2, GL_DIFFUSE, luzDifusa2 )
    glLightfv(GL_LIGHT2, GL_SPECULAR, luzEspecular2 )
    glLightfv(GL_LIGHT2, GL_POSITION, posicaoLuz2 )
    glLightfv(GL_LIGHT2, GL_SPOT_DIRECTION, direcao2); #direcao da luz
    glLightf(GL_LIGHT2, GL_SPOT_CUTOFF, 5); # angulo do cone, de 0 a 180. 
    

    # Habilita a definição da cor do material a partir da cor corrente
    glEnable(GL_COLOR_MATERIAL)
    # Habilita o uso de iluminação
    glEnable(GL_LIGHTING)
    
    # Habilita a luz de número 0
    if estadoluz0 == 1:
        glEnable(GL_LIGHT0)
    else:
        glDisable(GL_LIGHT0)
        
    # Habilita a luz de número 1
    if estadoluz1 == 1:
        glEnable(GL_LIGHT1)
    else:
        glDisable(GL_LIGHT1)

    # Habilita a luz de número 2
    if estadoluz2 == 1:
        glEnable(GL_LIGHT2)
        print('Luz Spot ligada.')
    else:
        glDisable(GL_LIGHT2)
    
    # Habilita o depth-buffering
    glEnable(GL_DEPTH_TEST)


def tela():
    global angulo
    global distanciamax
    global aux1
    global aux2

# AJUSTE DE APARÊNCIA

    # Especifica que a cor de fundo da janela será branca
    glClearColor(1.0, 1.0, 1.0, 1.0)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Limpar a tela
    glClearColor(1.0, 1.0, 1.0, 1.0) # Limpa a janela com a cor especificada
    glMatrixMode(GL_PROJECTION) # Muda a matriz de projeçao
    glLoadIdentity()# carrega a matriz identidade

    gluPerspective(angulo, 1, 0.1, distanciamax) # Especifica a projeção perspectiva

    glMatrixMode(GL_MODELVIEW) # Especifica sistema de coordenadas do modelo
    glLoadIdentity() # Inicializa sistema de coordenadas do modelo

#CÂMERA


    #gluLookAt(eyex, eyey, eyez, alvox, alvoy, alvoz, upx, upy, upz)
    #    eyex, eyey, eyez = posiçao da camera
    #    alvox, alvoy, alvoz = coordenada para onde a camera olha.
    #    upx, upy, upz = indica a posiçao vertical da camera.
    gluLookAt(sin(esqdir) * 13, 0 + cimabaixo ,cos(esqdir) * 13, aux1,aux2,0, 0,1,0) # Especifica posição do observador e do alvo
    print('Camera: (' + str( sin(esqdir) * 10) + ',' + str(cimabaixo) + "," + str(cos(esqdir) * 10) + ')')
    print('Alvo: (' + str(aux1) +','+str(aux2)+',0)')

   
    
    iluminacao_da_cena()
    glEnable(GL_DEPTH_TEST) # verifica os pixels que devem ser plotados no desenho 3d

    desenho()                    
    glFlush()                    # Aplica o desenho


# FUNÇÕES DO TECLADO E MOUSE    

# Função callback chamada para gerenciar eventos de teclas normais
# Obs.: maiusculo e minúsculo faz diferença.
def Teclado (tecla, x, y):
    global aux1
    global aux2
    global estadoluz0
    global estadoluz1
    global estadoluz2
    global esqdir
    global cimabaixo


    print("*** Tratamento de teclas comuns")
    print(">>> Tecla: ",tecla)
	
    if tecla==chr(27): # ESC ?
        sys.exit(0)

    if tecla == b'a':  # A
        aux1 = aux1 - 0.1
        print ("aux1 = ", aux1 )
	
    if tecla == b's': # S
        aux1 = aux1 + 0.1
        print ("aux1 = ", aux1 )
        
    if tecla == b'w': # W
        aux2 = aux2 + 0.1
        print ("aux2 = ", aux2 )

    if tecla == b'z': # Z
        aux2 = aux2 - 0.1
        print ("aux2 = ", aux2 )
        
    if tecla == b'0': # 0
        if estadoluz0 == 0:
            estadoluz0 = 1
            glEnable(GL_LIGHT0)
        else:
            estadoluz0 = 0
            glDisable(GL_LIGHT0)
    if tecla == b'1': # 1
        if estadoluz1 == 0:
            estadoluz1 = 1
            glEnable(GL_LIGHT1)
        else:
            estadoluz1 = 0
            glDisable(GL_LIGHT1)
    if tecla == b'2': # 2
        if estadoluz2 == 0:
            estadoluz2 = 1
            glEnable(GL_LIGHT2)
        else:
            estadoluz2 = 0
            glDisable(GL_LIGHT2)
    if tecla == b'i': #i
        aux1=-4
        esqdir=0
        cimabaixo=0
    if tecla == b'o': #i
        aux1=4
        esqdir=0
        cimabaixo=0
    if tecla == b'p': #i
        aux1=0
        esqdir=0
        cimabaixo=0
        
    tela()
    glutPostRedisplay()

# Função callback chamada para gerenciar eventos de teclas especiais
def TeclasEspeciais (tecla, x, y):
    global esqdir
    global cimabaixo
    if tecla == GLUT_KEY_LEFT:
        esqdir = esqdir - 0.1
    elif tecla == GLUT_KEY_RIGHT:
        esqdir = esqdir + 0.1
    elif tecla == GLUT_KEY_UP:
        cimabaixo = cimabaixo + 0.05
    elif tecla == GLUT_KEY_DOWN:
        cimabaixo = cimabaixo - 0.05
    tela()
    glutPostRedisplay()   

# Função callback chamada para gerenciar eventos do mouse
def ControleMouse(button, state, x, y):
    global angulo
    if (button == GLUT_LEFT_BUTTON):
        if (state == GLUT_DOWN): 
            if (angulo >= 10):
                angulo -= 2
		
    if (button == GLUT_RIGHT_BUTTON):
        if (state == GLUT_DOWN):   # Zoom-out
            if (angulo <= 130):
                angulo += 2
    tela()
    glutPostRedisplay()


# PROGRAMA PRINCIPAL
glutInit(argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
glutInitWindowSize(600,600)
glutCreateWindow(b"Quarto")
glutDisplayFunc(tela)
glutMouseFunc(ControleMouse)
glutKeyboardFunc (Teclado)
glutSpecialFunc (TeclasEspeciais)
glutMainLoop()