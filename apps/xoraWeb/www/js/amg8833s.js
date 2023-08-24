


class amg8833Sensor {

   tickMS = 200;

   constructor(canvasID, minTemp = 20, maxTemp = 40) {
      this.convasID = canvasID;
      this.grid = new amg8833Grid(this.canvasID);
      this.grid.init();
   }

   init() {
   }

   tempToColor(temp) {
      return ""
   }

};


class amg8833Grid {

   constructor(canvasID, cols = 8, rows = 8, minTemp = 20, maxTemp = 40) {
      this.canvasID = canvasID;
      this.cols = cols;
      this.rows = rows;
      this.minTemp = minTemp;
      this.maxTemp = maxTemp;
      this.canvas = document.getElementById(this.canvasID);
      if (this.canvas == null)
         console.log(`CanvasIsNull: ${this.canvasID}`);
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
      console.log(this.canvas);
   }

}