
import threading
import subprocess

def run_file(file_name):
    subprocess.run(['python', file_name])

files_to_run = ['Crash anomaly.py', 'heart_rate_classify.py', 'heart_anomaly.py']

threads = []
for file_name in files_to_run:
    thread = threading.Thread(target=run_file, args=(file_name,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
