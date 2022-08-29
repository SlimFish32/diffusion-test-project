import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

model_id = "CompVis/stable-diffusion-v1-4"
device = "cuda"


pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16, revision="fp16", use_auth_token=True)
pipe = pipe.to(device)

prompt = "a bitcoin in a hot tub"
with autocast("cuda"):
    image = pipe(prompt, guidance_scale=2)["sample"][0]  
    
image.save("hot_bitcoin.png")
