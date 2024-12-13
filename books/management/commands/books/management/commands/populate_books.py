from django.core.management.base import BaseCommand
from books.models import BookData


class Command(BaseCommand):
    help = "Populates the database with sample book data"

    def handle(self, *args, **kwargs):
        categories = [
            "Fiction", "Non-Fiction", "Science", "History",
            "Mystery", "Fantasy", "Biography", "Romance",
            "Thriller", "Poetry"
        ]

        books = [
            {"name": "1984", "category": "Science", "description": "A dystopian novel by George Orwell.",
             "rating": 4.8},
            {"name": "The Great Gatsby", "category": "Fiction",
             "description": "A novel written by F. Scott Fitzgerald.", "rating": 4.5},
            {"name": "To Kill a Mockingbird", "category": "Fiction", "description": "A novel by Harper Lee.",
             "rating": 4.9},
            {"name": "A Brief History of Time", "category": "Science", "description": "A book by Stephen Hawking.",
             "rating": 4.7},
            {"name": "The Catcher in the Rye", "category": "Fiction", "description": "A novel by J.D. Salinger.",
             "rating": 4.2},
            {"name": "The Da Vinci Code", "category": "Mystery", "description": "A mystery thriller by Dan Brown.",
             "rating": 4.3},
            {"name": "Pride and Prejudice", "category": "Romance", "description": "A novel by Jane Austen.",
             "rating": 4.6},
            {"name": "The Hobbit", "category": "Fantasy", "description": "A fantasy novel by J.R.R. Tolkien.",
             "rating": 4.8},
            {"name": "The Road", "category": "Fiction", "description": "A post-apocalyptic novel by Cormac McCarthy.",
             "rating": 4.4},
            {"name": "Steve Jobs", "category": "Biography", "description": "A biography by Walter Isaacson.",
             "rating": 4.7},
            {"name": "Becoming", "category": "Biography", "description": "A memoir by Michelle Obama.", "rating": 4.8},
            {"name": "The Shining", "category": "Thriller", "description": "A horror thriller by Stephen King.",
             "rating": 4.6},
            {"name": "Inferno", "category": "Mystery", "description": "A novel by Dan Brown.", "rating": 4.5},
            {"name": "The Alchemist", "category": "Fiction", "description": "A novel by Paulo Coelho.", "rating": 4.4},
            {"name": "The Art of War", "category": "History", "description": "An ancient Chinese military treatise.",
             "rating": 4.3},
            {"name": "The Odyssey", "category": "Poetry", "description": "An epic poem attributed to Homer.",
             "rating": 4.7},
            {"name": "Dune", "category": "Science", "description": "A science fiction novel by Frank Herbert.",
             "rating": 4.9},
            {"name": "Jane Eyre", "category": "Romance", "description": "A novel by Charlotte Brontë.", "rating": 4.5},
            {"name": "Gone Girl", "category": "Mystery", "description": "A thriller by Gillian Flynn.", "rating": 4.6},
            {"name": "The Iliad", "category": "Poetry", "description": "An epic poem attributed to Homer.",
             "rating": 4.6},
        ]

        for book in books:
            BookData.objects.create(
                name=book["name"],
                category=book["category"],
                description=book["description"],
                rating=book["rating"],
                image=None
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully populated the database with {len(books)} books!'))
