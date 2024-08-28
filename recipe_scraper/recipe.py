class Nutrition:
    def __init__(self, kcal, fat, sat_fats, carbs, sugars, fibre, protein, salt):
        self.kcal = kcal
        self.fat = fat
        self.sat_fats = sat_fats
        self.carbs = carbs
        self.sugars = sugars
        self.fibre = fibre
        self.protein = protein
        self.salt = salt

    def to_dict(self):
        return {
            "kcal": self.kcal,
            "fat": self.fat,
            "sat_fats": self.sat_fats,
            "carbs": self.carbs,
            "sugars": self.sugars,
            "fibre": self.fibre,
            "protein": self.protein,
            "salt": self.salt,
        }

class Recipe:
    def __init__(self, name, author, description, nutrition, ingredients, method, time, difficulty, servings, image_url):
        self.name = name
        self.author = author
        self.description = description
        self.nutrition = nutrition
        self.ingredients = ingredients
        self.method = method
        self.time = time
        self.difficulty = difficulty
        self.servings = servings
        self.image_url = image_url

    def to_dict(self):
        return {
            "name": self.name,
            "author": self.author,
            "description": self.description,
            "nutrition": self.nutrition.to_dict(),
            "ingredients": self.ingredients,
            "method": self.method,
            "time": self.time,
            "difficulty": self.difficulty,
            "servings": self.servings,
            "image_url": self.image_url,
        }
