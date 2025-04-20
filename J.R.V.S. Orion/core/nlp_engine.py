from transformers import pipeline

# Załaduj model z Hugging Face
generator = pipeline('text-generation', model='allegro/herbert-base-cased', tokenizer='allegro/herbert-base-cased')

def generate_response(user_input):
    """Generowanie odpowiedzi za pomocą modelu Hugging Face"""
    # Generowanie odpowiedzi w języku polskim
    response = generator(user_input, max_length=100, num_return_sequences=1)
    return response[0]['generated_text']
