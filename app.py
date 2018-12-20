from flask import Flask,render_template,request
app = Flask(__name__)
import random
import requests ## 터미널에서 pip install requests
import json #json 사용시 임포트
from faker import Faker

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route('/lotto')
def lotto():
    #####로또번호 6개 랜덤 뽑기 코드
    num_list = range(1,46)
    pick = random.sample(num_list,6)#인자, 개수
    #당첨번호 api
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
    res = requests.get(url).text
    print("res:"+res)#터미널에 reponse[200] 찍힘 
    #출력 결과:{"totSellamnt":76614176000,"returnValue":"success","drwNoDate":"2018-12-15","firstWinamnt":3144449125,"drwtNo6":45,"drwtNo4":30,"firstPrzwnerCo":6,"drwtNo5":33,"bnusNo":6,"firstAccumamnt":18866694750,"drwNo":837,"drwtNo2":25,"drwtNo3":28,"drwtNo1":2}
    ##터미널에 python ->python코드 사용 가능
    ##타입 찾기 type()
    ##터미널로 다시 돌아오기 exit()
    
    print(type(res))
    lotto_dict = json.loads(res)# json 코드 res를  딕셔너리로 바꿔 읽어줘 
    #json코드를 보니 날짜 데이터는 "drwNoDate" 인 것을 확인
    print(lotto_dict["drwNoDate"]) #키값 확인2018-12-15
    
    #####당첨번호 들고오기 
    # #첫번째 당첨 번호 들고오기
    # num1 = lotto_dict["drwtNo1"]
    
    
    ###for문으로 당첨 번호 들고오기
    week_num = []    
    drwtNo = ["drwtNo1","drwtNo2","drwtNo3","drwtNo4","drwtNo5","drwtNo6"]
   
    for num in drwtNo:
        number = lotto_dict[num]
        week_num.append(number) #리스트 추가 함수
        print(week_num)
    
    
    ###for문 다른 방법
    week_format_num = []
    for i in range(1,7):
        #포맷팅 python String format
        #a = "오"
        #b = "창희"
        #"오{}".format(b)
        #결과 : 오창희
        
        #week_format_num 리스트에 "drwtNo{}".format(i)를  추가한다
        week_format_num.append(lotto_dict["drwtNo{}".format(i)])
        
    #pick = 우리가 생성한 번호
    #week_num  = 이번 주 당첨 번호
    #sorted()사용
    ####위의 두 값을 비교해서 로또 당첨 등수 출력
    #로또 1등 : 6개 2등:5개 3등:4개 4등:3개 5등:2개
    
    #
    t = 0 #맞은 개수
    f = 0  #틀린개수
    c = 6 #총개수 
    for a in range(1,7):
        for b in range(1,7):
            if(week_format_num[a-1]==pick[b-1]):
                t = t+1
            
    f = c-t #틀린 개수 = 총 개수 - 맞은개수
    print(t)
    print(f)
    
    
    rank = ["꼴등","5등","4등","3등","2등","1등"]
    j = ""
    for i in range(6):
        if (t==i):
            print(rank[i])
            j = str(rank[i])         
        
    #####pick을 mylotto에 담아 lotto.html에 전달
    return render_template("lotto.html",pick = pick, week_num = week_num,week_format_num = week_format_num,t=t, f=f,j = j) 

@app.route('/lottery')
def lottery():
    # 로또 정보를 가져온다
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
    res = requests.get(url).text
    lotto_dict = json.loads(res)
    
    # 1등 당첨 번호를 week 리스트에 넣는다.
    week = []
    for i in range(1,7):
        num = lotto_dict["drwtNo{}".format(i)]
        week.append(num)
    
    # 보너스 번호를 bonus 변수에 넣는다.
    bonus = lotto_dict["bnusNo"]
    
    # 임의의 로또 번호를 생성한다.
    pick = random.sample(range(1,46),6)
    pick = [2, 25, 28, 30, 33, 6]
    # 비교해서 몇등인지 저장한다.
    match = len(set(pick) & set(week))
    
    if match==6:
        text = "1등"
    elif match==5:
        if bonus in pick:
            text = "2등"
        else:
            text = "3등"
    elif match==4:
        text = "4등"
    else:
        text = "꽝"
    
    # 사용자에게 데이터를 넘겨준다.
    
    return render_template("lottery.html",pick=pick, week=week,text=text)

@app.route('/ping')
def ping():
    return render_template("ping.html")
    
@app.route('/pong')
def pong():
    #ping에서 이름 입력 받고, pong으로 전달 한 후  00님의 전생 직업은 랜덤 입니다. 페이지
    input_name = request.args.get('name')#가져오고싶은 변수 이름 #request임포트 추가
    
    #faker 외부 라이브버리 사용 : 가짜 정보를 랜덤하게  보여줌
    #https://pypi.org/project/Faker/
    ##터미널 설치 $ pip install Faker , 임포트
    
    fake = Faker('ko_KR')
    fake_job = fake.job()
    
    return render_template("pong.html",html_name = input_name, fake_job = fake_job)