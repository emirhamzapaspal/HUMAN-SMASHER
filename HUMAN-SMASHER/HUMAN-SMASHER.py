import pygame, random, time

pygame.init()

width = 1000
height = 600
bulletshootup = False
bulletshootdown = False
bulletshootright = False
bulletshootleft = False
bulletdisplay = False
started = False
credits = False
game_over = False
score = 0
scolor = (0,255,255)
ccolor = (255,255,255)
font = pygame.font.SysFont("arialblack", 40)
font2 = pygame.font.SysFont("arialblack", 50)

yazi = font.render("GAME OVER Press R to Restart", True, (255,255,255))
yazi_pos = yazi.get_rect()
yazi_pos.topleft = (200, 200)

yazi7 = font.render("Press M to go to Menu", True, (255,255,255))
yazi7_pos = yazi7.get_rect()
yazi7_pos.topleft = (290, 300)

screen = pygame.display.set_mode((width, height))

player = pygame.image.load("img/player.png")
player_pos = player.get_rect()
player_pos.topleft = (500, 300)

enemy = pygame.image.load("img/enemyhuman.png")
enemy_pos = enemy.get_rect()
enemy_pos.topleft = (0,0)

bullet = pygame.image.load("img/bullet.png")
bullet_pos = bullet.get_rect()
bullet_pos.topleft = (player_pos.x + 15, player_pos.y)

running = True
while running == True:
    mouse_x ,mouse_y = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    yazi3 = font.render("START", True, (scolor))
    yazi3_pos = yazi3.get_rect()
    yazi3_pos.topleft = (430, 260)

    yazi4 = font.render("CREDITS", True, (ccolor))
    yazi4_pos = yazi4.get_rect()
    yazi4_pos.topleft = (430, 380)

    yazi5 = font.render("Press R to Return", True, (255,255,255))
    yazi5_pos = yazi5.get_rect()
    yazi5_pos.topleft = (500, 500)

    yazi6 = font.render("Yapımcı: Emir Hamza Paspal", True, (255,255,255))
    yazi6_pos = yazi6.get_rect()
    yazi6_pos.topleft = (200, 200)

    yazi8 = font.render("Your Score: " + str(score), True, (255,255,255))
    yazi8_pos = yazi8.get_rect()
    yazi8_pos.topleft = (290, 400)

    yazi9 = font2.render("HUMAN SMASHER", True, (255,255,255))
    yazi9_pos = yazi9.get_rect()
    yazi9_pos.topleft = (260, 100)

    screen.fill((100,100,100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    
    keys = pygame.key.get_pressed()
    if started == True:
        keys = pygame.key.get_pressed()
        if game_over == False:
            if keys[pygame.K_w]:
                player_pos.y -= 2
            if keys[pygame.K_s]:
                player_pos.y += 2
            if keys[pygame.K_a]:
                player_pos.x -= 2
            if keys[pygame.K_d]:
                player_pos.x += 2

            if enemy_pos.x < player_pos.x:
                enemy_pos.x += 1
            if enemy_pos.x > player_pos.x:
                enemy_pos.x -= 1
            if enemy_pos.y < player_pos.y:
                enemy_pos.y += 1
            if enemy_pos.y > player_pos.y:
                enemy_pos.y -= 1

            if enemy_pos.colliderect(player_pos):
                game_over = True
            else:
                game_over = False
            
            if bullet_pos.colliderect(enemy_pos):
                enemy_pos.x = random.randint(0, 1000)
                enemy_pos.y = random.randint(0, 600)
                score += 1

            gunright = pygame.image.load("img/gunright.png")
            gunright_pos = gunright.get_rect()
            gunright_pos.topleft = (player_pos.x + 15, player_pos.y)

            yazi2 = font.render("SCORE: " + str(score), True, (255,255,255))
            yazi2_pos = yazi.get_rect()
            yazi2_pos.topleft = (400, 50)

            gunleft = pygame.image.load("img/gunleft.png")
            gunleft_pos = gunleft.get_rect()
            gunleft_pos.topleft = (player_pos.x - 15, player_pos.y)

            gunup = pygame.image.load("img/gunup.png")
            gunup_pos = gunleft.get_rect()
            gunup_pos.topleft = (player_pos.x, player_pos.y - 20)

            gundown = pygame.image.load("img/gundown.png")
            gundown_pos = gunleft.get_rect()
            gundown_pos.topleft = (player_pos.x, player_pos.y + 20)

            if player_pos.y < 0:
                game_over = True
            elif player_pos.y > 600:
                game_over = True
            elif player_pos.x < 0:
                game_over = True
            elif player_pos.x > 1000:
                game_over = True

            screen.blit(player, player_pos)
            if mouse_y < player_pos.y - 30:
                screen.blit(gunup, gunup_pos)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    bulletshootup = True
                    bulletdisplay = True
            elif mouse_y > player_pos.y + 70:
                screen.blit(gundown, gundown_pos)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    bulletshootdown = True
                    bulletdisplay = True
            elif mouse_x > player_pos.x:
                screen.blit(gunright, gunright_pos)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    bulletshootright = True
                    bulletdisplay = True
            elif mouse_x < player_pos.x:
                screen.blit(gunleft, gunleft_pos)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    bulletshootleft = True
                    bulletdisplay = True
            
            if bulletdisplay == True:
                screen.blit(bullet, bullet_pos)
                if bulletshootup == True:
                    bullet_pos.y -= 5
                    if bullet_pos.y < 0:
                        bulletdisplay = False
                        bulletshootup = False
                if bulletshootdown == True:
                    bullet_pos.y += 5
                    if bullet_pos.y > 600:
                        bulletdisplay = False
                        bulletshootdown = False
                if bulletshootleft == True:
                    bullet_pos.x -= 5
                    if bullet_pos.x < 0:
                        bulletdisplay = False
                        bulletshootleft = False
                if bulletshootright == True:
                    bullet_pos.x += 5
                    if bullet_pos.x > 1000:
                        bulletdisplay = False
                        bulletshootright = False

            else:
                bullet_pos.topleft = (player_pos.x + 15, player_pos.y)

            screen.blit(enemy, enemy_pos)
            screen.blit(yazi2, yazi2_pos)

        else:
            screen.blit(yazi, yazi_pos)
            screen.blit(yazi7, yazi7_pos)
            screen.blit(yazi8, yazi8_pos)
            if keys[pygame.K_r]:
                score = 0
                game_over = False
                player_pos.topleft = (500, 300)
                enemy_pos.topleft = (0,0)
                bullet_pos.topleft = (player_pos.x + 15, player_pos.y)
                bulletshootup = False
                bulletshootdown = False
                bulletshootright = False
                bulletshootleft = False
                bulletdisplay = False
            elif keys[pygame.K_m]:
                started = False
    else:
        if credits == False:
            screen.blit(yazi9, yazi9_pos)
            screen.blit(yazi3, yazi3_pos)
            screen.blit(yazi4, yazi4_pos)
            if scolor == (0,255,255):
                if keys[pygame.K_DOWN]:
                    scolor = (255,255,255)
                    ccolor = (0,255,255)
                elif keys[pygame.K_SPACE]:
                    started = True
            if ccolor == (0,255,255):
                if keys[pygame.K_UP]:
                    scolor = (0,255,255)
                    ccolor = (255,255,255)
                elif keys[pygame.K_SPACE]:
                    print("sa")
                    credits = True
        else:
            screen.blit(yazi5, yazi5_pos)
            screen.blit(yazi6, yazi6_pos)
            if keys[pygame.K_r]:
                credits = False

    pygame.display.update()