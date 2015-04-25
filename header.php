<html>
<head>
    <meta charset="utf-8">
</head>
<body>
<div class="bs-example">
	    <nav role="navigation" class="navbar navbar-default">
		<!-- Brand and toggle get grouped for better mobile display -->
		<div class="navbar-header">
		    <button type="button" data-target="#navbarCollapse" data-toggle="collapse" class="navbar-toggle">
		        <span class="sr-only">Toggle navigation</span>
		        <span class="icon-bar"></span>
		        <span class="icon-bar"></span>
		        <span class="icon-bar"></span>
		    </button>
		    <a href="#" class="navbar-brand">GAMEZ</a>
		</div>
		<!-- Collection of nav links, forms, and other content for toggling -->
		<div id="navbarCollapse" class="collapse navbar-collapse">
		    <ul class="nav navbar-nav">
		        <li class="active"><a href="/dproject">Home</a></li>
   			<li><a href="action.php">Genres</a></li>
			
		        <li class="dropdown">
		            <a data-toggle="dropdown" class="dropdown-toggle" href="#">Game Console<b class="caret"></b></a>
		            <ul role="menu" class="dropdown-menu">
		                <li><a href="xbox_one.php">Xbox One</a></li>
		                <li><a href="xbox.php">Xbox 360</a></li>
		                <li><a href="ps_4.php">PS 4</a></li>
		                <li><a href="ps_3.php">PS 3</a></li>
		                <li><a href="pc.php">PC</a></li>
		             </ul>
		        </li>
		        <li class="dropdown">
		            <a data-toggle="dropdown" class="dropdown-toggle" href="#">Data Drill Down<b class="caret"></b></a>
		            <ul role="menu" class="dropdown-menu">
		                <li><a href="top_rated.php">Top Rated</a></li>
		                <li><a href="publisher.php">Publisher</a></li>
		                <li><a href="console.php">Console Type</a></li>
		                <li><a href="topgross.php">Top Grossing Games</a></li>
		                <li><a href="complete.php">Complete Collection</a></li>
		            </ul>
		        </li>
		    </ul>
		 <form role="search" class="navbar-form navbar-right" action="action4.php" method="POST">
		        <div class="form-group">
		            <input type="text" placeholder="Search" class="form-control" name="searchID" id="searchID">
		        </div>
			<button type="submit" class="btn btn-default">Search</button>
	 		<!--<button type="submit" class="btn btn-default" onclick="Search();">Submit</button>-->
		    </form>
		</div>
	    </nav>
	</div>
<script>/*
function Search() {
      var searchID = $("#searchID").val();
      $.ajax({
        type: "POST",
        url: "action4.php",
        data: { "searchID": searchID },
        success: function(msg){
        }
      });
    }*/
</script>
</body>
</html>
