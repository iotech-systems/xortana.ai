

class xoraVR {

   static SKYCAM_PEEK_INTERVAL = 800;

   constructor() {

   }

   init() {
      console.log("xoraVR load...");
      xoraVR.readSkyCamPeek();
   }

   run() { }

   static readSkyCamPeek() {
      let __onresp = (b64) => {      
            let src = `data:image/jpg;base64, ${b64}`,
               imgHtml = `<img class="sky-cam-peek" src="${src}"/>`;
            document.getElementById("skyCamDivBox").innerHTML = imgHtml;
            xora.xoraConsoleWrite("readSkyCamPeek");
            setTimeout(xoraVR.readSkyCamPeek, xoraVR.SKYCAM_PEEK_INTERVAL);
         };
      /* -- */
      $.get("/peek/skycam", __onresp);
   }

};
