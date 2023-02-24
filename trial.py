import os
import sys
from videohash import VideoHash


class FileHandler:
    def __init__(self, filename):
        self.fp_read = open(filename, "r")
        self.fp_write = open(filename, "a")

    def read_cache_data(self):
        all_files = self.fp_read.readlines()
        data = dict(map(lambda a: a.split(": "), all_files))
        # print(data)
        return data

    def write_cache_data(self, data):
        self.fp_write.write(data + "\n")
        

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        bpath = sys.argv[1]
    else:
        print("Link not provided. Exiting....")
        exit(1)
    
    FILENAME = "/workspaces/IBM_Project/Video_Database/database.txt"
    filehandler = FileHandler(FILENAME)

    try:
        if (bpath.startswith("http://") or bpath.startswith("https://") or bpath.startswith("www")):
            videohash1 = VideoHash(url=sys.argv[1])    
        else:
            videohash1 = VideoHash(path=sys.argv[1])

        video_database = os.listdir("/workspaces/IBM_Project/Video_Database")
        video_database.remove("database.txt")
        cached_data = filehandler.read_cache_data()

        # print(video_database)
        for i in video_database:
            # print(i)
            if (i in cached_data):
                vhash = cached_data[i]
            else:
                vhash = VideoHash(path="Video_Database/"+i).hash
                filehandler.write_cache_data(i + ": " + vhash)

            # print(videohash1.hash, " :::: \n" + vhash)
            if (videohash1.hash == str(vhash).removesuffix("\n")):
                print("Found Similar Video: ")
                print(i)
    except Exception as e:
        print("Exception: " + str(e))
