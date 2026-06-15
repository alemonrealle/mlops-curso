# Versionar `data/df.csv` con DVC

> **Contexto:** El archivo `df.csv` estaba siendo rastreado por Git, lo que impedía añadirlo a DVC. Estos pasos resuelven el conflicto y versionan el dataset actualizado correctamente.

---

## Paso 1 — Quitar `df.csv` del tracking de Git

```bash
git rm -r --cached 'data/df.csv'
```

> Esto **no borra** el archivo del disco, solo lo elimina del índice de Git.

---

## Paso 2 — Hacer commit de ese cambio

```bash
git commit -m "stop tracking data/df.csv"
```

---

## Paso 3 — Versionar el dataset con DVC

```bash
dvc add 'data/df.csv'
```

DVC generará un nuevo hash MD5 del dataset actualizado y creará el archivo `data/df.csv.dvc`.

---

## Paso 4 — Añadir el puntero `.dvc` a Git

```bash
git add 'data/df.csv.dvc' data/.gitignore
```

> Solo se sube el puntero `.dvc` a Git, **nunca** el CSV directamente.

---

## Paso 5 — Commit y push final

```bash
git commit -m "data: actualizar dataset df.csv v2.0 (+200 registros)"
git push
```

---

## Resumen de qué va dónde

| Archivo | ¿Va en Git? | Descripción |
|---|---|---|
| `data/df.csv` | ❌ NO (`.gitignore`) | Datos reales — pesado |
| `data/df.csv.dvc` | ✅ SÍ | Hash MD5 + tamaño — puntero ligero |
| `.dvc/cache/` | ❌ NO | Copia inmutable cacheada por DVC |

---

## Tip — Evitar este problema en el futuro

Añade esta línea a tu `.gitignore` para que Git ignore automáticamente cualquier CSV:

```
data/*.csv
```

---

## Bonus — Volver a una versión anterior del dataset

Si necesitas reproducir resultados con el dataset original:

```bash
git checkout HEAD~1 -- 'data/df.csv.dvc'
dvc checkout
```

DVC restaurará exactamente el CSV de esa versión. ✅
