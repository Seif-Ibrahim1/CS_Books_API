from django.core.management.base import BaseCommand
from core.models import Author, Book
import requests


class Command(BaseCommand):
    help = 'Retrieve and add books to the database'

    def handle(self, *args, **kwargs):
        BASE_URL = "https://www.googleapis.com/books/v1/volumes"

        keywords = [
            "computer science",
            "software engineering",
            "front-end development",
            "back-end development",
            "mobile app development",
            "data science",
            "artificial intelligence",
            "machine learning",
            "algortihms",
            "data structure",
            "computer security",
            "computer architecture",
            "Computer vision",
            "cloud computing",
            "computer networks",
            "image processing",
        ]

        for keyword in keywords:
            query = keyword

            fields = "items(volumeInfo/title,volumeInfo/description,volumeInfo/publishedDate,volumeInfo/imageLinks, volumeInfo/authors)&maxResults=40"

            url = f"{BASE_URL}?q={query}&fields={fields}"

            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                for book in data.get("items", []):
                    volume_info = book.get("volumeInfo", {})
                    title = volume_info.get("title", "Title not available")
                    description = volume_info.get("description", "Description not available")
                    published_date = volume_info.get("publishedDate", "Publication date not available")
                    if published_date[0] != 'P':
                        published_date = int(published_date[:4])
                    else:
                        published_date = None

                    image_links = volume_info.get("imageLinks", {})
                    thumbnail = image_links.get("thumbnail", "Thumbnail not available")
                    authors = volume_info.get("authors", [])
                    
                    author_objects = []
                    for author_name in authors:
                        existing_author = Author.objects.filter(name=author_name).first()
                        if existing_author is None:
                            author = Author.objects.create(name=author_name)
                            author_objects.append(author)
                        else:
                            author_objects.append(existing_author)

                    existing_book = Book.objects.filter(title=title).first()

                    if existing_book is None:
                        book_object = Book.objects.create(
                            title=title,
                            description=description,
                            publication_year=published_date,
                            thumbnail_url=thumbnail,
                        )
                        book_object.authors.set(author_objects)

                        book_object.save()
            else:
                print(f"Error: {response.status_code}")