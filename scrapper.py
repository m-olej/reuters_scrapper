from bs4 import BeautifulSoup
import os
import sys
import uuid
from pathlib import Path


def print_scraped(limit: bool):
    separator = "<<SEPARATOR>>"
    new_article = "<<NEW_ARTICLE>>"
    dups = {}
    merge("articles")
    with open("merged_results", "r+") as f:
        file = f.read()
        count = 0
        articles = file.split(new_article)
        for a in articles:
            if a.strip() == "":
                continue
            title, desc = a.split(separator)[:-1]
            if title in dups.keys():
                continue
            if limit and desc.strip() == "no description":
                continue

            count += 1
            dups[title] = desc

            print(f"title: {title}")
            print(f"description: {desc}")
            print()
        print("Gather articles: ", count)
        print("Duplicates: ", len(dups.keys()) - count)


def merge(dir_path: str) -> None:
    abs_path = Path.resolve(Path(dir_path)).parent
    dir_path = f"{abs_path}/{dir_path}"
    print("Provided path: ", dir_path)

    with open("merged_results", "w+") as f:
        for article in os.listdir(dir_path):
            f.write(open(f"{dir_path}/{article}", "r").read())
            # f.write("<<SEPARATOR>><<NEW_ARTICLE>>")


def scrape():
    """
    Scrape all html files in /html
    """
    for html_source in os.listdir("html"):
        html = open(f"html/{html_source}").read()

        soup = BeautifulSoup(html, "html.parser")

        articles = []

        for article in soup.find_all("li", {"data-testid": "StoryCard"}):
            title_tag = article.find("span", {"data-testid": "TitleHeading"})
            desc_tag = article.find("p", {"data-testid": "Description"})

            if title_tag:
                title = title_tag.get_text(strip=True)
                if desc_tag:
                    desc = desc_tag.get_text(strip=True)
                else:
                    desc = "no description"

                articles.append({"title": title, "desc": desc})

        for article in soup.find_all("div", {"data-testid": "VisualStoryContainer"}):
            title_tag = article.find("a", {"data-testid": "VisualStoryHeadline"})
            desc_tag = article.find("p", {"data-testid": "VisualStorySynopsis"})

            if title_tag:
                title = title_tag.get_text(strip=True)
                if desc_tag:
                    desc = desc_tag.get_text(strip=True)
                else:
                    desc = "no description"

                articles.append({"title": title, "desc": desc})

        separator = "<<SEPARATOR>>"
        new_article = "<<NEW_ARTICLE>>"

        with open(f"articles/articles-{str(uuid.uuid4())}.txt", "+a") as f:
            for article in articles:
                f.write(f"{article['title']}{separator}")
                f.write(f"{article['desc']}{separator}")
                f.write(new_article)


if __name__ == "__main__":
    if "scrape" in sys.argv[1:]:
        scrape()
    limit = False
    if "limit" in sys.argv[1:]:
        limit = True
    merge("articles")
    print_scraped(limit)
