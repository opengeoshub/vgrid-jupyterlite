# JupyterLite Demo

[![lite-badge](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://demo.vgrid.vn)

JupyterLite deployed as a static site to GitHub Pages, for demo purposes.

## ✨ Try it in your browser ✨

➡️ **https://demo.gishub.vn**

## Repository

➡️ **https://github.com/opengeoshub/vgrid-jupyterlite**

## Usage

Install vgrid, vgridpandas for JupyterLite using:

```bash
%pip install -q vgrid vgridpandas
```

Alternatively, you can install vgrid using piplite:

```python
import piplite
await piplite.install('vgrid')
await piplite.install('vgridpandas')
```

## How to get an updated version of JupyterLite

To clear local storage and sync with the latest version of JupyterLite site on GitHub, you can use:

Chrome Settings -> More tools -> Developer tools -> Application -> Storage -> IndexedDB -> JupyterLite Storage -> Right click files -> Clear

Then press F5 to refresh the page.

![](https://i.imgur.com/rL4rc6A.png)
