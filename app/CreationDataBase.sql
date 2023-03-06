
CREATE TABLE Tools(
itemID INTEGER PRIMARY KEY AUTOINCREMENT,
item TEXT NOT NULL,
catagory TEXT, 
vis_test TEXT,
pat_test TEXT,
donated_by TEXT,
date_listed DATE NOT NULL,
picture BLOB,
ppe_needed BOOLEAN,
Restriced_item BOOLEAN,
training_needed BOOLEAN
);

CREATE TABLE Users(
userName TEXT PRIMARY KEY,
password TEXT NOT NULL,
name TEXT NOT NULL,
address TEXT NOT NULL,
phoneNumber TEXT,
email TEXT,
admin_access BOOLEAN,
Restriced_view BOOLEAN,
Training_done BOOLEAN
);

CREATE TABLE Bookings (
BookingID INTEGER PRIMARY KEY AUTOINCREMENT,
userName TEXT NOT NULL,
itemID INTEGER NOT NULL,
Booked_for_day DATE NOT NULL,
Booked_for_start TIME NOT NULL,
booked_out_till TIME NOT NULL,
FOREIGN KEY (userName) REFERENCES Users (userName),
FOREIGN KEY (itemID) REFERENCES Tools (itemID)
);
