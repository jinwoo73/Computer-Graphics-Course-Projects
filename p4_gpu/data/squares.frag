// Fragment shader

#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

#define PROCESSING_LIGHT_SHADER

// These values come from the vertex shader
varying vec4 vertColor;
varying vec3 vertNormal;
varying vec3 vertLightDir;
varying vec4 vertTexCoord;

void main() { 
  float alpha = 0.9;
  float ygap = 0.05;
  float xgap = 0.05;
  float squaresize = 0.14;
  float a = sqrt(2)/2;
  for (int i = 0; i <5;i++) {
    for (int j = 0;j<5;j++) {
      if (i==0 && j==0) {
        continue;
      }
      if (i+j==1) {
        continue;
      }
      if (j-i ==3) {
        continue;
      }
      if (i==0 && j==4 ) {
        continue;
      }
      if (i==4 && j==0) {
        continue;
      }
      if (i - j ==3) {
        continue;
      }
      if (i+j ==7) {
        continue;
      }
      if (i==4 && j ==4) {
        continue;
      }

      // float x = vertTexCoord.x;
      // float y = vertTexCoord.y;
      
      float x = a*vertTexCoord.x -a*vertTexCoord.y;
      float y = a*vertTexCoord.x + a*vertTexCoord.y;
      float top = ygap + i*ygap + i*squaresize;
      float bottom = top + squaresize;
      float left = xgap + j*xgap + j*squaresize;
      float right = left + squaresize;
      

      if (x >= left - 0.48 && x <= right - 0.48 && y >= top+0.22 && y <= bottom+0.22 ) {
        // float newx = a*x -a*y;
        // float newy = a*x + a*y;
	      alpha = 0.0 ;
      }
      
      
    }
  }

  


  gl_FragColor = vec4(0.2, 0.4, 1.0, alpha);
  
  // x = vertTexCoord.x
  // y = vertTexCoord.y

  // alpha = 1.0

  // if (x >= 0.25 && x <= 0.75 && y >= 0.25 && y <= 0.75) {
	//   alpha = 0.0 
  // }`
  // else {
	//   alpha = 1.0
  // }
  // gl_FragColor = vec4(0.2, 0.4, 1.0, vertTexCoord.s);
  
}

