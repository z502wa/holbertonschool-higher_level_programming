#!/usr/bin/python3
# 10675@holbertonstudents.com
# Suhail Alaboud
"""
Module: task_02_requests
Functions to consume and process JSONPlaceholder posts
using Python's requests and csv modules.
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetch all posts from JSONPlaceholder and print status
    code and titles of each post.
    """
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get('title'))


def fetch_and_save_posts():
    """
    Fetch all posts from JSONPlaceholder and save selected
    fields (id, title, body) to a CSV file named posts.csv.
    """
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        fieldnames = ['id', 'title', 'body']
        with open('posts.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for post in posts:
                row = {key: post.get(key) for key in fieldnames}
                writer.writerow(row)
