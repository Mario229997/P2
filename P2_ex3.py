import subprocess

# Input values that user introduces. The input files will be a video or image
input_file = input('Enter the input file name (try with BBB_30.mp4 or Lenna.png): ')
width = input('Enter new width to resize (ex: 160): ')
height = input('Enter new height to resize (ex: 120): ')

input_name = input_file.partition('.')[0]                   # Read input file name (before .)
input_format = input_file.partition('.')[2]                 # Read the format of the input file (after .)
output_file = input_name+'_'+width+'x'+height+'.'+input_format      # Write the output file name

# Video resized to resolution given by the user
subprocess.run('ffmpeg -i '+input_file+' -s '+width+'x'+height+' -c:a copy Files_ex3/'+output_file+'', shell=True)

