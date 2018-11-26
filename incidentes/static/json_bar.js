const svg     = d3.select("svg"),
      margin  = {top: 20, right: 20, bottom: 30, left: 50},
      width   = +svg.attr("width")  - margin.left - margin.right,
      height  = +svg.attr("height") - margin.top  - margin.bottom,
      x       = d3.scaleBand().rangeRound([0, width]).padding(0.2),
      y       = d3.scaleLinear().rangeRound([height, 0]),
      g       = svg.append("g")
                   .attr("transform", `translate(${margin.left},${margin.top})`);


var dato={
  "Mantenimiento": "0,",
  "Vehículo_Mal_Estacionado": "20,",
  "Vehículo_Descompuesto": "32,",
  "Manifestación": "8,",
  "Cierre_de_Calle": "8,",
  "Accidente": "16,",
  "Obras": "7",
  "Obstáculo": "1",
  "Congestionamiento": "60"
}


d3.json("barras.json").then( data => {
  data = data.RECORDS;
  //var rainbow = d3.scaleSequential(d3.interpolateRainbow).domain([0,d3.sum(data, d => 1)]);
  
  x.domain(data.map(d => d.genre));
  y.domain([0, d3.max(data, d => d.count)]);

  g.append("g")
      .attr("class", "axis axis-x")
      .attr("transform", `translate(0,${height})`)
      .call(d3.axisBottom(x));

  g.append("g")
      .attr("class", "axis axis-y")
      .call(d3.axisLeft(y).ticks(10).tickSize(8));
  
  g.selectAll(".bar")
    .data(data)
    .enter().append("rect")
      .attr("class", "bar")
      .attr("x", d => x(d.genre))
      .attr("y", d => y(d.count))
      .attr("width", x.bandwidth())
      .attr("height", d => height - y(d.count));
      //.attr("fill", (d,i) => rainbow(i));
})
.catch(err => {
  svg.append("text")         
        .attr("y", 20)
        .attr("text-anchor", "left")  
        .style("font-size", "20px") 
        .style("font-weight", "bold")  
        .text(`Couldn't open the data file: "${err}".`);
});