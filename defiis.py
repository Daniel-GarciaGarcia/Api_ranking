import src.api as api 


def getUrl(url):

    print(f"Request Url{url}")
    res=request.get(f"https://github.com/ironhack-datalabs/datamad0820/pull/{url}")
    data=res.json
    return res

    memes= [getUrl(i) for i in range(1,400)]
    print(memes)