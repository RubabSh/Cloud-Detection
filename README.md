# AI-Based Cloud Detection for Satellite Imagery

## Overview

**AI-Based Cloud Detection** is a deep learning-based cloud segmentation and classification system designed for high-resolution optical satellite imagery.

The solution automatically detects cloud-covered regions and classifies satellite images as **Cloudy** or **No Cloud** before downstream processing or transmission.

---

## Dataset

The dataset was collected from publicly available satellite imagery archives containing data from:

* **WorldView-1**
* **GeoEye-1**

### Dataset Statistics

| Property         | Value                     |
| ---------------- | ------------------------- |
| Total Images     | 2,500                     |
| Image Type       | RGB Satellite Images      |
| Resolution       | < 0.5 meters              |
| Image Dimensions | 930 × 930 pixels          |
| Annotation Type  | Binary Segmentation Masks |

### Classes

| Class    | Description          |
| -------- | -------------------- |
| Cloud    | Cloud-covered pixels |
| No Cloud | Clear-sky pixels     |

---

## Model Architecture

The cloud segmentation model follows an **Encoder–Decoder architecture** implemented using **TensorFlow** and **Keras**.

### Training Configuration

| Parameter         | Value        |
| ----------------- | ------------ |
| Output Activation | Sigmoid      |
| Batch Size        | 4            |
| Loss Function     | Jaccard Loss |
| Optimizer         | Adam         |
| Learning Rate     | 0.0001       |

---

## Performance

| Metric         | Value         |
| -------------- | ------------- |
| IoU            | 0.80          |
| Pixel Accuracy | 92%           |
| Test Images    | 700           |
| Inference Time | < 1 sec/image |

---

## Project Structure

```text
project/
│
├── inference.py
├── env.yml
│
├── model/
│   └── trained_model
│
├── dataset/
│   ├── Train/
│   ├── Validation/
│   ├── Test/
│   │   ├── Cloud/
│   │   └── No_Cloud/
│   └── Masks/
│
└── README.md
```

---

## Installation

### Create Conda Environment

```bash
conda env create -f env.yml
```

### Activate Environment

```bash
conda activate cloudnet-env
```

---

## Test Dataset

A sample test dataset is available for evaluating the inference pipeline.

### Download Test Data
**Test Dataset:** [Google Drive Download](https://drive.google.com/drive/folders/1Myf0TfY72FrC8CmZIXZr39HLCDvBatgr?usp=drive_link)

After downloading, extract the files and place the images inside:

```text
dataset/Test/
```

---

## Running Inference

### Step 1: Download and Extract Test Images

Place the extracted test images inside:

```text
dataset/Test/
```

### Step 2: Run Inference

```bash
python inference.py
```

---

## Output

After inference, images are automatically categorized based on estimated cloud coverage.

### Cloudy Images

```text
dataset/Test/Cloud/
```

Contains images with:

```text
Cloud Coverage ≥ 20%
```

### No Cloud Images

```text
dataset/Test/No_Cloud/
```

Contains images with:

```text
Cloud Coverage < 20%
```

---

## Cloud Classification Logic

The predicted cloud mask is used to estimate cloud coverage.

| Cloud Coverage | Classification |
| -------------- | -------------- |
| ≥ 20%          | Cloudy         |
| < 20%          | No Cloud       |

---

## Processing Workflow

```text
Satellite Image
       │
       ▼
 Deep Learning Model
       │
       ▼
Cloud Segmentation Mask
       │
       ▼
Cloud Coverage Estimation
       │
       ▼
 ┌───────────────┬───────────────┐
 │ Cloud ≥ 20%  │ Cloud < 20%   │
 ▼              ▼
Cloudy       No Cloud
```

---

## Conclusion

The AI-Based Cloud Detection system demonstrates the feasibility of deep learning-based cloud segmentation for high-resolution satellite imagery.

### Key Results

* **IoU:** 0.80
* **Pixel Accuracy:** 92%
* **Inference Time:** < 1 second per image

These results validate the approach as a scalable solution for automated cloud detection and satellite image quality assessment.

---

## License

This project is intended for **research and development purposes**.
