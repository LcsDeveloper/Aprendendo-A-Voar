import numpy as np
import torch
from torch import nn
from torch.utils.data import Dataset, DataLoader
import matplotlib.pyplot as plt

import getdata
import network

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Rodando na {device}")

train_dataset = getdata.GetData("../data/data1_teste.txt")
train_dataloader = DataLoader(train_dataset, batch_size=2444, shuffle=True)

model = network.Network().to(device)
lossfunc = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)

def train(model, dataloader, lossfunc, optimizer):
    model.train()
    cumloss = 0.0
    for X, y in dataloader:
        X = X.unsqueeze(1).float().to(device)
        y = y.unsqueeze(1).float().to(device)

        pred = model(X)
        loss = lossfunc(pred, y)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        cumloss += loss.item() 
  
    return cumloss / len(dataloader)

def plot_comparinson(model, interval=(-10, 10), nsamples=10):
    fig, ax = plt.subplots(figsize=(10, 10))

    ax.grid(True, which='both')
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')

    samples = np.linspace(interval[0], interval[1], nsamples)
    model.eval()
    with torch.no_grad():
        pred = model(torch.tensor(samples).unsqueeze(1).float().to(device))

    ax.plot(samples, pred.cpu(), label="model")
    plt.legend()
    plt.show()

epochs = 20000
for t in range(epochs):
    train_loss = train(model, train_dataloader, lossfunc, optimizer)
    if t % 10 == 0:
        print(f"Epoch: {t}; Train Loss: {train_loss}")
    
plot_comparinson(model, [-100, 100], 100)
    
torch.save(model.state_dict(), "../model/model.pt")


