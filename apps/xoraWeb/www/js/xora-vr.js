

class xoraVR {

   static SKYCAM_PEEK_INTERVAL = 1000;

   constructor() {

   }

   demo() {
      try {
         // console.log("xoraVR::demo");
         // const width = window.innerWidth
         // const height = window.innerHeight
         // // Scene
         // const scene = new THREE.Scene()
         // scene.background = new THREE.Color('#00b140')
         // // Camera
         // const fov = 45 // AKA Field of View
         // const aspect = window.innerWidth / window.innerHeight
         // const near = 0.1 // the near clipping plane
         // const far = 100 // the far clipping plane
         // const camera = new PerspectiveCamera(fov, aspect, near, far)
         // camera.position.set(0, 0, 10)
         // // Renderer
         // const renderer = new THREE.WebGLRenderer()
         // renderer.setSize(window.innerWidth, window.innerHeight)
         // renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
         // // Creating a cube
         // const geometry = new THREE.BoxGeometry(2, 2, 2)
         // const material = new THREE.MeshBasicMaterial({ wireframe: true })
         // const cube = new THREE.Mesh(geometry, material)
         // scene.add(cube)
         // // Rendering the scene
         // const container = document.querySelector('#threejs-container')
         // container.append(renderer.domElement)
         // renderer.render(scene, camera);
      } catch(e) {
         console.log(e);
      }
   }

   init() {
      console.log("xoraVR load...");
      // this.demo();
      /* start skypeek every 488ms */
      setTimeout(this.readSkyCamPeek, xoraVR.SKYCAM_PEEK_INTERVAL);
   }

   run() {

   }

   readSkyCamPeek() {
      /* -- */
      console.log("readSkyCamPeek");
      let _this = this;
      const url = "/peek/skycam";
      $.get(url, function(resp) {
            console.log(resp);      
            setTimeout(_this.readSkyCamPeek, xoraVR.SKYCAM_PEEK_INTERVAL);
         });
      /* -- */
   }

};
