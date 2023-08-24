

var thermoApp = {

   MIN_TEMP: 20.0,
   MAX_TEMP: 40.0,
   /* -- */
   leftSesnor: null,
   rightSensor: null,
   leftCanvasID: "leftSensorGrid",
   rightCanvasID: "rightSensorGrid",
   dataUrl: "/read/thermals",

   init() {
      /* -- */
      thermoApp.leftSesnor = 
         new amg8833Sensor(thermoApp.leftCanvasID, thermoApp.MAX_TEMP, thermoApp.MAX_TEMP);
      thermoApp.leftSesnor.init();
      /* -- */
      thermoApp.rightSensor = 
         new amg8833Sensor(thermoApp.rightCanvasID, thermoApp.MAX_TEMP, thermoApp.MAX_TEMP);
      thermoApp.rightSensor.init();
      /* -- */
      setInterval(thermoApp.readThermalData, 2000);
   },

   readThermalData() {
      $.get(thermoApp.dataUrl, (jsObj) => {
            thermoApp.displayData(jsObj);
         });
   },

   displayData(jsObj) {
      /* -- */
      let lft = jsObj.LEFT,
         rgt = jsObj.RIGHT;
      /* -- */
      console.log([lft, rgt]);
   }

};


/* 
   start app here 
*/
document.addEventListener("DOMContentLoaded", thermoApp.init);
