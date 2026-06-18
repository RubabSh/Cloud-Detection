# \# AI-Based Cloud Detection – POC

# 

# \## Overview

# 

# \*\*AI-Based Cloud Detection – POC\*\* is a deep learning-based cloud segmentation and classification system developed for satellite imagery. The project aims to automatically detect cloud-covered regions in high-resolution optical satellite images and classify images as \*\*Cloudy\*\* or \*\*No Cloud\*\* before further processing or transmission.

# 

# Cloud detection is an essential preprocessing step in remote sensing workflows because clouds can obscure the Earth's surface and reduce the usability of optical imagery. Early cloud detection can significantly reduce bandwidth requirements by preventing the downlink of unusable satellite data.

# 

# \---

# 

# \## Project Objectives

# 

# \### 1. Dataset Acquisition \& Annotation

# 

# \* Curate a custom dataset from open-source satellite imagery archives.

# \* Manually annotate cloud regions to create segmentation masks.

# \* Prepare training-ready datasets for cloud segmentation.

# 

# \### 2. AI Model Development

# 

# \* Develop a deep learning model capable of accurately detecting and segmenting clouds in high-resolution satellite imagery.

# \* Train and optimize the model using annotated datasets.

# 

# \### 3. AI Model Inference

# 

# \* Develop a deployment-ready inference module.

# \* Automatically classify incoming images as:

# 

# &#x20; \* \*\*Cloudy\*\*

# &#x20; \* \*\*No Cloud\*\*

# 

# \---

# 

# \## Dataset

# 

# \### Source Imagery

# 

# The dataset was collected from open-source archives containing imagery from:

# 

# \* WorldView-1

# \* GeoEye-1

# 

# provided by Maxar Technologies.

# 

# \### Dataset Characteristics

# 

# | Property         | Value                     |

# | ---------------- | ------------------------- |

# | Total Images     | 2,500                     |

# | Image Type       | RGB Satellite Images      |

# | Resolution       | < 0.5 meters              |

# | Image Dimensions | 930 × 930 pixels          |

# | Annotation Tool  | CVAT                      |

# | Label Type       | Binary Segmentation Masks |

# 

# The dataset covers:

# 

# \* Diverse geographic locations

# \* Different seasons

# \* Various cloud conditions

# 

# Each image was manually annotated to generate cloud segmentation masks representing:

# 

# \* Cloud

# \* No Cloud

# 

# \---

# 

# \## Model Architecture

# 

# The cloud detection model is based on a custom deep learning architecture following an \*\*Encoder–Decoder\*\* design.

# 

# \### Framework

# 

# \* TensorFlow

# \* Keras

# 

# \### Training Parameters

# 

# | Parameter         | Value        |

# | ----------------- | ------------ |

# | Output Activation | Sigmoid      |

# | Batch Size        | 4            |

# | Loss Function     | Jaccard Loss |

# | Optimizer         | Adam         |

# | Learning Rate     | 0.0001       |

# 

# \---

# 

# \## Model Evaluation

# 

# The model was evaluated using standard segmentation metrics.

# 

# \### Intersection over Union (IoU)

# 

# \[

# IoU = \\frac{TP}{TP + FP + FN}

# ]

# 

# Measures overlap between predicted cloud masks and ground-truth masks.

# 

# \### Accuracy

# 

# \[

# Accuracy = \\frac{TP + TN}{TP + FP + TN + FN}

# ]

# 

# Measures the percentage of correctly classified pixels.

# 

# \---

# 

# \## Results

# 

# The trained model achieved:

# 

# | Metric         | Value            |

# | -------------- | ---------------- |

# | IoU            | 0.80             |

# | Accuracy       | 92%              |

# | Test Images    | 700              |

# | Inference Time | < 1 second/image |

# 

# \### Key Achievements

# 

# \* Accurate cloud segmentation

# \* Fast inference performance

# \* Reliable cloud coverage estimation

# \* Effective Cloudy / No Cloud classification

# 

# \---

# 

# \## Cloud Classification Logic

# 

# The inference module estimates cloud coverage from the predicted segmentation mask.

# 

# \### Decision Rule

# 

# | Cloud Coverage | Classification |

# | -------------- | -------------- |

# | ≥ 20%          | Cloudy         |

# | < 20%          | No Cloud       |

# 

# \---

# 

# \## Project Structure

# 

# ```text

# project/

# │

# ├── inference.py

# ├── env.yml

# ├── model/

# │   └── trained\_model

# │

# ├── dataset/

# │   ├── Train/

# │   ├── Validation/

# │   ├── Test/

# │   │   ├── Cloud/

# │   │   └── No\_Cloud/

# │   └── Masks/

# │

# └── README.md

# ```

# 

# \---

# 

# \## Installation

# 

# \### Create Conda Environment

# 

# ```bash

# conda env create -f env.yml

# ```

# 

# \### Activate Environment

# 

# ```bash

# conda activate cloudnet-env

# ```

# 

# \---

# 

# \## Running Inference

# 

# \### Step 1

# 

# Place test images inside:

# 

# ```text

# dataset/Test/

# ```

# 

# \### Step 2

# 

# Run inference:

# 

# ```bash

# python inference.py

# ```

# 

# \---

# 

# \## Output

# 

# After execution, images will automatically be categorized into:

# 

# \### Cloudy Images

# 

# ```text

# Test/Cloud/

# ```

# 

# Contains images with:

# 

# ```text

# Cloud Coverage ≥ 20%

# ```

# 

# \### No Cloud Images

# 

# ```text

# Test/No\_Cloud/

# ```

# 

# Contains images with:

# 

# ```text

# Cloud Coverage < 20%

# ```

# 

# \---

# 

# \## Sample Workflow

# 

# ```text

# Input Satellite Image

# &#x20;         │

# &#x20;         ▼

# &#x20;  Deep Learning Model

# &#x20;         │

# &#x20;         ▼

# &#x20;  Cloud Segmentation Mask

# &#x20;         │

# &#x20;         ▼

# &#x20;Cloud Percentage Estimation

# &#x20;         │

# &#x20;         ▼

# &#x20;┌───────────────┬───────────────┐

# &#x20;│ Cloud ≥ 20%   │ Cloud < 20%   │

# &#x20;▼               ▼

# &#x20;Cloudy        No Cloud

# ```

# 

# \---

# 

# \## Future Work

# 

# This project currently serves as a \*\*Proof of Concept (POC)\*\* and forms the foundation for future development under the \*\*Sat-AI\*\* initiative.

# 

# Planned improvements include:

# 

# \* Expansion of training datasets

# \* Improved model accuracy

# \* Faster inference performance

# \* Real-time deployment optimization

# \* Integration into operational satellite workflows

# \* Edge deployment for onboard processing

# 

# \---

# 

# \## Conclusion

# 

# The developed AI-based cloud detection system demonstrates strong performance in satellite image cloud segmentation, achieving an \*\*IoU of 0.80\*\* and \*\*92% pixel accuracy\*\* while maintaining \*\*sub-second inference times\*\*.

# 

# The project successfully validates the feasibility of using deep learning for automated cloud detection and establishes a scalable foundation for future satellite intelligence applications.

# 

# \---

# 

# \## License

# 

# This project is intended for research and development purposes.

# 

# \## Authors

# 

# Developed as part of the \*\*AI Based Cloud Detection – POC\*\* R\&D Project.



