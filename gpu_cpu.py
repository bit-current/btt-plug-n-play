import os
import psutil
import subprocess
import platform

def get_cpu_usage():
    # Get CPU usage as a percentage
    cpu_usage = psutil.cpu_percent(interval=1)
    return f"CPU Usage: {cpu_usage}%"

def get_gpu_usage():
    try:
        if platform.system() == 'Linux':
            # Check if intel_gpu_top is available
            subprocess.run(['which', 'intel_gpu_top'], check=True)

            # Run intel_gpu_top command to get GPU information
            result = subprocess.run(['sudo', 'intel_gpu_top', '-- ', '1', '1'], capture_output=True, text=True)

            # Extract GPU usage from the output
            gpu_usage_line = [line for line in result.stdout.split('\n') if 'render busy' in line][0]
            gpu_usage = gpu_usage_line.split(':')[-1].strip()
            return f"GPU Usage: {gpu_usage}"
        elif platform.system() == 'Darwin':
            # Run an AppleScript to get GPU usage on macOS
            script = 'tell application "Activity Monitor" to get the value of attribute "GPU usage" of the first window'
            result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
            gpu_usage = result.stdout.strip()
            return f"GPU Usage: {gpu_usage}%"
        else:
            return "GPU monitoring is only supported on Linux and macOS systems with Intel GPUs."

    except Exception as e:
        return f"Error retrieving GPU usage: {e}"

if __name__ == "__main__":
    # Get and print CPU usage
    cpu_info = get_cpu_usage()
    print(cpu_info)

    # Get and print GPU usage
    gpu_info = get_gpu_usage()
    print(gpu_info)
