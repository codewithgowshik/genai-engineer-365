import os
import json

from peft import LoraConfig, TaskType
from transformers import TrainingArguments


# =====================================
# 1. MODEL CONFIGURATION
# =====================================

MODEL_NAME = "Qwen/Qwen2.5-0.5B"

OUTPUT_DIR = "./lora-output"


# =====================================
# 2. LORA CONFIGURATION
# =====================================

lora_config = LoraConfig(

    r=8,

    lora_alpha=16,

    lora_dropout=0.05,

    target_modules=[
        "q_proj",
        "k_proj",
        "v_proj",
        "o_proj",
        "gate_proj",
        "up_proj",
        "down_proj"
    ],

    bias="none",

    task_type=TaskType.CAUSAL_LM
)


# =====================================
# 3. TRAINING CONFIGURATION
# =====================================

training_settings = {

    "output_dir": OUTPUT_DIR,

    "per_device_train_batch_size": 1,

    "gradient_accumulation_steps": 4,

    "learning_rate": 2e-4,

    "num_train_epochs": 1,

    "logging_steps": 10,

    "save_steps": 50,

    "save_total_limit": 2,

    "report_to": "none"

}


# =====================================
# 4. CREATE TRAINING ARGUMENTS
# =====================================

training_args = TrainingArguments(
    **training_settings
)


# =====================================
# 5. SAVE CONFIGURATION
# =====================================

os.makedirs(OUTPUT_DIR, exist_ok=True)

lora_config.save_pretrained(OUTPUT_DIR)

with open(
    os.path.join(OUTPUT_DIR, "training_settings.json"),
    "w"
) as file:

    json.dump(training_settings, file, indent=4)


# =====================================
# 6. DISPLAY CONFIGURATION
# =====================================

print("\n========== LORA CONFIGURATION ==========")

print("Model:", MODEL_NAME)

print("Rank:", lora_config.r)

print("Alpha:", lora_config.lora_alpha)

print("Dropout:", lora_config.lora_dropout)

print("Target Modules:", lora_config.target_modules)

print("Task Type:", lora_config.task_type)

print("\n========== TRAINING CONFIGURATION ==========")

print("Batch Size:", training_args.per_device_train_batch_size)

print("Gradient Accumulation:",
      training_args.gradient_accumulation_steps)

print("Learning Rate:", training_args.learning_rate)

print("Epochs:", training_args.num_train_epochs)


print("\nConfiguration saved successfully!")

print("Output directory:", OUTPUT_DIR)