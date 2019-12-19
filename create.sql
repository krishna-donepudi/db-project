-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2019-12-07 01:21:33.616

-- tables
-- Table: Bookings
CREATE TABLE Bookings (
    booking_id serial  NOT NULL,
    check_in_date date  NOT NULL,
    check_out_date date  NOT NULL,
    price decimal(32,2)  NOT NULL,
    booking_status text  NOT NULL,
    updated_date date  NOT NULL DEFAULT CURRENT_DATE,
    guest_id int  NOT NULL,
    product_id int  NOT NULL,
    CONSTRAINT Bookings_pk PRIMARY KEY (booking_id)
);

-- Table: Experiences
CREATE TABLE Experiences (
    product_id int  NOT NULL,
    experience_type text  NOT NULL,
    CONSTRAINT Experiences_pk PRIMARY KEY (product_id)
);

-- Table: Guests
CREATE TABLE Guests (
    user_id int  NOT NULL,
    CONSTRAINT Guests_pk PRIMARY KEY (user_id)
);

-- Table: Hosts
CREATE TABLE Hosts (
    user_id int  NOT NULL,
    description text  NOT NULL,
    CONSTRAINT Hosts_pk PRIMARY KEY (user_id)
);

-- Table: Messages
CREATE TABLE Messages (
    message_id serial  NOT NULL,
    message_content text  NOT NULL,
    date date  NOT NULL DEFAULT CURRENT_DATE,
    time time  NOT NULL DEFAULT CURRENT_TIME,
    guest_id int  NOT NULL,
    host_id int  NOT NULL,
    CONSTRAINT Messages_pk PRIMARY KEY (message_id)
);

-- Table: Products
CREATE TABLE Products (
    product_id int  NOT NULL,
    title text  NOT NULL,
    description text  NOT NULL,
    address text  NOT NULL,
    available_from date  NOT NULL,
    available_to date  NOT NULL,
    max_guest_count int  NOT NULL,
    price decimal(32,2)  NOT NULL,
    city_state_country text  NOT NULL,
    host_id int  NOT NULL,
    CONSTRAINT Products_pk PRIMARY KEY (product_id)
);

-- Table: Properties
CREATE TABLE Properties (
    product_id int  NOT NULL,
    property_type text  NOT NULL,
    bedroom_count int  NOT NULL,
    bathroom_count int  NOT NULL,
    bed_count int  NOT NULL,
    CONSTRAINT Properties_pk PRIMARY KEY (product_id)
);

-- Table: Reviews
CREATE TABLE Reviews (
    guest_id int  NOT NULL,
    product_id int  NOT NULL,
    rating_score int  NOT NULL,
    comment text  NOT NULL,
    response text  NOT NULL,
    CONSTRAINT Reviews_pk PRIMARY KEY (guest_id,product_id)
);

-- Table: Saves
CREATE TABLE Saves (
    guest_id int  NOT NULL,
    product_id int  NOT NULL,
    saved_date date  NOT NULL DEFAULT CURRENT_DATE,
    saved_time time  NOT NULL DEFAULT CURRENT_TIME,
    CONSTRAINT Saves_pk PRIMARY KEY (guest_id,product_id)
);

-- Table: Users
CREATE TABLE Users (
    user_id int  NOT NULL,
    email text  NOT NULL,
    password text  NOT NULL,
    first_name text  NOT NULL,
    last_name text  NOT NULL,
    date_of_birth date  NOT NULL,
    contact_number bigint  NOT NULL,
    CONSTRAINT Users_pk PRIMARY KEY (user_id)
);

-- foreign keys
-- Reference: Bookings_Guests (table: Bookings)
ALTER TABLE Bookings ADD CONSTRAINT Bookings_Guests
    FOREIGN KEY (guest_id)
    REFERENCES Guests (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Experiences_Products (table: Experiences)
ALTER TABLE Experiences ADD CONSTRAINT Experiences_Products
    FOREIGN KEY (product_id)
    REFERENCES Products (product_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Guests_Users (table: Guests)
ALTER TABLE Guests ADD CONSTRAINT Guests_Users
    FOREIGN KEY (user_id)
    REFERENCES Users (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Hosts_Users (table: Hosts)
ALTER TABLE Hosts ADD CONSTRAINT Hosts_Users
    FOREIGN KEY (user_id)
    REFERENCES Users (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Messages_Guests (table: Messages)
ALTER TABLE Messages ADD CONSTRAINT Messages_Guests
    FOREIGN KEY (guest_id)
    REFERENCES Guests (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Messages_Hosts (table: Messages)
ALTER TABLE Messages ADD CONSTRAINT Messages_Hosts
    FOREIGN KEY (host_id)
    REFERENCES Hosts (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Products_Bookings (table: Bookings)
ALTER TABLE Bookings ADD CONSTRAINT Products_Bookings
    FOREIGN KEY (product_id)
    REFERENCES Products (product_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Products_Hosts (table: Products)
ALTER TABLE Products ADD CONSTRAINT Products_Hosts
    FOREIGN KEY (host_id)
    REFERENCES Hosts (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Properties_Products (table: Properties)
ALTER TABLE Properties ADD CONSTRAINT Properties_Products
    FOREIGN KEY (product_id)
    REFERENCES Products (product_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Reviews_Guests (table: Reviews)
ALTER TABLE Reviews ADD CONSTRAINT Reviews_Guests
    FOREIGN KEY (guest_id)
    REFERENCES Guests (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Reviews_Products (table: Reviews)
ALTER TABLE Reviews ADD CONSTRAINT Reviews_Products
    FOREIGN KEY (product_id)
    REFERENCES Products (product_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Saves_Guests (table: Saves)
ALTER TABLE Saves ADD CONSTRAINT Saves_Guests
    FOREIGN KEY (guest_id)
    REFERENCES Guests (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Saves_Products (table: Saves)
ALTER TABLE Saves ADD CONSTRAINT Saves_Products
    FOREIGN KEY (product_id)
    REFERENCES Products (product_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

