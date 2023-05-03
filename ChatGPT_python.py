import openai


openai.api_key = "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" 

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write me a story for: " + prompt + "Make this story fitting for children and incorporate a good lesson in the end of the story.",
        max_tokens=50,
        n=1,
        stop=None,

        #look into possibly adding presence_penalty or frequency_penalty on top of temperature as well. 
        
        ## "Reasonable values for the penalty coefficients are around 0.1 to 1 if the aim is to just reduce
        #  repetitive samples somewhat. If the aim is to strongly suppress repetition, then one can increase
        #  the coefficients up to 2, but this can noticeably degrade the quality of samples. Negative values
        ## can be used to increase the likelihood of repetition." -OpenAI API

        temperature=0.5,
    )
        
    return response.choices[0].text.strip()

