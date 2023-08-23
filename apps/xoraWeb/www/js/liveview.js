
var liveView = null;
var TICK_INTERVAL = 16000;


class liveViewCls {

   static Instance = null;

   constructor() {
      /* -- */
      setInterval(() => {
            this.peekFolder("thums");         
         }, TICK_INTERVAL);
      /* -- */
      this.last_dirlst = [];
      $("div#viewPort").html("");
      liveViewCls.Instance = this;
      /* -- */
   }

   peekFolder(fld) {
      /* -- */
      let url = `/view/tf/${fld}`;
      /* -- */
      let _on_get = function(jsArr) {
            console.log(jsArr);
            jsArr.forEach(liveViewCls.Instance.onArrItem);
            console.log(liveViewCls.Instance.last_dirlst);
         };
      /* -- */
      $.get(url, _on_get);
   }

   onArrItem(i) {
      /* -- */
      console.log(i);
      if (liveViewCls.Instance.last_dirlst.includes(i))
         return;
      /* -- */
      console.log(i);
      liveViewCls.Instance.last_dirlst.append(i);
      /* -- */
      $.get(`/load/tf/img/thums/${i}`, (b64) => {
            let src = `data:image/jpg;base64, ${b64}`,
               dhtml = `<div class="thum-box" fn="${i}"><img src="${src}"></div>`;
            $("div#viewPort").append(dhtml);
         });
      /* -- */
   }

   /* <img src="data:image/png;base64, iVBORw0KGgoAAAANSUhEUgAAAAUA
      AAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO
         9TXL0Y4OHwAAAABJRU5ErkJggg==" alt="Red dot" /> */
   showThums(arr) {
      /* -- */
      let __oneach = function(i) {
            let src = "/",
               dhtml = `<div><img src="${src}"></div>`;
            $("div#viewPort").html(dhtml); 
         };
      /* -- */
      arr.forEach(__oneach);
   }

}

/* -- -- [ on doc loaded ] -- -- */
document.addEventListener("DOMContentLoaded", () => {
      liveView = new liveViewCls();
   });
