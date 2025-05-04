import json
import time


class BookCollection:
    """A class to manage a collection of Novel/Comics"""

    def __init__(self):
        """Initialize a new book collection with an empty list and set up file storage."""
        self.book_list = []
        self.storage_file = "Novel_Comics_collection.json"
        self.read_from_file()

    def read_from_file(self):
        """Load saved books from a JSON file into memory.
        If the file doesn't exist or is corrupted, start with an empty collection."""
        try:
            with open(self.storage_file, "r") as file:
                self.book_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.book_list = []

    def save_to_file(self):
        """Store the current book collection to a JSON file for permanent storage."""
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent=4)

    def create_new_book(self):
        """Add a new book to the collection by gathering information from the user."""
        book_title = input("Enter book title: ")
        #validating if its empty
        if not book_title:
            print("Book title cannot be empty.")
            return
        book_author = input("Enter author: ")
        #validating if its empty
        if not book_author:
            print("How can author have no name?")
            return
        publication_year = input("Enter publication year: ")
        #validating if its number
        if not publication_year.isdigit():
            print("Invalid year. Please enter a valid number.")
            return
        book_genre = input("Enter genre: ")
        #validating if its empty
        if not book_genre:
            print("Genre cannot be empty.")
            return
        is_book_read = (
            input("Have you read this book? (yes/no): ").strip().lower() == "yes"
        )

        chapter_no = input("Enter the current chapter number: ")
        #validation if it is a number
        if not chapter_no.isdigit():
             print("Invalid chapter number. even if chapter contain name write chapter's number only.")
             return


        new_book = {
            "title": book_title,
            "author": book_author,
            "year": publication_year,
            "genre": book_genre,
            "read": is_book_read,
            "on_chapter": chapter_no
        }

        self.book_list.append(new_book)
        self.save_to_file()
        print("Book added successfully!\n")


    def delete_book(self):
        """Remove a book from the collection using its title."""
        book_title = input("Enter the title of the book to remove: ")

        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                self.book_list.remove(book)
                self.save_to_file()
                print("Book removed successfully!\n")
                return
        print("Book not found!\n")


    def find_book(self):
        """Search for books in the collection by title or author name."""
        search_type = print("Search by:\n1. Title\n2. Author\nEither are your choice: ") 
        time.sleep(0.3)#For good user experience
        search_text = input("Enter search term: ").lower() 
        found_books = [
            book
            for book in self.book_list
            if search_text in book["title"].lower()
            or search_text in book["author"].lower()
        ]

        if found_books:
            print("Matching Books:")
            for index, book in enumerate(found_books, 1):
                reading_status = "Read" if book["read"] else "Unread"
                print(
                f"""{index}. 
                Book name--------{book['title']}
                By---------------{book['author']}
                Release on-------{book['year']}
                Genre------------{book['genre']}
                Read-------------{reading_status}
                Current Chapter--{book['on_chapter']}"""
               )
                time.sleep(1) #add pause for good exprieance
        else:
            print("No matching books found.\n")
            time.sleep(1) #add pause for good exprieance


    def update_book(self):
        """update the details of an existing book in the collection."""
        book_title = input("Enter the title of the book you want to edit: ")
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                print("Leave blank to keep existing value.")
                book["title"] = input(f"New title ({book['title']}): ") or book["title"]
                book["author"] = (
                    input(f"New author ({book['author']}): ") or book["author"]
                )
                book["year"] = input(f"New year ({book['year']}): ") or book["year"]
                book["genre"] = input(f"New genre ({book['genre']}): ") or book["genre"]
                book["on_chapter"] = input(f"New chapter number ({book['on_chapter']}): ") or book["on_chapter"]
                book["read"] = (
                    input("Have you read this book? (yes/no): ").strip().lower()
                    == "yes"
                )
                self.save_to_file()
                print("Book updated successfully!\n")
                time.sleep(1) #add pause for good exprieance
                return
        print(f"Book {book_title} not found!\n")
        time.sleep(1) #add pause for good exprieance

    def show_all_books(self):
        """Display all books in the collection with their details."""
        if not self.book_list:
            print("Your collection is empty.\n")
            time.sleep(1) #add pause for good exprieance
            return

        print("Your Book Collection:")
        time.sleep(1) #add pause for good exprieance
        for index, book in enumerate(self.book_list, 1):
            reading_status = "Read" if book["read"] else "Unread"
            print(
                f"""{index}. 
                Book name--------{book['title']}
                By---------------{book['author']}
                Release on-------{book['year']}
                Genre------------{book['genre']}
                Read-------------{reading_status}
                Current Chapter--{book['on_chapter']}"""
                
            )
        time.sleep(1) #add pause for good exprieance

    def show_reading_progress(self):
        """Calculate and display statistics about your reading progress."""
        total_books = len(self.book_list)
        completed_books = sum(1 for book in self.book_list if book["read"])
        completion_rate = (
            (completed_books / total_books * 100) if total_books > 0 else 0
        )
        print(f"Total books in collection: {total_books}")
        print(f"Reading progress: {completion_rate:.2f}%\n")

    def start_app(self):
        """Run the main application."""
        while True:
            print("🪭🪭 Welcome to Your Novel/Comics Collection Manager! ")
            time.sleep(0.3) #add pause for good exprieance
            print("1. Add a new Novel/Comics")
            time.sleep(0.3) #add pause for good exprieance
            print("2. Remove a Novel/Comics")
            time.sleep(0.3) #add pause for good exprieance
            print("3. Search for Novel/Comics")
            time.sleep(0.3) #add pause for good exprieance
            print("4. Update Novel/Comics details")
            time.sleep(0.3) #add pause for good exprieance
            print("5. View all Novel/Comics")
            time.sleep(0.3) #add pause for good exprieance
            print("6. View reading Novel/Comics")
            time.sleep(0.3) #add pause for good exprieance
            print("7. Exit")
            time.sleep(0.3) #add pause for good exprieance
            user_choice = input("Please choose an option 1 - 7: ")


            if user_choice == "1":
                self.create_new_book()
            elif user_choice == "2":
                self.delete_book()
            elif user_choice == "3":
                self.find_book()
            elif user_choice == "4":
                self.update_book()
            elif user_choice == "5":
                self.show_all_books()
            elif user_choice == "6":
                self.show_reading_progress()
            elif user_choice == "7":
                self.save_to_file()
                print("\n")
                print("Updating in process...")
                time.sleep(2) #add pause for good exprieance
                print("Thanks for using Novel/Comics Collection Manager. Peace out!")
                break
            else:
                print("Invalid choice. Please try again. chose from 1 - 7\n")


if __name__ == "__main__":
    book_manager = BookCollection()
    book_manager.start_app()