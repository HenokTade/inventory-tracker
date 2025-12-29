# GitHub Release Guide

This guide explains how to create and publish releases on GitHub for the Inventory Tracker project.

## Prerequisites
- Git repository pushed to GitHub
- All changes committed and pushed
- Release notes prepared in `releases/` directory

## Step-by-Step: Creating Git Tags

### 1. Create Baseline Tags

#### Baseline 1 (BL1)
```bash
# Navigate to project directory
cd "c:\Users\henok\OneDrive\Desktop\Inventoty Tracker"

# Create annotated tag for BL1
git tag -a BL1 -m "Baseline 1: Repository setup + initial documents + CI list"

# Push tag to GitHub
git push origin BL1
```

#### Baseline 2 (BL2)
```bash
# Create annotated tag for BL2
git tag -a BL2 -m "Baseline 2: Working prototype + CR implementations"

# Push tag to GitHub
git push origin BL2
```

### 2. Create Release Tags

#### Release v1.0.0
```bash
# Create annotated tag for v1.0.0
git tag -a v1.0.0 -m "Release v1.0.0: Initial working system"

# Push tag to GitHub
git push origin v1.0.0
```

#### Release v1.1.0
```bash
# Create annotated tag for v1.1.0
git tag -a v1.1.0 -m "Release v1.1.0: CR implementations"

# Push tag to GitHub
git push origin v1.1.0
```

### 3. Verify Tags
```bash
# List all tags
git tag -l

# View tag details
git show v1.0.0
```

## Step-by-Step: Creating GitHub Releases

### For Release v1.0.0

1. **Navigate to GitHub Repository**
   - Go to: `https://github.com/HenokTade/inventory-tracker`

2. **Access Releases Section**
   - Click on "Releases" (right sidebar or under "Code" tab)
   - Click "Create a new release" or "Draft a new release"

3. **Configure Release**
   - **Choose a tag**: Select `v1.0.0` from dropdown (or type it if not yet pushed)
   - **Release title**: `Release v1.0.0 - Initial Working System`
   - **Description**: Copy content from `releases/v1.0.0.md`

4. **Add Release Assets** (Optional)
   - Click "Attach binaries by dropping them here or selecting them"
   - Upload ZIP of source code (GitHub auto-generates this)
   - Upload any additional files (documentation PDFs, etc.)

5. **Publish**
   - Check "Set as the latest release" if applicable
   - Click "Publish release"

### For Release v1.1.0

1. **Navigate to Releases**
   - Go to repository → Releases → "Draft a new release"

2. **Configure Release**
   - **Choose a tag**: Select `v1.1.0`
   - **Release title**: `Release v1.1.0 - CR Implementations`
   - **Description**: Copy content from `releases/v1.1.0.md`

3. **Highlight Changes**
   - Emphasize new features (edit, search, roles)
   - Link to implemented CRs
   - Include upgrade instructions

4. **Add Assets** (Optional)
   - Source code archives
   - Documentation bundle
   - Migration scripts if needed

5. **Publish**
   - Check "Set as the latest release"
   - Click "Publish release"

## Release Checklist

### Before Creating Release
- [ ] All code committed and pushed to GitHub
- [ ] Release notes written and reviewed
- [ ] Tests passing
- [ ] Documentation updated
- [ ] CHANGE_LOG.md updated
- [ ] Version numbers consistent across files

### Creating the Release
- [ ] Git tag created with correct version
- [ ] Tag pushed to GitHub
- [ ] GitHub release created
- [ ] Release notes added to description
- [ ] Assets uploaded (if any)
- [ ] Release published

### After Release
- [ ] Verify release appears on GitHub
- [ ] Test download links work
- [ ] Update project README if needed
- [ ] Announce release (if applicable)
- [ ] Archive release documentation

## Tag Naming Conventions

### Baselines
- Format: `BL<number>`
- Examples: `BL1`, `BL2`, `BL3`
- Purpose: Mark configuration baselines

### Releases
- Format: `v<major>.<minor>.<patch>`
- Examples: `v1.0.0`, `v1.1.0`, `v2.0.0`
- Purpose: Mark software releases
- Follow [Semantic Versioning](https://semver.org/)

## Best Practices

### Release Notes
- ✅ Clear and concise descriptions
- ✅ Highlight breaking changes
- ✅ Include upgrade instructions
- ✅ List all new features and fixes
- ✅ Credit contributors

### Timing
- Create releases at stable points
- Don't release with known critical bugs
- Coordinate with team members
- Consider user impact

### Communication
- Announce releases to stakeholders
- Update documentation
- Provide migration guides
- Offer support for upgrades

## Troubleshooting

### Tag Already Exists
```bash
# Delete local tag
git tag -d v1.0.0

# Delete remote tag
git push origin :refs/tags/v1.0.0

# Recreate tag
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0
```

### Wrong Commit Tagged
```bash
# Tag specific commit
git tag -a v1.0.0 <commit-hash> -m "Release v1.0.0"
git push origin v1.0.0
```

### Release Not Showing
- Verify tag is pushed: `git ls-remote --tags origin`
- Check GitHub repository settings
- Ensure you have write permissions

## Quick Reference

### All Tags in One Go
```bash
# Create all tags
git tag -a BL1 -m "Baseline 1: Repository setup + initial documents + CI list"
git tag -a BL2 -m "Baseline 2: Working prototype + CR implementations"
git tag -a v1.0.0 -m "Release v1.0.0: Initial working system"
git tag -a v1.1.0 -m "Release v1.1.0: CR implementations"

# Push all tags at once
git push origin --tags
```

### View All Tags
```bash
git tag -l -n
```

---

**Note**: Replace `HenokTade/inventory-tracker` with your actual GitHub username and repository name if different.
