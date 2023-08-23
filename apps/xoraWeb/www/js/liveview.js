
var liveView = null;


class liveViewCls {

   constructor() {
      setInterval(() => {
         this.peekFolder("thums");         
      }, 2000);
   }

   peekFolder(fld) {
      let _this = this, 
         url = `/view/tf/${fld}`
      /* -- -- */
      $.get(url, function(jsArr) {
            $("div#viewPort").html("");
            _this.showThums(jsArr);
            /* -- -- */
            jsArr.forEach((i) => {
                  $.get(`/load/tf/img/thums/${i}`, (b64) => {
                        let src = `data:image/jpg;base64, ${b64}`,
                           dhtml = `<div><img src="${src}"></div>`;
                        $("div#viewPort").html(dhtml);
                     });
               });
            /* -- -- */
         });
      /* -- -- */
   }

   /* <img src="data:image/png;base64, iVBORw0KGgoAAAANSUhEUgAAAAUA
      AAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO
         9TXL0Y4OHwAAAABJRU5ErkJggg==" alt="Red dot" /> */
   showThums(arr) {
      arr.forEach((i) => {
            let src = "/", 
               dhtml = `<div><img src="${src}"></div>`;
            $("div#viewPort").html(dhtml);   
         });
   }

}

/* -- -- [ on doc loaded ] -- -- */
document.addEventListener("DOMContentLoaded", () => {
      liveView = new liveViewCls();
   });
