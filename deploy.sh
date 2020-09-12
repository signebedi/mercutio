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

API_JSON=$(printf '{"tag_name": "%s","target_commitish": "%s","name": "mercutio %s","body": "%s","draft": %s,"prerelease": %s}' "$VERSION" "$BRANCH" "$VERSION" "$MESSAGE" "$DRAFT" "$PRE" )
API_RESPONSE_STATUS=$(curl --data "$API_JSON" -s -i https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/releases?access_token=$GITHUB_ACCESS_TOKEN)
echo "$API_RESPONSE_STATUS"

python setup.py sdist bdist_wheel
twine upload dist/* --repository pypi --config-file .pypirc # uses project-scoped API token for mercutio

rm -rf dist/