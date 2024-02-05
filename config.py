from openai import OpenAI

client = OpenAI(api_key='YOUR OPENAI API KEY')

def gpt(text):
    completion = client.chat.completions.create(
    model = 'gpt-3.5-turbo', # Any model can be here
    messages = [
        {"role": "system", "content" : "You are a bot assistant imitating a real person."}, # Here the personality of the neural network is set
        {'role': 'user', 'content': f'{text}'}   # Request from the user who processes the neural network
    ],
    temperature = 0.5 # The amount of creativity of the neural network
    )
    
    english_text = completion.choices[0].message.content
    
    return english_text
