import os
import sqlite3
from django.test import TestCase
from exam.models import Paper
from exam.models import Question
from django.db import connection

class SimpleTest(TestCase):

    def test_paper_list(self):
        
        paper = Paper()
        paper.getList()
#         
#         curdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#         print(curdir)
#         db = sqlite3.connect(os.path.join(curdir, 'database/db.sqlite3'))
#         cursor = db.cursor()
#         items = cursor.execute('select * from paper')
#         print(items[0].__getattribute__('name'))

#         items =Paper.objects.all()
#         print(items[1].__getattribute__('name'))
# 
#         ques = Question.objects.all()
#         print(ques.count())
#         
#         papers = Paper.objects.all()
#         print(papers.count())
#         print(len(papers))
#         
#         
#         return papers
