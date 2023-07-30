from experta import *
import pandas as pd
import time 

qustion =  ''
answers = [] 
user_answer = None
output = ''
    
class Project(KnowledgeEngine):
    @Rule(NOT(Fact(Why=W())))
    def start(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'Why you want to buy this product?'  
        answers = ['Study', 'Social', 'Gaming', 'Business', 'ML server']
        self.why = user_input()
        self.declare(Fact(Why =self.why))
        user_answer = None
        
    
    @Rule(Fact(Why='1'),NOT(Fact(Do=W())))
    def q23(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'Do you care about touch screen?'
        answers = ['Yes', 'No'] 
        self.do = user_input()
        self.declare(Fact(Do =self.do))
        user_answer = None
        
    @Rule(Fact(Do='2'))
    def p20(self):
        global output
        output = 'The best device for you is Laptop'
        
    @Rule(Fact(Do='1'),NOT(Fact(What_n=W())))
    def q24(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'What is the nature of your usage?'
        answers = ['Heavy', 'Light', 'Medium', 'Don\'t know'] 
        self.what = user_input()
        self.declare(Fact(What_n =self.what))
        user_answer = None
    
    @Rule(Fact(What_n='1'))
    def p21(self):
        global output
        output = 'The best device for you is Laptop'
        
    @Rule(OR(Fact(What_n='2'),Fact(What_n='3')),NOT(Fact(screen_s=W())))
    def q25(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'What is the screen size you prefer?'  
        answers = ['<10', '10-14', '>14']
        self.s = user_input()
        self.declare(Fact(screen_s =self.s))
        user_answer = None

          
    @Rule(Fact(screen_s='3'))
    def p22(self):
        global output
        output = 'The best device for you is Laptop'
         
    @Rule(Fact(screen_s='1'))
    def p23(self):
        global output
        output = 'The best device for you is tablet'
        
    @Rule(Fact(screen_s='2'))
    def p24(self):
        global output
        output = 'The best devices for you are Laptop or tablet'
        
    @Rule(Fact(What_n='4'),NOT(Fact(work_n=W())))
    def q26(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'What is your working nature?'  
        answers = ['Browsing', 'Internet and document reading', 'Programing', 'Design']
        self.work = user_input()
        self.declare(Fact(work_n =self.work))
        user_answer = None

        
    @Rule(Fact(work_n='1'),NOT(Fact(screen_s=W())))
    def q27(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'What screen size you prefer?'  
        answers = ['<10', '10-14', '>14']
        self.s = user_input()
        self.declare(Fact(screen_s =self.s))
        user_answer = None
    
    @Rule(OR(Fact(work_n='2'),Fact(work_n='3')))
    def p25(self):
        global output
        output = 'The best device for you is Laptop'
    
    @Rule(Fact(Why='2'),NOT(Fact(Screen_s=W())))
    def q28(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'What screen size you prefer?'  
        answers = ['<7', '>7']
        self.S = user_input()
        self.declare(Fact(Screen_s =self.S))
        user_answer = None
    
    @Rule(Fact(Screen_s='1'))
    def p26(self):
        global output
        output = 'The best device for you is tablet'
            
    @Rule(Fact(Screen_s='2'))
    def p28(self):
        global output
        output = 'The best device for you is Laptop'
    
    @Rule(Fact(Why='3'),NOT(Fact(portabilitiy=W())))
    def q29(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'Do you care about Portability?'  
        answers = ['yes', 'no']
        self.p = user_input()
        self.declare(Fact(portabilitiy =self.p))
        user_answer = None
        
    @Rule(Fact(portabilitiy='1'))
    def p29(self):
        global output
        output = 'The best device for you is Laptop'
        
    @Rule(Fact(portabilitiy='2'),NOT(Fact(games=W())))
    def q30(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'What games you enjoy playing?'  
        answers = ['Storybased', 'Esport']
        self.g = user_input()
        self.declare(Fact(games =self.g))
        user_answer = None
        
    @Rule(Fact(games='1'),NOT(Fact(budget=W())))
    def q31(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'What is your budget?'  
        answers = ['800-1999', '2000-4000']
        self.b = user_input()
        self.declare(Fact(budget =self.b))
        user_answer = None
        
    @Rule(Fact(budget='1'))
    def p30(self):
        workbook = pd.read_excel('DeskTops.xlsx')
        cpu = [workbook['CPU'].loc[0]]
        gpu = [workbook['GPU'].loc[0]]
        ram = [workbook['RAM'].loc[0]]
        storage = [workbook['STORAGE'].loc[0]]
        df = pd.DataFrame({ 'cpu': cpu, 'gpu': gpu,'ram':ram,'storage':storage })
        df.index.name = 'ID'
        df.to_excel('output.xlsx')
        print('Your setup is ready on the Expert folder in an excel file named "output.xlsx"')
        
    @Rule(Fact(budget='2'))
    def p31(self):
        workbook = pd.read_excel('DeskTops.xlsx')
        cpu = [workbook['CPU'].loc[1]]
        gpu = [workbook['GPU'].loc[1]]
        ram = [workbook['RAM'].loc[1]]
        storage = [workbook['STORAGE'].loc[1]]
        df = pd.DataFrame({ 'cpu': cpu, 'gpu': gpu,'ram':ram,'storage':storage })
        df.index.name = 'ID'
        df.to_excel('output.xlsx')
        print('Your setup is ready on the Expert folder in an excel file named "output.xlsx"')
        
    @Rule(Fact(games='2'),NOT(Fact(budget=W())))
    def q32(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'What is your budget?'  
        answers = ['800-1999', '2000-4000']
        self.b = user_input()
        self.declare(Fact(budget =self.b))
        user_answer = None
        
    @Rule(Fact(budget='1'))
    def p32(self):
         workbook = pd.read_excel('DeskTops.xlsx')
         cpu = [workbook['CPU'].loc[2]]
         gpu = [workbook['GPU'].loc[2]]
         ram = [workbook['RAM'].loc[2]]
         storage = [workbook['STORAGE'].loc[2]]
         df = pd.DataFrame({ 'cpu': cpu, 'gpu': gpu,'ram':ram,'storage':storage })
         df.index.name = 'ID'
         df.to_excel('output.xlsx')
         print('Your setup is ready on the Expert folder in an excel file named "output.xlsx"')
          
    @Rule(Fact(budget='2'))
    def p33(self):
         workbook = pd.read_excel('DeskTops.xlsx')
         cpu = [workbook['CPU'].loc[3]]
         gpu = [workbook['GPU'].loc[3]]
         ram = [workbook['RAM'].loc[3]]
         storage = [workbook['STORAGE'].loc[3]]
         df = pd.DataFrame({ 'cpu': cpu, 'gpu': gpu,'ram':ram,'storage':storage })
         df.index.name = 'ID'
         df.to_excel('output.xlsx')
         print('Your setup is ready on the Expert folder in an excel file named "output.xlsx"')
    
    @Rule(Fact(Why='4'),NOT(Fact(DO=W())))
    def q33(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'Do you care about portability?'  
        answers = ['yes', 'no']
        self.do = user_input()
        self.declare(Fact(DO =self.do))
        user_answer = None
        
    @Rule(Fact(DO='1'))
    def p34(self):
        global output
        output = 'The best device for you is Laptop'
        
    @Rule(Fact(DO = '2'),NOT(Fact(wiyw = W())))
    def q1(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'What is your work?'  
        answers = ['Content Creator', 'Developer','Designer']
        self.wiyw = user_input()
        self.declare(Fact(wiyw = self.wiyw))
        user_answer = None


    @Rule(Fact(wiyw = '1'),NOT(Fact(wiyws = W())))
    def q2(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'What is your work specifically?'  
        answers = ['Video editing', 'Sound editing','Photo editing','Streamer']
        self.wiyws = user_input()
        self.declare(Fact(wiyws = self.wiyws))
        user_answer = None

    @Rule(Fact(wiyws = '1'),NOT(Fact(wsdyu = W())))
    def q3(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'What software do you use?' 
        answers = ['Final cut pro', 'Imovie','Sony vegas pro','Adobe premiere','Adobe after effects','Adobe premiere elements','Davinci resolve','Other',]
        self.wsdyu = user_input()
        self.declare(Fact(wsdyu = self.wsdyu))
        user_answer = None
    
    @Rule(OR(Fact(wsdyu = '1'),Fact(wsdyu = '2'),Fact(woywo = '1'),Fact(wsdyu2 = '1'),Fact(wsdyu2 = '2'),Fact(wsdyu3 = '1'),Fact(wsdyu3 = '2')),NOT(Fact(wiyb1 = W())))
    def q4(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'What is your budget?'  
        answers = ['500-999', '1000-1999','2000-4000']
        self.wiyb = user_input()
        self.declare(Fact(wiyb1 = self.wiyb))
        user_answer = None

    @Rule(Fact(wiyb1 = '1'))
    def p1(self):
        global output
        output = 'Mac Mini'
    
    @Rule(Fact(wiyb1 = '2'))
    def p2(self):
        global output
        output = 'Mac studio with M1 max'

    @Rule(Fact(wiyb1 = '3'))
    def p3(self):
        global output
        output = 'Mac studio with M1 ultra'

    @Rule(OR(Fact(wsdyu = '3'),Fact(wsdyu = '4'),Fact(wsdyu = '5'),Fact(wsdyu = '6'),Fact(woywo = '2'),Fact(dycau = '1'),Fact(dycaus = '1')),NOT(Fact(wiyb = W())))
    def q5(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'What is your budget?'  
        answers = ['1000-2499', '2500-5000']
        self.wiyb = user_input()
        self.declare(Fact(wiyb2 = self.wiyb))
        user_answer = None


    @Rule(Fact(wiyb2 = '1'))
    def p4(self):
        workbook = pd.read_excel('DeskTops.xlsx')
        cpu = [workbook['CPU'].loc[4]]
        gpu = [workbook['GPU'].loc[4]]
        ram = [workbook['RAM'].loc[4]]
        storage = [workbook['STORAGE'].loc[4]]
        df = pd.DataFrame({ 'cpu': cpu, 'gpu': gpu,'ram':ram,'storage':storage })
        df.index.name = 'ID'
        df.to_excel('output.xlsx')
        print('Your setup is ready on the Expert folder in an excel file named "output.xlsx"')
    
    @Rule(Fact(wiyb2 = '2'))
    def p5(self):
        global output
        output = 'Dell precision 3650'

    @Rule(OR(Fact(wsdyu = '7'),Fact(wsdyu = '8'),Fact(dycau = '2'),Fact(wsdyu2 = '7'),Fact(dycaus = '2'),Fact(wsdyu3 = '8')),NOT(Fact(woywo = W())))
    def q6(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'What OS you work on?'  
        answers = ['Mac', 'Windows']
        self.woywo = user_input()
        self.declare(Fact(woywo = self.woywo))
        user_answer = None

    
    @Rule(Fact(wiyws = '2'),NOT(Fact(wsdyu2 = W())))
    def q7(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'What software do you use?'  
        answers = ['Apple garageband ', 'Apple logic pro','Audacity','Adobe audition','Avid pro tools','Fl studio','Other']
        self.wsdyu = user_input()
        self.declare(Fact(wsdyu2 = self.wsdyu))
        user_answer = None


    @Rule(OR(Fact(wsdyu2 = '3'),Fact(wsdyu2 = '4'),Fact(wsdyu2 = '5'),Fact(wsdyu2 = '6')),NOT(Fact(dycau = W())))
    def q8(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'Do you care about upgrading specs?'  
        answers = ['yes', 'No','Dont know']
        self.dycau = user_input()
        self.declare(Fact(dycau = self.dycau))
        user_answer = None


    @Rule(Fact(wiyws = '3'),NOT(Fact(wsdyu3 = W())))
    def q9(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'What software do you use?'  
        answers = ['Apple photo', 'Pixelmator','Adobe photoshop','Adobe lightroom','DxO','Affinity','Luminar ai','Other']
        self.wsdyu = user_input()
        self.declare(Fact(wsdyu3 = self.wsdyu))
        user_answer = None


    @Rule(OR(Fact(wsdyu3 = '3'),Fact(wsdyu3 = '4'),Fact(wsdyu3 = '5'),Fact(wsdyu3 = '6'),Fact(wsdyu3 = '7')),NOT(Fact(dycaus = W())))
    def q10(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'Do you care about upgrading specs?'  
        answers = ['yes', 'no','dont know']
        self.dycaus = user_input()
        self.declare(Fact(dycaus = self.dycaus))
        user_answer = None


    @Rule(Fact(wiyws = '4'),NOT(Fact(dypwo = W())))
    def q11(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'Do you plan working on?'  
        answers = ['Beginner level', 'pro level']
        self.dypwo = user_input()
        self.declare(Fact(dypwo = self.dypwo))
        user_answer = None
    
    @Rule(Fact(dypwo = '1'),NOT(Fact(wiyb4 = W())))
    def q12(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'What is your budget?'  
        answers = ['1000-1999', '2000-3000']
        self.wiyb = user_input()
        self.declare(Fact(wiyb4 = self.wiyb))
        user_answer = None

    @Rule(Fact(wiyb4 = '1'))
    def p6(self):
        workbook = pd.read_excel('DeskTops.xlsx')
        cpu = [workbook['CPU'].loc[11]]
        gpu = [workbook['GPU'].loc[11]]
        ram = [workbook['RAM'].loc[11]]
        storage = [workbook['STORAGE'].loc[11]]
        df = pd.DataFrame({ 'cpu': cpu, 'gpu': gpu,'ram':ram,'storage':storage })
        df.index.name = 'ID'
        df.to_excel('output.xlsx')
        print('Your setup is ready on the Expert folder in an excel file named "output.xlsx"')

    @Rule(Fact(wiyb4 = '2'))
    def p7(self):
        workbook = pd.read_excel('DeskTops.xlsx')
        cpu = [workbook['CPU'].loc[12]]
        gpu = [workbook['GPU'].loc[12]]
        ram = [workbook['RAM'].loc[12]]
        storage = [workbook['STORAGE'].loc[12]]
        df = pd.DataFrame({ 'cpu': cpu, 'gpu': gpu,'ram':ram,'storage':storage })
        df.index.name = 'ID'
        df.to_excel('output.xlsx')
        print('Your setup is ready on the Expert folder in an excel file named "output.xlsx"')

    @Rule(Fact(dypwo = '2'),NOT(Fact(wiyb5 = W())))
    def q13(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'What is your budget?'  
        answers = ['1500-2999', '3000-5000']
        self.wiyb = user_input()
        self.declare(Fact(wiyb5 = self.wiyb))
        user_answer = None

    @Rule(Fact(wiyb5 = '1'))
    def p8(self):
        workbook = pd.read_excel('DeskTops.xlsx')
        cpu = [workbook['CPU'].loc[10]]
        gpu = [workbook['GPU'].loc[10]]
        ram = [workbook['RAM'].loc[10]]
        storage = [workbook['STORAGE'].loc[10]]
        df = pd.DataFrame({ 'cpu': cpu, 'gpu': gpu,'ram':ram,'storage':storage })
        df.index.name = 'ID'
        df.to_excel('output.xlsx')
        print('Your setup is ready on the Expert folder in an excel file named "output.xlsx"')

    @Rule(Fact(wiyb5 = '2'))
    def p9(self):
        workbook = pd.read_excel('DeskTops.xlsx')
        cpu = [workbook['CPU'].loc[9]]
        gpu = [workbook['GPU'].loc[9]]
        ram = [workbook['RAM'].loc[9]]
        storage = [workbook['STORAGE'].loc[9]]
        df = pd.DataFrame({ 'cpu': cpu, 'gpu': gpu,'ram':ram,'storage':storage })
        df.index.name = 'ID'
        df.to_excel('output.xlsx')
        print('Your setup is ready on the Expert folder in an excel file named "output.xlsx"')

    @Rule(Fact(wiyw = '2'),NOT(Fact(wiyws2 = W())))
    def q14(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'What is your work specifically?'  
        answers = ['Web Developer', 'Mobile Developer','Desktop app Developer','Video games Developer']
        self.wiyws2 = user_input()
        self.declare(Fact(wiyws2 = self.wiyws2))
        user_answer = None

    @Rule(Fact(wiyws2 = '1'),NOT(Fact(wodyp = W())))
    def q15(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'what os do you perfer?'  
        answers = ['Mac', 'Windows']
        self.wodyp = user_input()
        self.declare(Fact(wodyp = self.wodyp))
        user_answer =  None
    
    @Rule(OR(Fact(wodyp = '1'),Fact(wiyws2 = '2'),Fact(waygtd = '2')),NOT(Fact(wiyb6 = W())))
    def q16(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'What is your budget?'  
        answers = ['500-1000', '1000-2000']
        self.wiyb = user_input()
        self.declare(Fact(wiyb6 = self.wiyb))
        user_answer = None

    @Rule(Fact(wiyb6 = '1'))
    def p10(self):
        global output
        output = 'Mac Mini'

    @Rule(Fact(wiyb6 = '2'))
    def p11(self):
        global output
        output = 'Mac Studio with M1 max'
    
    @Rule(OR(Fact(wodyp = '2'),Fact(waygtd = '1')),NOT(Fact(wiyb7 = W())))
    def q17(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'What is your budget?'  
        answers = ['1000-1999', '2000-4000']
        self.wiyb = user_input()
        self.declare(Fact(wiyb7 = self.wiyb))
        user_answer=None

    @Rule(Fact(wiyb7 = '1'))
    def p12(self):
        global output
        output = 'HP pavilion Desktop TP01-1065HZ'

    @Rule(Fact(wiyb7 = '2'))
    def p13(self):
        global output
        output = 'HP Z4 G4 Workstation'

    @Rule(Fact(wiyws2 = '3'),NOT(Fact(waygtd = W())))
    def q18(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'What are you going to develop?'  
        answers = ['Windows app', 'Mac app']
        self.waygtd = user_input()
        self.declare(Fact(waygtd = self.waygtd))
        user_answer=None

    @Rule(Fact(wiyws2 = '4'),NOT(Fact(wgaygtd = W())))
    def q19(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'What games are you going to develop?'  
        answers = ['AAA', 'Indie']
        self.wgaygtd = user_input()
        self.declare(Fact(wgaygtd = self.wgaygtd))
        user_answer=None

    @Rule(Fact(wgaygtd = '1'),NOT(Fact(wiyb8 = W())))
    def q20(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'What is your budget?'  
        answers = ['2500-3499', '3500-4500']
        self.wiyb = user_input()
        self.declare(Fact(wiyb8 = self.wiyb))
        user_answer = None
    
    @Rule(Fact(wiyb8 = '1'))
    def p14(self):
        workbook = pd.read_excel('DeskTops.xlsx')
        cpu = [workbook['CPU'].loc[13]]
        gpu = [workbook['GPU'].loc[13]]
        ram = [workbook['RAM'].loc[13]]
        storage = [workbook['STORAGE'].loc[13]]
        df = pd.DataFrame({ 'cpu': cpu, 'gpu': gpu,'ram':ram,'storage':storage })
        df.index.name = 'ID'
        df.to_excel('output.xlsx')
        print('Your setup is ready on the Expert folder in an excel file named "output.xlsx"')
    
    @Rule(Fact(wiyb8 = '2'))
    def p15(self):
        workbook = pd.read_excel('DeskTops.xlsx')
        cpu = [workbook['CPU'].loc[14]]
        gpu = [workbook['GPU'].loc[14]]
        ram = [workbook['RAM'].loc[14]]
        storage = [workbook['STORAGE'].loc[14]]
        df = pd.DataFrame({ 'cpu': cpu, 'gpu': gpu,'ram':ram,'storage':storage })
        df.index.name = 'ID'
        df.to_excel('output.xlsx')
        print('Your setup is ready on the Expert folder in an excel file named "output.xlsx"')

    @Rule(Fact(wgaygtd = '2'),NOT(Fact(wiyb9 = W())))
    def q21(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'What is your budget?'  
        answers = ['800-1499', '1500-2200']
        self.wiyb = user_input()
        self.declare(Fact(wiyb9 = self.wiyb))
        user_answer=None
    
    @Rule(Fact(wiyb9 = '1'))
    def p16(self):
        workbook = pd.read_excel('DeskTops.xlsx')
        cpu = [workbook['CPU'].loc[8]]
        gpu = [workbook['GPU'].loc[8]]
        ram = [workbook['RAM'].loc[8]]
        storage = [workbook['STORAGE'].loc[8]]
        df = pd.DataFrame({ 'cpu': cpu, 'gpu': gpu,'ram':ram,'storage':storage })
        df.index.name = 'ID'
        df.to_excel('output.xlsx')
        print('Your setup is ready on the Expert folder in an excel file named "output.xlsx"')
    
    @Rule(Fact(wiyb9 = '2'))
    def p17(self):
        workbook = pd.read_excel('DeskTops.xlsx')
        cpu = [workbook['CPU'].loc[15]]
        gpu = [workbook['GPU'].loc[15]]
        ram = [workbook['RAM'].loc[15]]
        storage = [workbook['STORAGE'].loc[15]]
        df = pd.DataFrame({ 'cpu': cpu, 'gpu': gpu,'ram':ram,'storage':storage })
        df.index.name = 'ID'
        df.to_excel('output.xlsx')
        print('Your setup is ready on the Expert folder in an excel file named "output.xlsx"')

    @Rule(Fact(wiyw = '3'),NOT(Fact(wiyb10 = W())))
    def q22(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'What is your budget?'  
        answers = ['1000-2499', '2500-5000']
        self.wiyb = user_input()
        self.declare(Fact(wiyb10 = self.wiyb))
        user_answer=None

    @Rule(Fact(wiyb10 = '1'))
    def p18(self):
        workbook = pd.read_excel('DeskTops.xlsx')
        cpu = [workbook['CPU'].loc[4]]
        gpu = [workbook['GPU'].loc[4]]
        ram = [workbook['RAM'].loc[4]]
        storage = [workbook['STORAGE'].loc[4]]
        df = pd.DataFrame({ 'cpu': cpu, 'gpu': gpu,'ram':ram,'storage':storage })
        df.index.name = 'ID'
        df.to_excel('output.xlsx')
        print('Your setup is ready on the Expert folder in an excel file named "output.xlsx"')

    @Rule(Fact(wiyb10 = '2'))
    def p19(self):
        global output
        output = 'Dell precision 3650'

    @Rule(Fact(Why='5'),NOT(Fact(hliyb=W())))
    def mlq1(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'How large is your business?'  
        answers = ['small-medium', 'Large']
        self.hliyb = user_input()
        self.declare(Fact(hliyb =self.hliyb))
        user_answer=None

    @Rule(Fact(hliyb='1'),NOT(Fact(dyharic=W())))
    def mlq2(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'Do you have a reliable internet connection?'  
        answers = ['No', 'Yes']
        self.dyharic = user_input()
        self.declare(Fact(dyharic =self.dyharic))
        user_answer=None

    @Rule(Fact(dyharic='1'),NOT(Fact(wiyb11=W())))
    def mlq3(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'What is your budget?'  
        answers = ['1000-1499', '1500-2000']
        self.wiyb11 = user_input()
        self.declare(Fact(wiyb11 =self.wiyb11))
        user_answer=None

    @Rule(Fact(wiyb11='1'))
    def MLOutput1(self):
        global output
        output = 'Output1'
    
    @Rule(Fact(wiyb11='2'))
    def MLOutput2(self):
        global output
        output = 'Output2'

    @Rule(Fact(dyharic='2'),NOT(Fact(dycac=W())))
    def mlq4(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'Do you care about confidentiality?'  
        answers = ['No', 'Yes']
        self.dycac = user_input()
        self.declare(Fact(dycac =self.dycac))
        user_answer=None

    @Rule(OR(Fact(dycac='1'),Fact(dywalsoccs='2')),NOT(Fact(iadity=W())))
    def mlq5(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'Is anomaly detection important to you?'  
        answers = ['No', 'Yes']
        self.iadity = user_input()
        self.declare(Fact(iadity =self.iadity))
        user_answer=None

    @Rule(Fact(iadity='1'),NOT(Fact(dycacar=W())))
    def mlq6(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'Do you care about clustering and recommendation?'  
        answers = ['No', 'Yes']
        self.dycacar = user_input()
        self.declare(Fact(dycacar =self.dycacar))
        user_answer=None
        
    @Rule(Fact(dycacar='1'))
    def MLOutput3(self):
        global output
        output = 'Amazon ML or Microsoft Azura or Google AI or IBM Watson'
    

    @Rule(Fact(dycacar='2'))
    def MLOutput4(self):
        global output
        output = 'Amazon ML or Microsoft Azura or Google AI'

    @Rule(Fact(iadity='2'))
    def MLOutput5(self):
        global output
        output = 'Amazon ML or Microsoft Azura'

    @Rule(Fact(dycac='2'),NOT(Fact(wiyb12=W())))
    def mlq7(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'What is your budget?'  
        answers = ['1000-1499', '1500-2000']
        self.wiyb12 = user_input()
        self.declare(Fact(wiyb12 =self.wiyb12))
        user_answer=None

    @Rule(Fact(wiyb12='1'))
    def MLOutput6(self):
        global output
        output = 'Output3'
    
    @Rule(Fact(wiyb12='2'))
    def MLOutput7(self):
        global output
        output = 'Output4'

    @Rule(Fact(hliyb='2'),NOT(Fact(dywalsoccs=W())))
    def mlq8(self):
        global qustion 
        global answers
        global user_answer
        qustion =  'Do you want a local server or cloud computing service?'  
        answers = ['Local', 'Cloud service']
        self.dywalsoccs = user_input()
        self.declare(Fact(dywalsoccs =self.dywalsoccs))
        user_answer=None

    @Rule(Fact(dywalsoccs='1'))
    def MLOutput8(self):
        global output
        output = 'Output sites'
    


def user_input():
    global user_answer
    time.sleep(500/1000)
    if user_answer != None:
        return user_answer
    return user_input()


#wiyw What is your work
#wiyws What is your work specifically
#wsdyu What software do you use 
#wiyb What is your budget
#woywo What OS you work on
#dycau do you care about upgrading 
#dycaus do you care about upgrading specs
#dypwo do you plan working on 
#wodyp what os do you perfer
#waygtd what are you going to develop
#wgaygtd what games are you going to develop
#dyharic do you have a reliable internet connection
#dycac Do you care about confidentiality
#iadity is anomaly detection important to you 
#dycacar Do you care about clustering and recommendation
#hliyb How large is your business
#dywalsoccs Do you want a local server or cloud computing service