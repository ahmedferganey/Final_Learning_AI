# PyTorch Transfer Learning & Experiment Tracking — FoodVision Mini

## Overview

This project explores **transfer learning** in PyTorch by building an image classifier — **FoodVision Mini** — that distinguishes between **pizza, steak, and sushi** images. It starts from a pretrained CNN backbone (EfficientNet) rather than training from scratch, then extends into a second phase of **systematic experiment tracking** using TensorBoard to compare multiple model/data/epoch combinations and select the best-performing model.

The notebook builds on utilities (`data_setup.py`, `engine.py`, `utils.py`, `predictions.py`) from an earlier "PyTorch Going Modular" stage of the same course series, reusing them as importable helper modules rather than rewriting boilerplate.

## Dataset

- **FoodVision Mini** — a 3-class subset of the Food101 dataset: `pizza`, `steak`, `sushi`
- Two versions used across experiments:
  - **10% dataset** — smaller training subset
  - **20% dataset** — larger training subset (double the data)
- A fixed test set (from the 10% split) is used to evaluate all experiments consistently

## Part 1 — Transfer Learning Fundamentals

### 1. Setup
- Verifies `torch`/`torchvision` versions, installs `torchinfo` for model summaries
- Pulls in the `going_modular` helper scripts (`data_setup.py`, `engine.py`) from the course GitHub repo
- Sets device-agnostic code (`cuda` if available, else `cpu`)

### 2. Data Preparation
- Downloads and unzips the pizza/steak/sushi dataset
- Builds `train`/`test` DataLoaders via a reusable `create_dataloaders()` function
- Demonstrates **two ways to create image transforms**:
  - **Manual transforms** (`transforms.Compose` with resize, tensor conversion, ImageNet normalization)
  - **Automatic transforms** — pulled directly from a pretrained model's associated weights (`weights.transforms()`), introduced in `torchvision` v0.13+

### 3. Pretrained Model Setup (EfficientNet-B0)
- Loads `EfficientNet_B0` with `DEFAULT` (best available) ImageNet weights
- Inspects architecture via `torchinfo.summary()` (features → avgpool → classifier)
- **Freezes** the convolutional feature-extractor layers (`requires_grad = False`)
- Replaces the **classifier head** with a new `Dropout + Linear` layer matching the 3 target classes
- Confirms via summary that only the new classifier head is trainable

### 4. Training & Evaluation
- Trains using `CrossEntropyLoss` + `Adam` optimizer (lr = 0.001) via the reusable `engine.train()` function
- Achieves strong results quickly (test accuracy in the ~85–95% range across epochs) — a large improvement over a TinyVGG model trained from scratch in earlier notebooks
- Plots loss/accuracy curves with a `plot_loss_curves()` helper
- Makes predictions on both **test set images** and a **custom image** (a running "pizza dad" example image from the course), including a custom `pred_and_plot_image()` utility

## Part 2 — Experiment Tracking with TensorBoard

### 5. Introducing `SummaryWriter`
- Integrates `torch.utils.tensorboard.SummaryWriter` to log training/test loss and accuracy per epoch
- Modifies the `train()` function to accept and write to a `writer` instance

### 6. Custom `create_writer()` Helper
- Builds a helper function to generate a uniquely named log directory per experiment:
  `runs/YYYY-MM-DD/experiment_name/model_name/extra`
- Enables clean, organized comparison of many runs inside TensorBoard

### 7. Running Multiple Experiments
Sets up a **grid of experiments** varying three factors:
- **Model architecture:** EfficientNet-B0 vs. EfficientNet-B2
- **Dataset size:** 10% vs. 20% of the training data
- **Training length:** 5 vs. 10 epochs

This produces **8 total experiments**, each trained with its own fresh model instance, frozen base layers, and custom classifier head sized to the backbone's feature output (1280 for B0, larger for B2). Each trained model is saved to disk with `save_model()`.

### 8. Comparing Results in TensorBoard
- Loads the TensorBoard extension (`%load_ext tensorboard`) to visually compare all 8 runs
- Identifies **EfficientNet-B2, trained on 20% of the data for 10 epochs**, as the best-performing configuration (lowest test loss, ~93.8% test accuracy)
- Notes that a similar 5-epoch run performed nearly as well — suggesting **model size and data volume** mattered more than training duration in this case

### 9. Loading the Best Model & Making Predictions
- Reloads the best-performing model from its saved `state_dict()`
- Checks the model's **file size** (~29 MB) and discusses deployment size considerations (embedded vs. mobile vs. general use)
- Runs predictions on random test images and on the custom "pizza dad" image using the best model

## Key Concepts Covered
- Transfer learning (feature extraction with frozen base layers)
- Pretrained model weights & automatic vs. manual preprocessing transforms
- Modifying a classifier head for a custom number of classes
- Reusable modular training code (`engine.py`, `data_setup.py`, `utils.py`)
- Experiment tracking with TensorBoard (`SummaryWriter`)
- Systematic hyperparameter/architecture experimentation (grid of model × data × epochs)
- Model comparison, selection, and deployment-readiness considerations (file size)
- Making predictions on test-set and custom real-world images

## Requirements
- Python 3
- `torch` (1.12+), `torchvision` (0.13+)
- `torchinfo`
- `tensorboard`
- `matplotlib`
- `requests`, `tqdm`, `PIL`

## Notes
- This notebook is part of a course series (Daniel Bourke's *PyTorch for Deep Learning* / learnpytorch.io), building directly on a prior "PyTorch Going Modular" notebook whose scripts (`data_setup.py`, `engine.py`, `predictions.py`, `utils.py`) are imported and reused here.
- A trailing "3. The next" section at the end of the notebook is empty (placeholder for a follow-up project/notebook).