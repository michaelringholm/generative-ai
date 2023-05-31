from transformers import pipeline, set_seed
import os


def run_pipeline():
    # Specify the path to the generation configuration file
    generation_config_path = "./gpt2-test/config.json"
    generator = pipeline('text-generation', model='gpt2', device=0, config=generation_config_path)
    # Check the device on which the model is loaded
    device = generator.model.device
    if "cuda" in str(device):
        print("Model is using GPU")
    else:
        print("Model is using CPU")
    set_seed(5000)
    prompt="Write a small sample text using the STAR method, mark each section of the method with the corresponding letter such as S:, T:, A:, R: in your response,"
    prompt="Write a short story about a bear and a mouse"
    prompt="Once upon a time, there was a big bear and a mouse who were best friends,"
    generated_text_seq=generator(prompt, max_length=150, num_return_sequences=3)
    for generated_text in generated_text_seq:
        print(generated_text)
        #print_json_obj(generated_text)
    return

def download_model():
    from transformers import GPT2Tokenizer, GPT2Config, GPT2Model
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    model = GPT2Model.from_pretrained('gpt2')
    print("Model and tokenizer loaded successfully.")
    return

def print_json_obj(json_object):
    import json
    json_formatted_str = json.dumps(json_object, indent=2)
    print(json_formatted_str)
    return

def print_json_str(raw_json):
    import json
    json_object = json.loads(raw_json)
    json_formatted_str = json.dumps(json_object, indent=2)
    print(json_formatted_str)
    return

def main():
    os.system("cls")
    #download_model()
    run_pipeline()

main()