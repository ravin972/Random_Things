<?php
// SQLite database file
$dbFile = "user_data.db";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['name'];
    $email = $_POST['email'];

    // Create or open the SQLite database
    $db = new SQLite3($dbFile);

    if (!$db) {
        die("SQLite connection failed.");
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
