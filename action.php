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
			<div id="main-content">
			
				<?php
				
				// credential 
				$serverName = "localhost";
				$userName = "root";
				$password = "root";
				$dbname = "dbproject";

				$link = mysqli_connect($serverName, $userName, $password );

					
					//localhost connection
					if (!$link) {
							die('Could not connect to the database\n\n ' . mysql_error());
					}
					
					echo 'Connected to the server successfully.'."<br><br>";

					//database - project 2 connection 
					$db_selected = mysql_select_db("dbproject" , $link );
					
					if (!$db_selected) {
						die ('Can\'t use project2 : \n\n' . mysql_error());
					}

					echo 'Connected to the database successfully.'."<br><br>";

					//insert data into game_titles table
					$sql_title = "INSERT INTO game_titles (title, cond, game_type,game_inst,game_box,consoleId, categoryId)
					VALUES ('$_POST[title]', '$_POST[condition]', '$_POST[type]','$_POST[completenessInstruction]','$_POST[completenessBox]','$_POST[console]','$_POST[category]')";
						
					$query_title = mysqli_query($sql_title);
					
					//
					if(!$query_title)
					{
						die('Could not save the data in the game_title' . mysql_error());
					}
					echo "Data has been saved in Game Title table. <br>";
					
					$query_gameId = mysql_fetch_row(mysql_query("SELECT max(`gameId`) AS gameId FROM `game_titles` " ));
					$maxGameId = $query_gameId[0] ;
					//echo $maxGameId;					
					
					$sql_finance = "INSERT INTO game_finance (gameId, purchasePrice, gameMV,dateOfPurchase)
					VALUES ($maxGameId, '$_POST[pp]','$_POST[mp]','$_POST[dob]')";
					
					//executing the query		
					$query_finance = mysql_query($sql_finance);
					
					if(!$query_finance)
					{
						die('Could not save the data in the game_finance' . mysql_error());
					}
					
					echo '<br>Data has been saved in Game Finance table.'."<br><br>";

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
