<!DOCTYPE html>
<html>
	<title>Datatable Demo1 | CoderExample</title>
	<head>
  <link rel="stylesheet" type="text/css"  href="css/bootstrap.css"/>
    <link rel="stylesheet" type="text/css" href="css/style.css"/>
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <link rel="stylesheet" href="css/bootstrap-theme.min.css">
    <link rel="stylesheet" type="text/css" href="css/nv.d3.css">
    <link rel="stylesheet" href="css/jquery.dataTables.min.css"></style>
    <script src="js/jquery.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/d3.min.js" charset="utf-8"></script>
    <script src="js/nv.d3.js"></script>
    <script type="text/javascript" src="js/jquery.dataTables.min.js"></script>
		<script type="text/javascript" language="javascript" >
			$(document).ready(function() {
				var dataTable = $('#employee-grid').DataTable( {
					"processing": true,
					"serverSide": true,
					"ajax":{
						url :"genres.php", // json datasource
						type: "post",  // method  , by default get
						error: function(){  // error handling
							$(".employee-grid-error").html("");
							$("#employee-grid").append('<tbody class="employee-grid-error"><tr><th colspan="3">No data found in the server</th></tr></tbody>');
							$("#employee-grid_processing").css("display","none");
							
						}
					}
				} );
			} );
		</script>
	</head>
	<body>
		 <?php include 'header.php'; ?>
		<div class="container">
			<table id="employee-grid"  cellpadding="0" cellspacing="0" border="0" class="display" width="100%">
					<thead>
						<tr>
							<th>Game Name</th>
							<th>Genres</th>
						</tr>
					</thead>
			</table>
		</div>
	</body>
<div id="chart">
  <svg></svg>
</div>
</html>
<style>#chart svg {
  width: 100%;
  height: 600px;
}
</style>
<?php require "config.php";
		$searchID= $_POST['searchID'];
		$sql=$dbo->prepare("Select distinct gameGenre as Genre, count(gameGenre) as tot from gamelistgenres group by gameGenre");
		$sql->execute();
		$result = $sql->fetchAll();
		?>
<script>

nv.addGraph(function() {
  var chart = nv.models.discreteBarChart()
      .x(function(d) { return d.label })    //Specify the data accessors.
      .y(function(d) { return d.value })
     .showValues(true);

  d3.select('#chart svg')
      .datum(exampleData())
      .call(chart);

  nv.utils.windowResize(chart.update);

  return chart;
});
var aa = new Array();
var bb = new Array();
var cc = 
	[{
	key: "Cumulative Return",
	values:[
	
<?php 
	foreach($result as $row) { 
		$Genre = $row['Genre'];
   		$tot = $row['tot'];
	
	?>
	{
        	"label" :<?php echo "'$Genre'"  ?>,
        	"value" : <?php echo $tot ?>
	},
	<?php } ?> 
]}];
//Pie chart example data. Note how there is only a single array of key-value pairs.

function exampleData() {
  return cc;
}
</script>
