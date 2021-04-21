#!/bin/sh
PYTHONPATH=../ python commbot_faq.py --gpus 1 --max_epochs 3 --default_root_dir . --gradient_clip_val 1.0 --batch_size=32 --max_seq_len=64
