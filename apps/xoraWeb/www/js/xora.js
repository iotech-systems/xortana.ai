

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
   },

   xoraConsoleWrite(msg) {
      let d = new Date().toLocaleString(), 
         m = `<div class="xora-cons-ln">&nbsp;${d}&nbsp;|&nbsp;${msg}</div>`;
      $("div#xoraConsole").append(m);
   }

};


/* start app here */
document.addEventListener("DOMContentLoaded", () => {
      xora.init();
      xora.run();
   });
