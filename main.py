# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import pygame
import words
import codecs
from pygame.locals import*
import sys

def end(sc):
    f = pygame.font.Font("./font/okuribito.ttf", 70);
    gbtxt = f.render(u"くそおおおおおおおおおお", True, (255,0,0));
    tonyfinal = pygame.image.load("./image/tonyfinal.png").convert();
    sc.blit(gbtxt, (70, 524 + 188 / 2 - 10));
    sc.blit(tonyfinal,(439, 220));
    pygame.display.update();
#    t = raw_input();
    pygame.time.wait(1500);
#    str = "トニー乙";
#    f = open("data.txt", "a");
#    f.writelines(str);
#    f.close();
    pygame.quit();
    sys.exit();

def drawtony(sc):
    backimg = pygame.image.load("./image/heart.jpg").convert();
    tony = pygame.image.load("./image/tonyright.jpg").convert();

    textwindow1 = Rect(50, 518, 924, 200);
    textwindow2 = Rect(56, 524, 912, 188);
    
    sc.blit(backimg, (0,0));
    sc.blit(tony,((1024 - 432) / 2, 0));
    pygame.draw.rect(sc,(255,255,255),textwindow1);
    pygame.draw.rect(sc,(0,0,0),textwindow2);


#    den = pygame.image.load("den.png").convert();
#    sc.blit(den, (465, 100));
#    #pygame.display.update();

    pygame.display.update();


def check(str, w):
    i = 0;
    str = str.replace(u"\n", u"");
    for list in w.ques:
        if str == list:
            return i;
        i += 1;
    return -1;

def main():
    
    pygame.init();
    screen = pygame.display.set_mode((1024,768));
    font = pygame.font.Font("./font/crayon.ttf", 70);
    drawtony(screen);
    w = words.words();
    w.init();
    while(1):
        input = raw_input();
        input = unicode(input, "utf-8");
        #print(input);
        if input == u"exit":
            end(screen);
        if input == u"さようなら":
            end(screen);
        result = check(input, w);
        #print(result);
        if result != -1:
            ny = font.render(w.ans[result] + u"ニー！", True, (255,255,255));
            screen.blit(ny, (70, 524 + 188 / 2 - 10));
            pygame.display.update();
            pygame.time.wait(2000);
            drawtony(screen);
            continue;
        say = font.render(input + u"ってなあニー？", True, (255,255,255));
        screen.blit(say, (70, 524 + 188 / 2 - 10));
        pygame.display.update();
        input2 = raw_input();
        input2 = unicode(input2, "utf-8");
        teach = font.render(input2 + u"かあ、ありがトニー！", True, (255,255,255));
        drawtony(screen);
        screen.blit(teach, (70, 524 + 188 / 2 - 10));
        den = pygame.image.load("./image/den.png").convert();
        screen.blit(den, (455, 100));
        w.input(input, input2);
        pygame.display.update();
        pygame.time.wait(2000);
        drawtony(screen);

#        for event in pygame.event.get():
#            if event.type == QUIT:
#                pygame.quit();
#                sys.exit();
#                if event.type == KEYDOWN:
#                    if event.key == K_ESCAPE:
#                        pygame.quit();
#                        sys.exit();

if __name__ == "__main__":
    main();
