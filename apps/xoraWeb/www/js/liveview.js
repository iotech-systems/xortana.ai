
var liveView = null;


class liveViewCls {

   constructor() {
      setInterval(() => {
         this.peekFolder("thums");         
      }, 2000);
   }

   peekFolder(fld) {
      let url = `/view/tf/${fld}`
      $.get(url, (jsObj) => {
            console.log(jsObj);
         });
   }

}

/* -- -- [ on doc loaded ] -- -- */
document.addEventListener("DOMContentLoaded", () => {
      liveView = new liveViewCls();
   });
