import json

def extractCol(colNm="movieCd",file_path="/home/root2/data/movies/year={year}/data.json"):
    with open(file_path) as f:
        data=json.load(f)

    return list(map(lambda x:x[colNm],data))
