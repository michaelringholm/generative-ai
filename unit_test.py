import json
#import bloom_bot_module as model_bot
#import gpt2_bot_module as model_bot
import dialo_bot_module as model_bot

LLMModelInitDone=False
meta=any
llm="N/A"
def generateResponse(prompt):
    print("generateResponse() called...")
    global LLMModelInitDone
    global meta
    global llm
    if(LLMModelInitDone==False):
        meta=model_bot.init()
        LLMModelInitDone=True

    print("---------------------------------------------------------------")
    generatedResponse=model_bot.generate_response(meta.tokenizer, prompt, meta.device, meta.model)
    json.dumps(generatedResponse)
    return

generateResponse("How are you?")
generateResponse("Do you know what a cake is?")
generateResponse("Do you like cake?")
generateResponse("Is a strawberry cake healthy?")
generateResponse("Do you know what the STAR method is for answering?")
generateResponse("Give a sample reply using that method?")