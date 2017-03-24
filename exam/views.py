from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from exam.dao import PaperDao  
from exam.dao import QuestionDao
from exam.dao import AnswerDao

# Create your views here.
def index(request):
    context = {'title': 'qinlicang', 'items': ''}
    paperDao = PaperDao()
    items = paperDao.getSimuList()
    context['items'] = items
    return render(request, 'index.html', context)    
#     if request.method == 'GET':
#     if request.method == 'POST':
    #     t = get_template('index.html')
    #     html = t.render(context)
    #     return HttpResponse(html)

#显示一套试题的索引
def paper(request, paper_id):
    context = {'title': 'paper'}
    questionDao = QuestionDao()
    items = questionDao.getList(paper_id)
    context['items'] = items
    return render(request, 'paper.html', context)    

#显示一个问题
def paperitem(request, paper_id, question_id):
    context = {'title': 'paperitem'}
    questionDao = QuestionDao()
    question = questionDao.getItem(paper_id, question_id)
    context['question'] = question
    
    answerDao = AnswerDao()
    answers = answerDao.getList(question_id)
    context['answers'] = answers 
       
    return render(request, 'paperitem.html', context)

# 
# def gettitlesounds(request, soundname):
#     context = {'title': 'paperitem'}
#     return render(request, 'paperitem.html', context)
