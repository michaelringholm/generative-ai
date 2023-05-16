from transformers import GPT2LMHeadModel, GPT2Tokenizer, BloomModel, BloomTokenizerFast
import torch

# Load pre-trained model and tokenizer
model_name = 'gpt2'  # Replace with the desired model name, e.g., 'gpt2-medium'
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Set device (GPU if available, else CPU)
device = 'cuda' 
if torch.cuda.is_available():
    print("Using NVIDIA GPU.")
else:
    print("No NVIDIDA GPU available, using CPU instead.")
    device='cpu'
model.to(device)

# Encode input text
input_text = "In 30 words explain quantum physics?"
input_ids = tokenizer.encode(input_text, return_tensors='pt').to(device)

# Generate text
output = model.generate(input_ids, max_length=100, num_return_sequences=1)

# Decode and print generated text
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print("Generated text:", generated_text)
