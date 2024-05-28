// Fragment shader
// The fragment shader is run once for every pixel
// It can change the color and transparency of the fragment.

#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

#define PROCESSING_TEXLIGHT_SHADER

// Set in Processing
uniform sampler2D my_texture;
uniform sampler2D my_mask;
uniform float blur_flag;

// These values come from the vertex shader
varying vec4 vertColor;
varying vec3 vertNormal;
varying vec3 vertLightDir;
varying vec4 vertTexCoord;

void main() { 

  // grab the color values from the texture and the mask
  vec4 diffuse_color = texture2D(my_texture, vertTexCoord.xy);
  vec4 mask_color = texture2D(my_mask, vertTexCoord.xy);
  vec4 blur_col = vec4(0,0,0,0);
  int count = 0;
  int blur_radius = -3;
  vec2 texel_size = 1/textureSize(my_texture,0);
  for (int i = blur_radius; i < -blur_radius;i++) {
    for (int j = blur_radius; j < -blur_radius;j++) {
      vec2 xy = vertTexCoord.xy + vec2(i*texel_size.x,j*texel_size.y);
      vec4 sample_color = texture2D(my_texture,xy);
      blur_col += sample_color;
      count += 1;
    }
  }
  diffuse_color = blur_col/count;
  // diffuse_color = (blur_col.r/count,blur_col.g/count,blur_col.b/count,1.0);
  // half sheep, half mask
  // if (vertTexCoord.x > 0.5)
  //   diffuse_color = mask_color;

  // simple diffuse shading model
  // float diffuse = clamp(dot (vertNormal, vertLightDir),0.0,1.0);
  
  gl_FragColor = vec4(diffuse_color.r,diffuse_color.g,diffuse_color.b, 1.0);
}
