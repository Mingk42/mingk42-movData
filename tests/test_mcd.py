from movdata.mcd import save_movie_company

def test_movieCompanyDetail():
    rst=save_movie_company(0.1)
    assert rst
