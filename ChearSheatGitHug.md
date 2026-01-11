
# 🚀 Git Complete Reference Guide

**Autor:** Angel Cruz  
**Fecha:** Enero 2025  
**Propósito:** Referencia rápida de Git para desarrollo diario

---

## 📑 Tabla de Contenido

1. [Configuración Inicial](#configuración-inicial)
2. [Conceptos Básicos](#conceptos-básicos)
3. [Workflow Diario](#workflow-diario)
4. [Branches (Ramas)](#branches-ramas)
5. [Merge y Conflictos](#merge-y-conflictos)
6. [GitHub (Remoto)](#github-remoto)
7. [Pull Requests](#pull-requests)
8. [Comandos de Emergencia](#comandos-de-emergencia)
9. [.gitignore](#gitignore)
10. [Buenas Prácticas](#buenas-prácticas)
11. [Troubleshooting](#troubleshooting)

---

## 🔧 Configuración Inicial

### Primera vez con Git
```bash
# Configurar nombre (aparecerá en commits)
git config --global user.name "Angel Cruz"

# Configurar email (debe coincidir con GitHub)
git config --global user.email "tu-email@example.com"

# Editor por defecto (VS Code)
git config --global core.editor "code --wait"

# Ver configuración
git config --list

# Configurar credential helper (macOS)
git config --global credential.helper osxkeychain

# Colores en terminal
git config --global color.ui auto
```

### Verificar instalación
```bash
# Ver versión de Git
git --version

# Ver configuración de usuario
git config user.name
git config user.email
```

---

## 📖 Conceptos Básicos

### Estados de Git
```
Working Directory → Staging Area → Repository
     (add)              (commit)

1. Working Directory: Archivos en tu carpeta
2. Staging Area: Archivos preparados para commit
3. Repository: Historial de commits
```

### Áreas de Git
```
┌─────────────────┐
│ Working Dir     │  ← Aquí editas archivos
│ (Modified)      │
└────────┬────────┘
         │ git add
         ↓
┌─────────────────┐
│ Staging Area    │  ← Archivos preparados
│ (Staged)        │
└────────┬────────┘
         │ git commit
         ↓
┌─────────────────┐
│ Repository      │  ← Historial permanente
│ (Committed)     │
└────────┬────────┘
         │ git push
         ↓
┌─────────────────┐
│ Remote (GitHub) │  ← Respaldo en nube
└─────────────────┘
```

---

## 🔄 Workflow Diario

### Iniciar proyecto nuevo
```bash
# Crear carpeta
mkdir mi-proyecto
cd mi-proyecto

# Inicializar Git
git init

# Verificar
git status
```

### Workflow básico
```bash
# 1. Ver estado actual
git status

# 2. Agregar archivos al staging
git add archivo.py              # Agregar archivo específico
git add .                       # Agregar TODOS los archivos
git add *.py                    # Agregar todos los .py
git add carpeta/                # Agregar carpeta completa

# 3. Ver qué está en staging
git status

# 4. Commit (guardar cambios)
git commit -m "Mensaje descriptivo del cambio"

# 5. Ver historial
git log
git log --oneline              # Versión resumida
git log --oneline -5           # Últimos 5 commits

# 6. Push a GitHub (remoto)
git push origin main
```

### Ver cambios antes de commit
```bash
# Ver cambios no staged
git diff

# Ver cambios staged
git diff --staged

# Ver cambios de archivo específico
git diff archivo.py

# Ver cambios entre commits
git diff commit1 commit2
```

---

## 🌿 Branches (Ramas)

### Conceptos de Branches
```
main (rama principal)
├── feature/nueva-funcionalidad
├── fix/corregir-bug
└── experiment/probar-idea

Cada rama es una línea de desarrollo independiente
```

### Comandos de Branches
```bash
# Ver branches existentes
git branch                      # Locales
git branch -a                   # Todas (local + remoto)
git branch -v                   # Con último commit

# Crear branch nueva
git branch nombre-branch

# Crear y cambiar en un comando
git checkout -b nombre-branch
# o (más nuevo)
git switch -c nombre-branch

# Cambiar de branch
git checkout nombre-branch
# o
git switch nombre-branch

# Renombrar branch
git branch -m viejo-nombre nuevo-nombre

# Eliminar branch
git branch -d nombre-branch     # Solo si está merged
git branch -D nombre-branch     # Forzar eliminación

# Ver en qué branch estás
git branch                      # * indica branch actual
```

### Naming Conventions para Branches
```bash
feature/   → Nueva funcionalidad
  Ejemplo: feature/calculadora-avanzada
  
fix/       → Corrección de bug
  Ejemplo: fix/division-por-cero
  
hotfix/    → Fix urgente para producción
  Ejemplo: hotfix/security-patch
  
docs/      → Cambios en documentación
  Ejemplo: docs/update-readme
  
refactor/  → Refactorización de código
  Ejemplo: refactor/clean-functions
  
test/      → Agregar tests
  Ejemplo: test/unit-tests-calculator
  
experiment/→ Probar ideas
  Ejemplo: experiment/nueva-libreria
  
day/       → Para curso/aprendizaje
  Ejemplo: day/5-funciones-avanzadas
```

### Workflow con Branches
```bash
# 1. Crear branch desde main
git checkout main
git pull origin main            # Asegurar que main está actualizado
git checkout -b feature/mi-nueva-feature

# 2. Trabajar en la branch
# ... editar archivos ...
git add .
git commit -m "feat: Add new feature"

# 3. Push branch a GitHub
git push origin feature/mi-nueva-feature

# 4. Crear Pull Request en GitHub
# (Ver sección Pull Requests)

# 5. Después del merge, actualizar main local
git checkout main
git pull origin main

# 6. Eliminar branch local
git branch -d feature/mi-nueva-feature

# 7. Listo para nueva feature
git checkout -b feature/siguiente-feature
```

---

## 🔀 Merge y Conflictos

### Tipos de Merge
```bash
# 1. Fast-forward merge (sin conflictos, lineal)
git checkout main
git merge feature/mi-feature

# 2. Three-way merge (crea commit de merge)
git checkout main
git merge feature/mi-feature -m "Merge feature/mi-feature"

# 3. Squash merge (combina commits en uno)
git checkout main
git merge --squash feature/mi-feature
git commit -m "Add complete feature"
```

### Resolver Conflictos
```bash
# Cuando hay conflicto, Git te avisa:
# CONFLICT (content): Merge conflict in archivo.py

# 1. Ver archivos con conflicto
git status

# 2. Abrir archivo conflictivo
# Verás algo así:

<<<<<<< HEAD
tu código actual (main)
=======
código de la otra branch
>>>>>>> feature/mi-feature

# 3. Editar manualmente
# Decidir qué código mantener
# Eliminar los marcadores <<<<<<, =======, >>>>>>>

# 4. Marcar como resuelto
git add archivo.py

# 5. Completar merge
git commit -m "fix: Resolve merge conflict in archivo.py"

# 6. Push
git push origin main
```

### Abortar Merge
```bash
# Si el conflicto es muy complejo y quieres empezar de nuevo
git merge --abort

# Vuelves al estado antes del merge
```

---

## 🌐 GitHub (Remoto)

### Conectar repositorio local con GitHub
```bash
# 1. Crear repo en GitHub (sin README)

# 2. Agregar remote
git remote add origin https://github.com/usuario/repo.git

# 3. Verificar remote
git remote -v

# 4. Push inicial
git branch -M main
git push -u origin main
```

### Comandos Remote
```bash
# Ver remotes configurados
git remote -v

# Agregar remote
git remote add nombre-remote url

# Cambiar URL de remote
git remote set-url origin nueva-url

# Eliminar remote
git remote remove nombre-remote

# Renombrar remote
git remote rename viejo-nombre nuevo-nombre
```

### Push (Subir cambios)
```bash
# Push a main
git push origin main

# Push a branch específica
git push origin nombre-branch

# Push todas las branches
git push --all origin

# Push con fuerza (CUIDADO)
git push --force origin main    # Sobrescribe historial remoto

# Primera vez pushing branch
git push -u origin nombre-branch
# -u crea tracking, luego solo: git push
```

### Pull (Descargar cambios)
```bash
# Pull de main
git pull origin main

# Pull de branch específica
git pull origin nombre-branch

# Pull con rebase (sin crear merge commit)
git pull --rebase origin main

# Fetch (descargar sin merge)
git fetch origin
git merge origin/main           # Merge manual después
```

### Fetch vs Pull
```bash
# FETCH: Descarga cambios pero NO los aplica
git fetch origin
# Ahora puedes ver cambios antes de merge

# PULL: Descarga Y aplica cambios (fetch + merge)
git pull origin main
# Equivalente a:
# git fetch origin
# git merge origin/main
```

### Clone (Descargar repositorio)
```bash
# Clonar repositorio
git clone https://github.com/usuario/repo.git

# Clonar en carpeta específica
git clone https://github.com/usuario/repo.git mi-carpeta

# Clonar branch específica
git clone -b nombre-branch https://github.com/usuario/repo.git
```

---

## 🔃 Pull Requests

### Crear Pull Request (en GitHub)
```bash
# 1. Push de tu branch
git push origin feature/mi-feature

# 2. En GitHub:
#    - Verás banner: "Compare & pull request"
#    - Click en el botón
#    - O: Pull requests → New pull request

# 3. Configurar PR:
Title: [Descriptivo] Add new feature
Base: main ← Into
Compare: feature/mi-feature ← From

Description:
## What's Changed
- Added X functionality
- Fixed Y bug
- Updated Z documentation

## Testing
- [x] Tested locally
- [x] All tests passing
- [x] No conflicts

## Screenshots (si aplica)
[Imagen]

# 4. Create pull request

# 5. Review process
#    - Reviewer: Comenta, aprueba o solicita cambios
#    - Author: Hace cambios si necesario
#    - Push nuevos commits a MISMA branch
#    - PR se actualiza automáticamente

# 6. Merge
#    - Merge pull request
#    - Confirm merge
#    - Delete branch (cleanup)
```

### Actualizar PR con nuevos cambios
```bash
# Si el reviewer pidió cambios:

# 1. Hacer cambios localmente
# ... editar archivos ...

# 2. Commit
git add .
git commit -m "fix: Address review comments"

# 3. Push a MISMA branch
git push origin feature/mi-feature

# 4. PR se actualiza automáticamente en GitHub
```

### Sincronizar PR con main (si main cambió)
```bash
# Si main avanzó mientras trabajabas en tu branch

# 1. Actualizar main local
git checkout main
git pull origin main

# 2. Volver a tu branch
git checkout feature/mi-feature

# 3. Merge main en tu branch
git merge main

# 4. Resolver conflictos si hay
# ... resolver ...
git add .
git commit -m "fix: Merge main into feature branch"

# 5. Push
git push origin feature/mi-feature
```

---

## 🚨 Comandos de Emergencia

### Deshacer cambios
```bash
# Deshacer cambios en archivo (antes de add)
git checkout -- archivo.py
# o (más nuevo)
git restore archivo.py

# Deshacer ALL cambios no staged
git checkout .
# o
git restore .

# Quitar archivo de staging (después de add)
git reset HEAD archivo.py
# o
git restore --staged archivo.py

# Deshacer último commit (mantiene cambios)
git reset --soft HEAD~1

# Deshacer último commit (descarta cambios)
git reset --hard HEAD~1

# Deshacer últimos N commits
git reset --soft HEAD~3     # Mantiene cambios
git reset --hard HEAD~3     # Descarta cambios
```

### Modificar commits
```bash
# Modificar último commit (agregar archivos olvidados)
git add archivo-olvidado.py
git commit --amend --no-edit

# Modificar mensaje del último commit
git commit --amend -m "Nuevo mensaje"

# Modificar autor del último commit
git commit --amend --author="Nombre <email@example.com>"
```

### Stash (Guardar cambios temporalmente)
```bash
# Guardar cambios sin commit
git stash

# Guardar con mensaje
git stash save "Work in progress on feature X"

# Ver stashes guardados
git stash list

# Aplicar último stash (mantiene stash)
git stash apply

# Aplicar último stash (elimina stash)
git stash pop

# Aplicar stash específico
git stash apply stash@{2}

# Eliminar stash
git stash drop stash@{0}

# Eliminar todos los stashes
git stash clear
```

### Recuperar commits "perdidos"
```bash
# Ver historial de TODOS los cambios (incluso los "eliminados")
git reflog

# Recuperar commit específico
git checkout abc1234             # Hash del commit en reflog

# Crear branch desde commit recuperado
git checkout -b recovered-work abc1234
```

### Revertir commit (crear nuevo commit que deshace cambios)
```bash
# Revertir último commit (crea nuevo commit)
git revert HEAD

# Revertir commit específico
git revert abc1234

# Revertir sin hacer commit automáticamente
git revert --no-commit abc1234
# ... revisar cambios ...
git commit -m "Revert: Description"
```

---

## 🚫 .gitignore

### ¿Qué es .gitignore?

Archivo que indica qué archivos/carpetas Git debe IGNORAR (no versionar).

### Crear .gitignore
```bash
# Crear archivo
touch .gitignore

# Agregar patrones
echo "venv/" >> .gitignore
echo "*.pyc" >> .gitignore
```

### Patrones Comunes Python
```gitignore
# Virtual environments
venv/
env/
ENV/
.venv/

# Python cache
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# IDEs
.vscode/
.idea/
*.swp
*.swo

# macOS
.DS_Store

# Logs
*.log

# Database
*.db
*.sqlite3

# Environment variables
.env
.env.local

# Secrets
*_token*
*_secret*
*_key*
credentials*

# Jupyter
.ipynb_checkpoints

# Build
build/
dist/
*.egg-info/
```

### Ignorar archivo ya tracked
```bash
# Si ya hiciste commit del archivo:

# 1. Eliminar del tracking (mantiene archivo local)
git rm --cached archivo.py

# 2. Agregar a .gitignore
echo "archivo.py" >> .gitignore

# 3. Commit
git add .gitignore
git commit -m "chore: Add archivo.py to gitignore"
```

---

## ✅ Buenas Prácticas

### Commit Messages

#### Formato recomendado:
```
type: Short description (50 chars max)

Longer description if needed (wrap at 72 chars).
Explain WHAT and WHY, not HOW.

- Bullet points are ok
- Use imperative mood: "Add" not "Added"
```

#### Types comunes:
```
feat:     Nueva funcionalidad
fix:      Corrección de bug
docs:     Cambios en documentación
style:    Formato (sin cambios de código)
refactor: Refactorización (sin cambios funcionales)
test:     Agregar/modificar tests
chore:    Tareas de mantenimiento
perf:     Mejoras de performance
```

#### Ejemplos:
```bash
# Malo
git commit -m "fix"
git commit -m "cambios"
git commit -m "asdfsadf"

# Bueno
git commit -m "feat: Add temperature converter function"
git commit -m "fix: Resolve division by zero error"
git commit -m "docs: Update installation instructions"
git commit -m "refactor: Simplify calculator logic"

# Muy bueno (con descripción)
git commit -m "feat: Add password generator

- Support custom length (default 12)
- Include letters, numbers, and symbols
- Add strength validation
- Update README with usage examples"
```

### Frecuencia de Commits
```bash
# Commit cuando:
✅ Completes una unidad lógica de trabajo
✅ Código funciona (no rompes nada)
✅ Antes de cambiar de tarea
✅ Fin del día

# NO commit:
❌ Código a medias que no compila
❌ Archivos de configuración personal
❌ Archivos temporales
❌ Secrets/tokens/passwords
```

### Workflow de Branches
```bash
# 1. main siempre estable (siempre funciona)

# 2. Crear branch para cada feature
git checkout -b feature/descripcion-corta

# 3. Commits frecuentes en la branch

# 4. Pull Request para merge a main

# 5. Code review antes de merge

# 6. Delete branch después de merge
```

### Sincronización
```bash
# Antes de empezar a trabajar:
git checkout main
git pull origin main

# Antes de hacer PR:
git checkout main
git pull origin main
git checkout tu-branch
git merge main                 # Resolver conflictos localmente

# Fin del día:
git push origin tu-branch      # Backup en GitHub
```

---

## 🔧 Troubleshooting

### Problema: "fatal: not a git repository"
```bash
# Causa: No has inicializado Git en esta carpeta

# Solución:
git init
```

### Problema: "Your branch is ahead of 'origin/main'"
```bash
# Causa: Tienes commits locales no subidos

# Solución:
git push origin main
```

### Problema: "Your branch is behind 'origin/main'"
```bash
# Causa: GitHub tiene commits que tú no tienes

# Solución:
git pull origin main
```

### Problema: "fatal: refusing to merge unrelated histories"
```bash
# Causa: Intentas merge de repos con historiales diferentes

# Solución:
git pull origin main --allow-unrelated-histories
```

### Problema: "Permission denied (publickey)"
```bash
# Causa: SSH key no configurado

# Solución: Usar HTTPS en lugar de SSH
git remote set-url origin https://github.com/usuario/repo.git
```

### Problema: Olvidé en qué branch estoy
```bash
# Ver branch actual
git branch
# El * indica donde estás

# O ver en prompt
git status
# Primera línea dice: "On branch nombre"
```

### Problema: Commitié en branch equivocada
```bash
# Si NO has hecho push:

# 1. Copiar hash del commit
git log --oneline
# Ejemplo: abc1234

# 2. Volver al commit anterior
git reset --hard HEAD~1

# 3. Cambiar a branch correcta
git checkout branch-correcta

# 4. Aplicar commit ahí
git cherry-pick abc1234
```

### Problema: Commitié archivo con secret
```bash
# 1. REVOCAR el secret inmediatamente

# 2. Eliminar del historial
git rm --cached archivo-con-secret

# 3. Agregar a .gitignore
echo "archivo-con-secret" >> .gitignore

# 4. Commit
git add .gitignore
git commit -m "fix: Remove secret and add to gitignore"

# 5. Force push
git push --force origin main
```

### Problema: "Merge conflict" y no sé qué hacer
```bash
# Opción 1: Abortar merge
git merge --abort

# Opción 2: Resolver manualmente
# 1. Abrir archivo conflictivo
# 2. Buscar <<<<<<< y >>>>>>>
# 3. Editar y decidir qué mantener
# 4. Eliminar marcadores
# 5. git add archivo
# 6. git commit
```

---

## 📚 Comandos por Categoría

### Información
```bash
git status                     # Estado actual
git log                        # Historial de commits
git log --oneline              # Historial resumido
git log --graph --all          # Historial gráfico
git show                       # Ver último commit
git show abc1234               # Ver commit específico
git diff                       # Ver cambios
git branch                     # Ver branches
git remote -v                  # Ver remotes
```

### Crear/Inicializar
```bash
git init                       # Iniciar repo
git clone url                  # Clonar repo
git branch nombre              # Crear branch
git checkout -b nombre         # Crear y cambiar branch
```

### Cambios
```bash
git add archivo                # Agregar archivo
git add .                      # Agregar todos
git commit -m "msg"            # Commit
git commit --amend             # Modificar último commit
git reset HEAD archivo         # Unstage archivo
git checkout -- archivo        # Descartar cambios
```

### Branches
```bash
git branch                     # Listar branches
git checkout nombre            # Cambiar branch
git checkout -b nombre         # Crear y cambiar
git merge nombre               # Merge branch
git branch -d nombre           # Eliminar branch
```

### Remoto
```bash
git remote add origin url      # Agregar remote
git push origin main           # Push
git pull origin main           # Pull
git fetch origin               # Fetch
git clone url                  # Clone
```

### Emergencias
```bash
git stash                      # Guardar temporalmente
git stash pop                  # Recuperar guardado
git reset --soft HEAD~1        # Deshacer commit
git reset --hard HEAD~1        # Deshacer commit y cambios
git reflog                     # Ver todo el historial
git cherry-pick abc1234        # Aplicar commit específico
```

---

## 🎯 Workflows Completos

### Workflow: Nueva Feature
```bash
# 1. Actualizar main
git checkout main
git pull origin main

# 2. Crear branch
git checkout -b feature/mi-feature

# 3. Trabajar
# ... editar archivos ...

# 4. Commit frecuentemente
git add .
git commit -m "feat: Add X functionality"

# 5. Push
git push origin feature/mi-feature

# 6. Create PR en GitHub

# 7. Review & Merge

# 8. Actualizar main local
git checkout main
git pull origin main

# 9. Cleanup
git branch -d feature/mi-feature
```

### Workflow: Fix Bug Urgente
```bash
# 1. Crear hotfix branch desde main
git checkout main
git pull origin main
git checkout -b hotfix/fix-critical-bug

# 2. Fix
# ... corregir bug ...

# 3. Test
# ... verificar que funciona ...

# 4. Commit
git add .
git commit -m "hotfix: Fix critical bug in production"

# 5. Push y PR
git push origin hotfix/fix-critical-bug
# Create PR en GitHub

# 6. Merge inmediato (después de review rápido)

# 7. Cleanup
git checkout main
git pull origin main
git branch -d hotfix/fix-critical-bug
```

### Workflow: Día de Aprendizaje
```bash
# 1. Crear branch del día
git checkout -b day/5-funciones-avanzadas

# 2. Estudiar y practicar
# ... hacer ejercicios ...

# 3. Commit al finalizar
git add .
git commit -m "day 5: Complete advanced functions module

Completed:
- Lambda functions
- Map, filter, reduce
- Decorators basics
- 15 exercises"

# 4. Push
git push origin day/5-funciones-avanzadas

# 5. Create PR (opcional, o merge directo)

# 6. Update main
git checkout main
git pull origin main
git branch -d day/5-funciones-avanzadas
```

---

## 🔗 Recursos Adicionales

### Documentación Oficial
- Git: https://git-scm.com/doc
- GitHub: https://docs.github.com

### Visualizar Git
- https://git-school.github.io/visualizing-git/
- http://onlywei.github.io/explain-git-with-d3/

### Cheat Sheets
- https://education.github.com/git-cheat-sheet-education.pdf

### Tutoriales Interactivos
- https://learngitbranching.js.org/
- https://try.github.io/

---

## 📝 Notas Finales

### ¿Cuándo usar Git?
```
✅ Siempre que escribas código
✅ Proyectos personales de aprendizaje
✅ Colaboración con otros
✅ Quieras historial de cambios
✅ Quieras experimentar sin miedo

❌ Archivos binarios grandes (videos, etc)
❌ Archivos generados automáticamente
❌ Secrets/passwords/tokens
```

### Git vs GitHub
```
Git = Sistema de control de versiones (LOCAL)
      - Corre en tu computadora
      - Funciona offline
      - Maneja historial

GitHub = Plataforma en la nube (REMOTO)
         - Almacena repositorios
         - Facilita colaboración
         - Pull Requests
         - Issues, Projects, etc
```

### Mantén este documento actualizado
```bash
# Cada vez que aprendas algo nuevo:
# 1. Agregar al documento
# 2. Commit
git add GIT_REFERENCE.md
git commit -m "docs: Update Git reference with new learnings"
git push origin main
```

---

**Última actualización:** Enero 2025  
**Versión:** 1.0  
**Autor:** Angel Cruz - SAP Developer transitioning to Python + AI

---

**💡 Tip:** Mantén este archivo abierto en VS Code mientras trabajas.  
Usa `Cmd+F` para buscar comandos rápidamente.

**🎯 Recuerda:** La práctica hace al maestro. No temas experimentar con Git.  
Siempre puedes deshacer o recuperar casi cualquier cosa.

**🚀 Happy Coding!**