<?php
// SQLite database file
$dbFile = "user_data.db";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate and sanitize user inputs
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);

    if (!$name || !$email) {
        die("Invalid input data.");
    }

    // Create or open the SQLite database with error handling
    $db = new SQLite3($dbFile);

    if (!$db) {
        die("SQLite connection failed: " . $db->lastErrorMsg());
    }

    // Insert user information into the 'users' table
    $query = "INSERT INTO users (name, email) VALUES (:name, :email)";
    $stmt = $db->prepare($query);
    $stmt->bindParam(':name', $name, SQLITE3_TEXT);
    $stmt->bindParam(':email', $email, SQLITE3_TEXT);

    if ($stmt->execute()) {
        echo "Data saved successfully.";
    } else {
        echo "Error: " . $db->lastErrorMsg();
    }

    // Close the database connection
    $db->close();
}
?>
