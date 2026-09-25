# Optional maintainer checks

Agents normally [read ADAC directly from the repository](../SETUP.md). Copying the documents is optional; maintainer tooling is not required to use the method.

With Python 3.9+ from the repository root:

```sh
python3 maintainer/check.py
python3 -m unittest discover -s maintainer -p 'test_*.py' -v
```

The [publication manifest](../maintainer/public-files.txt) defines release contents, not a project installation list. The checker verifies paths, local Markdown links/anchors, current version headings/pointers and generic private-reference/secret patterns. PNG assets receive an existence/signature check; inspect their appearance and metadata separately. The mutation test exercises broken links/anchors, version mismatches and private references. These checks do not execute the ADAC method.

Private project implementations, fixtures and associated verification records must not enter the publication candidate. Preserve them only in the private source/archive. Before publication inspect both the exported tree and all history, refs, objects and commit metadata that could be published. Removing a file in a later commit does not remove it from earlier history. Use a separately reviewed clean snapshot when prior candidate history contains excluded material; never publish the private source repository or an older review archive.

Pattern checks alone do not prove privacy or rights. Review included content and notices manually. Preserve existing versioned method snapshots in their owning source; do not rewrite past evidence to make new claims. Record actual checks and limitations without creating new demonstrations or adoption claims.
