-- Create the database
CREATE DATABASE IF NOT EXISTS library_db;
USE library_db;

-- ------------------------------
-- Users table
-- ------------------------------
CREATE TABLE IF NOT EXISTS Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL
);

-- ------------------------------
-- Books table
-- ------------------------------
CREATE TABLE IF NOT EXISTS Books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    genre VARCHAR(100) NOT NULL
);

-- ------------------------------
-- Members table
-- ------------------------------
CREATE TABLE IF NOT EXISTS Members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    phone VARCHAR(20) NOT NULL
);

-- ------------------------------
-- Sample Data
-- ------------------------------

-- Users (password: password123)
INSERT INTO Users (username, password_hash) VALUES
('admin', '$pbkdf2-sha256$29000$Xw9yNw8kkPr1zSY/54nHtg$FqY7kZ/oSnU61ozTxE0xklTaI5M2Y//sB0oyElb3NY0'),
('john_doe', '$pbkdf2-sha256$29000$Xw9yNw8kkPr1zSY/54nHtg$FqY7kZ/oSnU61ozTxE0xklTaI5M2Y//sB0oyElb3NY0'),
('jane_smith', '$pbkdf2-sha256$29000$Xw9yNw8kkPr1zSY/54nHtg$FqY7kZ/oSnU61ozTxE0xklTaI5M2Y//sB0oyElb3NY0');

-- Books
INSERT INTO Books (title, author, genre) VALUES
('The Great Gatsby', 'F. Scott Fitzgerald', 'Classic'),
('1984', 'George Orwell', 'Dystopian'),
('To Kill a Mockingbird', 'Harper Lee', 'Classic'),
('Pride and Prejudice', 'Jane Austen', 'Romance'),
('The Catcher in the Rye', 'J.D. Salinger', 'Classic'),
('The Hobbit', 'J.R.R. Tolkien', 'Fantasy'),
('Moby-Dick', 'Herman Melville', 'Adventure'),
('War and Peace', 'Leo Tolstoy', 'Historical'),
('The Odyssey', 'Homer', 'Epic'),
('Crime and Punishment', 'Fyodor Dostoevsky', 'Philosophical');

-- Members
INSERT INTO Members (name, email, phone) VALUES
('Alice Johnson', 'alice@example.com', '123-456-7890'),
('Bob Smith', 'bob@example.com', '098-765-4321'),
('Carol Williams', 'carol@example.com', '555-123-4567'),
('David Brown', 'david@example.com', '555-987-6543'),
('Eva Davis', 'eva@example.com', '555-654-3210'),
('Frank Miller', 'frank@example.com', '555-321-0987'),
('Grace Lee', 'grace@example.com', '555-111-2222'),
('Hannah Wilson', 'hannah@example.com', '555-333-4444'),
('Ian Clark', 'ian@example.com', '555-555-6666'),
('Julia Lewis', 'julia@example.com', '555-777-8888');

select * from Books;
select * from Members;