import os
import urllib.request

class FileManager:

    @staticmethod
    def ensure_directories():
        """
        Ensures that the required directories are set up.
        """
        input_dir = "../data/input"
        output_dir = "../data/output"
        os.makedirs(input_dir, exist_ok=True)
        os.makedirs(output_dir, exist_ok=True)

    @staticmethod
    def download_recipes_csv():
        """
        Downloads the recipes.csv file if it doesn't exist.
        """
        filename = "../data/input/recipes.csv"
        if not os.path.isfile(filename):
            recipe_csv_url = "https://docs.google.com/spreadsheets/d/" \
                             "1l3vf7RfApXYlh1b1uMpExacXw4V6jJ0y3wr2yntM8ko/export?format=csv"
            urllib.request.urlretrieve(recipe_csv_url, filename)
            print("Downloaded recipes.csv")
        else:
            print("recipes.csv already exists")
