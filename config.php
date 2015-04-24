<?php
$host_name = "localhost";
$database = "dbproject"; // Change your database nae
$username = "root";          // Your database user id 
$password = "root";          // Your password

//////// Do not Edit below /////////
try {
$dbo = new PDO('mysql:host='.$host_name.';dbname='.$database, $username, $password);
} catch (PDOException $e) {
print "Error!: " . $e->getMessage() . "<br/>";
die();
}
?>
