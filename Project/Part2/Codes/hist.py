import torch
from torch.utils.data import Dataset, DataLoader
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Sample custom dataset
class MyDataset(Dataset):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx], self.labels[idx]

# Sample data (100 samples) with 10 classes
data = torch.randn(100, 3, 32, 32)
labels = torch.randint(0, 10, (100,))  # Labels from 0 to 9

# Create dataset and DataLoader
dataset = MyDataset(data, labels)
dataloader = DataLoader(dataset, batch_size=10, shuffle=False)

# Initialize a counter for each class
class_count = np.zeros(10, dtype=int)

# Count occurrences
for _, labels in dataloader:
    for l in labels:
        class_count[l.item()] += 1

# Create a histogram
plt.figure(figsize=(10, 5))
plt.bar(range(10), class_count, color='blue', alpha=0.7)
plt.xlabel('Classes')
plt.ylabel('Number of Samples')
plt.title('Histogram of Class Distribution')
plt.xticks(range(10))  # Set x-ticks to be class numbers
plt.show()
