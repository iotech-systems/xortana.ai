


class amg8833Sensor {

   tickMS = 200;

   constructor(canvasID) {
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

   constructor(canvasID, cols = 8, rows = 8) {
      this.divID = divID;
      this.cols = cols;
      this.rows = rows;
      this.canvas = document.getElementById(canvasID);
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