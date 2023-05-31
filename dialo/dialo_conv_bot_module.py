# GPT-2 is a probabilistic model, and its responses are generated based on statistical patterns learned from the training data. While these suggestions can help mitigate the issue, complete control over the model's output is challenging
from transformers import AutoModelForCausalLM as SelectedModel
from transformers import AutoTokenizer as SelectedTokenizer
import torch
import os

def collect_garbage():
    import gc
    del variables
    gc.collect()

def try_model():
    from transformers import AutoModelForCausalLM, AutoTokenizer
    import torch


    tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-large", padding_side='left')
    model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-large")

    # Let's chat for 6 lines
    for step in range(6):
        # encode the new user input, add the eos_token and return a tensor in Pytorch
        new_user_input_ids = tokenizer.encode(input(">> User:") + tokenizer.eos_token, return_tensors='pt')

        # append the new user input tokens to the chat history
        bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

        # generated a response while limiting the total chat history to 1000 tokens, 
        chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

        # pretty print last ouput tokens from bot
        print("DialoGPT: {}".format(tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)))
    return

def generate_response(tokenizer, input_text, device, model):
    print("generate_response() called...")
    #from transformers import AutoTokenizer, AutoModelForCausalLM

    input_ids = tokenizer.encode(input_text, return_tensors='pt').to(device)
    # You can modify temperature, this value is used to adjust the randomness of the generated output. Higher values (e.g., 1.0) will produce more diverse and random responses, while lower values (e.g., 0.2) will make the output more focused and deterministic.
    temperature=1.0
    # Tokens can be words, characters or subwords, sequences are different response variations
    output = model.generate(input_ids, max_length=1000, do_sample=True, pad_token_id=tokenizer.eos_token_id, temperature=temperature) 
    #generated_text = tokenizer.decode(output[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    #generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    generated_text = tokenizer.decode(output[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    print("RAW[0] =============>")    
    print(generated_text)
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

    model_name="microsoft/DialoGPT-medium"    
    tokenizer = SelectedTokenizer.from_pretrained(model_name)
    model = SelectedModel.from_pretrained(model_name)
    
    #encoded_input = tokenizer(text, return_tensors='pt')
    #output = model(**encoded_input)
    
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
    #device='cpu' # force use of CPU
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




