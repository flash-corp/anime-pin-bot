import random

def get_random_prompts(n=10):
    with open("prompts.txt", "r") as f:
        all_prompts = [line.strip() for line in f.readlines() if line.strip()]
    return random.sample(all_prompts, min(n, len(all_prompts)))
