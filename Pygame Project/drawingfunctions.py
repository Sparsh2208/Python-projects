def drawRecShapes(x,color):
    if x==1:
        pygame.draw.rect(Window,color,Rect(20,20,60,60))
    elif x==2:
        pygame.draw.rect(Window,color,Rect(120,20,60,60))
    elif x==3:
        pygame.draw.rect(Window,color,Rect(220,20,60,60))
    elif x==4:
        pygame.draw.rect(Window,color,Rect(320,20,60,60))
    elif x==5:
        pygame.draw.rect(Window,color,Rect(20,120,60,60))
    elif x==6:
        pygame.draw.rect(Window,color,Rect(120,120,60,60))
    elif x==7:
        pygame.draw.rect(Window,color,Rect(220,120,60,60))
    elif x==8:
        pygame.draw.rect(Window,color,Rect(320,120,60,60))
    elif x==9:
        pygame.draw.rect(Window,color,Rect(20,220,60,60))
    elif x==10:
        pygame.draw.rect(Window,color,Rect(120,220,60,60))
    elif x==11:
        pygame.draw.rect(Window,color,Rect(220,220,60,60))
    elif x==12:
        pygame.draw.rect(Window,color,Rect(320,220,60,60))
    elif x==13:
        pygame.draw.rect(Window,color,Rect(20,320,60,60))
    elif x==14:
        pygame.draw.rect(Window,color,Rect(120,320,60,60))
    elif x==15:
        pygame.draw.rect(Window,color,Rect(220,320,60,60))
    elif x==16:
        pygame.draw.rect(Window,color,Rect(320,320,60,60))

def drawCirShapes(x,color):
    if x==1:
        pygame.draw.circle(Window,color,(50,50),30)
    elif x==2:
        pygame.draw.circle(Window,color,(150,50),30)
    elif x==3:
        pygame.draw.circle(Window,color,(250,50),30)
    elif x==4:
        pygame.draw.circle(Window,color,(350,50),30)
    elif x==5:
        pygame.draw.circle(Window,color,(50,150),30)
    elif x==6:
        pygame.draw.circle(Window,color,(150,150),30)
    elif x==7:
        pygame.draw.circle(Window,color,(250,150),30)
    elif x==8:
        pygame.draw.circle(Window,color,(350,150),30)
    elif x==9:
        pygame.draw.circle(Window,color,(50,250),30)
    elif x==10:
        pygame.draw.circle(Window,color,(150,250),30)
    elif x==11:
        pygame.draw.circle(Window,color,(250,250),30)
    elif x==12:
       pygame.draw.circle(Window,color,(350,250),30)
    elif x==13:
        pygame.draw.circle(Window,color,(50,350),30)
    elif x==14:
        pygame.draw.circle(Window,color,(150,350),30)
    elif x==15:
        pygame.draw.circle(Window,color,(250,350),30)
    elif x==16:
        pygame.draw.circle(Window,color,(350,350),30)

def drawTriShapes(x,color):
    if x==1:
        pygame.draw.polygon(Window,color,( (10,20),(90,20),(50,80) ))
    elif x==2:
        pygame.draw.polygon(Window,color,( (110,20),(190,20),(150,80) ))
    elif x==3:
        pygame.draw.polygon(Window,color,( (210,20),(290,20),(250,80) ))
    elif x==4:
        pygame.draw.polygon(Window,color,( (310,20),(390,20),(350,80) ))
    elif x==5:
        pygame.draw.polygon(Window,color,( (10,120),(90,120),(50,180) ))
    elif x==6:
        pygame.draw.polygon(Window,color,( (110,120),(190,120),(150,180) ))
    elif x==7:
        pygame.draw.polygon(Window,color,( (210,120),(290,120),(250,180) ))
    elif x==8:
        pygame.draw.polygon(Window,color,( (310,120),(390,120),(350,180) ))
    elif x==9:
        pygame.draw.polygon(Window,color,( (10,220),(90,220),(50,280) ))
    elif x==10:
        pygame.draw.polygon(Window,color,( (110,220),(190,220),(150,280) ))
    elif x==11:
        pygame.draw.polygon(Window,color,( (210,220),(290,220),(250,280) ))
    elif x==12:
       pygame.draw.polygon(Window,color,( (310,220),(390,220),(350,280) ))
    elif x==13:
        pygame.draw.polygon(Window,color,( (10,320),(90,320),(50,380) ))
    elif x==14:
        pygame.draw.polygon(Window,color,( (110,320),(190,320),(150,380) ))
    elif x==15:
        pygame.draw.polygon(Window,color,( (210,320),(290,320),(250,380) ))
    elif x==16:
        pygame.draw.polygon(Window,color,( (310,320),(390,320),(350,380) ))

def drawDiamShapes(x,color):
    if x==1:
        pygame.draw.polygon(Window,color,( (10,50),(50,20),(90,50),(50,80) ))
    elif x==2:
        pygame.draw.polygon(Window,color,( (110,50),(150,20),(190,50),(150,80) ))
    elif x==3:
        pygame.draw.polygon(Window,color,( (210,50),(250,20),(290,50),(250,80) ))
    elif x==4:
        pygame.draw.polygon(Window,color,( (310,50),(350,20),(390,50),(350,80) ))
    elif x==5:
        pygame.draw.polygon(Window,color,( (10,150),(50,120),(90,150),(50,180) ))
    elif x==6:
        pygame.draw.polygon(Window,color,( (110,150),(150,120),(190,150),(150,180) ))
    elif x==7:
        pygame.draw.polygon(Window,color,( (210,150),(250,120),(290,150),(250,180) ))
    elif x==8:
        pygame.draw.polygon(Window,color,( (310,150),(350,120),(390,150),(350,180) ))
    elif x==9:
        pygame.draw.polygon(Window,color,( (10,250),(50,220),(90,250),(50,280) ))
    elif x==10:
        pygame.draw.polygon(Window,color,( (110,250),(150,220),(190,250),(150,280) ))
    elif x==11:
        pygame.draw.polygon(Window,color,( (210,250),(250,220),(290,250),(250,280) ))
    elif x==12:
       pygame.draw.polygon(Window,color,( (310,250),(350,220),(390,250),(350,280) ))
    elif x==13:
        pygame.draw.polygon(Window,color,( (10,350),(50,320),(90,350),(50,380) ))
    elif x==14:
        pygame.draw.polygon(Window,color,( (110,350),(150,320),(190,350),(150,380) ))
    elif x==15:
        pygame.draw.polygon(Window,color,( (210,350),(250,320),(290,350),(250,380) ))
    elif x==16:
        pygame.draw.polygon(Window,color,( (310,350),(350,320),(390,350),(350,380) ))
