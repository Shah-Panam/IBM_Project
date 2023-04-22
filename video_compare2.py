import os
import cv2
from skimage.metrics import structural_similarity as ssim

# Load the videos
video1 = cv2.VideoCapture('/workspaces/IBM_Project/Video_Database/Video2_e.mp4')

videos_folder = "/workspaces/IBM_Project/Video_Database"

# Get the frames per second (fps) of the videos
fps1 = video1.get(cv2.CAP_PROP_FPS)

v1_total_frames = int(video1.get(cv2.CAP_PROP_FRAME_COUNT))

width = 640
height = 480

filename_ls = list(filter(lambda filename : filename.endswith('.mp4') or filename.endswith('.avi'), os.listdir(videos_folder)))
total = len(filename_ls)
vid_count = 0

# Loop through all the videos in the folder
for filename in filename_ls:
    vid_count += 1

    video2 = cv2.VideoCapture(filename)
    fps2 = video2.get(cv2.CAP_PROP_FPS)
    v2_total_frames = int(video2.get(cv2.CAP_PROP_FRAME_COUNT))
    total_frames = min(v1_total_frames,v2_total_frames)

    # Initialize the frame counters
    frame_count1 = 0
    frame_count2 = 0

    # Initialize the frame similarity scores
    similarity_scores = []

    # Reset the file pointer to the beginning of the first video
    video1.set(cv2.CAP_PROP_POS_FRAMES, 0)

    # Loop through the frames of the videos
    while True:
        # Read a frame from each video
        ret1, frame1 = video1.read()
        ret2, frame2 = video2.read()

        # If either video has reached the end, break the loop
        if not ret1 or not ret2:
            break

        # Increment the frame counters
        frame_count1 += 1
        frame_count2 += 1

        # Skip every other frame
        if frame_count1 % 2 == 0 and frame_count2 % 2 == 0:
            continue

        frame1 = cv2.resize(frame1, (width, height))
        frame2 = cv2.resize(frame2, (width, height))

        # Convert the frames to grayscale
        gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

        # Calculate the structural similarity index (SSIM) between the frames
        ssim_score = ssim(gray1, gray2, full=True)[0]

        # Append the similarity score to the list
        similarity_scores.append(ssim_score)

        progress_percent = int(frame_count1 / total_frames * 100)
        print("Video {}/{}  Progress: {}%".format(vid_count, total, progress_percent), end="\r")

    # Calculate the average similarity score
    avg_similarity_score = sum(similarity_scores) / len(similarity_scores)

    # Print the average similarity score
    # print("The average similarity score between the two videos is:", avg_similarity_score)
    print("The similarity between the two videos is:", avg_similarity_score*100, "%")
    video2.release()
        
# Release the video capture objects
video1.release()
# video2.release()
