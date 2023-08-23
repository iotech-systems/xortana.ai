
var mbltools = {

      init() {
         $("div#btnTopCamTakePic").on("click", mbltools.skyCamTakePic);
      },

      skyCamTakePic() {
         /* "/cam/<camid>/<act>/<args>" */
         let img_prefix = $("#txtImgPrefix").val(), 
            url = `/cam/sky/take_img/(${img_prefix})`;
         $.post(url, (resp) => {
               console.log(resp);
            });
      }

};


/* 
   -- -- [ on doc loaded ] -- -- 
*/
document.addEventListener("DOMContentLoaded", mbltools.init);
