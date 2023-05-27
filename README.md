# libraries_database
Mock database of a library.

Database was created for university and educational purposes. Database is made up of 6 tables - members, employees, books, genres, loans and ratings in MariaDB DBMS. 

Data for tables members and employees were made with the help of Mockaroo on https://www.mockaroo.com/, while book data was downloaded from https://data.world/divyanshj/users-books-dataset and then shortened and modified to fit specific purposes. Extra data was randomly generated, including the genre of the book defined in genres table.

Data for tables loans and ratings was geerated via Python script also available on the repository. Data was inserted into the libraries database and exported as an SQL file.

The libary files are then modified into star shape for data warehouse and OLAP analysis purposes. Data warehouse consists of five tables - bookreturn, books, dates, employees and members. Those files can be found in the dw file.

Documentation of all processes is provided in a .pdf document. For now, it is solely in Croatian.
