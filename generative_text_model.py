from transformers import pipeline

print("Loading GPT-2 model... Please wait.")

# Load GPT-2 model
generator = pipeline(
    "text-generation",
    model="gpt2"
)

print("Model Loaded Successfully!")

while True:

    prompt = input("\nEnter a topic (or type 'exit' to quit): ")

    if prompt.lower() == "exit":
        print("Exiting Program...")
        break

    result = generator(
        prompt,
        max_length=150,
        num_return_sequences=1,
        temperature=0.8,
        do_sample=True
    )

    print("\nGenerated Text:\n")
    print(result[0]["generated_text"])
    print("\n" + "="*60)