import subprocess

# EXERCISE 1
subprocess.run('ffprobe -loglevel 0 -print_format json -show_format -show_streams BBB.mp4', shell=True)

# EXERCISE 2

# Cut 1 minute video from BBB.mp4 without audio
input_video = 'BBB.mp4'
output_video = 'Files_ex2/BBB_1_minute.mp4'
subprocess.run('ffmpeg -ss 00:00:00 -to 00:01:00 -i '+input_video+' -c copy -an '+output_video+'', shell=True)

# Extract 1 minute audio from BBB.mp4 in mp3 format
input_video = 'BBB.mp4'
output_audio = 'Files_ex2/BBB_1_minute_audio.mp3'
subprocess.run('ffmpeg -ss 00:00:00 -to 00:01:00 -i '+input_video+' -q:a 0 -map a '+output_audio+'', shell=True)

# Extract 1 minute audio from BBB.mp4 in ACC format
input_video = 'BBB.mp4'
output_audio = 'Files_ex2/BBB_1_minute_audio.aac'
subprocess.run('ffmpeg -ss 00:00:00 -to 00:01:01 -i '+input_video+' -c copy '+output_audio+'', shell=True)

# Package 1 minute video with 1 minute mp3 audio
input_video = 'Files_ex2/BBB_1_minute.mp4'
input_audio = 'Files_ex2/BBB_1_minute_audio.mp3'
output_video = 'Files_ex2/BBB_1_minute_mp3.mp4'
subprocess.run('ffmpeg -i '+input_video+' -i '+input_audio+' -shortest -c:v copy -c:a aac -b:a 256k '+output_video+'', shell=True)

# Package 1 minute video with 1 minute aac audio
input_video = 'Files_ex2/BBB_1_minute.mp4'
input_audio = 'Files_ex2/BBB_1_minute_audio.aac'
output_video = 'Files_ex2/BBB_1_minute_aac.mp4'
subprocess.run('ffmpeg -i '+input_video+' -i '+input_audio+' -shortest -c:v copy -c:a aac -b:a 256k '+output_video+'', shell=True)


# EXERCISE 3

# Input values that user introduces. The input files will be a video or image
input_file = input('Enter the input file name (try with BBB_30.mp4 or Lenna.png): ')
width = input('Enter new width to resize (ex: 160): ')
height = input('Enter new height to resize (ex: 120): ')

input_name = input_file.partition('.')[0]                   # Read input file name (before .)
input_format = input_file.partition('.')[2]                 # Read the format of the input file (after .)
output_file = input_name+'_'+width+'x'+height+'.'+input_format      # Write the output file name

# Video resized to resolution given by the user
subprocess.run('ffmpeg -i '+input_file+' -s '+width+'x'+height+' -c:a copy Files_ex3/'+output_file+'', shell=True)

