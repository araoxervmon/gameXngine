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
    <style>
        text {
            font: 12px sans-serif;
        }
        svg {
            display: block;
        }
        html, body, #chart1, svg {
            margin: 0px;
            padding: 0px;
            height: 100%;
            width: 100%;
        }
    </style>
<div id="chart1">
<svg></svg>
</div>
<svg id="test1" class="mypiechart"></svg>

<script>
    historicalBarChart = [
        {
            key: "Cumulative Return",
            values: [
                {
                    "label" : "xbox" ,
                    "value" : 29.765957771107
                } ,
                {
                    "label" : "PC" ,
                    "value" : 40
                } ,
                {
                    "label" : "PSP" ,
                    "value" : 32.807804682612
                } ,
                {
                    "label" : "Wii" ,
                    "value" : 96.45946739256
                } ,
                {
                    "label" : "Others" ,
                    "value" : 20.19434030906893
                } ,
            ]
        }
    ];

    nv.addGraph(function() {
        var chart = nv.models.discreteBarChart()
            .x(function(d) { return d.label })
            .y(function(d) { return d.value })
            .staggerLabels(true)
            //.staggerLabels(historicalBarChart[0].values.length > 8)
            .tooltips(false)
            .showValues(true)
            .duration(250)
            ;

        d3.select('#chart1 svg')
            .datum(historicalBarChart)
            .call(chart);

        nv.utils.windowResize(chart.update);
        return chart;
    });


    var testdata = [
        {key: "One", y: 5},
        {key: "Two", y: 2},
        {key: "Three", y: 9},
        {key: "Four", y: 7},
        {key: "Five", y: 4},
        {key: "Six", y: 3},
        {key: "Seven", y: 0.5}
    ];
    var testdata2 = [
        {key: "One", y: 5},
        {key: "Two", y: 2},
        {key: "Three", y: 9},
        {key: "Four", y: 7},
        {key: "Five", y: 4},
        {key: "Six", y: 3},
        {key: "Seven", y: 0.5}
    ];

    var height = 350;
    var width = 350;

    nv.addGraph(function() {
        var chart = nv.models.pieChart()
            .x(function(d) { return d.key })
            .y(function(d) { return d.y })
            .width(width)
            .height(height);

        d3.select("#test1")
            .datum(testdata2)
            .transition().duration(1200)
            .attr('width', width)
            .attr('height', height)
            .call(chart);

        // update chart data values randomly
        setInterval(function() {
            testdata2[0].y = Math.floor(Math.random() * 10);
            testdata2[1].y = Math.floor(Math.random() * 10);
            chart.update();
        }, 4000);

        return chart;
    });

    nv.addGraph(function() {
        var chart = nv.models.pieChart()
            .x(function(d) { return d.key })
            .y(function(d) { return d.y })
            //.labelThreshold(.08)
            //.showLabels(false)
            .color(d3.scale.category20().range().slice(8))
            .growOnHover(false)
            .tooltipContent(function(key, y, e, graph) {
                return '<h3 style="padding: 5px; background-color: '
                        + e.color + '"><strong>Yo, the value is</strong></h3>'
                        + '<p style="padding:5px;">' +  y + '</p>';
            })
            .width(width)
            .height(height);

        // make it a half circle
        chart.pie
            .startAngle(function(d) { return d.startAngle/2 -Math.PI/2 })
            .endAngle(function(d) { return d.endAngle/2 -Math.PI/2 });

        // MAKES LABELS OUTSIDE OF DONUT
        //chart.pie.donutLabelsOutside(true).donut(true);

        d3.select("#test2")
            .datum(testdata)
            .transition().duration(1200)
            .attr('width', width)
            .attr('height', height)
            .call(chart);

        // disable and enable some of the sections
        var is_disabled = false;
        setInterval(function() {
            chart.dispatch.changeState({disabled: {2: !is_disabled, 4: !is_disabled}});
            is_disabled = !is_disabled;
        }, 3000);

        return chart;
    });

</script>
</body>
</html>
