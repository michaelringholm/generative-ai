from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
from torch.utils.data import Dataset, DataLoader

# Load pre-trained model and tokenizer
model_name = 'bert-base-uncased'
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Define your custom dataset
class CustomDataset(Dataset):
    def __init__(self, texts, labels):
        self.texts = texts
        self.labels = labels

    def __getitem__(self, idx):
        encoding = tokenizer(self.texts[idx], truncation=True, padding=True, return_tensors='pt')
        label = torch.tensor(self.labels[idx])
        return encoding, label

    def __len__(self):
        return len(self.texts)

# Load your custom dataset
train_texts = ['Example sentence 1', 'Example sentence 2']
train_labels = [0, 1]  # Example binary labels (0 or 1)

train_dataset = CustomDataset(train_texts, train_labels)
train_dataloader = DataLoader(train_dataset, batch_size=16, shuffle=True)

# Fine-tune the model
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-5)
loss_fn = torch.nn.CrossEntropyLoss()

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

model.train()
for epoch in range(3):  # Adjust the number of epochs as needed
    running_loss = 0.0
    for inputs, labels in train_dataloader:
        inputs = {key: value.to(device) for key, value in inputs.items()}
        labels = labels.to(device)

        optimizer.zero_grad()
        outputs = model(**inputs)
        loss = loss_fn(outputs.logits, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()

    epoch_loss = running_loss / len(train_dataloader)
    print(f"Epoch {epoch + 1} Loss: {epoch_loss:.4f}")

# Save the fine-tuned model
model.save_pretrained('fine_tuned_model')
tokenizer.save_pretrained('fine_tuned_model')
