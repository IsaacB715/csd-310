CREATE DATABASE whatabook;

USE whatabook;

DROP USER IF EXISTS 'whatabook_user'@'localhost';

CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;


CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);


INSERT INTO store(locale)
    VALUES('648 Huntington Ave. Boston MA 02115-5912 USA');



INSERT INTO book(book_name, author, details)
    VALUES('Intro To NoSQL', 'Flynn Thomas', 'A beginners guide to NoSQL and data Structures');

INSERT INTO book(book_name, author, details)
    VALUES('Night Road', 'Jeanette Reader', 'Exploring the twentieth century');

INSERT INTO book(book_name, author, details)
    VALUES('The New Age', 'Timothy Miranda', 'A look into modern astronomy');

INSERT INTO book(book_name, author, details)
    VALUES('The Isand', 'Caitlan Andrade', 'A thrilling escape from an island controlled by pirates');

INSERT INTO book(book_name, author, details)
    VALUES('An Odd Place', 'Alan Calverts', 'Wandering through uninhabited land');

INSERT INTO book(book_name, author, details)
    VALUES("Advanced Python", 'Gilbert Storey', 'Advanced guide to python programming');

INSERT INTO book(book_name, author, details)
    VALUES('Networks', 'Mahira Allison', 'How networks operate');

INSERT INTO book(book_name, author, details)
    VALUES('The Last Meeting', 'Ned Rowley', 'Mysteries of an adventerous figure');

INSERT INTO book(book_name, author, details)
    VALUES('Shallow Spaces', 'Elina Kirk', 'How the mind operates');




INSERT INTO user(first_name, last_name) 
    VALUES('Jeffery', 'Hill');

INSERT INTO user(first_name, last_name)
    VALUES('Chance', 'Hull');

INSERT INTO user(first_name, last_name)
    VALUES('Rubi', 'Ashton');




INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Jeffery'), 
        (SELECT book_id FROM book WHERE book_name = 'Shallow Spaces')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Chance'),
        (SELECT book_id FROM book WHERE book_name = 'The New Age')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Rubi'),
        (SELECT book_id FROM book WHERE book_name = 'Intro To NoSQL')
    );
