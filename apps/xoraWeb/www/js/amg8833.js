
/*
   = = = = = = = = = = = = [ SENSOR ] = = = = = = = = = = = =
*/
class amg8833Sensor {

   constructor(chan, canvasID, minTemp = 20, maxTemp = 40) {
      this.channel = chan;
      this.canvasID = canvasID;
      this.grid = new amg8833Grid(this.canvasID, 8, 8, minTemp, maxTemp);
      this.grid.init();
      this.data = null;
      this.dataLen = 0;
   }

   init() {
   }

   setData(data) {
      this.data = data;
   }

   sortFrames() {
      /* -- */
      console.log(`[ ${this.channel} | sortFrames: ${this.data.length} ]`)
      if (this.data.length == 0)
         return;
      /* -- */
      let _oneach = function(frame) {
            console.log(frame);
            let (idx, buff) = frame.split("::");
            console.log([idx, buff]);
         };
      /* -- */
      this.data.forEach(_oneach);
   }

   nextFrameTick() {
      console.log(`[ ${this.channel} | nextFrameTick ]`);
   }

   tempToColor(temp) {
      return ""
   }

};


/*
   = = = = = = = = = = = = [ GRID ] = = = = = = = = = = = =
*/
class amg8833Grid {

   constructor(canvasID, cols = 8, rows = 8, minTemp = 20, maxTemp = 40) {
      /* -- */
      this.canvasID = canvasID;
      this.cols = cols;
      this.rows = rows;
      this.minTemp = parseFloat(minTemp);
      this.maxTemp = parseFloat(maxTemp);
      this.tempRange = (this.maxTemp - this.minTemp);
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

   rgbFromTemp(tempStr) {
      /* -- */
      let scale = 100, 
         tempFlt = parseFloat(tempStr);
      if (tempFlt < this.minTemp)
         tempFlt = this.minTemp;
      if (tempFlt > this.maxTemp)
         tempFlt = this.maxTemp;
      /* -- */
      let tempInt = parseInt(tempFlt * scale);
      console.log([tempFlt, tempInt]);
      /* -- */
   
   }

   preFillGrid() {
      /* -- */
      let MAX = 255
         , colorStep = (MAX / 8)
         , boxW = 80;
      /* -- */
      for (let r = 0; r < this.rows; r++) {
         for (let c = 0; c < this.cols; c++) {
            /* -- */
            this.cntx2d.fillStyle = 
               `rgb(${Math.floor(MAX - (colorStep * r))}
               , 0
               , ${Math.floor(MAX - (colorStep * c))})`;
            /* -- */
            this.cntx2d.fillRect(c * boxW, r * boxW, boxW, boxW);
         }
      }
      /* -- */
   }
}
