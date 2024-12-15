

def find_possible_movies(movies):

    movies.sort(key = lambda movie: movie['ending_hour'])
    
    ans = []
    end_time = 0
    


    for movie in movies:

        start = movie['starting_hour']
        end = movie['ending_hour']

        if start >= end_time:
            ans.append(movie)
            end_time = end
    


    return ans



my_movies = [
    {"name": "Inception", "starting_hour": 0, "ending_hour": 140},  
    {"name": "The Dark Knight", "starting_hour": 80, "ending_hour": 200},  
    {"name": "Interstellar", "starting_hour": 180, "ending_hour": 380},  
    {"name": "Tenet", "starting_hour": 380, "ending_hour": 500},  
    {"name": "Parasite", "starting_hour": 520, "ending_hour": 650},  
    {"name": "La La Land", "starting_hour": 600, "ending_hour": 770}, 
    {"name": "The Matrix", "starting_hour": 770, "ending_hour": 900},  
]



result = find_possible_movies(my_movies)



print("Max movies:", len(result))
print("Movies:", [movie['name'] for movie in result])