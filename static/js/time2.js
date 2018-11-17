//bring in data
var all_data;
var tbody = d3.select("#tablerow");

// unpack  rows
function unpack(rows, key){
  return rows.map(function(row) {return row[key]; });
}

function tableNSF(NSFData){
  var tbody = d3.select("#tablerow");
  for(var i = 0; i < NSFData.length; i++){
    var row_data = NSFData[i];
    var row_html = tbody.append("tr");
    var cell1 = row_html.append("td");
    cell1.text(row_data.NSFName);
    var cell2 = row_html.append("td");
    cell2.text(row_data.UnitId);
    var cell3 = row_html.append("td");
    cell3.text(row_data.Year);
    var cell4 = row_html.append("td");
    cell4.text(row_data.AcademicDiscipline);
    var cell5 = row_html.append("td");
    cell5.text(row_data.TotalRDExpenditures);
  }
}

// function buildTrace(discipline){
//   var trace = {
//     x: Year,
//     y: Expenditures,
//     type: "scatter"
//   };
//   return trace;  
// };

// function buildChart(NSFData){
//   // console.log(NSFData);
//   all_data => {
//     var Tracedata = discipline.map(y => {
//         var d = rows.filter(r => r.discipline === y)

//         return {
//           type: 'scatter',
//           name: y,
//           x: d.map(r => r.Year),
//           y: d.map(r => r.TotalRDExpenditures)
//         }
//       })
  // for( var i = 0; i < NSFData.length; i++){
  //   if (NSFData.AcademicDiscipline[i] != NSFData.AcademicDiscipline[i-1]);
  //   Expend += expend.push(TotalRDExpenditures);
  // var chart_data = NSFData[i];
  // if(NSData.AcademicDiscipline[i+1] != NSFData.AcademicDiscipline[i]){
  // //Build new trace
  // var new_trace = buildTrace(NSFData);
  // traces.push({"dis": last_dis, "trace": new_trace });
  // //Reset list
  // };
  // };

//   Plotly.newPlot('scatterchart',Tracedata)
//       // return trace;  
//   }
// };
  
function filterUni(){
  // d3.event.preventDefault();
  var school = d3.select("#unifilter").property("value");
  var filteredData = all_data;
  if(school){
    filteredData = filteredData.filter(row => row.NSFName === school);
  };
//   return filteredData;
tbody.html("");


filteredData.forEach(function(UniData){
  var row = tbody.append("tr");

  Object.entries(UniData).forEach(function([key, value]) {
    var cell = tbody.append("td");
    cell.text(value);
  });
});
};

function renderTableAndChart(){
  //2)  Do filtering
  var filtered_data = filterUni();
  // 3) Build table
  tableNSF(all_data);
//   // 4) Build chart
// //   buildChart(all_data);
};

d3.selectAll("#clickbutton").on("click",filterUni);

//1) Download csv
d3.csv('NSF_expenditures_nu.csv').then(function(NSFData){  
  all_data = NSFData;
  renderTableAndChart();
  // console.log(all_data);
});


//function to filter data
// d3.csv('NSF_expenditures_nu.csv').then(function(NSFData){  

    // NSFData.forEach(function(data){
    //   data.NSFame = +data.NSFName;
    //   data.AcademicDiscipline = +data.AcademicDiscipline;
    //   data.TotalRDExpenditures = +data.TotalRDExpenditures;
    //   data.Year = +data.Year
    // });

      //   if(last_dis != UniData.dis){
      //     //Build new trace
      //     var new_trace = buildTrace(all_dis_data);
      //     traces.push({"dis": last_dis, "trace": new_trace });
      //     //Reset list
      //     all_dis_data = [];
      //     last_dist = 
      //     };
      // }; 
//});
//  d3.selectAll("#clickbutton").on("click",filterUni);
// console.log(NSFData);
//  NSFData();
// console.log(data.TotalRDExpenditures);
// console.log(data.Year);


//     function buildTrace(list_of_rows){
//         var trace = {
//           x: unpack(list_of_rows, 'Year'),
//           y: unpack(list_of_rows, 'TotalRDExpenditures'),
//           type: "scatter"
//         };
//         return trace;  
//     };



//     var trace = {
//       x: unpack(rows, 'Year'),
//       y: unpack(rows, 'TotalRDExpenditures'),
//       type: "scatter"
//     };

// var data = [trace]

//     var layout = {
//         title: 'Med Expenditures',
//         xaxis: {
//           range: ['2000', '2018'],
//           type: 'date'
//         },
//         yaxis: {
//           autorange: true,
//           type: 'linear'
//         }
//     };  
  
//   Plotly.plot('scatterchart',data, layout);