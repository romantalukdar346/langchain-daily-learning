from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM

# load_dotenv()
# llm = HuggingFaceEndpoint(
#     repo_id="HuggingFaceH4/zephyr-7b-beta",
#     task="text_generation"
# )

# model = ChatHuggingFace(llm=llm)
# Define the structure of the output using Pydantic
# This will help in parsing the output into a structured format 

model= OllamaLLM(model="phi3:mini")
# model= OllamaLLM(model="llama3.2")

json_schema= {
   "title": "Review",
   "type": "object",

   "proparties":{
            "Key_themes":{
                "type": "array",
                "items":{
                    "type":"string"
                    }
                },
    
            "summary":{
                "type": "string",
                "description": "A brief summary of the review"
                },

            "sentiment":{
                "type": "string",
                "enum": ["positive", "negative"],
                "description": "Overall sentiment of the review"
                },

            "pros":{
                "type": ["array", "null"],
                "items":{
                    "type": "string",
                    "description": "List of positive aspects mentioned in the review"
                    }
                },

            "cons":{
                "type": ["array", "null"],
                "items":{
                    "type": "string",
                    "description": "List of negative aspects mentioned in the review"
                    }
                },

            "name":{
                "type": ["string", "null"],
                "description": "Name of the reviewer",
                "default": "Roman"
                }

    },
    "requeired": ["Key_themes", "summary", "sentiment","name"]
}

structured_output = model.with_structured_output(json_schema)

result = structured_output.invoke(
    """I bought this phone when I cracked the screen on my Galaxy S9 and realized that a replacement screen at $160 was only slightly less expensive than an entirely new phone.

I initially looked at used phones in the Galaxy S series, but even these from a couple generations ago were not cheaper, and lacked some features.

This phone is excellent. It has a large, bright screen. I'm a fan that it does not have rounded edges on the screen, which should help against breaking in the future. It has expandable storage, it can take a physical SIM card and an eSIM, and it's 5G capable.

The only things I don't prefer about this phone is that the camera (despite the reported mega pixel count) seems like it over sharpens pictures to compensate for lower quality, the rumble/vibrate feels cheaper (and louder) than my previous phone, and there are a few occasions where it performs a bit sluggish or apps in the background have to restart due to limited memory.

All in all, this phone has everything I wanted, and at a price where if another break occurs I could just as easily replace it than deal with a costly fix. If you need the best camera or extra do-dads (like built in AI, or extra buttons for virtual assistants that I find annoying) you may benefit from paying more, but if you're looking for a solid phone for browsing, streaming or messaging, this is it.""")


print("---------------------------------------------------------")
print(result.Key_themes)
print(result.summary)
print(result.sentiment) 
("---------------------------------------------------------")
