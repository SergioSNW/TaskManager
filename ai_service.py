import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_simple_tasks(description):
    
    if not client.api_key:
        return ["Error. OpenAI API key is not set."]
    
    try: 
        prompt = f"""Break down the following task into 3 to 5 simple, actionable steps.
        
        Task: {description}
        
        Response format:
        - Step one
        - Step two
        - Step three
        etc.
        
        Respond only with the steps, one for each line and startting each step with a dash. Do not include any additional text or explanations."""
        
        params = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant that breaks down complex tasks into simple, actionable steps."},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 150,
            "verbosity": "medium",
            "reasoning-effort": "minimal"
        }
        
        # The double asterisks (**) are used to unpack the params dictionary into keyword arguments for the create method.
        response = client.chat.completions.create(**params)
        
        content = response.choices[0].message.content.strip()
        
        subtasks = []
        
        for line in content.split("\n"):
            line = line.strip()
            if line and line.startswith("-"):
                subtask = line[1:].strip()
                if subtask:
                    substacks.append(subtask)
                
        return subtasks if subtasks else ["Error. No valid steps were generated. Please try again with a different task."]
        
        
    except Exception:
        return ["Error. An error occurred while processing the request."]