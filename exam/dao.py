import json
from django.db import models
from django.db.models import Q
from exam.models import Paper
from exam.models import Question
from exam.models import Answers

def tojson(obj):
    keys = []
    for field in obj._meta.fields:
        keys.append(field.name)
        
    out = {}
    for attr in keys:
        value = getattr(obj, attr)
        if isinstance(value, models.Model):
            value = json.loads(tojson(value))
        out[attr] = value
    
#     return json.dumps(out, ensure_ascii=False)
    return out

class PaperDao(Paper):
    def getSimuList(self):
        items = Paper.objects.filter(name__contains='模拟试题')
        out = []
        for item in items:
            out.append(tojson(item))
#             str = tojson(item)
#             print(str)
#             print(type(item))
#             out.append(eval(str))

        return out
    
    def getSpecList(self):
        paper = Paper()
        items = paper.objects.exclude(name__contains='模拟试题')
        out = []
        for item in items:
            out.append(tojson(item))
        return out
    
    
class QuestionDao(Question):
    def getList(self, paperID):
        items = Question.objects.filter(paper_id=paperID)
        out = []
        for item in items:
            out.append(tojson(item))
        return out

    def getItem(self, paperID, questionID):
        print(paperID)
        print(questionID)
        items = Question.objects.filter(Q(paper_id=paperID, question_id=questionID))
        if(items is not None):
            for item in items:
                return tojson(item)

class AnswerDao(Answers):
    def getList(self, questionID):
        items = Answers.objects.filter(question_id=questionID)
        out = []
        for item in items:
            out.append(tojson(item))
        return out
