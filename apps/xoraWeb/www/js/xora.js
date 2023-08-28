

var xora = {

   topCam: null,
   xorVR: null,

   init() {
      console.log("xora.ini");
      xora.topCam = new CamTop();
      xora.topCam.init();
      /* vr env. */
      xora.xorVR = new xoraVR();
      xora.xorVR.init();
      xora.xorVR.run();
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
