#!/usr/bin/python3
"""Module to get posts from an API."""
import requests
import csv


url = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Get posts and print their titles."""

    response = requests.get(url)

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Get posts and save them in a CSV file."""

    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        with open("posts.csv", "w", newline="") as file:
            writer = csv.DictWriter(
                file, fieldnames=["id", "title", "body"]
            )

            writer.writeheader()

            for post in posts:
                writer.writerow({
                    "id": post["id"],
                    "title": post["title"],
                    "body": post["body"]
                })
