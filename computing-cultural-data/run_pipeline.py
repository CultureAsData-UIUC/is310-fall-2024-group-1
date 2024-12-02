import subprocess

def run_script(script_name):
    try:
        print(f"Running {script_name}...")
        subprocess.run(['python', script_name], check=True)
        print(f"Completed {script_name}.")
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}")

if __name__ == "__main__":
    scripts = [
        'clean_dress_up_games.py',
        'validate_dress_up_games.py',
        'analyze_dress_up_games.py',
        'visualize_dress_up_games.py',
        'sentiment_analysis.py'
    ]

    for script in scripts:
        run_script(script)
