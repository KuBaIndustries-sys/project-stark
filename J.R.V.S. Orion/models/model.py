import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
import random

# Wczytanie danych
df = pd.read_csv("dane.csv")
X = df[["cecha1", "cecha2", "cecha3"]].values.tolist()
y = df["wartość_docelowa"].values.tolist()
data = list(zip(X, y))

class JRVS(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(JRVS, self).__init__()
        self.hidden_size = hidden_size
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x, hidden):
        out, hidden = self.lstm(x, hidden)
        out = self.fc(out[:, -1, :])
        return out, hidden

    def init_hidden(self, batch_size):
        return (torch.zeros(1, batch_size, self.hidden_size),
                torch.zeros(1, batch_size, self.hidden_size))

class EvolutionaryTrainer:
    def __init__(self, model, learning_rate=0.001):
        self.model = model
        self.criterion = nn.MSELoss()
        self.optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    def train(self, data, epochs=10):
        for epoch in range(epochs):
            total_loss = 0
            for x, y in data:
                x, y = torch.tensor(x, dtype=torch.float32), torch.tensor(y, dtype=torch.float32)
                hidden = self.model.init_hidden(x.size(0))

                self.optimizer.zero_grad()
                output, _ = self.model(x, hidden)
                loss = self.criterion(output, y)
                loss.backward()
                self.optimizer.step()

                total_loss += loss.item()
            print(f"Epoch {epoch+1}/{epochs}, Loss: {total_loss:.4f}")

    def evolve(self, mutation_rate=0.1):
        for param in self.model.parameters():
            if random.random() < mutation_rate:
                noise = torch.randn_like(param) * 0.1
                param.data += noise
        print("Model evolved!")

    def save_model(self, path="jrvs_model.pth"):
        torch.save(self.model.state_dict(), path)

    def load_model(self, path="jrvs_model.pth"):
        self.model.load_state_dict(torch.load(path))
        self.model.eval()

class AIModel:
    def __init__(self):
        input_size = 3
        hidden_size = 16
        output_size = 1
        self.model = JRVS(input_size, hidden_size, output_size)
        self.trainer = EvolutionaryTrainer(self.model)
        self.trainer.load_model()  # Ładowanie wcześniej wytrenowanego modelu

    def respond(self, user_input):
        # Przykładowa konwersja wejścia tekstowego na dane wejściowe do modelu
        # W rzeczywistości należy to zaimplementować zgodnie z wymaganiami modelu
        processed_input = self.process_input(user_input)
        x = torch.tensor(processed_input, dtype=torch.float32).unsqueeze(0)  # Dodaj wymiar batch_size
        hidden = self.model.init_hidden(x.size(0))
        output, _ = self.model(x, hidden)
        return output.item()  # Zwrócenie wartości odpowiedzi

    def process_input(self, user_input):
        # Przetwarzanie wejścia użytkownika, np. konwersja na wartości cech
        # Tutaj musisz zaimplementować logikę przetwarzania wejścia
        # Na przykład:
        # return [float(value) for value in user_input.split(",")]
        return [0.1, 0.2, 0.3]  # Zastąp to odpowiednim przetwarzaniem

# Przykładowe użycie
if __name__ == "__main__":
    ai_model = AIModel()
    response = ai_model.respond("Przykładowe zapytanie")
    print(f"Odpowiedź modelu: {response}")
