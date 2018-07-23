import sys

import App.constants as const
import App.validations as validations
import App.aws as aws
import App.emotion as emotion
import App.custom as custom
import App.sound as sound

file_path = sys.argv[-1]

print('Check env')
validations.env_check(const.ENV_VARS)

print('Check file for validity')
validations.check_file(file_path)

print('Upload to S3')
fileUrl = aws.upload_images(file_path)

print('Delete Local File')
validations.remove_file(file_path)

print('Run Analysis')
faces = emotion.analyze_file(fileUrl)

print('Sort Result')
emotions = custom.sort_results(faces)

print('Display Result')
custom.print_result(emotions)

print('Play Sound')
sound.play_sound(emotions)
