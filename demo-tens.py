import tensorflow as tf
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained model and tokenizer
model_name = 'gpt2'  # Replace with the desired model name, e.g., 'gpt2-medium'
model = TFGPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Encode input text
input_text = "Write a code snippet for uploading a string to S3"
input_ids = tokenizer.encode(input_text, return_tensors='tf')

# Generate text
output = model.generate(input_ids, max_length=200, num_return_sequences=1)
print("Generated text:", output[0])
print("Generated text:", output[1])
print("Generated text:", output[2])

# Decode and print generated text
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print("Generated text:", generated_text)
