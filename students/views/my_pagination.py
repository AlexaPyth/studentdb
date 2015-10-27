# -*- coding: utf-8 -*-
__author__ = 'sasha'

class MyPaginator(object ):
    def __init__(self,students,per_page):
        self.studs = students
        self.per_page = per_page
        self.number = ''
    class MyExept(Exception):
        pass

    class NonInt(Exception):
        pass

    def num_pages(self):
        if len(self.studs)%self.per_page > 0:
            num_page = len(self.studs) // self.per_page + 1
        return num_page

    def page(self,nom_page):
        try:
            if not isinstance(nom_page,int):
                raise self.NonInt
            if nom_page > self.num_pages():
                raise self.MyExept

        except self.NonInt:
            nom_page = 1
        except self.MyExept:
            nom_page = self.num_pages()
        self.number = nom_page
        start = (self.number-1)*self.per_page+1
        finn =  self.number*self.per_page+1
        return (self.studs[start:finn],self.number)

