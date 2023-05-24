import requests
import json

# from bs4 import BeautifulSoup
# from selenium import webdriver
# from urllib.request import urlopen
# from urllib.parse import quote_plus

API_KEY = 'd5b9c2045ac1632bce6b9299e5f11870'



def actors_data():
    actors = []
    lst = [
        10057315,10062025,10055626,10066899,10087814,20201026,10037018,10021341,10067353,10087253,
        10006171,20111688,10061467,10036883,10088975,10037291,10006380,10006537,10004466,10005276,
        10000558,10002387,20279929,20191126,20112070,10087751,20125838,10087280,10056670,10019065,
        10054128,10072251,10030016,20133966,10040874,20112885,10028667,10001901,10029474,10061252,
        10087820,10061581,20347172,20126329,20125801,20121022,20111341,10057469,20125794,10001919
        ]
    name_lst = [
        '이정재','정우성','이병헌','조인성','한혜진','김태리','송강호','마동석','조진웅','하정우',
        '김하늘','강하늘','전지현','손예진','현빈','송혜교','김혜수','김희애','김서형','김윤석',
        '강동원','권상우','남주혁','박보검','박은빈','한지민','김고은','하지원','이영애','류승룡',
        '유해진','최민식','배두나','천우희','심은경','강소라','박보영','공유','박해일','전도연',
        '한효주','정경호','이나영','박해진','김보라','조정석','이동욱','이준기','김수현','공효진',
        ]
    
    for i in range(len(lst)):
        url = f'http://kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleInfo.json?key={API_KEY}&peopleCd={lst[i]}'
        response = requests.get(url).json()
        result = response['peopleInfoResult']['peopleInfo']

        # key = quote_plus(name_lst[i])
        # key = name_lst[i]
        # search_url = f'https://www.google.com/search?q={key}&sxsrf=APwXEdcA04FOamFyF6Ikq-Qwo8QduROzXg:1684888865674&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiV_suS3Iz_AhVGQ94KHZSIBPQQ_AUoAXoECAEQAw&biw=871&bih=872&dpr=1.1'
        
        # driver = webdriver.Chrome('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --profile-directory="Profile 6"')
        # options = webdriver.ChromeOptions()
        # options.add_experimental_option('excludeSwitches',['enable-logging'])
        # driver.get(search_url)

        # html = urlopen(search_url)
        # html = requests.get(search_url).text
        # soup = bs(html, 'html.parser')
        # img = soup.find_all()
        
        # n = 0
        # while n < 1:
        #     for x in img:
        #         img_url = x['data-source']
        #         print(img_url)
        #         with urlopen(img_url) as f :
        #             with open('final_back/media/actors/' + str(key)+'.jpg','wb') as h: # w - write b - binary
        #                 img = f.read()
        #                 h.write(img)
        #     n += 1

        fields = {
            'code': result['peopleCd'],
            'name' : result['peopleNm'],
            'en_name':result['peopleNmEn'],
            'filmos': list(set(film['movieNm'] for film in result['filmos'])),
            'img': f'/actors/{name_lst[i]}.jpg',
        }
        data = {
            'pk': i+1,
            'model':'today.actor',
            'fields':fields
        }
        
        actors.append(data)

    w = open('today/fixtures/actors_list.json','w',encoding = 'utf-8')
    json.dump(actors, w, indent=4,ensure_ascii=False)


actors_data()

# def get_img():
#     lst = [
#         '이정재','정우성','이병헌','조인성','한혜진','김태리','송강호','마동석','조진웅','하정우',
#         '김하늘','강하늘','전지현','손예진','현빈','송혜교','김혜수','김희애','김서형','김윤석',
#         '강동원','권상우','남주혁','박보검','박은빈','한지민','김고은','하지원','이영애','류승룡',
#         '유해진','최민식','배두나','천우희','심은경','강소라','박보영','공유','박해일','전도연',
#         '한효주','정경호','이나영','박해진','김보라','조정석','이동욱','이준기','김수현','공효진',
#         ]
#     id_lst = []

#     # 이름 검색 결과로 id 반환
#     for name in lst:
#         search_url = f'https://api.themoviedb.org/3/search/person?api_key={API_KEY}&query={name}&language=ko&page=1'
#         response = requests.get(search_url).json()
#         id_lst.append(response['results']['id'])