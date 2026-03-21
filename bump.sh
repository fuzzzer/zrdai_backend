#!/bin/bash

set -e

LAST_TAG=$(git describe --tags --abbrev=0 2>/dev/null || echo "v0.0.0")

CLEAN_TAG=${LAST_TAG#v}

IFS='.' read -r MAJOR MINOR PATCH <<< "$CLEAN_TAG"

MAJOR=${MAJOR:-0}
MINOR=${MINOR:-0}
PATCH=${PATCH:-0}

NEW_PATCH=$((PATCH + 1))

NEW_VERSION="${MAJOR}.${MINOR}.${NEW_PATCH}"

echo "Latest tag found : ${LAST_TAG}"
echo "Bumping version to: v${NEW_VERSION}"

git tag "v${NEW_VERSION}" -m "Version ${NEW_VERSION} of the project"
git push --tags

echo "Version updated to ${NEW_VERSION}, committed, and tagged successfully."