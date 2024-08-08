Checked warping methods - TPS and Appearance Flow (AF)
AF is a bit computationally costly, but more realistic than TPS.
So right now, for 2D images, anything is fine..but real time k liye TPS would be quicker but thoda poor quality hoga
Similarly for the Inpainting module, Alpha blending is quicker but lighting wagera me seamless blending ka issue hoga . 
Comparatively Diffusion models offer better quality and realism but iska computational cost zada hai

i think keeping realtime in mind, i should go with TPS and follow it with a second order difference constraint to refine the warping. and alpha blending for inpainting
