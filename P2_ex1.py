import subprocess

subprocess.run('ffprobe -loglevel 0 -print_format json -show_format -show_streams BBB.mp4', shell=True)

