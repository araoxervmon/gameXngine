<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<head>
<link rel="icon" href="images/favicon.png" type="image/png" sizes="16x16">
    <meta charset="utf-8">
    <title>Game Search Engine</title>
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
</head>
</head>

	<body>
		<?php require "config.php";
		 include 'header.php'; 
		$searchID= $_POST['searchID'];
		$sql=$dbo->prepare("SELECT * FROM game_titles WHERE title LIKE '" .$searchID. "%'");
		$sql->execute();
		$result = $sql->fetchAll();
		?>

		<div class="container">
	<div class="row">
      <div class="table-responsive">
        <table id="myTable" class="table table-hover table-bordered" >  
          <thead>
            <tr>
              <th>#</th>
              <th>Title</th>
              <th>Condition</th>
              <th>Game Type</th>
              <th>Gamebox</th>
            </tr>
          </thead>
	<?php 
		foreach($result as $row) {
			$id = $row['gameId'];
   			$title = $row['title'];
   			$condition = $row['cond'];
   			$gameType = $row['game_type'];
   			$gameBox = $row['game_box'];
	
	?>
          <tbody>
            <tr>
              <td><?php echo $id; ?></td>
              <td><?php echo $title; ?></td>
              <td><?php echo $condition; ?></td>
              <td><?php echo $gameType; ?></td>
              <td><?php echo $gameBox; ?></td>
            </tr>
          </tbody>
	<?php
	}
	?>
	</table>   
      </div>
      <div class="col-md-12 text-center">
      <ul class="pagination pagination-lg pager" id="myPager"></ul>
      </div>
</div>
</div>
<style>

#chart svg {
  height: 400px;
}

</style>


<div id="chart">
  <svg></svg>
</div>
</body>
</html>
<script>
$(document).ready(function(){$.fn.pageMe = function(opts){
    var $this = this,
        defaults = {
            perPage: 7,
            showPrevNext: false,
            hidePageNumbers: false
        },
        settings = $.extend(defaults, opts);
    
    var listElement = $this;
    var perPage = settings.perPage; 
    var children = listElement.children();
    var pager = $('.pager');
    
    if (typeof settings.childSelector!="undefined") {
        children = listElement.find(settings.childSelector);
    }
    
    if (typeof settings.pagerSelector!="undefined") {
        pager = $(settings.pagerSelector);
    }
    
    var numItems = children.size();
    var numPages = Math.ceil(numItems/perPage);

    pager.data("curr",0);
    
    if (settings.showPrevNext){
        $('<li><a href="#" class="prev_link">«</a></li>').appendTo(pager);
    }
    
    var curr = 0;
    while(numPages > curr && (settings.hidePageNumbers==false)){
        $('<li><a href="#" class="page_link">'+(curr+1)+'</a></li>').appendTo(pager);
        curr++;
    }
    
    if (settings.showPrevNext){
        $('<li><a href="#" class="next_link">»</a></li>').appendTo(pager);
    }
    
    pager.find('.page_link:first').addClass('active');
    pager.find('.prev_link').hide();
    if (numPages<=1) {
        pager.find('.next_link').hide();
    }
  	pager.children().eq(1).addClass("active");
    
    children.hide();
    children.slice(0, perPage).show();
    
    pager.find('li .page_link').click(function(){
        var clickedPage = $(this).html().valueOf()-1;
        goTo(clickedPage,perPage);
        return false;
    });
    pager.find('li .prev_link').click(function(){
        previous();
        return false;
    });
    pager.find('li .next_link').click(function(){
        next();
        return false;
    });
    
    function previous(){
        var goToPage = parseInt(pager.data("curr")) - 1;
        goTo(goToPage);
    }
     
    function next(){
        goToPage = parseInt(pager.data("curr")) + 1;
        goTo(goToPage);
    }
    
    function goTo(page){
        var startAt = page * perPage,
            endOn = startAt + perPage;
        
        children.css('display','none').slice(startAt, endOn).show();
        
        if (page>=1) {
            pager.find('.prev_link').show();
        }
        else {
            pager.find('.prev_link').hide();
        }
        
        if (page<(numPages-1)) {
            pager.find('.next_link').show();
        }
        else {
            pager.find('.next_link').hide();
        }
        
        pager.data("curr",page);
      	pager.children().removeClass("active");
        pager.children().eq(page+1).addClass("active");

    
    }
};

$(document).ready(function(){
    
  $('#myTable').pageMe({pagerSelector:'#myPager',showPrevNext:true,hidePageNumbers:false,perPage:10});
    
});
});

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

//Donut chart example
nv.addGraph(function() {
  var chart = nv.models.pieChart()
      .x(function(d) { return d.label })
      .y(function(d) { return d.value })
      .showLabels(true)     //Display pie labels
      .labelThreshold(.05)  //Configure the minimum slice size for labels to show up
      .labelType("percent") //Configure what type of data to show in the label. Can be "key", "value" or "percent"
      .donut(true)          //Turn on Donut mode. Makes pie chart look tasty!
      .donutRatio(0.35)     //Configure how big you want the donut hole size to be.
      ;

    d3.select("#chart2 svg")
        .datum(exampleData())
        .transition().duration(350)
        .call(chart);

  return chart;
});

var aa = new Array();
var bb = new Array();
var cc = 
	[
	
<?php 
	foreach($result as $row) { 
		$id = $row['gameId'];
   		$title = $row['title'];
   		$condition = $row['cond'];
   		$gameType = $row['game_type'];
   		$gameBox = $row['game_box'];
	
	?>
	{
        	"label" : aa.push(<?php echo "'$title'"?>),
        	"value" : bb.push(<?php echo $id?>)
	},
	<?php } ?> 
];
//Pie chart example data. Note how there is only a single array of key-value pairs.

function exampleData() {
  return cc;
}
</script>
