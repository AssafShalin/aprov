from pulsar import provider

def search(query):
    resp = provider.GET("http://pulsar.assafdev.mobi/", params={
        "q": query,
    })
    return resp.json()

def search_episode(episode):
    return search("%(title)s S%(season)02dE%(episode)02d" % episode)

def search_movie(movie):
    return search("%(title)s %(year)d" % movie)

provider.register(search, search_movie, search_episode)