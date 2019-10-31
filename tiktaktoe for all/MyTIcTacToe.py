import sys, pygame

import random

pygame.init()

size = (400,400)

screen = pygame.display.set_mode(size)

start_img = pygame.image.load('untitled4.png')

start_img1 = pygame.image.load('untitled5.png')

start_img2 = pygame.image.load('untitled6.png')

background = "ultimate-tic-tac-toe12-01.png"

x_image = 'x_img.png'

o_image = 'o_img.png'

cross_1 = pygame.image.load('0.png')

cross_2 = pygame.image.load('3.png')

cross_3 = pygame.image.load('1.png')

cross_4 = pygame.image.load('2.png')

bag = pygame.image.load(background)

img_1 = pygame.image.load(x_image)

img_2 = pygame.image.load(o_image)

game_over_x = pygame.image.load('untitled.png')

game_over_o = pygame.image.load('untitled1.png')

game_over_draw = pygame.image.load('untitled2.png')

game_over_bg = pygame.image.load('untitled3.png')

restart = pygame.image.load('restart.png')

restart1 = pygame.image.load('restart1.png')

restart2 = pygame.image.load('restart2.png')

run = True

innit = 1

click = 0

re_game = 0

re_game_menu = 0
while run:
    if innit == 1: 
        cross_pos = [(30,0), (30,100), (30,200), (30,30), (130,30), (230,30)]

        pos_list = [(60,50),
                    (160,50),
                    (260,50),
                    (60,160),
                    (160,160),
                    (260,160),
                    (60,270),
                    (160,270),
                    (260,270)]


        x_1 = 0
        x_2 = 0
        x_3 = 0
        x_4 = 0
        x_5 = 0
        x_6 = 0
        x_7 = 0
        x_8 = 0
        x_9 = 0
        first_x = None
        first_o = None
        second_x = None
        second_o = None
        third_x = None
        third_o = None
        fourth_x = None
        fourth_o = None
        fifth_x = None
        fifth_o = None

        x_pos = 0
        o_list = []

        ran_num = None
        o_pos2 = None
        o_pos3 = None
        o_pos4 = None

        win_str = '012345678036147258048246'

        win_init = [int(n) for n in win_str]

        win_list = []

        v_list = []

        for i in range(24):
            if i in [0,3,6,9,12,15,18,21]:
                win_list.append(win_init[i:i+3]) 

        pos = list(range(9))

        not_list = []

        i = 0

        the_list = [0,7,3,8,5,6,2,7,0,5,1,6,1,8,2,3]
        for L in range(8):
            not_list.append(the_list[i:i+2])
            i += 2


        ono_list = []

        j = 0

        the_list1 = [1,5,5,7,7,3,3,1]
        for L in range(4):
            ono_list.append(the_list1[j:j+2])
            j += 2

        diffi_level = None
        x_selec = None
        o_selec = 1
        triple_o = None
        triple_x = None
        spec_pos = [0,2,6,8,1,3,5,7]
        corner_pos = [0,2,6,8]

        ran_lili = []
        ran_lili_1 = []

        win_pos = []

        scaliton = 1
        innit = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if click != 1 and re_game == 1:
        re_game_menu = 1
        
    
    if re_game_menu == 1:
        screen.blit(restart, (0,0))
        if 20 < height < 150 and 20 < width < 350:
            screen.blit(restart1, (0,0))
            if click == 1:    
                re_game = 0
                re_game_menu = 0
        if 245 < height < 340 and 55 < width < 340:
            screen.blit(restart2, (0,0))
            if click == 1:              
                run = 0
                     
    height = pygame.mouse.get_pos()[1]
    width = pygame.mouse.get_pos()[0]
    click = pygame.mouse.get_pressed()[0]
    
    block_list = [ 30 < height < 145 and 30 < width < 145,
     30 < height < 145 and 145 < width < 250,
     30 < height < 145 and 250 < width < 350,
     145 < height < 250 and 30 < width < 145,
     145 < height < 250 and 145 < width < 250,
     145 < height < 250 and 250 < width < 350,
     250 < height < 350 and 30 < width < 145,
     250 < height < 350 and 145 < width < 250,
     250 < height < 350 and 250 < width < 350 ]  
    if re_game == 0:
        screen.fill((252, 252, 252))

        screen.blit(start_img, (0,0))   
        if diffi_level == None:
            if 130 < height < 190 and 60 < width < 190:
                screen.blit(start_img1, (0,0))
                if click == 1:
                    diffi_level = 1
            if 240 < height < 300 and 65 < width < 360:
                screen.blit(start_img2, (0,0))   
                if click == 1:
                    diffi_level = 2
            
    if diffi_level == 1:
        screen.fill((252, 252, 252))
        screen.blit(bag, (30,30))
        if click == 0:
            x_selec = 1
            
        while click ==1 and x_selec == 1:
            if block_list[0] and 0 not in o_list:
                x_1 = 1
                x_selec = 0
                    
            if block_list[1] and 1 not in o_list:
                x_2 = 1
                x_selec = 0
                
            if block_list[2] and 2 not in o_list:
                x_3 = 1
                x_selec = 0
                
            if block_list[3] and 3 not in o_list:
                x_4 = 1
                x_selec = 0
                
            if block_list[4] and 4 not in o_list:
                x_5 = 1
                x_selec = 0
                
            if block_list[5] and 5 not in o_list:
                x_6 = 1
                x_selec = 0
                
            if block_list[6] and 6 not in o_list:
                x_7 = 1
                x_selec = 0
                
            if block_list[7] and 7 not in o_list:
                x_8 = 1  
                x_selec = 0
                
            if block_list[8] and 8 not in o_list:
                x_9 = 1
                x_selec = 0
            click = 0

        def add_x():
            if x_1 == 1:    
                screen.blit(img_1, pos_list[0])

            if x_2 == 1:
                screen.blit(img_1, pos_list[1]) 

            if x_3 == 1:
                screen.blit(img_1, pos_list[2]) 

            if x_4 == 1:
                screen.blit(img_1, pos_list[3]) 

            if x_5 == 1:
                screen.blit(img_1, pos_list[4]) 

            if x_6 == 1:
                screen.blit(img_1, pos_list[5]) 

            if x_7 == 1:
                screen.blit(img_1, pos_list[6]) 

            if x_8 == 1:
                screen.blit(img_1, pos_list[7]) 

            if x_9 == 1:
                screen.blit(img_1, pos_list[8]) 

        add_x()

        while x_selec == 0 and o_selec == 1:
            for true_item in range(9):
                if block_list[true_item]:
                    first_x = true_item
            if first_x == 4:
                ran_num = random.choice(corner_pos)
            elif first_x in [1,3,5,7]:
                ran_num = random.choice([3,4,5,1,4,7])
            else:            
                ran_num = random.choice([3,4,5,1,7])

            if ran_num != first_x:        
                o_selec = 0
                first_o = 1

        if first_o == 1:
            screen.blit(img_2, pos_list[ran_num])
            o_list.append(ran_num)


        if o_selec == 0:
            x_selec = 1

        x_list = [x_1, x_2, x_3, x_4, x_5, x_6, x_7, x_8, x_9]         

        if x_list.count(1) == 2 and second_o == None:
            x_selec = 0
            for true_item in range(9):
                if block_list[true_item] and click == 1:
                    second_x = true_item 

        if second_x != None and second_o != 1:
            for n in range(8):

                if [first_x,second_x] == win_list[n][0:2] or [second_x,first_x] == win_list[n][0:2]:
                        if win_list[n][2] != ran_num:
                            o_pos2 = win_list[n][2]
                            second_o = 1
                if [first_x,second_x] == win_list[n][1:3] or [second_x,first_x] == win_list[n][1:3]:
                        if win_list[n][0] != ran_num:    
                            o_pos2 = win_list[n][0]
                            second_o = 1
                if [first_x,second_x] == [win_list[n][0],win_list[n][2]] or [second_x,first_x] == [win_list[n][0],win_list[n][2]]:
                        if win_list[n][1] != ran_num:
                            o_pos2 = win_list[n][1]
                            second_o = 1


        if second_o != 1 and second_x != None:

            for n in range(8):
                if ran_num in win_list[n]:
                    if first_x not in win_list[n] and second_x not in win_list[n]:
                        ran_list = win_list[n].copy()
                        ran_list.remove(ran_num)
                        ran_lili.append(ran_list)
                        o_pos2 = random.choice(random.choice(ran_lili))
                        if ran_num == 4:
                            if [first_x,second_x] in not_list or [second_x,first_x] in not_list:
                                o_pos2 = random.choice(ran_lili[0])
                            if [first_x,second_x] == ono_list[0] or [second_x,first_x] == ono_list[0] or [first_x,second_x] == ono_list[2] or [second_x,first_x] == ono_list[2]:
                                o_pos2 = random.choice(ran_lili[0])
                            if len(ran_lili) == 2:
                                if [first_x,second_x] == ono_list[1] or [second_x,first_x] == ono_list[1] or [first_x,second_x] == ono_list[3] or [second_x,first_x] == ono_list[3]:
                                    o_pos2 = random.choice(ran_lili[1])

                        second_o = 1

        if second_o != 1 and second_x != None:
            for n in range(8):
                if ran_num not in win_list[n] and first_x not in win_list[n] and second_x not in win_list[n]:
                    ran_list = win_list[n].copy()
                    ran_lili.append(ran_list)
                    o_pos2 = random.choice(random.choice(ran_lili))
                    second_o = 1    

        if second_o == 1:
            screen.blit(img_2, pos_list[o_pos2])
            o_list.append(o_pos2)

        if second_o == 1:
            x_selec = 1

        if x_list.count(1) == 3 and third_o == None:
            x_selec = 0
            for true_item in range(9):
                if block_list[true_item] and click == 1:
                    third_x = true_item 

        if third_x != None and third_o != 1 and triple_x == None and triple_o == None:
            for n in range(8):

                if [ran_num,o_pos2] == win_list[n][0:2] or [o_pos2,ran_num] == win_list[n][0:2]:
                    if win_list[n][2] not in [first_x,second_x,third_x]:
                        o_pos3 = win_list[n][2]
                        third_o = 1
                        triple_o = n
                if [ran_num,o_pos2] == win_list[n][1:3] or [o_pos2,ran_num] == win_list[n][1:3]:
                    if win_list[n][0] not in [first_x,second_x,third_x]:    
                        o_pos3 = win_list[n][0]
                        third_o = 1
                        triple_o = n
                if [ran_num,o_pos2] == [win_list[n][0],win_list[n][2]] or [o_pos2,ran_num] == [win_list[n][0],win_list[n][2]]:
                    if win_list[n][1] not in [first_x,second_x,third_x]:
                        o_pos3 = win_list[n][1]
                        third_o = 1
                        triple_o = n

        if third_x != None and third_o != 1 and triple_x == None and triple_o == None:
            for n in range(8):

                if [first_x,third_x] == win_list[n][0:2] or [third_x,first_x] == win_list[n][0:2] or [second_x,third_x] == win_list[n][0:2] or [third_x,second_x] == win_list[n][0:2]:
                        if win_list[n][2] not in [o_pos2,ran_num]:
                            if win_list[n][2] not in [first_x,second_x,third_x]:
                                o_pos3 = win_list[n][2]
                                third_o = 1
                if [first_x,third_x] == win_list[n][1:3] or [third_x,first_x] == win_list[n][1:3] or [second_x,third_x] == win_list[n][1:3] or [third_x,second_x] == win_list[n][1:3]:
                        if win_list[n][0] not in [o_pos2,ran_num]:
                            if win_list[n][0] not in [first_x,second_x,third_x]:
                                o_pos3 = win_list[n][0]
                                third_o = 1
                if [first_x,third_x] == [win_list[n][0],win_list[n][2]] or [third_x,first_x] == [win_list[n][0],win_list[n][2]] or [second_x,third_x] == [win_list[n][0],win_list[n][2]] or [third_x,second_x] == [win_list[n][0],win_list[n][2]]:
                        if win_list[n][1] not in [o_pos2,ran_num]:
                            if win_list[n][1] not in [first_x,second_x,third_x]:
                                o_pos3 = win_list[n][1]
                                third_o = 1



        if third_x != None and third_o != 1 and triple_x == None and triple_o == None:
            for n in range(8):
                    if ran_num in win_list[n] or o_pos2 in win_list[n]:
                        if first_x not in win_list[n] and second_x not in win_list[n] and third_x not in win_list[n]:
                            ran_list = win_list[n].copy()
                            if ran_num in win_list[n]:
                                ran_list.remove(ran_num)
                            if o_pos2 in win_list[n]:
                                ran_list.remove(o_pos2)
                            ran_lili_1.append(ran_list)
                            o_pos3 = random.choice(random.choice(ran_lili_1))
                            third_o = 1

        if third_o == 1:
            screen.blit(img_2, pos_list[o_pos3])
            o_list.append(o_pos3)



        if third_o == 1:
            x_selec = 1

        if x_list.count(1) == 4 and fourth_o == None:
            x_selec = 0
            for true_item in range(9):
                if block_list[true_item] and click == 1:
                    fourth_x = true_item 
        
        for n in range(8):
            if win_list[n][0] in [first_x,second_x,third_x,fourth_x,fifth_x]:
                if win_list[n][1] in [first_x,second_x,third_x,fourth_x,fifth_x]:
                    if win_list[n][2] in [first_x,second_x,third_x,fourth_x,fifth_x]:
                        triple_x = n   
                        
                        
        if fourth_x != None and fourth_o != 1 and triple_x == None and triple_o == None:
            for n in range(8):

                if [ran_num,o_pos3] == win_list[n][0:2] or [o_pos3,ran_num] == win_list[n][0:2] or [o_pos2,o_pos3] == win_list[n][0:2] or [o_pos3,o_pos2] == win_list[n][0:2]:
                    if win_list[n][2] not in [first_x,second_x,third_x,fourth_x]:
                        o_pos4 = win_list[n][2]
                        fourth_o = 1
                        triple_o = n
                if [ran_num,o_pos3] == win_list[n][1:3] or [ran_num,o_pos3] == win_list[n][1:3] or [o_pos2,o_pos3] == win_list[n][1:3] or [o_pos2,o_pos3] == win_list[n][1:3]:
                    if win_list[n][0] not in [first_x,second_x,third_x,fourth_x]:    
                        o_pos4 = win_list[n][0]
                        fourth_o = 1
                        triple_o = n
                if [ran_num,o_pos3] == [win_list[n][0],win_list[n][2]] or [ran_num,o_pos3] == [win_list[n][0],win_list[n][2]] or [o_pos2,o_pos3] == [win_list[n][0],win_list[n][2]] or [o_pos2,o_pos3] == [win_list[n][0],win_list[n][2]]:
                    if win_list[n][1] not in [first_x,second_x,third_x,fourth_x]:
                        o_pos4 = win_list[n][1]
                        fourth_o = 1
                        triple_o = n

        if fourth_x != None and fourth_o != 1 and triple_x == None and triple_o == None:
            for n in range(8):

                if [first_x,fourth_x] == win_list[n][0:2] or [fourth_x,first_x] == win_list[n][0:2] or [second_x,fourth_x] == win_list[n][0:2] or [fourth_x,second_x] == win_list[n][0:2] or [third_x,fourth_x] == win_list[n][0:2] or [fourth_x,third_x] == win_list[n][0:2]:
                        if win_list[n][2] not in [o_pos3,o_pos2,ran_num]:
                            if win_list[n][2] not in [first_x,second_x,third_x,fourth_x]:
                                o_pos4 = win_list[n][2]
                                fourth_o = 1
                if [first_x,fourth_x] == win_list[n][1:3] or [fourth_x,first_x] == win_list[n][1:3] or [second_x,fourth_x] == win_list[n][1:3] or [fourth_x,second_x] == win_list[n][1:3] or [third_x,fourth_x] == win_list[n][1:3] or [fourth_x,third_x] == win_list[n][1:3]:
                        if win_list[n][0] not in [o_pos3,o_pos2,ran_num]:    
                            if win_list[n][0] not in [first_x,second_x,third_x,fourth_x]:
                                o_pos4 = win_list[n][0]
                                fourth_o = 1
                if [first_x,fourth_x] == [win_list[n][0],win_list[n][2]] or [fourth_x,first_x] == [win_list[n][0],win_list[n][2]] or [second_x,fourth_x] == [win_list[n][0],win_list[n][2]] or [fourth_x,second_x] == [win_list[n][0],win_list[n][2]] or [third_x,fourth_x] == [win_list[n][0],win_list[n][2]] or [fourth_x,third_x] == [win_list[n][0],win_list[n][2]]:
                        if win_list[n][1] not in [o_pos3,o_pos2,ran_num]:
                            if win_list[n][2] not in [first_x,second_x,third_x,fourth_x]:
                                o_pos4 = win_list[n][1]
                                fourth_o = 1

        if fourth_x != None and fourth_o != 1 and triple_x == None and triple_o == None:
            for r in [first_x,ran_num,second_x,o_pos2,third_x,o_pos3,fourth_x]:
                pos.remove(r)
            o_pos4 = random.choice(pos)
            for n in range(8):

                if [first_x,fifth_x] == win_list[n][0:2] or [fifth_x,first_x] == win_list[n][0:2] or [second_x,fifth_x] == win_list[n][0:2] or [fifth_x,second_x] == win_list[n][0:2] or [third_x,fifth_x] == win_list[n][0:2] or [fifth_x,third_x] == win_list[n][0:2] or [fourth_x,fifth_x] == win_list[n][0:2] or [fifth_x,fourth_x] == win_list[n][0:2]:
                    if win_list[n][2] in pos:
                        o_pos4 = win_list[n][2]
                if [first_x,fifth_x] == win_list[n][1:3] or [fifth_x,first_x] == win_list[n][1:3] or [second_x,fifth_x] == win_list[n][1:3] or [fifth_x,second_x] == win_list[n][1:3] or [third_x,fifth_x] == win_list[n][1:3] or [fifth_x,third_x] == win_list[n][1:3] or [fourth_x,fifth_x] == win_list[n][1:3] or [fifth_x,fourth_x] == win_list[n][1:3]:
                    if win_list[n][0] in pos:
                        o_pos4 = win_list[n][0]
                if [first_x,fifth_x] == [win_list[n][0],win_list[n][2]] or [fifth_x,first_x] == [win_list[n][0],win_list[n][2]] or [second_x,fifth_x] == [win_list[n][0],win_list[n][2]] or [fifth_x,second_x] == [win_list[n][0],win_list[n][2]] or [third_x,fifth_x] == [win_list[n][0],win_list[n][2]] or [fifth_x,third_x] == [win_list[n][0],win_list[n][2]] or [fourth_x,fifth_x] == [win_list[n][0],win_list[n][2]] or [fifth_x,fourth_x] == [win_list[n][0],win_list[n][2]]:
                    if win_list[n][1] in pos:
                        o_pos4 = win_list[n][1]
            fourth_o = 1
        
        for n in range(8):
            if win_list[n][0] in [ran_num,o_pos2,o_pos3,o_pos4]:
                if win_list[n][1] in [ran_num,o_pos2,o_pos3,o_pos4]:
                    if win_list[n][2] in [ran_num,o_pos2,o_pos3,o_pos4]:
                        triple_o = n
                        
        if fourth_o == 1:
            screen.blit(img_2, pos_list[o_pos4])
            o_list.append(o_pos4)

        if fourth_o == 1:
            x_selec = 1

        if x_list.count(1) == 5:
            x_selec = 0
            for true_item in range(9):
                if block_list[true_item] and click == 1:
                    fifth_x = true_item


        if triple_x != None:
            if triple_x < 3:
                screen.blit(cross_1, cross_pos[triple_x])
            elif 2 < triple_x < 6:
                screen.blit(cross_2, cross_pos[triple_x])
            elif triple_x == 6:
                screen.blit(cross_3, (30,30))
            elif triple_x == 7:
                screen.blit(cross_4, (30,30))
            screen.blit(game_over_bg, (0,0))
            screen.blit(game_over_x, (30,30))
            x_selec = 0

        if triple_o != None and triple_x == None:
            if triple_o < 3:
                screen.blit(cross_1, cross_pos[triple_o])
            elif 2 < triple_o < 6:
                screen.blit(cross_2, cross_pos[triple_o])
            elif triple_o == 6:
                screen.blit(cross_3, (30,30))
            elif triple_o == 7:
                screen.blit(cross_4, (30,30))
            screen.blit(game_over_bg, (0,0))
            screen.blit(game_over_o, (30,30))
            x_selec = 0

        if fifth_x != None:
            screen.blit(game_over_bg, (0,0))
            screen.blit(game_over_draw , (30,30))
            pygame.display.flip()
            pygame.time.delay(1000)
            innit = 1
            re_game = 1
        
        if triple_x != None or triple_o != None:
            pygame.display.flip()
            pygame.time.delay(1000)
            innit = 1
            re_game = 1
        pygame.display.flip()
            
    if diffi_level == 2:
        if click == 0:
            x_selec = 1
        
        screen.fill((252, 252, 252))
        screen.blit(bag, (30,30))

        while click ==1 and x_selec == 1:
            if block_list[0] and 0 not in o_list:
                x_1 = 1
                x_selec = 0
                    
            if block_list[1] and 1 not in o_list:
                x_2 = 1
                x_selec = 0
                
            if block_list[2] and 2 not in o_list:
                x_3 = 1
                x_selec = 0
                
            if block_list[3] and 3 not in o_list:
                x_4 = 1
                x_selec = 0
                
            if block_list[4] and 4 not in o_list:
                x_5 = 1
                x_selec = 0
                
            if block_list[5] and 5 not in o_list:
                x_6 = 1
                x_selec = 0
                
            if block_list[6] and 6 not in o_list:
                x_7 = 1
                x_selec = 0
                
            if block_list[7] and 7 not in o_list:
                x_8 = 1  
                x_selec = 0
                
            if block_list[8] and 8 not in o_list:
                x_9 = 1
                x_selec = 0
            click = 0
                
        def add_x():
            if x_1 == 1:    
                screen.blit(img_1, pos_list[0])

            if x_2 == 1:
                screen.blit(img_1, pos_list[1]) 

            if x_3 == 1:
                screen.blit(img_1, pos_list[2]) 

            if x_4 == 1:
                screen.blit(img_1, pos_list[3]) 

            if x_5 == 1:
                screen.blit(img_1, pos_list[4]) 

            if x_6 == 1:
                screen.blit(img_1, pos_list[5]) 

            if x_7 == 1:
                screen.blit(img_1, pos_list[6]) 

            if x_8 == 1:
                screen.blit(img_1, pos_list[7]) 

            if x_9 == 1:
                screen.blit(img_1, pos_list[8]) 

        add_x()

        while x_selec == 0 and o_selec == 1:
            for true_item in range(9):
                if block_list[true_item]:
                    first_x = true_item
            if first_x == 4:
                ran_num = random.choice(corner_pos)
            elif first_x in [1,3,5,7]:
                if first_x == 1:
                    ran_num = random.choice([0,2,4])
                if first_x == 3:
                    ran_num = random.choice([0,6,4])
                if first_x == 5:
                    ran_num = random.choice([2,8,4])
                if first_x == 7:
                    ran_num = random.choice([6,8,4])
                    
                    
            else:        
                ran_num = 4

            if ran_num != first_x:        
                o_selec = 0
                first_o = 1

        if first_o == 1:
            screen.blit(img_2, pos_list[ran_num])
            o_list.append(ran_num)


        if o_selec == 0:
            x_selec = 1

        x_list = [x_1, x_2, x_3, x_4, x_5, x_6, x_7, x_8, x_9]         

        if x_list.count(1) == 2 and second_o == None:
            x_selec = 0
            for true_item in range(9):
                if block_list[true_item] and click == 1:
                    second_x = true_item 

        if second_x != None and second_o != 1:
            for n in range(8):

                if [first_x,second_x] == win_list[n][0:2] or [second_x,first_x] == win_list[n][0:2]:
                        if win_list[n][2] != ran_num:
                            o_pos2 = win_list[n][2]
                            second_o = 1
                if [first_x,second_x] == win_list[n][1:3] or [second_x,first_x] == win_list[n][1:3]:
                        if win_list[n][0] != ran_num:    
                            o_pos2 = win_list[n][0]
                            second_o = 1
                if [first_x,second_x] == [win_list[n][0],win_list[n][2]] or [second_x,first_x] == [win_list[n][0],win_list[n][2]]:
                        if win_list[n][1] != ran_num:
                            o_pos2 = win_list[n][1]
                            second_o = 1


        if second_o != 1 and second_x != None:

            for n in range(8):
                if ran_num in win_list[n]:
                    if first_x not in win_list[n] and second_x not in win_list[n]:
                        ran_list = win_list[n].copy()
                        ran_list.remove(ran_num)
                        ran_lili.append(ran_list)
                        o_pos2 = random.choice(random.choice(ran_lili))
                        if ran_num == 4:
                            if [first_x,second_x] in not_list or [second_x,first_x] in not_list:
                                o_pos2 = random.choice(ran_lili[0])
                            if [first_x,second_x] == ono_list[0] or [second_x,first_x] == ono_list[0] or [first_x,second_x] == ono_list[2] or [second_x,first_x] == ono_list[2]:
                                o_pos2 = random.choice(ran_lili[0])
                            if len(ran_lili) == 2:
                                if [first_x,second_x] == ono_list[1] or [second_x,first_x] == ono_list[1] or [first_x,second_x] == ono_list[3] or [second_x,first_x] == ono_list[3]:
                                    o_pos2 = random.choice(ran_lili[1])
                        
                        if [first_x,second_x] == [4,0] or [first_x,second_x] == [4,8]:
                            o_pos2 = random.choice([2,6])
                        if [first_x,second_x] == [4,2] or [first_x,second_x] == [4,6]:
                            o_pos2 = random.choice([0,8])
                            
                        
                        second_o = 1

        if second_o != 1 and second_x != None:
            for n in range(8):
                if ran_num not in win_list[n] and first_x not in win_list[n] and second_x not in win_list[n]:
                    ran_list = win_list[n].copy()
                    ran_lili.append(ran_list)
                    o_pos2 = random.choice(random.choice(ran_lili))
                    second_o = 1    

        if second_o == 1:
            screen.blit(img_2, pos_list[o_pos2])
            o_list.append(o_pos2)

        if second_o == 1:
            x_selec = 1

        if x_list.count(1) == 3 and third_o == None:
            x_selec = 0
            for true_item in range(9):
                if block_list[true_item] and click == 1:
                    third_x = true_item 

        if third_x != None and third_o != 1 and triple_x == None and triple_o == None:
            for n in range(8):

                if [ran_num,o_pos2] == win_list[n][0:2] or [o_pos2,ran_num] == win_list[n][0:2]:
                    if win_list[n][2] not in [first_x,second_x,third_x]:
                        o_pos3 = win_list[n][2]
                        third_o = 1
                        triple_o = n
                if [ran_num,o_pos2] == win_list[n][1:3] or [o_pos2,ran_num] == win_list[n][1:3]:
                    if win_list[n][0] not in [first_x,second_x,third_x]:    
                        o_pos3 = win_list[n][0]
                        third_o = 1
                        triple_o = n
                if [ran_num,o_pos2] == [win_list[n][0],win_list[n][2]] or [o_pos2,ran_num] == [win_list[n][0],win_list[n][2]]:
                    if win_list[n][1] not in [first_x,second_x,third_x]:
                        o_pos3 = win_list[n][1]
                        third_o = 1
                        triple_o = n

        if third_x != None and third_o != 1 and triple_x == None and triple_o == None:
            for n in range(8):

                if [first_x,third_x] == win_list[n][0:2] or [third_x,first_x] == win_list[n][0:2] or [second_x,third_x] == win_list[n][0:2] or [third_x,second_x] == win_list[n][0:2]:
                        if win_list[n][2] not in [o_pos2,ran_num]:
                            if win_list[n][2] not in [first_x,second_x,third_x]:
                                o_pos3 = win_list[n][2]
                                third_o = 1
                if [first_x,third_x] == win_list[n][1:3] or [third_x,first_x] == win_list[n][1:3] or [second_x,third_x] == win_list[n][1:3] or [third_x,second_x] == win_list[n][1:3]:
                        if win_list[n][0] not in [o_pos2,ran_num]:
                            if win_list[n][0] not in [first_x,second_x,third_x]:
                                o_pos3 = win_list[n][0]
                                third_o = 1
                if [first_x,third_x] == [win_list[n][0],win_list[n][2]] or [third_x,first_x] == [win_list[n][0],win_list[n][2]] or [second_x,third_x] == [win_list[n][0],win_list[n][2]] or [third_x,second_x] == [win_list[n][0],win_list[n][2]]:
                        if win_list[n][1] not in [o_pos2,ran_num]:
                            if win_list[n][1] not in [first_x,second_x,third_x]:
                                o_pos3 = win_list[n][1]
                                third_o = 1



        if third_x != None and third_o != 1 and triple_x == None and triple_o == None:
            for n in range(8):
                    if ran_num in win_list[n] or o_pos2 in win_list[n]:
                        if first_x not in win_list[n] and second_x not in win_list[n] and third_x not in win_list[n]:
                            ran_list = win_list[n].copy()
                            if ran_num in win_list[n]:
                                ran_list.remove(ran_num)
                            if o_pos2 in win_list[n]:
                                ran_list.remove(o_pos2)
                            ran_lili_1.append(ran_list)
                            o_pos3 = random.choice(random.choice(ran_lili_1))
                            third_o = 1

        if third_o == 1:
            screen.blit(img_2, pos_list[o_pos3])
            o_list.append(o_pos3)



        if third_o == 1:
            x_selec = 1

        if x_list.count(1) == 4 and fourth_o == None:
            x_selec = 0
            for true_item in range(9):
                if block_list[true_item] and click == 1:
                    fourth_x = true_item 
        
        for n in range(8):
            if win_list[n][0] in [first_x,second_x,third_x,fourth_x,fifth_x]:
                if win_list[n][1] in [first_x,second_x,third_x,fourth_x,fifth_x]:
                    if win_list[n][2] in [first_x,second_x,third_x,fourth_x,fifth_x]:
                        triple_x = n  
        
        if fourth_x != None and fourth_o != 1 and triple_x == None and triple_o == None:
            for n in range(8):

                if [ran_num,o_pos3] == win_list[n][0:2] or [o_pos3,ran_num] == win_list[n][0:2] or [o_pos2,o_pos3] == win_list[n][0:2] or [o_pos3,o_pos2] == win_list[n][0:2]:
                    if win_list[n][2] not in [first_x,second_x,third_x,fourth_x]:
                        o_pos4 = win_list[n][2]
                        fourth_o = 1
                        triple_o = n
                if [ran_num,o_pos3] == win_list[n][1:3] or [ran_num,o_pos3] == win_list[n][1:3] or [o_pos2,o_pos3] == win_list[n][1:3] or [o_pos2,o_pos3] == win_list[n][1:3]:
                    if win_list[n][0] not in [first_x,second_x,third_x,fourth_x]:    
                        o_pos4 = win_list[n][0]
                        fourth_o = 1
                        triple_o = n
                if [ran_num,o_pos3] == [win_list[n][0],win_list[n][2]] or [ran_num,o_pos3] == [win_list[n][0],win_list[n][2]] or [o_pos2,o_pos3] == [win_list[n][0],win_list[n][2]] or [o_pos2,o_pos3] == [win_list[n][0],win_list[n][2]]:
                    if win_list[n][1] not in [first_x,second_x,third_x,fourth_x]:
                        o_pos4 = win_list[n][1]
                        fourth_o = 1
                        triple_o = n

        if fourth_x != None and fourth_o != 1 and triple_x == None and triple_o == None:
            for n in range(8):

                if [first_x,fourth_x] == win_list[n][0:2] or [fourth_x,first_x] == win_list[n][0:2] or [second_x,fourth_x] == win_list[n][0:2] or [fourth_x,second_x] == win_list[n][0:2] or [third_x,fourth_x] == win_list[n][0:2] or [fourth_x,third_x] == win_list[n][0:2]:
                        if win_list[n][2] not in [o_pos3,o_pos2,ran_num]:
                            if win_list[n][2] not in [first_x,second_x,third_x,fourth_x]:
                                o_pos4 = win_list[n][2]
                                fourth_o = 1
                if [first_x,fourth_x] == win_list[n][1:3] or [fourth_x,first_x] == win_list[n][1:3] or [second_x,fourth_x] == win_list[n][1:3] or [fourth_x,second_x] == win_list[n][1:3] or [third_x,fourth_x] == win_list[n][1:3] or [fourth_x,third_x] == win_list[n][1:3]:
                        if win_list[n][0] not in [o_pos3,o_pos2,ran_num]:    
                            if win_list[n][0] not in [first_x,second_x,third_x,fourth_x]:
                                o_pos4 = win_list[n][0]
                                fourth_o = 1
                if [first_x,fourth_x] == [win_list[n][0],win_list[n][2]] or [fourth_x,first_x] == [win_list[n][0],win_list[n][2]] or [second_x,fourth_x] == [win_list[n][0],win_list[n][2]] or [fourth_x,second_x] == [win_list[n][0],win_list[n][2]] or [third_x,fourth_x] == [win_list[n][0],win_list[n][2]] or [fourth_x,third_x] == [win_list[n][0],win_list[n][2]]:
                        if win_list[n][1] not in [o_pos3,o_pos2,ran_num]:
                            if win_list[n][1] not in [first_x,second_x,third_x,fourth_x]:
                                o_pos4 = win_list[n][1]
                                fourth_o = 1

        if fourth_x != None and fourth_o != 1 and triple_x == None and triple_o == None:
            for r in [first_x,ran_num,second_x,o_pos2,third_x,o_pos3,fourth_x]:
                pos.remove(r)
            o_pos4 = random.choice(pos)
            for n in range(8):

                if [first_x,fifth_x] == win_list[n][0:2] or [fifth_x,first_x] == win_list[n][0:2] or [second_x,fifth_x] == win_list[n][0:2] or [fifth_x,second_x] == win_list[n][0:2] or [third_x,fifth_x] == win_list[n][0:2] or [fifth_x,third_x] == win_list[n][0:2] or [fourth_x,fifth_x] == win_list[n][0:2] or [fifth_x,fourth_x] == win_list[n][0:2]:
                    if win_list[n][2] in pos:
                        o_pos4 = win_list[n][2]
                if [first_x,fifth_x] == win_list[n][1:3] or [fifth_x,first_x] == win_list[n][1:3] or [second_x,fifth_x] == win_list[n][1:3] or [fifth_x,second_x] == win_list[n][1:3] or [third_x,fifth_x] == win_list[n][1:3] or [fifth_x,third_x] == win_list[n][1:3] or [fourth_x,fifth_x] == win_list[n][1:3] or [fifth_x,fourth_x] == win_list[n][1:3]:
                    if win_list[n][0] in pos:
                        o_pos4 = win_list[n][0]
                if [first_x,fifth_x] == [win_list[n][0],win_list[n][2]] or [fifth_x,first_x] == [win_list[n][0],win_list[n][2]] or [second_x,fifth_x] == [win_list[n][0],win_list[n][2]] or [fifth_x,second_x] == [win_list[n][0],win_list[n][2]] or [third_x,fifth_x] == [win_list[n][0],win_list[n][2]] or [fifth_x,third_x] == [win_list[n][0],win_list[n][2]] or [fourth_x,fifth_x] == [win_list[n][0],win_list[n][2]] or [fifth_x,fourth_x] == [win_list[n][0],win_list[n][2]]:
                    if win_list[n][1] in pos:
                        o_pos4 = win_list[n][1]
                    
            fourth_o = 1
        
        for n in range(8):
            if win_list[n][0] in [ran_num,o_pos2,o_pos3,o_pos4]:
                if win_list[n][1] in [ran_num,o_pos2,o_pos3,o_pos4]:
                    if win_list[n][2] in [ran_num,o_pos2,o_pos3,o_pos4]:
                        triple_o = n
                        
        if fourth_o == 1:
            screen.blit(img_2, pos_list[o_pos4])
            o_list.append(o_pos4)

        if fourth_o == 1:
            x_selec = 1

        if x_list.count(1) == 5:
            x_selec = 0
            for true_item in range(9):
                if block_list[true_item] and click == 1:
                    fifth_x = true_item    

        if triple_x != None:
            if triple_x < 3:
                screen.blit(cross_1, cross_pos[triple_x])
            elif 2 < triple_x < 6:
                screen.blit(cross_2, cross_pos[triple_x])
            elif triple_x == 6:
                screen.blit(cross_3, (30,30))
            elif triple_x == 7:
                screen.blit(cross_4, (30,30))
            screen.blit(game_over_bg, (0,0))
            screen.blit(game_over_x, (30,30))
            x_selec = 0

        if triple_o != None and triple_x == None:
            if triple_o < 3:
                screen.blit(cross_1, cross_pos[triple_o])
            elif 2 < triple_o < 6:
                screen.blit(cross_2, cross_pos[triple_o])
            elif triple_o == 6:
                screen.blit(cross_3, (30,30))
            elif triple_o == 7:
                screen.blit(cross_4, (30,30))
            screen.blit(game_over_bg, (0,0))
            screen.blit(game_over_o, (30,30))
            x_selec = 0
            
        if fifth_x != None:
            screen.blit(game_over_bg, (0,0))
            screen.blit(game_over_draw , (30,30))
            pygame.display.flip()
            pygame.time.delay(1000)
            innit = 1
            re_game = 1
            
        if triple_x != None or triple_o != None:
            pygame.display.flip()
            pygame.time.delay(1000)
            innit = 1
            re_game = 1
            
        pygame.display.flip()
        
    pygame.display.flip() 
            

pygame.quit()