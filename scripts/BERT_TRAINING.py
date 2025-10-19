from transformers import AutoTokenizer, DataCollatorWithPadding, Trainer, TrainingArguments
from transformers import AutoModelForSequenceClassification, EarlyStoppingCallback
from datasets import load_from_disk
from evaluate import load
import numpy as np
import torch

datasets = load_from_disk('Data/test_novelty')

checkpoint = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)

def tokenize_function(example):
    return tokenizer(example["text"], truncation=True)

tokenized_datasets = datasets.map(tokenize_function, batched=True)
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

tokenized_datasets = tokenized_datasets.remove_columns(["text", "id"])
tokenized_datasets = tokenized_datasets.rename_column("score", "labels")
tokenized_datasets.set_format("torch")

def compute_metrics(eval_preds):
    logits, labels = eval_preds
    predictions = np.argmax(logits, axis=-1)
    
    accuracy = load('accuracy')
    f1 = load('f1')
    precision = load('precision')
    recall = load('recall')
    
    accuracy_result = accuracy.compute(predictions=predictions, references=labels)
    f1_result = f1.compute(predictions=predictions, references=labels)
    precision_result = precision.compute(predictions=predictions, references=labels)
    recall_result = recall.compute(predictions=predictions, references=labels)
    
    return {
        'accuracy': accuracy_result['accuracy'],
        'f1': f1_result['f1'],
        'precision': precision_result['precision'],
        'recall': recall_result['recall']
    }

device = torch.device("mps") if torch.backends.mps.is_available() else torch.device("cpu")

model = AutoModelForSequenceClassification.from_pretrained(checkpoint, num_labels=2)
model.to(device)

training_args = TrainingArguments(
    output_dir='./novelty_bert_checkpoints', 

    eval_strategy="steps",  # Evaluate the model every N steps (not per epoch)
    eval_steps=200,  # Run evaluation on validation set every 200 training steps
    save_steps=400,  # Save model checkpoint every 400 training steps
    learning_rate=2e-5,  # Learning rate for the optimizer

    per_device_train_batch_size=16,  # Number of training samples processed per device before updating weights
    per_device_eval_batch_size=16,  # Number of evaluation samples processed per device
    
    num_train_epochs=1,  # Total number of complete passes through the training dataset
    
    weight_decay=0.01,  # L2 regularization coefficient to prevent overfitting
    
    load_best_model_at_end=True,  # After training, load the checkpoint with the best validation performance
    metric_for_best_model="f1",  # Use F1 score to determine which checkpoint is "best"
    greater_is_better=True,
    
    warmup_steps=100,  # Number of steps to gradually increase learning rate from 0 to learning_rate (helps training stability)
    
    logging_steps=50,  # Log training metrics (loss, learning rate) every 50 steps
    
    report_to="none",  # Disable automatic logging to external tools (wandb, tensorboard, etc.)
)

trainer = Trainer(
    model=model,
    args=training_args, 
    train_dataset=tokenized_datasets["train"], 
    eval_dataset=tokenized_datasets["validation"],  
    compute_metrics=compute_metrics,  # Calculate metrics on validation set
    processing_class=tokenizer,  # Tokenizer for processing
    data_collator=data_collator,  # Handles dynamic padding of batches
    callbacks=[EarlyStoppingCallback(early_stopping_patience=3)]  # Stop training if validation metric doesn't improve for 3 consecutive evaluations
)

trainer.train()

trainer.save_model('./novelty_bert_final')
tokenizer.save_pretrained('./novelty_bert_final')

trainer.evaluate(tokenized_datasets['test'])