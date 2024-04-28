import pandas as pd
import json

# Initialize empty lists to store prompts and responses
prompts = []
responses = []

# Open the JSONL file and read each line
with open(r'C:\Users\PK\Desktop\projects\Finetune_LLM\decision_support_system_GPT_3_5\training_examples.jsonl', 'r') as file:
    for line in file:
        data = json.loads(line)
        # print(data)
        messages = data['messages']
        for message in messages:
            if message["role"] == "user":
                prompts.append(message["content"])
            elif message["role"] == "assistant":
                responses.append(message["content"])

# Create DataFrame
df = pd.DataFrame({"prompt": prompts, "response": responses})

# Display the DataFrame
print(df)

df.to_excel('training_samples.xlsx')