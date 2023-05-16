from transformers import BloomForCausalLM, BloomTokenizerFast
import torch

# Load pre-trained model and tokenizer
#model_name = 'bigscience/bloomz'  # Replace with the desired model name, e.g., 'gpt2-medium'
model_name="bigscience/bloomz-1b7"
model = BloomForCausalLM.from_pretrained(model_name)
tokenizer = BloomTokenizerFast.from_pretrained(model_name)

# Set device (GPU if available, else CPU)
device = 'cuda' 
if torch.cuda.is_available():
    print("Using NVIDIA GPU.")
else:
    print("No NVIDIDA GPU available, using CPU instead.")
    device='cpu'
#model.to(device)

print('current memory allocated: {}'.format(torch.cuda.memory_allocated() / 1024 ** 2))
print('max memory allocated: {}'.format(torch.cuda.max_memory_allocated() / 1024 ** 2))
print('cached memory: {}'.format(torch.cuda.memory_reserved() / 1024 ** 2))