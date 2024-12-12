import requests as reqs
import os
import json
import time
from tqdm import tqdm

API_KEY=os.getenv("MOVIE_API_KEY")

def save_json(data, file_path):
    # file path mkdir
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w", encoding="utf8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


    return True


def req(url):
    resp = reqs.get(url)
    json = resp.json()
    return json


def save_movies(year, per_page=10, sleep_time=1):
    home_path = os.path.expanduser("~")
    file_path = f"{home_path}/data/movies/year={year}/data.json"
    
    baseUrl=f"https://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key={API_KEY}&openStartDt={year}&openEndDt={year}"

    print(f"{year}년 영화정보를 불러옵니다.")
    # 위 경로가 있으면 API 호출을 멈추고 프로그램 종료
    if os.path.exists(file_path):
        print(f"[Warning] 데이터가 이미 존재합니다: [File Path] {file_path}")
        print("영화정보 불러오기를 종료합니다.")
        return True

    # total cnt get, total_pages calc

    json=req(baseUrl+"&curPage=1")
    totCnt=json["movieListResult"]["totCnt"]
    total_pages = (totCnt // per_page) +1
    # loop in total pages, call api
    total_data=[]

    for page in tqdm(range(1, total_pages+1)):
        time.sleep(sleep_time)
        json=req(baseUrl+f"&curPage={page}")
        data=json["movieListResult"]["movieList"]
        total_data.extend(data)
        pass

    save_json(total_data, file_path)
    print("영화정보 불러오기를 종료합니다.")
    return True
