// Fragment shader

#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

#define PROCESSING_LIGHT_SHADER

uniform float cx;
uniform float cy;

// These values come from the vertex shader
varying vec4 vertColor;
varying vec3 vertNormal;
varying vec3 vertLightDir;
varying vec4 vertTexCoord;
//Basic Idea: Start with a point, apply operation to it over again(c: given by the shader,
//z: position of the actual pixel we are shading(use texture coord to figure that out)  )
//for loop (starting z: position of the pixel, if magnitude > 50: not in the fractal else different color)

//
vec2 calculateSine(vec2 z) {
  return vec2(sin(z.x)*cosh(z.y),cos(z.x)*sinh(z.y));
}
vec2 complexMult(vec2 a,vec2 b) {
  return vec2(a.x*b.x -a.y *b.y,a.x*b.y + a.y*b.x);
}
void main() { 

  vec4 diffuse_color = vec4 (1.0, 1.0, 1.0, 1.0);
  float diffuse = clamp(dot (vertNormal, vertLightDir),0.0,1.0);
  
  vec2 c = vec2(cx,cy); 
  float real = vertTexCoord.x*(6.28) -3.14;
  float imag = vertTexCoord.y*(6.28) -3.14;
  vec2 z = vec2(real,imag);
  for (int i = 0;i<50;i++) {
    if (length(z) >50) {
      diffuse_color =  vec4(1.0,0.0,0.0,1.0);
      break;
    }

    vec2 z1 = complexMult(c,calculateSine(z));
    z = z1;

  }

  gl_FragColor = vec4(diffuse * diffuse_color.rgb, 1.0);

}