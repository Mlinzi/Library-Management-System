import mysql.connector
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from tkcalendar import DateEntry

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System - By Ashrit N")

        self.root.minsize(width=400, height=200)
        
        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="yourpass",
            database="library_db"
        )
        self.cursor = self.db_connection.cursor()
        
        self.all_frames = self.create_frames()
        self.create_widgets()
        
        self.show_page(self.all_frames[0])  # Show the main frame
        self.clear_entry_widgets()

    def clear_entry_widgets(self):                                #To remove the data from the text boxes
        # Clear entry widgets in the add book frame
        self.entry_title.delete(0, tk.END)
        self.entry_author.delete(0, tk.END)
        self.entry_year.delete(0, tk.END)
        self.entry_genre.delete(0, tk.END)
        self.entry_copies.delete(0, tk.END)

        # Clear entry widgets in the add member frame
        self.entry_member_first_name.delete(0, tk.END)
        self.entry_member_last_name.delete(0, tk.END)
        self.entry_member_email.delete(0, tk.END)

        # Clear entry widgets in the add loan frame
        self.entry_loan_book_id.delete(0, tk.END)
        self.entry_loan_member_id.delete(0, tk.END)
        self.entry_loan_date.delete(0, tk.END)
        self.entry_due_date.delete(0, tk.END)

        # Clear entry widgets in the returned book frame
        self.entry_returned_loan_id.delete(0, tk.END)
        self.entry_returned_date.delete(0, tk.END)
    
    def create_frames(self):             # To create the frames used
        main_frame = tk.Frame(self.root)
        add_book_frame = tk.Frame(self.root)
        add_member_frame = tk.Frame(self.root)
        add_loan_frame = tk.Frame(self.root)
        returned_book_frame = tk.Frame(self.root)
        show_pending_loans_frame = tk.Frame(self.root)
        show_returned_books_frame = tk.Frame(self.root)
        show_all_books_frame = tk.Frame(self.root)
        show_all_members_frame = tk.Frame(self.root)
        
        return [main_frame, add_book_frame, add_member_frame, add_loan_frame,returned_book_frame ,show_pending_loans_frame, show_returned_books_frame, show_all_books_frame,show_all_members_frame]


    def create_widgets(self):                     # To create the widgets used
        # Main frame:
        # Create widgets for main frame
        self.button_add_book = tk.Button(self.all_frames[0], text="Add Book", command=lambda: self.show_page(self.all_frames[1]))
        self.button_add_member = tk.Button(self.all_frames[0], text="Add Member", command=lambda: self.show_page(self.all_frames[2]))
        self.button_add_loan = tk.Button(self.all_frames[0], text="Add Loan", command=lambda: self.show_page(self.all_frames[3]))
        self.button_show_pending_loans = tk.Button(self.all_frames[0], text="Show Pending Loans", command=lambda: (self.show_page(self.all_frames[5]), self.show_pending_loans()))
        self.button_show_returned_books = tk.Button(self.all_frames[0], text="Show Returned Books", command=lambda: (self.show_page(self.all_frames[6]), self.show_returned_books()))
        self.button_show_all_books = tk.Button(self.all_frames[0], text="Show All Books (And delete)", command=lambda: self.show_page(self.all_frames[7]))
        self.button_show_all_members = tk.Button(self.all_frames[0], text="Show All Members (And delete)", command=lambda: self.show_page(self.all_frames[8]))
        self.button_enter_returned_book = tk.Button(self.all_frames[0], text="Enter Returned Book", command=lambda: self.show_page(self.all_frames[4])) 
        # Pack the buttons on the main frame
        self.button_add_book.pack()
        self.button_add_member.pack()
        self.button_add_loan.pack()
        self.button_show_pending_loans.pack()
        self.button_show_returned_books.pack()
        self.button_show_all_books.pack()
        self.button_show_all_members.pack()
        self.button_enter_returned_book.pack() 

        # Create widgets for adding a book
        tk.Label(self.all_frames[1], text="Title").pack()
        self.entry_title = tk.Entry(self.all_frames[1])
        self.entry_title.pack()
        tk.Label(self.all_frames[1], text="Author").pack()
        self.entry_author = tk.Entry(self.all_frames[1])
        self.entry_author.pack()
        tk.Label(self.all_frames[1], text="Year").pack()
        self.entry_year = tk.Entry(self.all_frames[1])
        self.entry_year.pack()
        tk.Label(self.all_frames[1], text="Genre").pack()
        self.entry_genre = tk.Entry(self.all_frames[1])
        self.entry_genre.pack()
        tk.Label(self.all_frames[1], text="Copies").pack()
        self.entry_copies = tk.Entry(self.all_frames[1])
        self.entry_copies.pack()
        self.button_add_book_confirm = tk.Button(self.all_frames[1], text="Confirm", command=self.add_book)
        self.button_back_add_book = tk.Button(self.all_frames[1], text="Back", command=lambda: self.show_page(self.all_frames[0]))
        self.button_add_book_confirm.pack()
        self.button_back_add_book.pack()
        
        # Create widgets for adding a member
        tk.Label(self.all_frames[2], text="First Name").pack()
        self.entry_member_first_name = tk.Entry(self.all_frames[2])
        self.entry_member_first_name.pack()
        tk.Label(self.all_frames[2], text="Last Name").pack()
        self.entry_member_last_name = tk.Entry(self.all_frames[2])
        self.entry_member_last_name.pack()
        tk.Label(self.all_frames[2], text="Email").pack()
        self.entry_member_email = tk.Entry(self.all_frames[2])
        self.entry_member_email.pack()
        self.button_add_member_confirm = tk.Button(self.all_frames[2], text="Confirm", command=self.add_member)
        self.button_back_add_member = tk.Button(self.all_frames[2], text="Back", command=lambda: self.show_page(self.all_frames[0]))
        self.button_add_member_confirm.pack()
        self.button_back_add_member.pack()
        
        # Create widgets for adding a loan
        tk.Label(self.all_frames[3], text="Book ID").pack()
        self.entry_loan_book_id = tk.Entry(self.all_frames[3])
        self.entry_loan_book_id.pack()
        tk.Label(self.all_frames[3], text="Member ID").pack()
        self.entry_loan_member_id = tk.Entry(self.all_frames[3])
        self.entry_loan_member_id.pack()
        tk.Label(self.all_frames[3], text="Loan Date").pack()
        self.entry_loan_date = DateEntry(self.all_frames[3], date_pattern="yyyy-mm-dd")  # Specify date format
        self.entry_loan_date.pack()
        tk.Label(self.all_frames[3], text="Due Date").pack()
        self.entry_due_date = DateEntry(self.all_frames[3], date_pattern="yyyy-mm-dd")  # Specify date format
        self.entry_due_date.pack()
        self.button_add_loan_confirm = tk.Button(self.all_frames[3], text="Confirm", command=self.add_loan)
        self.button_back_add_loan = tk.Button(self.all_frames[3], text="Back", command=lambda: self.show_page(self.all_frames[0]))
        self.button_add_loan_confirm.pack()
        self.button_back_add_loan.pack()

        # Create widgets for the returned book frame
        tk.Label(self.all_frames[4], text="Loan ID").pack()
        self.entry_returned_loan_id = tk.Entry(self.all_frames[4])
        self.entry_returned_loan_id.pack()
        tk.Label(self.all_frames[4], text="Returned Date").pack()
        self.entry_returned_date = DateEntry(self.all_frames[4], date_pattern="yyyy-mm-dd")  # Specify date format
        self.entry_returned_date.pack()
        self.button_confirm_returned = tk.Button(self.all_frames[4], text="Confirm", command=self.enter_returned_book)
        self.button_confirm_returned.pack()
        self.button_back_returned = tk.Button(self.all_frames[4], text="Back", command=lambda: self.show_page(self.all_frames[0]))
        self.button_back_returned.pack()

        # Listbox for showing pending loans

        # Create a new frame for showing loans
        loans_frame = tk.Frame(self.root)
        self.all_frames.append(loans_frame)

        # Create a Treeview widget for showing loans and pending loans
        self.loans_tree = ttk.Treeview(self.all_frames[5], columns=("LoanID", "BookID", "MemberID", "LoanDate", "DueDate"), show="headings")
        self.loans_tree.heading("LoanID", text="Loan ID")
        self.loans_tree.heading("BookID", text="Book ID")
        self.loans_tree.heading("MemberID", text="Member ID")
        self.loans_tree.heading("LoanDate", text="Loan Date")
        self.loans_tree.heading("DueDate", text="Due Date")
        self.loans_tree.pack()
        # Button to go back
        self.button_back_show_pending_loans = tk.Button(self.all_frames[5], text="Back", command=lambda: self.show_page(self.all_frames[0]))
        self.button_back_show_pending_loans.pack()

        # Create Treeview widget for returned books
        self.returned_books_tree = ttk.Treeview(self.all_frames[6], columns=("LoanID", "BookID", "MemberID", "LoanDate", "DueDate", "ReturnedDate"), show="headings")
        self.returned_books_tree.heading("LoanID", text="Loan ID")
        self.returned_books_tree.heading("BookID", text="Book ID")
        self.returned_books_tree.heading("MemberID", text="Member ID")
        self.returned_books_tree.heading("LoanDate", text="Loan Date")
        self.returned_books_tree.heading("DueDate", text="Due Date")
        self.returned_books_tree.heading("ReturnedDate", text="Returned Date")
        self.returned_books_tree.pack()
        # Button to go back
        self.button_back_show_pending_loans = tk.Button(self.all_frames[6], text="Back", command=lambda: self.show_page(self.all_frames[0]))
        self.button_back_show_pending_loans.pack()

        # Create a Treeview widget for showing all books
        self.all_books_tree = ttk.Treeview(self.all_frames[7], columns=("ID", "Title", "Author", "Year", "Copies"), show="headings")
        self.all_books_tree.heading("ID", text="ID")
        self.all_books_tree.heading("Title", text="Title")
        self.all_books_tree.heading("Author", text="Author")
        self.all_books_tree.heading("Year", text="Year")
        self.all_books_tree.heading("Copies", text="Copies")
        self.all_books_tree.pack()

        self.update_all_books_list()    # Update the list ofbooks in the UI
        self.update_all_members_list()  # Update the list of members in the UI
        self.populate_authors_table()   # Update the list of authors in the db

        # displaying table is taken care of in show_all_books

        # Back button
        self.button_delete_book = tk.Button(self.all_frames[7], text="Delete Book", command=self.delete_selected_book)
        self.button_delete_book.pack()
        self.button_back_show_all_books = tk.Button(self.all_frames[7], text="Back", command=lambda: self.show_page(self.all_frames[0]))
        self.button_back_show_all_books.pack()

        # Create a Treeview widget for showing all members
        self.all_members_tree = ttk.Treeview(self.all_frames[8], columns=("MemberID", "FirstName", "LastName", "Email"), show="headings")
        self.all_members_tree.heading("MemberID", text="Member ID")
        self.all_members_tree.heading("FirstName", text="First Name")
        self.all_members_tree.heading("LastName", text="Last Name")
        self.all_members_tree.heading("Email", text="Email")
        self.all_members_tree.pack()

        self.update_all_members_list()

        self.button_delete_member = tk.Button(self.all_frames[8], text="Delete Member", command=self.delete_selected_member)
        self.button_delete_member.pack()

        # Button to go back
        self.button_back_show_all_members = tk.Button(self.all_frames[8], text="Back", command=lambda: self.show_page(self.all_frames[0]))
        self.button_back_show_all_members.pack()

        
    # Define functions to interact with the database
    def add_author(self, first_name, last_name):
        query = "INSERT INTO Authors (FirstName, LastName) VALUES (%s, %s)"
        values = (first_name, last_name)
        self.cursor.execute(query, values)
        self.db_connection.commit()
    
    def add_genre(self, genre_name):
        sql = "INSERT INTO Genres (GenreName) VALUES (%s)"
        values = (genre_name,)
        self.cursor.execute(sql, values)
        self.db_connection.commit()
        return self.cursor.lastrowid  # Get the auto-generated genre ID
    
    def add_book(self):
        title = self.entry_title.get()
        author = self.entry_author.get()
        year = self.entry_year.get()
        genres = self.entry_genre.get()  # Get the comma-separated string of genres
        copies = self.entry_copies.get()
        # Split genres into a list
        genre_list = [genre.strip() for genre in genres.split(',')]

        # Insert genres into Genres table and get their IDs
        genre_ids = []
        for genre in genre_list:
            genre_id = self.add_genre(genre)
            genre_ids.append(genre_id)

        # Insert book information along with genre IDs
        sql = "INSERT INTO Books (Title, Author, PublicationYear, CopiesAvailable, GenreID) VALUES (%s, %s, %s, %s, %s)"
        values = (title, author, year, copies, genre_ids[0])  # Use the first genre ID for now
        self.cursor.execute(sql, values)
        self.db_connection.commit()

        self.entry_title.delete(0, tk.END)
        self.entry_author.delete(0, tk.END)
        self.entry_year.delete(0, tk.END)
        self.entry_genre.delete(0, tk.END)
        self.entry_copies.delete(0, tk.END)

        self.update_all_books_list()
        messagebox.showinfo("Success", "Book added successfully!")

    def add_member(self):
        first_name = self.entry_member_first_name.get()
        last_name = self.entry_member_last_name.get()
        email = self.entry_member_email.get()
        
        query = "INSERT INTO Members (FirstName, LastName, Email) VALUES (%s, %s, %s)"
        values = (first_name, last_name, email)
        self.cursor.execute(query, values)
        self.db_connection.commit()

        self.update_all_members_list()

        messagebox.showinfo("Success", "Member added successfully!")
    
    def add_loan(self):
        book_id = self.entry_loan_book_id.get()
        member_id = self.entry_loan_member_id.get()
        loan_date = self.entry_loan_date.get()
        due_date = self.entry_due_date.get()

        sql = "INSERT INTO Loans (BookID, MemberID, LoanDate, DueDate) VALUES ( %s, %s, %s, %s)"
        values = ( book_id, member_id, loan_date, due_date)

        self.cursor.execute(sql, values)
        self.db_connection.commit()
        messagebox.showinfo("Success", "Loan added successfully!")

    def enter_returned_book(self):
        loan_id = self.entry_returned_loan_id.get()
        returned_date = self.entry_returned_date.get()

        if loan_id and returned_date:
            try:
                sql = "UPDATE Loans SET ReturnedDate = %s WHERE LoanID = %s"
                values = (returned_date, loan_id)
                self.cursor.execute(sql, values)
                self.db_connection.commit()
                messagebox.showinfo("Success", "Returned book information updated successfully!")
            except Exception as e:
                print("An error occurred while updating returned book information:", e)
        else:
            messagebox.showwarning("Warning", "Please enter both Loan ID and Returned Date.")

    def show_pending_loans(self):
        try:
            sql = "SELECT * FROM Loans WHERE ReturnedDate IS NULL"
            self.cursor.execute(sql)
            pending_loans = self.cursor.fetchall()

            # Clear the existing items in the Treeview
            self.loans_tree.delete(*self.loans_tree.get_children())

            for loan in pending_loans:
                self.loans_tree.insert("", "end", values=loan)
        except Exception as e:
            print("An error occurred:", e)

    def show_returned_books(self):
        try:
            sql = "SELECT * FROM Loans WHERE ReturnedDate IS NOT NULL"
            self.cursor.execute(sql)
            returned_books = self.cursor.fetchall()

            # Clear the existing items in the Treeview
            self.returned_books_tree.delete(*self.returned_books_tree.get_children())

            for book in returned_books:
                self.returned_books_tree.insert("", "end", values=book)
        except Exception as e:
            print("An error occurred:", e)
   
    def show_all_books(self):
        try:
            sql = "SELECT * FROM books"  
            self.cursor.execute(sql)
            all_books = self.cursor.fetchall()

            self.all_books_tree.delete(*self.all_books_tree.get_children())

            print(len(all_books))

            for book in all_books:
                book_data = book + ("",)                                           # Add an empty value for the delete button column
                self.all_books_tree.insert("", "end", values=book_data)
        except Exception as e:
            print("An error occurred:", e)

        # Add a column for the delete button
        self.all_books_tree.heading("#6", text="Delete")
 

    def delete_book(self, book_id):
        try:
            sql = "DELETE FROM Books WHERE BookID = %s"
            self.cursor.execute(sql, (book_id,))
            self.db_connection.commit()
            self.update_all_books_list()                                            # Update the list of books in the UI
            messagebox.showinfo("Success", "Book deleted successfully!")
        except Exception as e:
            print("An error occurred while deleting book:", e)

    def delete_selected_book(self):
        selected_item = self.all_books_tree.focus()
        if selected_item:
            book_id = self.all_books_tree.item(selected_item)['values'][0]
            self.delete_book(book_id)
        else:
            messagebox.showwarning("Warning", "Please select a book to delete.")

    def show_all_members(self):
        try:
            sql = "SELECT * FROM Members"
            self.cursor.execute(sql)
            all_members = self.cursor.fetchall()

            # Clear the existing items in the Treeview
            self.all_members_tree.delete(*self.all_members_tree.get_children())

            # Insert the updated list of members into the Treeview
            for member in all_members:
                self.all_members_tree.insert("", "end", values=member)
        except Exception as e:
            print("An error occurred while retrieving members:", e)

    def delete_member(self, member_id):
        try:
            sql = "DELETE FROM Members WHERE MemberID = %s"
            self.cursor.execute(sql, (member_id,))
            self.db_connection.commit()

            # Fetch the updated list of members
            self.update_all_members_list()

            messagebox.showinfo("Success", "Member deleted successfully!")
        except Exception as e:
            print("An error occurred while deleting member:", e)

    def delete_selected_member(self):
        try:
            selected_item = self.all_members_tree.focus()
            if selected_item:
                member_id = self.all_members_tree.item(selected_item)['values'][0]
                self.delete_member(member_id)
            else:
                messagebox.showwarning("Warning", "Please select a member to delete.")
        except Exception as e:
            print(e)


    def update_all_members_list(self):
        try:
            sql = "SELECT * FROM Members"
            self.cursor.execute(sql)
            all_members = self.cursor.fetchall()

            # Clear the existing items in the Treeview
            self.all_members_tree.delete(*self.all_members_tree.get_children())

            # Insert the updated list of members into the Treeview
            for member in all_members:
                self.all_members_tree.insert("", "end", values=member)
        except Exception as e:
            print("An error occurred:", e)

    def update_all_books_list(self):
        try:
            sql = "SELECT * FROM books"
            self.cursor.execute(sql)
            all_books = self.cursor.fetchall()

            # Clear the existing items in the Treeview
            self.all_books_tree.delete(*self.all_books_tree.get_children())

            # Insert the updated list of books into the Treeview
            for book in all_books:
                self.all_books_tree.insert("", "end", values=book)
        except Exception as e:
            print("An error occurred:", e)

    def populate_authors_table(self):
        try:
            # Get distinct author names from the Books table
            sql = "SELECT DISTINCT Author FROM books"
            self.cursor.execute(sql)
            distinct_authors = self.cursor.fetchall()

            for author in distinct_authors:
                # Check if the author already exists in the Authors table
                check_sql = "SELECT AuthorID FROM Authors WHERE CONCAT(FirstName, ' ', LastName) = %s"
                self.cursor.execute(check_sql, (author[0],))
                existing_author = self.cursor.fetchone()

                if not existing_author:
                    # Insert the author into the Authors table
                    author_name_parts = author[0].split(' ')
                    if len(author_name_parts) > 1:
                        first_name = author_name_parts[0]
                        last_name = ' '.join(author_name_parts[1:])
                    else:
                        first_name = author_name_parts[0]
                        last_name = ""

                    # Insert author into Authors table with the new AuthorID    
                    insert_sql = "INSERT INTO Authors (FirstName, LastName) VALUES (%s, %s)"
                    self.cursor.execute(insert_sql, (first_name, last_name))
                    self.db_connection.commit()
            print("Authors table populated successfully.")
        except Exception as e:
            print("An error occurred while populating Authors table:", e)

    def show_page(self, page):
        # Hide all frames
        for frame in self.all_frames:
            frame.pack_forget()
        
        # Show the selected frame
        page.pack()

        if page == self.all_frames[0]:
            self.clear_entry_widgets()

    def go_back(self):
        self.show_page(self.all_frames[0])
        self.update_all_members_list()




if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
