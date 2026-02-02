# Releasing nts ERPNext

* Make a new bench dedicated for releasing
```
bench init release-bench --nts-path git@github.com:nts/nts.git
```

* Get ERPNext in the release bench
```
bench get-app erpnext git@github.com:nts/erpnext.git
```

* Configure as release bench. Add this to the common_site_config.json
```
"release_bench": true,
```

* Add branches to update in common_site_config.json
```
"branches_to_update": {
    "staging": ["develop", "hotfix"],
    "hotfix": ["develop", "staging"]
}
```

* Use the release commands to release
```
Usage: bench release [OPTIONS] APP BUMP_TYPE
```

* Arguments :
  * _APP_ App name e.g [nts|erpnext|yourapp]
  * _BUMP_TYPE_ [major|minor|patch|stable|prerelease]
* Options:
  * --from-branch git develop branch, default is develop
  * --to-branch git master branch, default is master
  * --remote git remote, default is upstream
  * --owner git owner, default is nts
  * --repo-name git repo name if different from app name
  
* When updating major version, update `develop_version` in hooks.py, e.g. `9.x.x-develop`
