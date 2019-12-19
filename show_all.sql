-- Users

\c airbnb


\! echo "Users table of all users";
SELECT *
  FROM Users;

-- Guests
\! echo "Table of guests of Airbnb";
SELECT *
  FROM Guests;

-- Hosts
\! echo "Table of hosts of Airbnb";
SELECT *
  FROM Hosts;

-- Products
\! echo "Table of all products that Airbnb offers";
SELECT *
  FROM Products;

-- Saves
\! echo "Table of all the saved products of all users";
SELECT *
  FROM Saves;

-- Bookings
\! echo "Table of all past bookings for Airbnb";
SELECT *
  FROM Bookings;

-- Properties
\! echo "Table of all products that are properties";
SELECT *
  FROM Properties;

-- Experiences
\! echo "Table of all products that are experiences";
SELECT *
  FROM Experiences;