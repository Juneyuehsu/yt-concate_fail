# 4 steps
# 1. get all video list from channel
# 2. download youtube subtitle
# 3. download youtube video
# 4/ edit video

from yt_concate.pipeline.steps.get_video_list import GetVideoList
# from yt_concate.pipeline.steps.get_video_list import StepException
from yt_concate.pipeline.pipeline import Pipeline

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID

    }

    steps = [
        GetVideoList(),
    ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()

# video_list = get_all_video_in_channel(CHANNEL_ID)
# print(len(video_list))
