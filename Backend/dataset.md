## Matt - Dataset Preparation
Need a clean dataset for YOLO training using existing public data. Focus only on these classes: rbc, wbc, and crystals?

## Use CVAT

- Define labels: rbc, wbc, crystals (clarify with Jessie)
- Create Tasks: Create separate tasks for each dataset (e.g., Dataset_A_cleaning) & upload images to their respective tasks.
- If the dataset has existing annotations, import them and remap the labels (eg: erythrocytes -> rbc):
**Annotation** Draw bounding boxes if needed

## Export & Merge (for Jessie's Model)
1. Repo structure:
```
dataset/images/ (train/val)

dataset/labels/ (train/val)
```
**Split data:** 80% train / 20% val.

2. Create dataset.yaml

YAML
train: dataset/images/train
val: dataset/images/val
nc: 3
names: ["rbc", "wbc", "crystals"]
