
from django.shortcuts import render
from experta import *
from django.views import View
import time 
from threading import Thread
from . import project_final as ps
from . import pop 

class get_answers_class(View):
    def get(self, request):
        thread = Thread(target=experta)
        thread.start() 
        time.sleep(500/1000)
        return render(request,'setup_finder_UI/ui.html', {'qustion':ps.qustion, 'answers':ps.answers}) 
    
    def post(self, request):
        ps.user_answer = request.POST.get('user_answer')
        time.sleep(500/1000)
        if ps.output != '':
            return render(request,'setup_finder_UI/output.html', {'output':ps.output})
        return render(request,'setup_finder_UI/ui.html', {'qustion':ps.qustion, 'answers':ps.answers})
    
    
def experta():
    print('experta started')
    ps.output = ''
    engine = ps.Project()
    engine.reset()
    engine.run()
    print('experta terminated')


