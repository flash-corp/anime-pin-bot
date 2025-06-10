from generate_images import run_generate
from post_to_pinterest import run_post

if __name__ == "__main__":
    print("Generating images...")
    run_generate()
    print("Posting to Pinterest...")
    run_post()
