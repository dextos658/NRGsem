import { Vector } from './math/Vector.js';
import { Matrix } from './math/Matrix.js';
import { Quaternion } from './math/Quaternion.js';

export class Camera {

constructor(options) {
  
    Object.assign(this, {
        fovX       : 1,
        fovY       : 1,
        near       : 0.1,
        far        : 5,
        zoomFactor : 0.001
    }, options);

    this.position = new Vector();
    console.log("Position")
    console.log(this.position)
    this.rotation = new Quaternion();
    console.log("Rotation")
    console.log(this.rotation)
    this.viewMatrix = new Matrix();
    this.projectionMatrix = new Matrix();
    this.transformationMatrix = new Matrix();
    this.isDirty = false;
}

updateViewMatrix() {
    console.log("updateViewMatrix")
    this.rotation.toRotationMatrix(this.viewMatrix.m);
    console.log(this.rotation)
    console.log(this.position)
    this.viewMatrix.m[ 3] = this.position.x;
    this.viewMatrix.m[ 7] = this.position.y;
    this.viewMatrix.m[11] = this.position.z;
    this.viewMatrix.inverse();
}

updateProjectionMatrix() {
    console.log("updateProjectionMatrix")
    const w = this.fovX * this.near;
    const h = this.fovY * this.near;
    this.projectionMatrix.fromFrustum(-w, w, -h, h, this.near, this.far);
}

updateMatrices() {
    console.log("upade")
    this.updateViewMatrix();
    this.updateProjectionMatrix();
    this.transformationMatrix.multiply(this.projectionMatrix, this.viewMatrix);
}

resize(width, height) {
    console.log("resize")
    this.fovX = width * this.zoomFactor;
    this.fovY = height * this.zoomFactor;
    this.isDirty = true;
}

zoom(amount) {
    console.log("zoom")
    const scale = Math.exp(amount);
    this.zoomFactor *= scale;
    this.fovX *= scale;
    this.fovY *= scale;
    this.isDirty = true;
}

}
