# src https://gist.github.com/mcguffin/746afffa0929ca8e2ea2ba8538776742

# get version number
REGEX="[0-9]\.[0-9]\.[0-9]"
VERSION=`grep -o "$REGEX" src/mercutio/_version.py`

# set a standard, simple message -- in the future, summarize from CHANGELOG
MESSAGE=$(printf "Release of version %s" $VERSION)


DRAFT="false"
PRE="false"
BRANCH="master"
GITHUB_ACCESS_TOKEN=`cat .github_token`

# get repo name and owner
REPO_REMOTE=$(git config --get remote.origin.url)

if [ -z $REPO_REMOTE ]; then
	echo "Not a git repository"
	exit 1
fi

REPO_NAME=$(basename -s .git $REPO_REMOTE)
REPO_OWNER=$(git config --get user.name)
https://api.github.com/user/repos?access_token=883651d227d1610682e906c9c5d4fe5fc18faae8
API_JSON=$(printf '{"tag_name": "%s","target_commitish": "%s","name": "mercutio %s","body": "%s","draft": %s,"prerelease": %s}' "$VERSION" "$BRANCH" "$VERSION" "$MESSAGE" "$DRAFT" "$PRE" )
API_RESPONSE_STATUS=$(curl --data "$API_JSON" -s -i -H "Authorization: token $GITHUB_ACCESS_TOKEN" https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/releases)
echo "$API_RESPONSE_STATUS"

# finally deploy to pypi and clean up
python setup.py sdist bdist_wheel
twine upload dist/* --repository pypi --config-file .pypirc # uses project-scoped API token for mercutio
rm -rf dist/