import cv2
import os
import time

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--data_root', help='dataset', default='videos', type=str)
parser.add_argument('--save_dir', help='save dir', default='videos', type=str)
args = parser.parse_args()


def get_video_duration(filename):
    video = cv2.VideoCapture(filename)
    fps = video.get(cv2.CAP_PROP_FPS)
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_count / fps
    video.release()
    return int(duration)

def splitVideoByStepDuration(video, saveDir, durationStep):
    print(video)
    saveDir += (os.path.basename(os.path.dirname(video)) + str(int(time.time())) + '/')
    print(saveDir)
    os.makedirs(saveDir, exist_ok=True)

    duration = get_video_duration(video)
    print(duration)
    startSplitDuration = 0
    index = 1
    while startSplitDuration < duration:
        subPath = saveDir + str(index) + os.path.splitext(video)[1]
        cmd = f"ffmpeg -i {video} -ss {str(startSplitDuration)} -to {str(startSplitDuration + durationStep)} {subPath}"
        print(f'CMD: {cmd}')
        os.system(cmd)

        startSplitDuration += durationStep
        index += 1


data_root = args.data_root
save_dir = args.save_dir
identities = os.listdir(data_root)
identities = [x if not x.endswith('.DS_Store') else os.remove(os.path.join(data_root, x)) for x in identities]
identities.sort()
for identity in identities:
    print(f'Processing dataset {identity}')
    splitVideoByStepDuration(os.path.join(data_root, identity), save_dir, 3)


