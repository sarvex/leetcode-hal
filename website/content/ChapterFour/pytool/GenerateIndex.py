import os
import glob

indexFile = 'index.txt'
current_working_dir = os.getcwd()
# print(f"current_working_dir: {current_working_dir}")

dir_names = glob.glob("*.md")
dir_names.sort()
# print(dir_names)
print(len(dir_names))
content = [
    '- [{}]({{{{< relref "/ChapterFour/{}" >}}}})'.format(
        file_name[:-3], file_name) for file_name in dir_names
]
with open(indexFile, "w") as myfile:
        myfile.write('\n'.join(content))

print("Finished")