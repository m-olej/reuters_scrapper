from bs4 import BeautifulSoup
import os


def print_scraped():
    separator = "<<SEPARATOR>>"
    new_article = "<<NEW_ARTICLE>>"

    with open("articles.txt", "r+") as f:
        file = f.read()
        count = 0
        articles = file.split(new_article)
        for a in articles:
            if a.strip() == "":
                continue
            count += 1
            title, desc = a.split(separator)[:-1]

            print(f"title: {title}")
            print(f"description: {desc}")
            print()
        print("Gathered articles: ", count)


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

        with open("articles.txt", "+a") as f:
            for article in articles:
                f.write(f"{article['title']}{separator}")
                f.write(f"{article['desc']}{separator}")
                f.write(new_article)


if __name__ == "__main__":
    scrape()
    print_scraped()
