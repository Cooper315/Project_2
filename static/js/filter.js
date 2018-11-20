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
d3.selectAll("#clickbutton").on("click",filterUni);
