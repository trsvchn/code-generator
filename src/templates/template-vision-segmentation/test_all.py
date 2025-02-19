import os
from argparse import Namespace

import pytest
from data import setup_data
from torch import Tensor
from torch.utils.data.dataloader import DataLoader


@pytest.mark.skipif(os.getenv("RUN_SLOW_TESTS", 0) == 0, reason="Skip slow tests")
def test_setup_data():
    config = Namespace(
        data_path="~/data", train_batch_size=1, eval_batch_size=1, num_workers=0
    )
    dataloader_train, dataloader_eval = setup_data(config)

    assert isinstance(dataloader_train, DataLoader)
    assert isinstance(dataloader_eval, DataLoader)
    train_batch = next(iter(dataloader_train))
    assert isinstance(train_batch, dict)
    assert isinstance(train_batch["image"], Tensor)
    assert isinstance(train_batch["mask"], Tensor)
    assert train_batch["image"].ndim == 4
    assert train_batch["mask"].ndim == 3
    eval_batch = next(iter(dataloader_eval))
    assert isinstance(eval_batch, dict)
    assert isinstance(eval_batch["image"], Tensor)
    assert isinstance(eval_batch["mask"], Tensor)
    assert eval_batch["image"].ndim == 4
    assert eval_batch["mask"].ndim == 3
