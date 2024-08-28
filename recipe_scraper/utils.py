import csv

def get_urls_from_csv(data_path: str, sample=0):
    """
    Finds and returns a list of URLs from the recipes.csv dataset.
    :param data_path: path to the input csv list
    :param sample: if given, the function will return only n=sample urls
    :return: list of urls
    """
    bbc_urls = []
    with open(data_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if "www.bbcgoodfood.com" in row[0]:
                bbc_urls.append(row[0])
                if 0 < sample == len(bbc_urls):
                    break

    return bbc_urls
