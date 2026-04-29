# BrainPop Lab Website: Internal Guide

Welcome to the BrainPop website repository. This site is built using **Jekyll** and is hosted via **GitHub Pages**. It has been designed to be easily maintainable by any lab member without needing to write code. 

All content is managed through plain-text files in the `_data/` folder. When you push changes to the `main` branch, the website will automatically rebuild and update within a few minutes.

---

## Quick Reference: How to Update

### 1. Updating Text Content
Most of the site's text (About, Join Us, Contact) lives in `_data/content.yml`.
- **Formatting:** We use Markdown for text.
- **Important:** In YAML files, multi-line text must be indented. If you see a `|`, ensure the text below it is indented by at least two spaces.

### 2. Managing the Team (People)
The team list is in `_data/people.yml`.
- **To add a member:** 
  1. Upload their photo to `assets/images/people/`. Use a square or portrait aspect ratio.
  2. Add a new entry in `_data/people.yml` following the existing pattern.
  3. Ensure the `image:` field matches the filename you uploaded.
- **Profile Photos:** Faisal's photo is `faisal_mushtaq.jpg`. Others use silhouettes (`placeholder.png`) until a real photo is provided.

### 3. Adding Projects
Projects are listed in `_data/projects.yml`.
- **Categories:** Use `category: "Research"`, `"Training"`, or `"Software"`. These are color-coded automatically.
- **Images:** Project header images are stored in `assets/images/projects/`.

### 4. Partnerships & Funders
Managed in `_data/partnerships.yml`.
- **Partners:** Displayed with descriptions and links.
- **Funders:** Displayed as simplified cards (logo + name) at the bottom of the page.
- **Logos:** Logos are stored in `assets/images/logos/`.

---

## Project Structure

```text
brainpop-site/
├── _data/             <-- EDIT THESE FOR CONTENT
│   ├── content.yml      # About, Join, Contact text
│   ├── people.yml       # Team members & bios
│   ├── projects.yml     # Research, Training, Software projects
│   └── partnerships.yml # Partners and Funders info
├── _includes/         <-- HTML Layout Sections
├── assets/
│   ├── css/style.css    # Site styling (editorial aesthetic)
│   └── images/          # Photos and Logos
└── index.md           # Homepage structure
```

---

## Aesthetic Guidelines
The site follows a clean, editorial aesthetic. To maintain this look:
- **Typography:** We use *Newsreader* for headings and *DM Sans* for body text.
- **Colors:** Use the `--accent` green (`#067843`) sparingly for emphasis.
- **Imagery:** Use high-quality, atmospheric photography. Hero and section backgrounds should be darkened/processed to ensure text legibility.

## Technical Notes
- **Local Preview:** If you have Jekyll installed, run `bundle exec jekyll serve` to preview changes locally at `localhost:4000`.
- **Deployment:** The site is live at [faisalmushtaq.github.io/brainpop-site/](https://faisalmushtaq.github.io/brainpop-site/).
- **Scroll Offset:** If you add new sections, the CSS includes a `scroll-margin-top` fix to ensure the fixed header doesn't cover section titles when navigating.

---
*Maintained by the BrainPop Lab. For major structural changes, please consult with the PI.*

<!-- Triggering workflow cache refresh -->
# Trigger workflow
