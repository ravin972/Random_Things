<?php
// Specify the SQLite database file name and location
$dbFile = "user_data.db";

// Create or open the SQLite database
$db = new SQLite3($dbFile);

// Create a table to store user information
$query = "CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
);";

$db->exec($query);

// Close the database connection
$db->close();
?>
