from movdata.cli import ping
from movdata.ml import save_movies

def ping_test():
    rst=ping()
    assert rst=="pong"


def test_save_data():
    save_movies(year=2015, sleep_time=0.1)
    assert 1==1
