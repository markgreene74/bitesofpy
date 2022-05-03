# https://codechalleng.es/bites/94/
from collections import namedtuple
import os
import pickle
import urllib.request

# prework
# download pickle file and store it in a tmp file
pkl_file = "pycon_videos.pkl"
data = f"https://bites-data.s3.us-east-2.amazonaws.com/{pkl_file}"
tmp = os.getenv("TMP", "/tmp")
pycon_videos = os.path.join(tmp, pkl_file)
urllib.request.urlretrieve(data, pycon_videos)

# the pkl contains a list of Video namedtuples
Video = namedtuple("Video", "id title duration metrics")


def load_pycon_data(pycon_videos=pycon_videos):
    """Load the pickle file (pycon_videos) and return the data structure
    it holds"""
    with open(pycon_videos, "rb") as f:
        return pickle.load(f)


def get_most_popular_talks_by_views(videos):
    """Return the pycon video list sorted by viewCount"""
    # >>> videos[0]
    # Video(id='T-TwcmT6Rcw',
    #       title='...',
    #       duration='PT45M8S',
    #       metrics={'viewCount': '6360',
    #               'likeCount': '144',
    #               'dislikeCount': '2',
    #               'favoriteCount': '0',
    #               'commentCount': '14'})
    return sorted(videos, key=lambda x: int(x.metrics["viewCount"]), reverse=True)


def get_most_popular_talks_by_like_ratio(videos):
    """Return the pycon video list sorted by most likes relative to
    number of views, so 10 likes on 175 views ranks higher than
    12 likes on 300 views. Discount the dislikeCount from the likeCount.
    Return the filtered list"""
    return sorted(
        videos,
        key=lambda x: (int(x.metrics["likeCount"]) - int(x.metrics["dislikeCount"]))
        / int(x.metrics["viewCount"]),
        reverse=True,
    )


def get_talks_gt_one_hour(videos):
    """Filter the videos list down to videos of > 1 hour"""
    return [v for v in videos if "H" in v.duration]


def get_talks_lt_twentyfour_min(videos):
    """Filter videos list down to videos that have a duration of less than
    24 minutes"""
    result = []
    for v in videos:
        # parse 'PT1H56M1S'
        _duration = (
            v.duration.replace("PT", "")
            .replace("H", ":")
            .replace("M", ":")
            .replace("S", "")
            .split(":")
        )
        if len(_duration) < 3 and int(_duration[0]) < 24:
            result.append(v)
    return result
