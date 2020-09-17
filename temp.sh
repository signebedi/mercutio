# get version number
REGEX="[0-9]*\.[0-9]*\.[0-9]*"
VERSION=`grep -o "$REGEX" src/mercutio/_version.py`

# pull relevant commit messages from the git log and write to a temporary file
git log $(git describe --tags --abbrev=0)..HEAD --pretty=%B | grep ^Added > .commits
git log $(git describe --tags --abbrev=0)..HEAD --pretty=%B | grep ^Changed >> .commits
git log $(git describe --tags --abbrev=0)..HEAD --pretty=%B | grep ^Fixed >> .commits
git log $(git describe --tags --abbrev=0)..HEAD --pretty=%B | grep ^Docs >> .commits
git log $(git describe --tags --abbrev=0)..HEAD --pretty=%B | grep ^Tests >> .commits

COMMITS=$(cat .commits)

# set a standard, simple message -- in the future, summarize from CHANGELOG
M=$(printf $'Release of version %s\n%s' $VERSION "$COMMITS")
# sed command brought to you by https://stackoverflow.com/a/1252191
MESSAGE=`echo "$M" | sed ':a;N;$!ba;s/\n/\<br\/\>/g'`


echo "$MESSAGE"
# remove the temporary file
rm .commits