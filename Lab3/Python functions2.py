movies = [
    {
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
    },
    {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
    },
    {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
    },
    {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
    },
    {
        "name": "The Choice",
        "imdb": 6.2,
        "category": "Romance"
    },
    {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
    },
    {
        "name": "Love",
        "imdb": 6.0,
        "category": "Romance"
    },
    {
        "name": "Bride Wars",
        "imdb": 5.4,
        "category": "Romance"
    },
    {
        "name": "AlphaJet",
        "imdb": 3.2,
        "category": "War"
    },
    {
        "name": "Ringing Crime",
        "imdb": 4.0,
        "category": "Crime"
    },
    {
        "name": "Joking muck",
        "imdb": 7.2,
        "category": "Comedy"
    },
    {
        "name": "What is the name",
        "imdb": 9.2,
        "category": "Suspense"
    },
    {
        "name": "Detective",
        "imdb": 7.0,
        "category": "Suspense"
    },
    {
        "name": "Exam",
        "imdb": 4.2,
        "category": "Thriller"
    },
    {
        "name": "We Two",
        "imdb": 7.2,
        "category": "Romance"
    }
]


# Task 1
def rating(movies):
    for movie in movies:

        if movie['imdb'] > 5.5:
            print("True")
        else:
            print("False")


# Task 2
def rating2(movies):
    o = []
    for movie in movies:

        if movie['imdb'] > 5.5:
            o.append(movie["name"])

    print(o)


# Task 3
def category(movies):
    category1 = input()
    for movie in movies:

        if movie['category'] == category1:
            print(movie["name"])


# Task 4
def avarge(movies):
    avg = 0
    for movie in movies:
        avg += movie["imdb"]

    avg /= 15
    print(avg)


# Task 5
def avarge1(movies):
    category1 = input()
    avg = 0
    cnt = 0;
    for movie in movies:
        if movie["category"] == category1:
            avg += movie["imdb"]
            cnt += 1

    avg /= cnt
    print(avg)
