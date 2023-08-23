
var mbltools = {

      init() {
         $("div#btnTopCamTakePic").on("click", mbltools.skyCamTakePic);
      },

      skyCamTakePic() {
         /* -- */
         $("div#btnTopCamTakePic").css("opacity", "0.5");
         $("div#btnTopCamTakePic").off();
         let img_prefix = $("#txtImgPrefix").val(), 
            url = `/cam/sky/take_img/(${img_prefix})`;
         /* -- */
         $.post(url, (resp) => {
               console.log(resp);
            });
         /* -- */
         setInterval(() => {
               $("div#btnTopCamTakePic").css("opacity", "1.0");
               $("div#btnTopCamTakePic").off().on("click", mbltools.skyCamTakePic);
            }, 2400);
      }

};


/* 
   -- -- [ on doc loaded ] -- -- 
*/
document.addEventListener("DOMContentLoaded", mbltools.init);
