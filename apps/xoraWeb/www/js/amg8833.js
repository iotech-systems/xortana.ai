


class amg8833Sensor {

   tickMS = 200;

   constructor(chan, canvasID, minTemp = 20, maxTemp = 40) {
      this.channel = chan;
      this.canvasID = canvasID;
      this.grid = new amg8833Grid(this.canvasID, 8, 8, minTemp, maxTemp);
      this.grid.init();
      this.data = null;
   }

   init() {
   }

   setData(data) {
      // console.log(`setData: ${this.channel} | ${data}`);
      this.data = data;
   }

   tempToColor(temp) {
      return ""
   }

};


class amg8833Grid {

   constructor(canvasID, cols = 8, rows = 8, minTemp = 20, maxTemp = 40) {
      /* -- */
      this.canvasID = canvasID;
      this.cols = cols;
      this.rows = rows;
      this.minTemp = minTemp;
      this.maxTemp = maxTemp;
      /* -- */
      this.canvas = document.getElementById(this.canvasID);
      if (this.canvas == null)
         console.log(`CanvasIsNull: ${this.canvasID}`);
      console.log([this.canvas.width, this.canvas.height]);
      /* -- */
      this.cntx2d = this.canvas.getContext("2d");
      this.css_width = 0;
      this.css_height = 0;
   }

   init() {
      this.preFillGrid();
   }

   load(arr) {
      /* -- -- */
      let __onrow = function(row) {

         };
      /* -- -- */
      arr.forEach(__onrow);
   }

   preFillGrid() {
      let colorStep = (255 / 8)
         , boxW = 80;
      for (let r = 0; r < this.rows; r++) {
         for (let c = 0; c < this.cols; c++) {
            this.cntx2d.fillStyle = `rgb(${Math.floor(255 - colorStep * r)}, 0, ${Math.floor(255 - colorStep * c)})`;
            this.cntx2d.fillRect(c * boxW, r * boxW, boxW, boxW);
         }
      }
   }
}
