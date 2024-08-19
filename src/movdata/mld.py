import requests as reqs
import os
import json
import time
from tqdm import tqdm

from movdata.utils import extractCol

API_KEY=os.getenv("MOVIE_API_KEY")

def save_json(data, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w", encoding="utf8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


    return True


def req(url):
    resp = reqs.get(url)
    json = resp.json()
    return json


def save_movies(year, sleep_time=1):
    home_path = os.path.expanduser("~")
    file_path = f"{home_path}/data/movies/movieDetail/year={year}/data.json"
    
    if os.path.exists(file_path):
        print(f"[Warning] 데이터가 이미 존재합니다: [File Path] {file_path}")
        print("영화상세정보 불러오기를 종료합니다.")
        return True

    movieCdList=extractCol(colNm="movieCd",file_path=f"{home_path}/data/movies/movieList/year={year}/data.json")
    total_data=[]
    """ 
    for code in tqdm(movieCdList):
        print(f"movieCd {code}의 영화상세정보를 불러옵니다.")
        baseUrl=f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={API_KEY}&movieCd={code}"
        json=req(baseUrl)
        data=json["movieInfoResult"]["movieInfo"]

        total_data.extend(data)
        time.sleep(sleep_time)
    """
    for i in tqdm(range(len(movieCdList))):
        print(f"[{year}년] movieCd {movieCdList[i]}의 영화상세정보를 불러옵니다.")
        baseUrl=f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={API_KEY}&movieCd={movieCdList[i]}"
        json=req(baseUrl)
        data=json["movieInfoResult"]["movieInfo"]

        total_data.extend(data)
        time.sleep(sleep_time)
    save_json(total_data, file_path)
    print("영화상세정보 불러오기가 모두 완료되었습니다.")
    
    return True


def call(sleep_time=1):
    home_path = os.path.expanduser("~")
    baseDir="/home/root2/data/movies/movieList/"
    yearDir=os.listdir(baseDir)

    for d in yearDir:
        s,y=d.split("=")
        save_movies(year=y,sleep_time=sleep_time)

    return True
