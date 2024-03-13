import torch
from torch.utils.data import DataLoader
from sklearn.model_selection import KFold

from src.dataset import Fruits
from src.logger import Logger


def train():
    BATCH_SIZE = 4

    logger = Logger()
    logger.log_training_loss(1, 0.5)  # Example usage of logger

    dataset = Fruits(file="utils/train_fruits.csv")
    print(len(dataset))

    kf = KFold(n_splits=5, shuffle=True, random_state=64)

    for fold, (train_index, val_index) in enumerate(kf.split(dataset)):
        print("Fold: ", fold)
        train_dataset = torch.utils.data.Subset(dataset, train_index)
        val_dataset = torch.utils.data.Subset(dataset, val_index)

        train_dataloader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True, num_workers=4)
        val_dataloader = DataLoader(val_dataset, batch_size=BATCH_SIZE, shuffle=True, num_workers=4)

        for sample in train_dataloader:
            print(sample.shape)
            print(torch.max(sample))
            print(torch.min(sample))
            break

        for sample in val_dataloader:
            print(sample.shape)
            print(torch.max(sample))
            print(torch.min(sample))
            break


if __name__ == "__main__":
    train()
