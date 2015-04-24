<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Video Games</title>
<link href="css/style.css" rel="stylesheet" type="text/css" />
</head>

	<body>
		<div id="container">
			<div id="header">
				<div id="header-bottom">&nbsp;</div> 
			</div>
			<div id="main-content"  >
				<?php

				$serverName = "localhost";
				$userName = "root";
				$password = "root";
				$dbname = "dbproject";

				$link = mysqli_connect($serverName, $userName, $password, $dbname );

					
					//localhost connection
					if (!$link) {
							die('Could not connect to the database\n\n ' . mysql_error());
					}
					
					echo 'Connected to the server successfully.'."<br><br>";

					//database - project 2 connection 
					$db_selected = mysql_select_db("dbproject" , $link );/*
					
					if (!$db_selected) {
						die ('Can\'t use project2 : \n\n' . mysql_error());
					}

					echo 'Connected to the database successfully.'."<br><br>";		
*/
					//inser data into game_titles table
					$sql_console = "SELECT game_titles.gameId,game_titles.title, cond, game_inst, game_box, dateOfPurchase, purchasePrice, gameMV
									FROM game_titles
									LEFT JOIN game_finance ON game_titles.gameId = game_finance.gameId
									WHERE game_titles.consoleId =  '$_POST[console]' "; 
					
					$result = mysqli_query($sql_console);
					
					//echo 'something'.$result;	
						
					if($result) {
					
						//Question
						echo "<h2>Navigation to the games the collector OWNS: The user chooses from the menu one
						game console and is presented with a list of his games with information on the date</h2> <br><br>";
					
						//heading
						echo "<table border='1'> 
								<tr> 
									<th> Game Id </th>
									<th> Game Title </th>									
									<th> Condition </th> 
									<th> Game Instruction </th> 
									<th> Game Box </th> 
									<th> Date of Purchase </th>
									<th> Purchase Price</th>
									<th> Market Price </th>					
								</tr>";
						
					
						// output data of each row
						while($row = mysql_fetch_array($result)) {
						
							echo "<tr>"; 
								echo "<td>" . $row['gameId'] . "</td>"; 
								echo "<td>" . $row['title'] . "</td>"; 
								echo "<td>" . $row['cond'] . "</td>"; 
								echo "<td>" . $row['game_inst'] . "</td>"; 
								echo "<td>" . $row['game_box'] . "</td>"; 
								echo "<td>" . $row['dateOfPurchase'] . "</td>";
								echo "<td>" . $row['purchasePrice'] . "</td>";
								echo "<td>" . $row['gameMV'] . "</td>";			
							echo "</tr>";
					  }
					} else {
					echo "0 results";
					}
					echo "</table>";
					
					echo "<br><br><br><a href='index.html'>Jump to our main page</a>";
					
					mysql_close($link);
				?>

			</div>
		  
			<div class="clearfloat" />
			<div id="footer">
				<p> videogames   Copyright &copy 2012  |  All Rights Reserved</p>
			</div>
		
		</div>
	</body>
</html>
