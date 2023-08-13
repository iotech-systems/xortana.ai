

var xora = {

   topCam: null,

   init() {
      console.log("xora.ini");
      xora.topCam = new CamTop();
      xora.topCam.init();
   },

   run() {
      console.log("run...");
   }

};


/* start app here */
document.addEventListener("DOMContentLoaded", () => {
      xora.init();
      xora.run();
   });
