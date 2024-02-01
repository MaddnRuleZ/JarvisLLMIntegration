from openai import OpenAI
api_key = "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"

def main_loop():
    print("Started LLM Integration enter exit to exit")

    insertStatement = ""
    while insertStatement != "exit":
        insertStatement = input().split(";")
        string1 = ""
        string2 = ""
        if len(insertStatement) > 0:
            string1 = insertStatement[0]
        elif len(insertStatement) > 1:
            string2 = insertStatement[1]
        client = OpenAI(api_key=api_key)

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": string1},
                {"role": "user", "content": string2}
            ]
        )
        print(completion.choices[0].message.content)

if __name__ == '__main__':
    main_loop()
