"""
Midterm Practical Exam — Movie Collection Manager
Student: Selidio, Bea Bianca C.
"""

movies = []


def display_menu():
    print("1. Add a movie")
    print("2. View all movies")
    print("3. Count watched vs unwatched")
    print("4. Find a movie")
    print("5. Exit")

    input("Choose an option:")
    pass


def add_movie(movie_list):

    title = input("Enter movie title: ")
    director = input("Enter director: ")
    status = input("Enter watched or unwatched: ")
    
    movie = {
        "title": title,
        "director": director,
        "status": status,
    }
    movies.append(movie)
    print(f"\n'{title}' was added successfully!")    
    pass


def view_movies(movie_list):
    if not movies:
        print("\nYour movie collection is empty.")
        return
    
    print("\nYour Movie Collection") 
    for index, movie in enumerate(movies, start=1):
        print(f"{index}. {movie['title']} ({movie['status']}) - Dir: {movie['director']} ")
        pass

def status_movie(movie_list):
     if  watched:
            print("")
            return
        
        print("\nYour Movie Collection") 
    # loop through the list
    # count Watched vs Unwatched
    # return both counts
    pass


def find_movie():
    search_title = input("Enter the title to search: ").lower()
    found = [m for m in movies if search_title in m['title'].lower()]
    
    if found:
        print("\nSearch Results ")
        for movie in found:
            print(f"- {movie['title']} ({movie['status']}) | Director: {movie['director']}")
    else:
        print("\nNo matching movies found.")
    pass


def main():
    while True:
        print("\nMovie Collection Manager")
        print("1. Add a movie")
        print("2. View all movies")
        print("3. Count watched vs unwatched")
        print("4. Find a movie")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            add_movie()
        elif choice == '2':
            view_movies()
        elif choice == '3':
            status_movie()
        elif choice == '4':
            find_movie()
        elif choice == '5':
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please pick a number from 1 to 5.")
if __name__ == "main":
    pass


main()
