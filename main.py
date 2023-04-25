import config
import requests
import pandas as pd


def fetch_data(search_key):
    """
    Fetches and shows search results from API.

    Args:
        search_key (str): a valid title string
    
    Returns:
        Returns result as dataframe

    """
    api_key=config.omdb_api_key
    url= f"http://www.omdbapi.com/?apikey={api_key}&s={search_key}&type=movie"
    try:
        response= requests.get(url)
        json_response= response.json()
        df= pd.json_normalize(json_response["Search"])
        print(df)
    except:
        print("API or Search Key ERROR!!")


def user_menu():
    """
    Menu for movie search
    
    """
    while True:
        print()
        print("WELCOME TO MOVIE RECOMMENDER SYSTEM")
        print("1. Search a movie")
        print("2. Exit")
        print()

        user_input= input("Enter an option: ")

        if user_input=="1":
            movie_title_input= input("Enter movie title: ")
            if(movie_title_input):
                fetch_data(movie_title_input)
                break
            else:
                print("Enter valid movie title!!")
        elif user_input=="2":
            break
        else:
            print("Enter valid input")


user_menu()
