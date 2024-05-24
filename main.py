from openai import OpenAI

def describe_recording(recording_data):
    # Define the prompt for identifying the field name
    prompt = f"""
        You're a test automation speciailist.
        Provided is a json file containing a list of steps performed by a user during a test recording. The steps are proved as a list.
        Each step provided metadata surrounding the interaction type, field, and page.
        
        Recordings completed on Microsoft's D365 Finance & Operations will also include extra information, such as the fields role, controlname and the form it belongs to.
        
        From this steps file. Figure out what the test is trying to achieve and write a concise description. do not include any information that is not required e.g. reference to the json file, data/values used in the steps, filter words, introduction, summary.
        
        E.g.
        
        "Creates a sales order with a hardware item, and then confirms it. After confirmation the test invoices and delivers the final amount".

        JSON data with steps:
        {recording_data}
        """
    #print(prompt)
    #print("\n\n\n\n")
    # Make the API request
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": "You are an automation engineer."},
            {"role": "user", "content": prompt}
        ]
    )
    #input_cost = response.usage.prompt_tokens * 0.0000005
    #output_cost = response.usage.completion_tokens * 0.0000015
    #print("$", input_cost + output_cost, sep="")
    # Parse the response
    if len(response.choices) > 0:
        return response.choices[0].message.content
    else:
        return ""



# Example usage
client = OpenAI()

with open('input.txt', 'r') as file:
    recording_data = file.read()

desc = describe_recording(recording_data)
print(desc)