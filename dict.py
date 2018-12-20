import random

phonebook = {
    "치킨집":"02-000-0000",
    "피자집":"062-123-4567"
}
print(phonebook["치킨집"])

#가수그룹의 딕셔너리를 만들어주세요
#변수명: 그룹이름
#key:이름
#value :나이 (가상)

shinee = {
    "온유":"30",
    "종현":"29",
    "Key":"28",
    "민호":"28",
    "태민":"26"
}

winner = {
    "강승윤":20,
    "송민호":21,
    "김진우":22,
    "이승훈":23
}

#딕셔너리 안에 딕셔너리 넣기
idol = {
    "shinee":shinee,
    "winner":winner
}

# print(idol)
# print(idol["shinee"]["태민"])

score = {
    "수학":50,
    "국어":70,
    "영어":100
}

#딕셔너리 for문 돌리기
for key,value in score.items():
    # print(key)
    # print(value)
    pass

for key in score.keys():
    print(key)

for value in score.values():
    print(value)

score_sum = 0
for value in score.values():
    score_sum = score_sum + value
print(score_sum/3)


ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "python standard library": ["os", "random", "webbrowser"],
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"],
            "scrapying": ["requests", "bs4"],
        },
        "web" : ["HTML", "CSS"]
    },
    "classes": {
        "gj1":  {
            "lecturer": "ChangE",
            "manager": "pro1",
            "class president": "서희수",
            "groups": {
                "두드림": ["구종민", "김녹형", "윤은솔", "이준원", "이창훈"],
                "런치타임": ["문영국", "박나원","박희승", "서희수", "황인식"],
                "Friday": ["강민지", "박현진", "서상준", "안현상", "최진호"],
                "TMM": ["김훈", "송건희", "이지선", "정태준", "조호근"],
                "살핌": ["문동식", "이중봉", "이지희", "차상권", "최보균"]
            }
        },
        "gj2": {
            "lecturer": "teacher2",
            "manager": "pro2"
        },
        "gj3": {
            "lecturer": "teacher3",
            "manager": "pro3"
        }
    }
}
#1. ssafy를 진행하는 지역(location)은 몇 개 인가요?
print(len(ssafy["location"]))

#2. python standard library 'request'가 있나요??
#for문
request =["request"]

# for i in (len(set(ssafy["language"]["python"]["python standard library"])):
#     if(ssafy["language"]["python"]["python standard library"][i]==request[0]):
#         print



#3. gj1반의 반장의 이름을 출력하세요.
print(ssafy["classes"]["gj1"]["class president"])

# 4. ssafy에서 배우는 언어들을 출력하세요 : dictionary.keys활용
for key in score.keys():
    print(key)


# 5. ssafy gj2의 강사와 매니저의 이름을 출력하세요
    # 예시) teacher2
    #       pro2
# 6. framework들의 이름과 설명을 다음과 같이 출력하세요
    # 예시) 
    # flask는 micro이다.
    # django는 full-functioning이다.
# 7. 오늘 당번을 뽑기 위해 '살핌'조원중 1명을 랜덤으로 뽑아주세요
    # 예시)
    # 오늘 당번은 문동식입니다.