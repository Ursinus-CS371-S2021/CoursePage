class Canvas2D {
	constructor() {
		this.container = document.getElementById("Canvas2DContainer");
		this.canvas = d3.select("#Canvas2D");
		this.canvas.on("mousedown", this.mouseDown.bind(this));

		// Clear all graph elements if any exist
		this.canvas.selectAll("*").remove();
		this.points = this.canvas.append("g")
		.attr("class", "points");
		this.lines = this.canvas.append("g")
		.attr("class", "lines");

		this.canvas.call(d3.zoom()
			.scaleExtent([1/4, 8])
			.on("zoom", this.zoomed.bind(this))
			.filter(function () {
				return d3.event.ctrlKey;
		}));
	}

	/**
	  * Return a list of points as a 2D array
	  * @return A 2d array of the form [[x1, y1], [x2, y2], ...]
	  */
	getPoints() {
		let P = [];
		d3.selectAll("circle").each(function() {
			let sel = d3.select(this);
			const x = parseFloat(sel.attr("cx"));
			const y = parseFloat(sel.attr("cy"))
			P.push([x, y]);
		});
		return P;
	}

	/**
	 * 
	 * @param {float} x1 x position of first endpoint
	 * @param {float} y1 y position of first endpoint
	 * @param {float} x2 x position of second endpoint
	 * @param {float} y2 y position of second endpoint
	 * @param {array} color [r, g, b] color spec 
	 * @param {float} width Width of line
	 */
	drawLine(x1, y1, x2, y2, color, width) {
		if (color === undefined) {
			color = [0, 0, 0];
		}
		if (width === undefined) {
			width = 2;
		}
		this.lines.append("line")
		.attr("x1", x1)
		.attr("y1", y1)
		.attr("x2", x2)
		.attr("y2", y2)
		.attr("stroke", d3.rgb(color[0], color[1], color[2]))
		.attr("stroke-width", width);
		
	}

	/**
	 * Remove all of the points from the canvas
	 */
	clearPoints() {
		d3.select(".points").remove();
		this.points = this.canvas.append("g")
		.attr("class", "points");
	}

	/**
	 * Remove all of the line segments from the canvas
	 */
	clearLines() {
		d3.select(".lines").remove();
		this.lines = this.canvas.append("g")
		.attr("class", "lines");
	}

	/**
	 * Remove a particular point from the canvas
	 */
	removeNode() {
		d3.select(this).remove();
	}

	/**
	 * React to a mouse down event by adding a node
	 */
	mouseDown() {
		let point = d3.mouse(d3.event.currentTarget);
		this.points.append("circle")
			.attr("r", 5)
			.attr("fill", d3.rgb(0, 0, 0))
			.attr("cx", point[0])
			.attr("cy", point[1])
			.call(d3.drag()
			.on("drag", this.dragNode)
			)
			.on("dblclick", this.removeNode)
	}

	/** A callback function to handle dragging on a node */
	dragNode() {
		d3.select(this).attr("cx", d3.event.x);
		d3.select(this).attr("cy", d3.event.y);
	}

	/** A callback function to handle zooming/panning */
	zoomed() {
		this.points.attr("transform", d3.event.transform);
	}

	/**
	 * A function which toggles all of the visible elements to show
	 */
	show = function() {
		this.container.style("display", "block");
	}

	/**
	 * A function which toggles all of the visible elements to hide
	 */
	hide = function() {
		this.container.style("display", "none");
	}

}
