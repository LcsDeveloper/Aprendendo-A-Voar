import torch
from torch.utils.data import Dataset, DataLoader

class GetData(Dataset):
    def __init__(self, path_data):
        self.data = []
        with open(path_data, "r") as arq:
            lines = arq.readlines()
            for line in lines:
                l = line.split()
                self.data = [(float(l[0]), float(l[1]))]
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, i):
        return self.data[i]