
var liveView = null;
var TICK_INTERVAL = 16000;


class tfViewCls {

   static Instance = null;

   constructor() {
      /* -- */
      setInterval(() => {
            this.peekFolder("thums");         
         }, TICK_INTERVAL);
      /* -- */
      this.last_dirlst = [];
      this.lastLoadedImgCnt = 0;
      $("div#viewPort").html("");
      tfViewCls.Instance = this;
      /* -- */
   }

   init() {
      $("div#topFreeBox").htm(`<div id="lastTickDts"></div>`);
      $("div#viewPort").html("");
      this.peekFolder("thums");
   }

   peekFolder(fld) {
      /* -- */
      let url = `/view/tf/${fld}`;
      let _on_get = function(jsArr) {
            /* -- */
            if (!Array.isArray(jsArr)) {
               console.log(`peekFolder: ${fld} | returned NotArray`);
               return;
            }
            /* -- */
            jsArr.forEach(tfViewCls.Instance.onArrItem);
            let dts = new Date().toLocaleString();
            $("div#lastTickDts").html(dts);
         };
      /* -- */
      $.get(url, _on_get);
   }

   onArrItem(i) {
      /* -- */
      let fn = String(i[0]);
      if (tfViewCls.Instance.last_dirlst.includes(fn))
         return;
      /* -- */
      tfViewCls.Instance.last_dirlst.push(fn);
      $.get(`/load/tf/img/thums/${fn}`, (b64) => {
            let src = `data:image/jpg;base64, ${b64}`,
               dhtml = `<div class="thum-box" fn="${fn}"><img src="${src}"/>` + 
               `<div class="fn-lbl">${fn}</div></div>`;
            /* -- */
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
      liveView = new tfViewCls();
      liveView.init();
   });
