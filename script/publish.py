import os
import sys

import frontmatter
import json
import requests

from dotenv import load_dotenv

load_dotenv()


def get_front_matter_from_md_file(path):
    post = frontmatter.load(path)
    keys = post.keys()

    with open(
        os.path.join(os.path.dirname(__file__), "article-template.json")
    ) as article_template:
        article = json.load(article_template)
        actual_article = article["article"]

    for k, v in actual_article.items():
        if k in keys:
            actual_article[k] = post[k].split(",") if k == "tags" else post[k]
    actual_article["body_markdown"] = post.content
    return article


def publish_to_dev(article):
    headers = {
        "Content-Type": "application/json",
        "api-key": os.getenv("API_KEY"),
    }
    response = requests.post(
        "https://dev.to/api/articles", headers=headers, data=article
    )
    return response.json()["id"]


def main():  # sourcery skip: avoid-builtin-shadow
    file_path = sys.argv[1]
    article = json.dumps(get_front_matter_from_md_file(file_path))
    id = publish_to_dev(article)
    result = json.loads(article)
    result["article"]["id"] = id
    published_article = file_path.replace(".md", ".json")
    with open(published_article, "w") as outfile:
        json.dump(result, outfile)
    print(f"Article posted to DEV.to and ID is: {id}")
    print(f"Published file: {published_article}")


if __name__ == "__main__":
    main()
