
var thermoApp = {

   MIN_TEMP: 24.0,
   MAX_TEMP: 38.0,
   TICK_INTERVAL: 2000,
   leftSensor: null,
   rightSensor: null,
   leftCanvasID: "leftSensorGrid",
   rightCanvasID: "rightSensorGrid",
   dataUrl: "/read/thermals",
   frameFreq: 0,
   frameFreqTimerID: 0,

   init() {
      /* -- */
      thermoApp.leftSensor = 
         new amg8833Sensor("LEFT", thermoApp.leftCanvasID, thermoApp.MIN_TEMP, thermoApp.MAX_TEMP);
      thermoApp.leftSensor.init();
      /* -- */
      thermoApp.rightSensor = 
         new amg8833Sensor("RIGHT", thermoApp.rightCanvasID, thermoApp.MIN_TEMP, thermoApp.MAX_TEMP);
      thermoApp.rightSensor.init();
      /* -- */
      setTimeout(thermoApp.readThermalData, thermoApp.TICK_INTERVAL);
   },

   readThermalData() {
      $.get(thermoApp.dataUrl, (jsObj) => {
            thermoApp.displayData(jsObj);
         });
   },

   displayData(jsObj) {
      try {
         clearInterval(thermoApp.frameFreqTimerID);
         thermoApp.leftSensor.setData(jsObj.LEFT);
         thermoApp.rightSensor.setData(jsObj.RIGHT);
         /* -- */
         let freq = parseInt(jsObj.FRAME_FREQ),
            tickMS = (1000 / freq);
         thermoApp.sortFrames();
         /* tick frames */
         thermoApp.frameFreqTimerID = 
            setInterval(thermoApp.frameTickCallback, tickMS);
         /* -- */
      } catch(e) {
         console.log(e);
      } finally {
         setTimeout(thermoApp.readThermalData, thermoApp.TICK_INTERVAL);
      }
   },

   frameTickCallback() {
      thermoApp.leftSensor.nextFrameTick();
      thermoApp.rightSensor.nextFrameTick();
   },

   sortFrames() {
      thermoApp.leftSensor.sortFrames();
      thermoApp.rightSensor.sortFrames();
   }

};


/* 
   start app here 
*/
document.addEventListener("DOMContentLoaded", thermoApp.init);
