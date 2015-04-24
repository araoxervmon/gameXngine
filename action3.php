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

						//server credential
						$serverName = "localhost";
						$userName = "root";
						$password = "root";
						$dbname = "dbproject";

						$link = mysqli_connect($serverName, $userName, $password, $dbname );

						//localhost connection
						if (!$link) {
								die('Could not connect to the database.\n\n ' . mysql_error());
						}
						
						echo 'Connected to the server successfully'."<br><br>";

						//database - project 2 connection 
					/*	$db_selected = mysql_select_db("dbproject" , $link );
						
						if (!$db_selected) {
							die ('Can\'t use project2 : \n\n' . mysql_error());
						}

						echo 'Connected to the database successfully.'."<br><br>";*/

						//based on post data from the front end we can decide which query needs to be executed. 
						if(isset($_POST["1"]) )
						{
							$query1 = "select  g.title, c.consoleName   from game_titles g, console c
										  where c.consoleId = g.consoleId;";
							
							echo "<h2>The number of unique games per system </h2><br>";	
							
							echo "<table border='1'> 
									<tr> 
										<th> Title </th> 
										<th> Console Name </th>					
									</tr>";					  
						
							//executing query
							$query1Data = mysqli_query($query1);
							
							if($query1Data) {
								// output data of each row
								while($row = mysql_fetch_array($query1Data)) {
									
								echo "<tr>"; 
									echo "<td>" . $row["title"] . "</td>"; 
									echo "<td>" . $row["consoleName"]."</td>";			
								echo "</tr>";
							  }
							  
							} else {
								echo "0 results";
							}
							echo "</table>";
							echo "<br><br><br><a href='index.html'>Jump to our main page</a>";
						}elseif( isset($_POST["2"]))
						{
							$query2 = "select title from game_titles group by title having count(title) > 1;";
							
							echo "<h2>A list with the duplicate games in the collection</h2><br>";
							echo "<table border='1'> 
									<tr> 
										<th> Title </th>										
									</tr>";
									
							//executing query
							$query2Data = mysqli_query($query2);
							
							if($query2Data) {
								// output data of each row
								while($row = mysql_fetch_array($query2Data)) {
									echo "<tr>"; 
										echo "<td>" . $row["title"] . "</td>"; 
									echo "</tr>";
								}
							} else {
								echo "0 results";
							}
							echo "</table>";
							echo "<br><br><br><a href='index.html'>Jump to our main page</a>";
						}elseif(isset($_POST["3"]))
						{
							
							$query3 = "select sum(gameMV) from game_finance;";
						
							$query3Data = mysqli_query($query3);
							echo "<h2>The total cost of the person’s collection </h2><br>";
							echo "<table border='1'> 
									<tr> 
										<th> Sum of Market price  </th>								
									</tr>";
									
							//executing query
							if($query3Data) {
								// output data of each row
								$row = mysql_fetch_row($query3Data);
										echo "<tr>"; 
											echo "<td>" . $row[0] . "</td>"; 
										echo "</tr>";				
							  
							} else {
								echo "0 results";
							}
							echo "</table>";
							echo "<br><br><br><a href='index.html'>Jump to our main page</a>";
						}elseif(isset($_POST["4"]))
						{
							
					 
							 $query4 = "select IF(game_inst = 'N' or game_box = 'N', title,'') as incomplete_games,
											   IF(game_inst = 'Y' and game_box = 'Y', title,'') as complete_games
											   from game_titles;";
						
							//executing query		
							$query4Data = mysqli_query($query4);
							
							echo "<h2>The collector’s complete games and the games missing something (box and/or manual)</h2> <br><br>";
							echo "<table border='1'> 
									<tr> 
										<th> Incomplete Games name </th> 
										<th> Complete Games name </th>					
									</tr>";
							
							if($query4Data) {
								// output data of each row
								while($row = mysql_fetch_array($query4Data)) {
									echo "<tr>"; 
											echo "<td>" . $row["incomplete_games"] . "</td>";
											echo "<td>" . $row["complete_games"] . "</td>";	
									echo "</tr>";			
								  }
							} else {
								echo "0 results";
							}
							echo "</table>";
							echo "<br><br><br><a href='index.html'>Jump to our main page</a>";

						}elseif( isset($_POST["5"]))
						{
							$query5 = "select g.title from game_titles g, game_finance f 
									   where g.gameId = f.gameId and 
									   f.gameMV = (select max(gameMV) from game_finance);";
						
							//executing query
							$query5Data = mysqli_query($query5);
								
							echo "<h2>The collector’s most expensive game (based on the current market value)</h2> <br><br>"; 			
							echo "<table border='1'> 
									<tr> 
										<th> Title </th>										
									</tr>";
							
							if($query5Data) {
								// output data of each row
								while($row = mysql_fetch_array($query5Data)) {
								
								echo "<tr>"; 
											echo "<td>" . $row["title"]. "</td>";							
								echo "</tr>";		
							  }
							} else {
								echo "0 results";
							}		
							echo "</table>";
							echo "<br><br><br><a href='index.html'>Jump to our main page</a>";
						
						}elseif( isset($_POST["6"]))
						{
							$query6 = "select g.title from game_titles g , game_finance f
									   where g.gameId = f.gameId and 
									   f.purchasePrice < f.gameMV";
						
						    //executing query
							$query6Data = mysqli_query($query6);		
							echo "<h2>The games that the collector purchased for a price lower than the current market price </h2> <br>"; 
							
							echo "<table border='1'> 
									<tr> 
										<th> Title </th>									
									</tr>";
									
							if($query6Data) {
								// output data of each row
								while($row = mysql_fetch_array($query6Data)) {
								
								echo "<tr>"; 
											echo "<td>" . $row["title"]. "</td>";							
								echo "</tr>";			
							  }
							} else {
								echo "0 results";
							}
							echo "</table>";
							echo "<br><br><br><a href='index.html'>Jump to our main page</a>";

						}elseif( isset($_POST["7"]))
						{
							$query7 = "select g.title, (f.gameMV - f.purchasePrice) as increase_value 
									   from game_titles g ,game_finance f
									   where g.gameId = f.gameId and 
									   (f.gameMV - f.purchasePrice) = (select max(gameMV - purchasePrice) from game_finance);";
										  
							//executing query
							$query7Data = mysqli_query($query7);
							echo "<h2>The game that has the highest increase in value (current value minus money paid) for and what is this increase.</h2><br>";
							
							echo "<table border='1'> 
									<tr> 
										<th> Title </th> 
										<th> Increased value </th>					
									</tr>";
							
							if($query7Data) {
								// output data of each row
								while($row = mysql_fetch_array($query7Data)) {
								
								echo "<tr>"; 
											echo "<td>" . $row["title"]. "</td>";
											echo "<td>" . $row["increase_value"]. "</td>";						
								echo "</tr>";
							  }
							} else {
								echo "0 results";
							}
							echo "</table>";
							echo "<br><br><br><a href='index.html'>Jump to our main page</a>";
						
						}else
						{
							echo "Nothing has entered...pls enter the appropriate query";
						}
						
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
