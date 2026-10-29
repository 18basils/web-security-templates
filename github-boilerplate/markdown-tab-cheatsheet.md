# 📑 GitHub Markdown Tab View & Collapsible Section Cheatsheet

GitHub Flavored Markdown (GFM) does not execute arbitrary JavaScript tabs in `README.md`. However, you can achieve clean, interactive, tab-like experiences using these production-proven patterns:

---

## Pattern 1: Native Collapsible Accordion Tabs (`<details>` & `<summary>`)

The cleanest native way to present multi-platform installation guides or code snippets without cluttering your README.

### Example Code:

````markdown
<!-- Tab 1: Windows (Active / Open by default with 'open' attribute) -->
<details open>
<summary><b>💻 Windows Installation (Click to toggle)</b></summary>
<br>

```powershell
winget install :owner.:project
# Or run Setup.exe
```
</details>

<!-- Tab 2: macOS -->
<details>
<summary><b>🍏 macOS Installation</b></summary>
<br>

```bash
brew install --cask :project
# Or drag App to /Applications
```
</details>

<!-- Tab 3: Linux -->
<details>
<summary><b>🐧 Linux Installation</b></summary>
<br>

```bash
sudo snap install :project
```
</details>
````

---

## Pattern 2: Horizontal Pill Tab Navigation (Anchor Jumping)

Create horizontal tab pill navigation at the top of a section that smoothly jumps between platform guides:

```markdown
<!-- Navigation Bar -->
| [💻 Windows](#-windows-setup) | [🍏 macOS](#-macos-setup) | [🐧 Linux](#-linux-setup) | [📱 Mobile](#-mobile-setup) |
| :---: | :---: | :---: | :---: |

### 💻 Windows Setup
Instructions for Windows...

### 🍏 macOS Setup
Instructions for macOS...

### 🐧 Linux Setup
Instructions for Linux...

### 📱 Mobile Setup
Instructions for Mobile...
```

---

## Pattern 3: Matrix Grid Comparison View

For comparing feature parity across multiple operating systems or subscription tiers:

```markdown
| Feature | Windows 10/11 | macOS Sonoma/Sequoia | Android (Compose) | iOS (SwiftUI) |
| :--- | :---: | :---: | :---: | :---: |
| **Core Sync Engine** | ✅ | ✅ | ✅ | ✅ |
| **Hardware Acceleration** | ✅ | ✅ | ✅ | ✅ |
| **System Tray / Menu Bar** | ✅ | ✅ | ❌ | ❌ |
| **Home Screen Widgets** | ❌ | ❌ | ✅ | ✅ |
| **Offline Execution** | ✅ | ✅ | ✅ | ✅ |
```

---

## Pattern 4: Documentation Generator Code Tabs (MkDocs / Docusaurus / VitePress)

If your project uses a static documentation generator, use their native tab syntax:

### Material for MkDocs:
````markdown
=== "Python"
    ```python
    pip install my-package
    ```

=== "Node.js"
    ```bash
    npm install my-package
    ```

=== "Go"
    ```bash
    go get github.com/owner/package
    ```
````

### Docusaurus / Starlight:
````markdown
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs>
  <TabItem value="npm" label="npm" default>
    ```bash
    npm install my-package
    ```
  </TabItem>
  <TabItem value="yarn" label="Yarn">
    ```bash
    yarn add my-package
    ```
  </TabItem>
  <TabItem value="pnpm" label="pnpm">
    ```bash
    pnpm add my-package
    ```
  </TabItem>
</Tabs>
````
