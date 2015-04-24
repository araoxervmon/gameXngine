<?php
$host = "localhost";
$uname = "root";
$pass = "root";
$database = "dbproject";

$connection=mysqli_connect($host,$uname,$pass,$database) or die("connection in not ready <br>");
	if (isset($_REQUEST['query'])) {
		$query = $_REQUEST['query'];
		$sql = mysqli_query ("SELECT * FROM game_titles WHERE title LIKE '%{$query}%'");
		$array = array();
		while ($row = mysql_fetch_assoc($sql)) {
		$array[] = $row['title'];
		}
		echo json_encode ($array); //Return the JSON Array
	}
?>
