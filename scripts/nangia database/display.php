<!DOCTYPE html>
<html>
<head>
    <title>Display User Information</title>
</head>
<body>
    <h1>User Information</h1>
    <table border="1">
        <tr>
            <th>Name</th>
            <th>Email</th>
        </tr>
        <?php
        // SQLite database file
        $dbFile = "user_data.db";

        // Create or open the SQLite database
        $db = new SQLite3($dbFile);

        if (!$db) {
            die("SQLite connection failed.");
        }

        // Retrieve and display user information
        $query = "SELECT * FROM users";
        $result = $db->query($query);

        while ($row = $result->fetchArray(SQLITE3_ASSOC)) {
            echo "<tr>";
            echo "<td>" . $row['name'] . "</td>";
            echo "<td>" . $row['email'] . "</td>";
            echo "</tr>";
        }

        // Close the database connection
        $db->close();
        ?>
    </table>
</body>
</html>
