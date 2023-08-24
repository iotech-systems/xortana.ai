

var thermoApp = {

   MIN_TEMP: 20.0,
   MAX_TEMP: 40.0,
   /* -- */
   leftSensor: null,
   rightSensor: null,
   leftCanvasID: "leftSensorGrid",
   rightCanvasID: "rightSensorGrid",
   dataUrl: "/read/thermals",

   init() {
      /* -- */
      thermoApp.leftSensor = 
         new amg8833Sensor("LEFT", thermoApp.leftCanvasID, thermoApp.MAX_TEMP, thermoApp.MAX_TEMP);
      thermoApp.leftSensor.init();
      /* -- */
      thermoApp.rightSensor = 
         new amg8833Sensor("RIGHT", thermoApp.rightCanvasID, thermoApp.MAX_TEMP, thermoApp.MAX_TEMP);
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
      thermoApp.leftSensor.setData(jsObj.LEFT);
      thermoApp.rightSensor.setData(jsObj.RIGHT);
   }

};


/* 
   start app here 
*/
document.addEventListener("DOMContentLoaded", thermoApp.init);
