from dataclasses import dataclass
from typing import List
from user import User


@dataclass
class Comment:
    comment: str
    user: User
    sub_comments = []


@dataclass
class Post:
    title: str
    description: str
    user: User
    comments = []
    karma: float = 0


class Community():
    def __init__(self, name):
        self.name = name
        self.posts = []
        self.founders = [User]
        print(f"Community Founded: {name}")

    def create_post(self, title: str, description: str, user: User):
        p = Post(title, description, user)
        print(f"Post Created in {self.name}: {title} by {user}")
        self.posts.append(p)
