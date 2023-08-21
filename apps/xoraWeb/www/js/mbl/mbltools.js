
var mbltools = {

      init() {
         // $("div.btn-menu").on("click", () => {
         //    });
         $("div#btnTopCamTakePic").on("click", mbltools.skyCamTakePic);
      },

      skyCamTakePic() {
         /* "/cam/<camid>/<act>/<args>" */
         let url = "/cam/sky/take_img/('someapth.abdc.a'; arg1; 44; 'run')";
         $.post(url, (resp) => {
               console.log(resp);
            });
      }

};


/* -- -- [ on doc loaded ] -- -- */
document.addEventListener("DOMContentLoaded", mbltools.init);
