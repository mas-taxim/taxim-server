# taxim-server
taxim backend server repo

## Set up

### Clone

Checkout all of git repository submodules first:

```bash
git submodule update --init
```

### Install

**Install packages:**

```bash
pip install -r requirements.txt
```

**Install packages (conda):**
```bash
conda install --file requirements.conda.txt
```

## Run
---
### default
```bash
uvicorn main:app --reload
```

### window
```bash
run.bat
```
### linux & mac
```bash
./run.sh
```
