
class CamTop {

   static tickCount = 0;

   constructor() {
      this.tickInterval = 200;
      this.timerInt = 0;
      this.lastTick;
      this.msg;
   }

   init() {
      this.timerInt = setInterval(this.camTick, this.tickInterval);
   }

   run() {
     console.log("camtop run ...");
   }

   camTick() {
      CamTop.tickCount++;
      //console.log(`cam_tick: ${CamTop.tickCount}`);
   }

};
