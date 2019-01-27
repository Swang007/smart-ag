var data = document.getElementById("testData");

// d3.text("src/testdata.csv", function(data) {
// d3.text("{{ url_for('static', filename='src/testdata.csv') }}", function(data) {
//     var parsedCSV = d3.csv.parseRows(data);
//     window.chartTimes = [1, 2, 3, 4, 5];
//     window.chartHeights = [1, 2, 3, 2, 3];
//     window.chartWater = [1, 2, 3, 2, 3];
    // for (i = 0; i < parsedCSV.length; i++) {
    //     chartTimes.push(parsedCSV[i][0]);
    //     chartHeights.push(parsedCSV[i][1]);
    //     chartWater.push(parsedCSV[i][2]);
    // }
//     console.log(chartTimes[0]);
//     return parsedCSV;
    
// })

// function parseCSV(parsedCSV) {
//     chartTimes = [];
//     chartHeights = [];
//     chartWater = [];
//     for (i = 0; i < parsedCSV.length; i++) {
//         chartTimes.push(parsedCSV[i][0]);
//         chartHeights.push(parsedCSV[i][1]);
//         chartWater.push(parsedCSV[i][2]);
//     }
//     return [chartTimes, chartHeights, chartWater];
// }
// var chartTimes = [2,2,2];
// var chartHeights = [0.1,0.1,1];
// var chartWater = [0.3,3,4];



var ctx = document.getElementById('firstChart').getContext('2d');
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: ['Jan', 'Feb', 'March', 'April', 'May'],
        datasets: [{
            label: "Data Stuff",
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data: [1,2,3,2,4],
        }]
    },

    // Configuration options go here
    options: {}
});
