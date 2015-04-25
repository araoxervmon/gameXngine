<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css"  href="css/bootstrap.css"/>
    <link rel="stylesheet" type="text/css" href="css/style.css"/>
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <link rel="stylesheet" href="css/bootstrap-theme.min.css">
    <link href="css/nv.d3.css" rel="stylesheet" type="text/css">
    <script src="js/jquery.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/d3.min.js" charset="utf-8"></script>
    <script src="js/nv.d3.js"></script>
</head>
<body>
	<?php require "config.php";
		$sql=$dbo->prepare("SELECT count(gameName) as gamecount, console.consoleName as consoleName FROM `gamelist` left join 			console on gamelist.consoleId = console.consoleId group by consoleName ");
		$sql->execute();
		$sql1=$dbo->prepare("SELECT gameName,ratings FROM gamelist WHERe ratings > 9.5 LIMIT 10");
		$sql1->execute();
		$result = $sql->fetchAll();
		$result1 = $sql1->fetchAll();
		?>
<h2>Console Types</h2>
<div id="chart">
  <svg></svg>
</div>
<h2>Top 10 Games</h2>
<div id="topchart">
  <svg></svg>
</div>

    <style>
       
#chart svg {
  height: 500px;
}
#topchart svg {
  width: 100%;
  height: 500px;
}

    </style>
<script>
//Regular pie chart example
nv.addGraph(function() {
  var chart = nv.models.pieChart()
      .x(function(d) { return d.label })
      .y(function(d) { return d.value })
      .showLabels(true);

    d3.select("#chart svg")
        .datum(exampleData())
        .transition().duration(350)
        .call(chart);

  return chart;
});

var cc = 
	[
	
<?php 
	foreach($result as $row) { 
		$gamecount = $row['gamecount'];
   		$consoleName = $row['consoleName'];
	
	?>
	{
        	"label" : <?php echo "'$consoleName'"?>,
        	"value" :<?php echo $gamecount?>
	},
	<?php } ?> 
];
//Pie chart example data. Note how there is only a single array of key-value pairs.

function exampleData() {
  return cc;
}


nv.addGraph(function() {
  var chart = nv.models.discreteBarChart()
      .x(function(d) { return d.label })    //Specify the data accessors.
      .y(function(d) { return d.value })
     .showValues(true)
     .staggerLabels(true);

  d3.select('#topchart svg')
      .datum(topData())
      .call(chart);

  nv.utils.windowResize(chart.update);

  return chart;
});
var dd = 
	[{
	key: "Cumulative Return",
	values:[
	
<?php 
	foreach($result1 as $rows) { 
		$gameName = $rows['gameName'];
   		$ratings = $rows['ratings'];
	
	?>
	{
        	"label" :<?php echo "'$gameName'"  ?>,
        	"value" : <?php echo $ratings ?>
	},
	<?php } ?> 
]}];
//Pie chart example data. Note how there is only a single array of key-value pairs.

function topData() {
  return dd;
}
</script>
</body>
</html>
