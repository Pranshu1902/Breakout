import pygame

pygame.init()


dis = pygame.display.set_mode((400,500))

pygame.display.set_caption("Breakout")


# colors

red = [255,0,0]

blue = [0,0,255]
light_blue = [0,0,128]

green = [0,255,0]

white = [255,255,255]

color1 = [255,0,0]
color2 = [255,0,0]
color3 = [255,0,0]
color4 = [255,0,0]
color5 = [255,0,0]
color6 = [255,0,0]
color7 = [255,0,0]


# text

font = pygame.font.Font('freesansbold.ttf', 15)
font2 = pygame.font.Font('freesansbold.ttf', 90) 
text = font.render('Welcome! Press R to restart', True, green, light_blue)

textRect = text.get_rect()  
textRect.center = (110, 13)
dis.blit(text, textRect)

text2 = font2.render('You Won', True, green, light_blue)
textrect = text2.get_rect()
textrect.center = (200, 200)




# slider
x_slider = 300

pygame.draw.rect(dis, green, [x_slider,460,90,15])


# red bricks

pygame.draw.rect(dis, red, [5,30,50,15])
pygame.draw.rect(dis, red, [60,30,50,15])
pygame.draw.rect(dis, red, [115,30,50,15])
pygame.draw.rect(dis, red, [170,30,50,15])
pygame.draw.rect(dis, red, [225,30,50,15])
pygame.draw.rect(dis, red, [280,30,50,15])
pygame.draw.rect(dis, red, [335,30,60,15])



#defining the variables to remeber the old values of ball
x_ball_old = 0
y_ball_old = 0

# ball

x_ball = 150
y_ball = 250

pygame.draw.circle(dis, white, (x_ball,y_ball), 10, 0)

pygame.display.update()

#motion 

run = True

def mainloop(run, x_slider, x_ball, y_ball, x_ball_old, y_ball_old):
    while run:
        pygame.time.delay(40)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

        # motion of the slider
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x_slider >5:
            x_slider -= 10
        elif keys[pygame.K_RIGHT] and x_slider<310:
            x_slider += 10
        if keys[pygame.K_r]:
            mainloop(True, 300, 150, 250, 0, 0)

        # motion of ball vertically
    
        # hitting the striker
        if y_ball == 450 and x_ball>= x_slider and x_ball < x_slider + 90:
            y_ball_old = y_ball
            y_ball-=10
        # in between, going up
        elif y_ball<450  and y_ball > 50 and y_ball_old > y_ball:
            y_ball_old = y_ball
            y_ball-=10
        # in between, going down
        elif y_ball < 450  and y_ball > 50 and y_ball_old < y_ball:
            y_ball_old = y_ball
            y_ball+=10
            if x_ball_old < x_ball:
                x_ball+=10
            else:
                x_ball-=10
        # htting the bricks
        elif y_ball <= 50:
            y_ball_old = y_ball
            y_ball +=10
        # going below the striker
        elif y_ball_old < y_ball and y_ball >= 450:
            y_ball_old = y_ball
            y_ball+=10
        
    

        # motion of the ball horizontally

        # hitting the left wall 
        if x_ball - 10 < 5:
            x_ball_old = x_ball
            x_ball+=10
        # hitting the right wall
        elif x_ball + 10 > 395:
            x_ball_old = x_ball
            x_ball -= 10
        # hitting the striker while going right
        elif x_ball>= x_slider and x_ball < x_slider + 90 and x_ball_old < x_ball:
            x_ball_old = x_ball
            x_ball +=10
        # hitting the striker while going left
        elif x_ball>= x_slider and x_ball < x_slider + 90 and x_ball_old > x_ball:
            x_ball_old = x_ball
            x_ball -=10
        # going left in between
        elif x_ball_old > x_ball:
            x_ball_old = x_ball
            x_ball -=10
        # going right in between
        elif x_ball_old < x_ball:
            x_ball_old = x_ball
            x_ball+=10
      
        


        global color1
        global color2
        global color3
        global color4
        global color5
        global color6
        global color7
        
        
        # removing the bricks if hit
    
        if y_ball - 10 == 40 and x_ball >= 5 and x_ball <= 55:
            color1 = [0,0,0]
        elif y_ball - 10 == 40 and x_ball >= 60 and x_ball <= 110:
            color2 = [0,0,0]
        elif y_ball - 10 == 40 and x_ball >= 115 and x_ball <= 165:
            color3 = [0,0,0]
        elif y_ball - 10 == 40 and x_ball >= 170 and x_ball <= 220:
            color4 = [0,0,0]
        elif y_ball - 10 == 40 and x_ball >= 225 and x_ball <= 275:
            color5 = [0,0,0]
        elif y_ball - 10 == 40 and x_ball >= 280 and x_ball <= 330:
            color6 = [0,0,0]
        elif y_ball - 10 == 40 and x_ball >= 335 and x_ball <= 395:
            color7 = [0,0,0]


        if y_ball > 470:
            run = False
    
    
        dis.fill([0,0,0])

        if color1 == [0,0,0] and color2 == [0,0,0] and color3 == [0,0,0] and color4 == [0,0,0] and color5 == [0,0,0] and color6 == [0,0,0] and color7 == [0,0,0]:
            dis.fill([0,0,0])
            dis.blit(text2, textrect)
            pygame.display.update()
            pygame.time.delay(1500)
            run = False

    

    
        #ball
        pygame.draw.circle(dis, white, (x_ball,y_ball), 10, 0)
    
        # slider
        pygame.draw.rect(dis, green, [x_slider,460,90,15])

        # red bricks
        pygame.draw.rect(dis, color1, [5,30,50,15])
        pygame.draw.rect(dis, color2, [60,30,50,15])
        pygame.draw.rect(dis, color3, [115,30,50,15])
        pygame.draw.rect(dis, color4, [170,30,50,15])
        pygame.draw.rect(dis, color5, [225,30,50,15])
        pygame.draw.rect(dis, color6, [280,30,50,15])
        pygame.draw.rect(dis, color7, [335,30,60,15])


        # text
        dis.blit(text, textRect)


    
        pygame.display.update()


    pygame.quit()


mainloop(True, 300, 150, 250, 0, 0)
