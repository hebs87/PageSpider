from urllib.request import urlopen


def load_urls_from_file(file_path: str):
    try:
        with open(file_path) as f:
            content = f.readline()
            return content
    except FileNotFoundError:
        print("The file " + file_path + " could not be found")
        exit(2)


def load_page(url: str):
    response = urlopen(url)
    html = response.read().decode('utf-8')
    return html


def scrape_page(page_contents: str):
    # TODO analyse the text
    pass
