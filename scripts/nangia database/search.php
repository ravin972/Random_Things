<!DOCTYPE html>
<html>
<head>
    <title>Search Results</title>
</head>
<body>
    <h1>Search Results</h1>
    <form action="search.php" method="post">
        <label for="searchName">Search by Name:</label>
        <input type="text" name="searchName" required>
        <input type="submit" value="Search">
    </form>
    <?php
    // SQLite database file (same as in process.php)
    $dbFile = "user_data.db";

    // Create or open an SQLite database connection with error handling
    $db = new SQLite3($dbFile);

    if (!$db) {
        die("SQLite connection failed: " . $db->lastErrorMsg());
    }

    // Process user input (name to search for)
    $searchName = $_POST['searchName'];

    // Query the SQLite database for matching user records with prepared statements
    $query = "SELECT * FROM users WHERE name LIKE :searchName";
    $stmt = $db->prepare($query);
    $stmt->bindValue(':searchName', "%$searchName%", SQLITE3_TEXT);
    $result = $stmt->execute();

    // Display search results in a table format
    if ($result) {
        echo "<table border='1'>";
        echo "<tr><th>Name</th><th>Email</th></tr>";
        while ($row = $result->fetchArray(SQLITE3_ASSOC)) {
            echo "<tr>";
            echo "<td>" . htmlspecialchars($row['name']) . "</td>"; // Sanitize user data
            echo "<td>" . htmlspecialchars($row['email']) . "</td>"; // Sanitize user data
            echo "</tr>";
        }
        echo "</table>";
    } else {
        echo "No matching records found.";
    }

    // Close the database connection
    $db->close();
    ?>
</body>
</html>
