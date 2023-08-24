

var thermoApp = {

   leftCanvasID: "leftSensorGrid",
   rightCanvasID: "rightSensorGrid",
   leftSesnor: null,
   rightSensor: null,
   dataUrl: "/read/thermals",

   init() {
      /* -- */
      thermoApp.leftSesnor = new amg8833Sensor(thermoApp.leftCanvasID);
      thermoApp.leftSesnor.init();
      /* -- */
      thermoApp.rightSensor = new amg8833Sensor(thermoApp.rightCanvasID);
      thermoApp.rightSensor.init();
      /* -- */
      setInterval(thermoApp.readThermalData, 2000);
   },

   readThermalData() {
      $.get(thermoApp.dataUrl, (jsArr) => {
            console.log(jsArr);
         });
   }

};


/* 
   start app here 
*/
document.addEventListener("DOMContentLoaded", thermoApp.init);
