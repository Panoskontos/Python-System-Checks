import platform
import psutil

# Computer
print(f"Computer name: {platform.node()}")
print(f"Machine Type: {platform.machine()}")
print(f"Processor Type: {platform.processor()}")
print(f"Architecture: {platform.architecture()}")
print(f"-------- Python ---------")
print(f"{platform.python_build()}")
print(f"{platform.python_compiler()}")
print(f"{platform.python_branch()}")
print(f"{platform.python_implementation()}")
print(f"{platform.python_revision()}")
print(f"{platform.python_version()}")
print(f"--------- System --------")
print(f"{platform.system()}")
print(f"{platform.uname()}")
print(f"\n\n--------- psutil --------")
print(f"Number of cores: {psutil.cpu_count(logical=False)}")
print(f"Number of cores: {psutil.cpu_count(logical=True)}")
print(f"CPU frequency: {psutil.cpu_freq()}")
print(f"(IMPORTANT)CPU utilization: {psutil.cpu_percent(interval=1)}")
print(f"Total RAM: {psutil.virtual_memory().total}")
print(f"RAM Usage : {psutil.virtual_memory().percent}")

