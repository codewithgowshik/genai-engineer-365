import torch
import transformers
import datasets
import peft
import accelerate
import trl

print("=" * 45)
print("       PEFT ENVIRONMENT CHECK")
print("=" * 45)

# Python package versions
print("\nINSTALLED LIBRARIES")

print("PyTorch:", torch.__version__)
print("Transformers:", transformers.__version__)
print("Datasets:", datasets.__version__)
print("PEFT:", peft.__version__)
print("Accelerate:", accelerate.__version__)
print("TRL:", trl.__version__)

# Hardware information
print("\nHARDWARE INFORMATION")

if torch.cuda.is_available():
    print("CUDA available: Yes")
    print("GPU:", torch.cuda.get_device_name(0))
    print("GPU count:", torch.cuda.device_count())
else:
    print("CUDA available: No")
    print("Running with CPU.")

# PEFT availability
print("\nPEFT INFORMATION")

from peft import LoraConfig, get_peft_model

print("LoRAConfig imported successfully.")
print("get_peft_model imported successfully.")

print("\n" + "=" * 45)
print("ENVIRONMENT SETUP SUCCESSFUL!")
print("=" * 45)