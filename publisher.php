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
		$sql=$dbo->prepare("SELECT  publisher, count(publisher) as tot from gamelist  group by publisher");
		$sql1=$dbo->prepare("select publisher, max(ratings) as ratings from (select b.gameName, b.publisher, b.ratings, b.releaseDate from (select publisher as publisher_name, c from (select publisher, count(publisher) as c from (SELECT * FROM `gamelist`) a group by publisher) b where c != 1) a, (select * from `gamelist`) b where a.publisher_name = b.publisher union all select b.gameName, a.publisher_name, b.ratings, b.releaseDate from (select publisher, 'other' as publisher_name, c from (select publisher, count(publisher) as c from (SELECT * FROM `gamelist`) a group by publisher) b where c = 1) a, (select * from `gamelist`) b where a.publisher = b.publisher) as total where ratings != 'NR' and ratings > 9 group by publisher order by publisher");
		$start = microtime(true);
		$sql->execute();
		$sql1->execute();
		$end = microtime(true);
		
		$result = $sql->fetchAll();
		$result1 = $sql1->fetchAll();
		?>

		<div class="container">
	<div class="row">
      <div class="table-responsive">
        <table id="myTable" class="table table-hover table-bordered" >  
          <thead>
            <tr>
              <th><?php echo "About ".$sql->rowCount(). " results Time took (" . ($end - $start) . ") seconds."; ?></th>
            </tr>
          </thead>
	<?php 
		foreach($result as $row) {
   			$publisher = $row['publisher'];
   			$tot = $row['tot'];
	
	?>
          <tbody>
            <tr>
              <td>
		<div class="well"><a href="#" class="pull-left"><img src="https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSrHD8gMbTdeIpym2_4b2XZBtKbFO1XiwxrAjQZ9QQR71fiv4isoA"  class="media-object">
					</a><div class="media-body">
					<h1>Publisher Name: <?php echo $publisher; ?> </h1>
					<h1>Number of Games: <?php echo $tot; ?></h1>
					</div></div><hr></td>
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
<div id="chart">
  <svg></svg>
</div>
</body>
</html>
<style>

#chart svg {
  height: 400px;
}

</style>
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
    
  $('#myTable').pageMe({pagerSelector:'#myPager',showPrevNext:true,hidePageNumbers:false,perPage:20});
    
});
});


nv.addGraph(function() {
  var chart = nv.models.discreteBarChart()
      .x(function(d) { return d.label })    //Specify the data accessors.
      .y(function(d) { return d.value })
     .showValues(true)
     .staggerLabels(true);

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
	foreach($result1 as $rows) { 
		$publisher = $rows['publisher'];
   		$ratings = $rows['ratings'];
	
	?>
	{
        	"label" :<?php echo "'$publisher'"  ?>,
        	"value" : <?php echo $ratings ?>
	},
	<?php } ?> 
]}];
//Pie chart example data. Note how there is only a single array of key-value pairs.

function exampleData() {
  return cc;
}
</script>
