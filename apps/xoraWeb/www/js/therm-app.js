

var thermoApp = {

   leftCanvasID: "",
   rightCanvasID: "",
   leftSesnor: null,
   rightSensor: null,
   dataUrl: "/read/thermals",

   init() {
      thermoApp.leftSesnor = new amg8833Sensor();
      thermoApp.rightSensor = new amg8833Sensor();
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
