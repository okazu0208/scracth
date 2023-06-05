import torch
from torch.cuda.amp import autocast
from diffusers import StableDiffusionPipeline
import cv2
ldm = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4",
 revision="fp16",
 torch_dtype=torch.float32,
 use_auth_token='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')
prompt = '猫'
with autocast(enabled=torch.cuda.is_available()):
 image = ldm(prompt, height=400, width=400).images[0]
 image.save("ai.png")