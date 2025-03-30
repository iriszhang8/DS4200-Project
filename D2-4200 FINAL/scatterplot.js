const svg = d3.select("svg"),
    margin = { top: 20, right: 30, bottom: 50, left: 60 },
    width = +svg.attr("width") - margin.left - margin.right,
    height = +svg.attr("height") - margin.top - margin.bottom,
    g = svg.append("g").attr("transform", `translate(${margin.left},${margin.top})`);

d3.csv("costco_cleaned.csv").then(data => {
    data.forEach(d => {
        d.price = +d.price;
        d.rating = +d.rating;
    });

    const xScale = d3.scaleLinear()
        .domain([0, d3.max(data, d => d.price) * 1.1])
        .range([0, width]);

    const yScale = d3.scaleLinear()
        .domain([0, 5])
        .range([height, 0]);

    g.append("g")
        .attr("transform", `translate(0, ${height})`)
        .call(d3.axisBottom(xScale));

    g.append("g")
        .call(d3.axisLeft(yScale));

    g.selectAll("circle")
        .data(data)
        .enter()
        .append("circle")
        .attr("cx", d => xScale(d.price))
        .attr("cy", d => yScale(d.rating))
        .attr("r", 4)
        .attr("fill", "steelblue")
        .append("title")
        .text(d => `${d.title}\nPrice: $${d.price}\nRating: ${d.rating}`);
});
