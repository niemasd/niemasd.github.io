# Usage

## Build Website

```bash
./scripts/build_website.py -o HTML_OUT_DIR
```

## Build CV PDF

```bash
pandoc -o PDF_OUT_DIR --pdf-engine=xelatex --from markdown <(./scripts/build_cv.py)
```

# Acknowledgements

## Social Media Icons

The icons in [`site/assets/social/`](sites/assets/social) are from [Simple Icons](https://simpleicons.org).
