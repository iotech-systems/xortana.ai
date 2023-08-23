
var liveView = null;


class liveViewCls {

   constructor() {
      setInterval(() => {
         this.peekFolder("thums");         
      }, 8000);
      this.last_dirlst = [];
   }

   peekFolder(fld) {
      let _this = this, 
         url = `/view/tf/${fld}`
      /* -- -- */
      $.get(url, function(jsArr) {
            console.log(jsArr);
            $("div#viewPort").html("");
            jsArr.forEach((i) => {
                  /* -- */
                  if (_this.last_dirlst.includes(i))
                     return;
                  /* -- */
                  console.log(i);
                  _this.last_dirlst.append(i);
                  $.get(`/load/tf/img/thums/${i}`, (b64) => {
                        let src = `data:image/jpg;base64, ${b64}`,
                           dhtml = `<div class="thum-box"><img src="${src}"></div>`;
                        $("div#viewPort").append(dhtml);
                     });
                  /* -- */
               });
            /* -- -- */
            console.log(_this.last_dirlst);
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
