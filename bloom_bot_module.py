from transformers import BloomForCausalLM, BloomTokenizerFast
import torch
from obj import Obj
import os

def collect_garbage():
    import gc
    del variables
    gc.collect()

def generate_response(tokenizer, input_text, device, model):
    print("generate_response() called...")
    input_ids = tokenizer.encode(input_text, return_tensors='pt').to(device)
    # Tokens can be words, characters or subwords, sequences are different response variations
    output = model.generate(input_ids, max_length=5000, num_return_sequences=1) 
    print("OUTPUT =============>")
    print(output)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    print("RAW[0] =============>")    
    print(generated_text)
    #print("RAW[1] =============>")    
    #print(tokenizer.decode(output[1], skip_special_tokens=True))
    prompt_length = len(tokenizer.decode(input_ids[0], skip_special_tokens=True))
    generated_text = generated_text[prompt_length:]
    print("CROPPED =============>")
    print(generated_text)
    return generated_text

def init():
    # Load pre-trained model and tokenizer
    print("init() called...")
    os.environ['TRANSFORMERS_CACHE'] = 'd:\cache'
    #model_name = 'bigscience/bloomz'  # Replace with the desired model name, e.g., 'gpt2-medium'

    model_name="bigscience/bloomz-7b1"
    from transformers import AutoModelForCausalLM, AutoTokenizer
    checkpoint = "bigscience/bloomz-7b1"
    tokenizer = AutoTokenizer.from_pretrained(checkpoint)
    model = AutoModelForCausalLM.from_pretrained(checkpoint)
    #model = AutoModelForSequenceClassification.from_pretrained(checkpoint, low_mem=True)    

    
    #model_name="bigscience/bloomz-1b7"
    #model_name="bigscience/bloomz-560m"
    #model = BloomForCausalLM.from_pretrained(model_name)
    #tokenizer = BloomTokenizerFast.from_pretrained(model_name)

    #collect_garbage()
    torch.cuda.empty_cache()
    # Set device (GPU if available, else CPU)
    device = 'cuda' 
    if torch.cuda.is_available():
        print("Using NVIDIA GPU.")
    else:
        print("No NVIDIDA GPU available, using CPU instead.")
        device='cpu'
    device='cpu' # Model too big to fit in VRAM force use of CPU
    model.to(device)
    print("Welcome to Bloom chat [using:", model_name, "]")
    #print("MODEL:", model)
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




