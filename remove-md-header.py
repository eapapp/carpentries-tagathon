"""
Remove header from blog posts written in markdown
from the Data Carpentry Blog
"""

from os import listdir, mkdir
from os.path import isfile, join, exists

filelist = [f for f in listdir("./md") if isfile(join("./md", f))]

for mdfile in filelist:
    
    if mdfile[-3:] == ".md":
    
        with open("./md/" + mdfile, 'r', encoding="utf8") as fullfile:

            count = 0
            maintext = []
            for line in fullfile:
                
                if count >= 2:  # End of YAML front matter (second occurence of ---)
                    maintext.append(line)
                
                elif line.startswith("---"):
                    count+=1

                elif line.startswith('title: ') or line.startswith('Title: '):
                    title = line[7:-1]
                    if len(title.strip()) > 0: title = "# " + title.strip('" “”') + "\n"
                    maintext.append(title)

                elif line.startswith('teaser: ') or line.startswith('Teaser: '):
                    teaser = line[8:-1]
                    if len(teaser.strip()) > 0: teaser = "## " + teaser.strip('" “”') + "\n"
                    maintext.append(teaser)

            fullfile.close()

        if not exists("./clean/"):
            mkdir("./clean/")

        newname = "./clean/" + mdfile[:-3] + "_clean" + mdfile[-3:]
        newfile = open(newname, "w")
        for line in maintext:
            newfile.write(line)  # + "\n")
        newfile.close()
