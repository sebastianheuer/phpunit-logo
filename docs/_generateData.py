import yaml
import os
import re

submissionsDir = '../suggestions'

data = []

for subdir, dirs, files in os.walk(submissionsDir):
    for file in files:
        if os.path.splitext(file)[1] not in ('.png', '.jpeg', '.jpg', '.gif'):
            continue
        fullPath = os.path.join(subdir, file).replace('../', '/')
        authorGitHubAlias = re.findall(r'/suggestions/(.*)/', fullPath)[0]
        data.append({'path': fullPath, 'author': authorGitHubAlias});



with open('_data/submissions.yml', 'w') as outfile:
    yaml.dump(data, outfile, default_flow_style=False)
