# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import pygame
from pygame.locals import*
import sys
import codecs
import re
import string

class words:
    def __init__(self):
        self.i = 0;
        self.j = 0;
        self.ques = [];
        self.ans = [];
        

    def init(self):
        self.f_ques = codecs.open("./data/ques.txt", "r", "utf-8");
        for str in self.f_ques:
            str = string.replace(str, "\n", "");
            self.ques.append(str);
            #print(self.ques[self.i]);
            self.i += 1;

        self.f_ans = codecs.open("./data/ans.txt", "r", "utf-8");
        for str in self.f_ans:
            str = string.replace(str, "\n", "");
            self.ans.append(str);
            #print(self.ans[self.j]);
            self.j += 1;

    def input(self, str1, str2):
        self.f_ques = codecs.open("./data/ques.txt", "a", "utf-8");
        self.f_ans = codecs.open("./data/ans.txt", "a", "utf-8");
        self.f_ques.write(str1 + u"\n");
        self.f_ans.write(str2 + u"\n");
        self.ques.append(str1);
        self.ans.append(str2);
        self.f_ques.close();
        self.f_ans.close();

    def check(self, str):
        i = 0;
        str = str.replace(u"\n", u"");
        for list in self.ques:
            if str == list:
                return i;
            i += 1;
        return -1;

