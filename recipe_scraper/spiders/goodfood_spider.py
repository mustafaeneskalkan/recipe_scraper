import scrapy
from recipe_scraper.utils import get_urls_from_csv
from recipe_scraper.recipe import Recipe, Nutrition

class GoodFoodSpider(scrapy.Spider):
    name = 'goodfood'

    def __init__(self, sample=0, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = get_urls_from_csv("../data/input/recipes.csv", sample)

    def parse(self, response):
        header = response.xpath('//div[contains(@class, "recipe-header")]')
        recipe_title = header.xpath('h1[contains(@class, "recipe-header__title")]/text()').get()
        attrib = header.xpath('//div[contains(@class, "recipe-header__chef")]/span/a/text()').get()
        img = header.xpath('//img[contains(@itemprop, "image")]/@src').get()
        description = header.xpath('//div[contains(@class, "recipe-header__description")]//text()').get()
        time = {
            "prep": {
                'hrs': header.xpath('//span[contains(@class, "recipe-details__cooking-time-prep")]/span[contains(@class, "hrs")]/text()').get(),
                'mins': header.xpath('//span[contains(@class, "recipe-details__cooking-time-prep")]/span[contains(@class, "mins")]/text()').get(),
            },
            "cook": {
                'hrs': header.xpath('//span[contains(@class, "recipe-details__cooking-time-cook")]/span[contains(@class, "hrs")]/text()').get(),
                'mins': header.xpath('//span[contains(@class, "recipe-details__cooking-time-cook")]/span[contains(@class, "mins")]/text()').get(),
            }
        }

        difficulty = header.xpath('//section[contains(@class, "recipe-details__item--skill-level")]/span[contains(@class, "recipe-details__text")]/text()').get()
        servings = header.xpath('//section[contains(@class, "recipe-details__item--servings")]/span[contains(@class, "recipe-details__text")]/text()').get()

        nutrition_list = header.xpath('//ul[contains(@class, "nutrition")]')
        nutrition_object = Nutrition(
            kcal=nutrition_list.xpath('//span[contains(@itemprop, "calories")]/text()').get(),
            fat=nutrition_list.xpath('//span[contains(@itemprop, "fatContent")]/text()').get(),
            sat_fats=nutrition_list.xpath('//span[contains(@itemprop, "saturatedFatContent")]/text()').get(),
            carbs=nutrition_list.xpath('//span[contains(@itemprop, "carbohydrateContent")]/text()').get(),
            sugars=nutrition_list.xpath('//span[contains(@itemprop, "sugarContent")]/text()').get(),
            fibre=nutrition_list.xpath('//span[contains(@itemprop, "fiberContent")]/text()').get(),
            protein=nutrition_list.xpath('//span[contains(@itemprop, "proteinContent")]/text()').get(),
            salt=nutrition_list.xpath('//span[contains(@itemprop, "sodiumContent")]/text()').get()
        )

        details = response.xpath('//div[contains(@class, "responsive-tabs")]')
        ingredients = details.xpath('section[contains(@id, "recipe-ingredients")]//div[contains(@class, "ingredients-list__content")]/ul/li/@content').getall()
        method = details.xpath('section[contains(@id, "recipe-method")]//div[contains(@class, "method")]/ol/li/p/text()').getall()

        recipe_object = Recipe(
            name=recipe_title,
            author=attrib,
            description=description,
            nutrition=nutrition_object,
            ingredients=ingredients,
            method=method,
            time=time,
            difficulty=difficulty,
            servings=servings,
            image_url=img
        )

        yield recipe_object.to_dict()
