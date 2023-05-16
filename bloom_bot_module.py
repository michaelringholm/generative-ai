from transformers import BloomForCausalLM, BloomTokenizerFast
import torch
from obj import Obj

def collect_garbage():
    import gc
    del variables
    gc.collect()

def generate_response(tokenizer, input_text, device, model):
    input_ids = tokenizer.encode(input_text, return_tensors='pt').to(device)
    # Generate text
    output = model.generate(input_ids, max_new_tokens=100, num_return_sequences=1)
    # Decode and print generated text
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    print("=============>")
    print(generated_text)
    return generated_text

def init():
    # Load pre-trained model and tokenizer
    #model_name = 'bigscience/bloomz'  # Replace with the desired model name, e.g., 'gpt2-medium'
    #model_name="bigscience/bloomz-1b7"
    model_name="bigscience/bloomz-560m"
    model = BloomForCausalLM.from_pretrained(model_name)
    tokenizer = BloomTokenizerFast.from_pretrained(model_name)

    #collect_garbage()
    torch.cuda.empty_cache()
    # Set device (GPU if available, else CPU)
    device = 'cuda' 
    if torch.cuda.is_available():
        print("Using NVIDIA GPU.")
    else:
        print("No NVIDIDA GPU available, using CPU instead.")
        device='cpu'
    model.to(device)
    print("Welcome to Bloom chat [using:", model_name, "]")
    print("MODEL:", model)
    print("DEVICE:", device)
    print("MODEL_NAME:", model_name)
    return Obj(tokenizer=tokenizer,device=device,model=model,model_name=model_name)

def askQuestions():
    # Encode input text
    meta=init()
    print("Welcome to Bloom chat [using:", meta.model_name, "]")
    print("---------------------------------------------------------------")
    input_text = "In 30 words explain quantum physics?"
    generate_response(input_text, meta.device, meta.model)
    print("---------------------------------------------------------------")
    input_text = "In max 50 words explain the rules of football as we know it in Europe?"
    generate_response(input_text, meta.device, meta.model)
    print("---------------------------------------------------------------")
    input_text = "In 20 words explain cloud computing?"
    generate_response (input_text, meta.device, meta.model)
    input_text = "In 20 words advise me how to make my teenage at home clean her room?"
    generate_response(input_text, meta.device, meta.model)
    input_text = "Create a short story, max 200 words, about a bear, a fox, and them playing football? The fox was evil."
    generate_response(input_text, meta.device, meta.model)




