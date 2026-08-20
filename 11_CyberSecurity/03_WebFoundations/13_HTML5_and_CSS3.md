# 13. HTML5 and CSS3

> Phase 3 — Web Foundations

This module teaches HTML and CSS as the structural and presentation layers of the web. The goal is not to memorize tags or CSS properties in isolation. You should understand how a browser interprets a document, how semantic structure affects accessibility and maintainability, how the cascade decides which styles win, and how to build responsive layouts that remain usable on different devices.

JavaScript is intentionally not treated as a separate Phase 3 course because the unified track does not list a standalone JavaScript Fundamentals course. Browser-side JavaScript is introduced in **Client-Side Technologies**, where it is needed to understand DOM manipulation, events, browser APIs, and asynchronous requests.

## 1. Topic Title

**HTML5 and CSS3**

## 2. Learning Objectives

By the end of this module, you should be able to:

- Explain the role of HTML, CSS, JavaScript, the browser, and the web server in a web application.
- Build valid HTML documents using semantic elements instead of relying only on generic `<div>` elements.
- Create accessible headings, navigation, images, tables, forms, audio/video, and embedded content.
- Explain block-level versus inline behavior and how CSS changes default rendering.
- Apply CSS using selectors, inheritance, the cascade, specificity, and source order.
- Explain the box model and calculate element dimensions correctly.
- Build page layouts with Flexbox and CSS Grid.
- Create responsive designs using relative units, media queries, and mobile-first techniques.
- Use pseudo-classes, pseudo-elements, custom properties, transitions, and basic animations appropriately.
- Debug HTML and CSS using browser developer tools.

## 3. Prerequisites

You should already understand:

- Basic computer and operating-system concepts from Phase 1.
- Files, directories, extensions, and text editors.
- Basic client-server terminology is helpful, but this module also introduces the browser side of that relationship.
- No prior HTML or CSS experience is required.

Recommended tools:

- A modern browser such as Chrome, Edge, or Firefox.
- Visual Studio Code or another text editor.
- Browser Developer Tools.
- A simple local web server. Python can provide one with `python -m http.server`.

## 4. Core Concepts Explanation


### 4.1 What HTML, CSS, and JavaScript Actually Do

A browser receives resources—normally HTML, CSS, JavaScript, images, fonts, and other files—and converts them into an interactive page.

At a high level:

- **HTML** describes document structure and meaning.
- **CSS** controls presentation and layout.
- **JavaScript** adds behavior and dynamic interaction.
- The **browser** parses these resources and constructs internal representations used to render the page.

Suppose a server returns this HTML:
```html
<h1>Server Status</h1>
<p>All systems operational.</p>
```
HTML tells the browser that one piece of text is a top-level heading and another is a paragraph. It does not primarily say "make this 32 pixels tall." Those visual decisions belong in CSS.

Now add CSS:
```css
h1 {
    font-size: 2rem;
    margin-bottom: 0.5rem;
}

p {
    color: #444;
}
```
The browser applies the style rules to the matching elements. Later, JavaScript could update the status text after receiving data from an API.

Keeping structure, presentation, and behavior conceptually separate improves maintainability. A large application may bundle them using frameworks, but the browser still ultimately deals with these three responsibilities.
### 4.2 Anatomy of a Complete HTML Document

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="A simple infrastructure status page">

    <title>Infrastructure Status</title>

    <link rel="stylesheet" href="styles.css">

    <style>
        /* Small embedded styles are possible, but external CSS is preferable
           for most maintainable projects. */
    </style>
</head>
<body>
    <header>
        <h1>Infrastructure Status</h1>
    </header>

    <main>
        <p>Current service health will appear here.</p>
    </main>

    <script src="app.js" defer></script>
</body>
</html>
```
Important parts:

**`<!DOCTYPE html>`** tells the browser to use standards-oriented HTML parsing. It is not an HTML element.

**`<html lang="en">`** is the root element. The `lang` attribute helps screen readers, translation tools, and search engines understand the document language.

**`<meta charset="UTF-8">`** sets the character encoding. UTF-8 should be your default for modern web pages.

**Viewport metadata** is essential for responsive design. Without it, mobile browsers may render the page as a scaled desktop layout.

**`<link rel="stylesheet">`** loads an external stylesheet.

**`<style>`** allows internal CSS. It is useful for experiments or very small pages but should not become the default for larger projects.

**`<script src="..." defer>`** loads JavaScript. `defer` allows the browser to continue parsing the HTML while downloading the script and executes it after parsing is complete.
### 4.3 Elements, Tags, Attributes, and the DOM Tree

An HTML element consists of a start tag, content, and usually an end tag:
```html
<p class="message">Backup completed.</p>
```
Here:

- `<p>` begins a paragraph element.
- `class="message"` is an attribute.
- `Backup completed.` is text content.
- `</p>` closes the element.

Elements are nested to form a tree:
```html
<main>
    <section>
        <h2>Servers</h2>
        <ul>
            <li>web-01</li>
            <li>db-01</li>
        </ul>
    </section>
</main>
```
The browser converts this structure into the **Document Object Model (DOM)**. JavaScript later interacts with this DOM tree rather than editing the source file directly.

Correct nesting matters. A child should be closed before its parent closes. Browser error recovery can make invalid markup appear to work, but relying on recovery creates inconsistent behavior and debugging problems.
### 4.4 Semantic HTML

Semantic elements communicate meaning, not just appearance. Common semantic elements include:

- `<header>` — introductory content for a page or section.
- `<nav>` — major navigation links.
- `<main>` — the dominant content of the page.
- `<section>` — a thematic grouping, usually with a heading.
- `<article>` — a self-contained item that could stand independently.
- `<aside>` — tangential or supporting content.
- `<footer>` — closing information for a page or section.
- `<figure>` and `<figcaption>` — media and its caption.
- `<time>` — machine-readable time/date information.

Compare:
```html
<!-- Generic structure -->
<div class="top">
    <div class="links">...</div>
</div>

<!-- Semantic structure -->
<header>
    <nav>...</nav>
</header>
```
Both can be styled, but the semantic version communicates intent to browsers, assistive technologies, developers, and automated tools.

Do not use semantic tags merely because they exist. A `<section>` should represent a meaningful thematic section, not just a CSS wrapper.
### 4.5 Headings and Document Hierarchy

HTML provides headings from `<h1>` to `<h6>`. Their purpose is document hierarchy.

Example:
```html
<h1>Cloud Operations Dashboard</h1>

<section>
    <h2>Compute</h2>

    <section>
        <h3>Production Servers</h3>
    </section>
</section>

<section>
    <h2>Storage</h2>
</section>
```
Do not choose `<h4>` because it "looks smaller." Use the heading level that matches the content hierarchy, then use CSS to control appearance.

A logical heading hierarchy improves keyboard navigation and screen-reader navigation.
### 4.6 Paragraphs, Inline Text, and Formatting Semantics

```html
<p>
    The deployment is <strong>blocked</strong> because the
    <em>production approval</em> is missing.
</p>

<p>
    Run <code>systemctl status nginx</code> to inspect the service.
</p>

<pre><code>
server {
    listen 80;
}
</code></pre>
```
Useful inline semantics:

- `<strong>` indicates strong importance.
- `<em>` indicates stress emphasis.
- `<code>` represents code.
- `<kbd>` represents keyboard/user input.
- `<samp>` represents sample program output.
- `<mark>` highlights relevant text.
- `<small>` represents side comments or fine print.
- `<abbr>` can provide an expanded meaning for abbreviations.

Avoid using `<b>` and `<i>` only as replacements for CSS unless their HTML semantics are appropriate.
### 4.7 Block and Inline Elements

Historically HTML elements were often described as **block** or **inline** based on default browser CSS.

A block-level element usually:

- Begins on a new line.
- Expands to available inline width.
- Accepts layout dimensions in expected ways.

An inline element usually:

- Flows inside text.
- Does not start a new line by default.
- Is sized by its content.

Example:
```html
<p>
    Server <span class="healthy">web-01</span> is online.
</p>
```
```css
.healthy {
    color: green;
    font-weight: 700;
}
```
`<p>` behaves as a block by default. `<span>` is an inline generic container.

CSS can change this using `display`:
```css
.badge {
    display: inline-block;
    padding: 0.25rem 0.5rem;
}
```
### 4.8 `<div>` and `<span>`

`<div>` and `<span>` are generic containers with little semantic meaning.

Use:

- `<div>` when you need a generic block/container for grouping or layout.
- `<span>` when you need a generic inline hook inside text.

Do **not** build the entire page from nested `<div>` elements if semantic alternatives fit the content.
### 4.9 Links and URLs

```html
<a href="/reports/today.html">Today's Report</a>

<a href="https://example.com/docs" target="_blank" rel="noopener">
    External Documentation
</a>

<a href="#database-status">Jump to Database Status</a>
```
`href` can contain:

- Absolute URLs.
- Relative URLs.
- Fragment identifiers beginning with `#`.
- Special schemes such as `mailto:` or `tel:`.

When opening untrusted external content in a new browsing context, `rel="noopener"` prevents the opened page from obtaining direct access to the opener in older patterns and communicates safer intent.

Use descriptive link text. "Read the backup policy" is better than "click here."
### 4.10 Images and Accessible Alternative Text

```html
<img
    src="images/network-diagram.png"
    alt="Diagram showing web servers connected to a load balancer and database"
    width="900"
    height="500"
>
```
The `alt` attribute provides a text alternative.

Good alternative text depends on purpose. If the image communicates architecture, describe the useful architecture. If it is decorative, use `alt=""` so assistive software can ignore it.

Providing intrinsic `width` and `height` helps the browser reserve layout space and can reduce content movement while the image loads.
### 4.11 Lists

```html
<h2>Deployment Steps</h2>
<ol>
    <li>Run tests</li>
    <li>Build image</li>
    <li>Deploy to staging</li>
</ol>

<h2>Supported Platforms</h2>
<ul>
    <li>Linux</li>
    <li>Windows</li>
</ul>

<dl>
    <dt>HTTP</dt>
    <dd>Application-layer protocol used for web communication.</dd>

    <dt>TLS</dt>
    <dd>Protocol that protects data in transit.</dd>
</dl>
```
### 4.12 Tables

```html
<table>
    <caption>Server Health</caption>
    <thead>
        <tr>
            <th scope="col">Hostname</th>
            <th scope="col">Environment</th>
            <th scope="col">Status</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th scope="row">web-01</th>
            <td>Production</td>
            <td>Healthy</td>
        </tr>
        <tr>
            <th scope="row">db-01</th>
            <td>Production</td>
            <td>Warning</td>
        </tr>
    </tbody>
</table>
```
Use tables for tabular data, not general page layout. `<caption>`, `<thead>`, `<tbody>`, `<th>`, and `scope` improve clarity and accessibility.
### 4.13 Forms: The Most Important HTML Interaction Primitive

```html
<form action="/login" method="post">
    <div>
        <label for="username">Username</label>
        <input
            id="username"
            name="username"
            type="text"
            autocomplete="username"
            required
        >
    </div>

    <div>
        <label for="password">Password</label>
        <input
            id="password"
            name="password"
            type="password"
            autocomplete="current-password"
            required
        >
    </div>

    <button type="submit">Sign in</button>
</form>
```
Important form concepts:

**`name`** controls the key used when form data is submitted.

**`id`** identifies an element in the document and connects labels using `for`.

**`type`** changes input behavior and validation.

**`required`**, `min`, `max`, `pattern`, and related attributes provide browser-level validation.

Client-side validation improves usability but is **not a security boundary**. A user can bypass the browser and send arbitrary requests, so the server must independently validate all submitted data.
### 4.14 Common Input Types

```html
<input type="email" name="email">
<input type="number" name="replicas" min="1" max="10">
<input type="date" name="maintenance_date">

<label>
    <input type="checkbox" name="notify" value="yes">
    Notify operations team
</label>

<label>
    <input type="radio" name="environment" value="dev">
    Development
</label>

<label>
    <input type="radio" name="environment" value="prod">
    Production
</label>

<select name="region">
    <option value="eu">Europe</option>
    <option value="me">Middle East</option>
</select>

<textarea name="notes" rows="5"></textarea>
```
### 4.15 HTML Entities

```html
<p>5 &lt; 10</p>
<p>Tom &amp; Sara</p>
<p>&copy; 2026 Example Company</p>
```
Entities are useful when a character would otherwise be interpreted as markup or when a named entity improves readability. In modern UTF-8 HTML, many ordinary characters can be written directly.
### 4.16 Audio, Video, iframe, and Embedded Content

```html
<video controls width="720">
    <source src="demo.mp4" type="video/mp4">
    Your browser does not support embedded video.
</video>
```
```html
<iframe
    src="https://example.com/embedded-content"
    title="Embedded architecture documentation"
    loading="lazy">
</iframe>
```
Embedded third-party content has security, privacy, and performance implications. Later security modules will discuss sandboxing, content security policies, and trust boundaries. For now, understand that an `<iframe>` creates a nested browsing context rather than simply copying HTML into the page.
### 4.17 CSS Syntax

```css
selector {
    property: value;
}
```
Example:
```css
.server-card {
    border: 1px solid #ccc;
    padding: 1rem;
    border-radius: 0.5rem;
}
```
A CSS rule has:

- A selector.
- A declaration block.
- Property/value declarations.

CSS is forgiving: unsupported or invalid declarations are usually ignored rather than crashing the page. This makes debugging important because a typo may fail silently.
### 4.18 CSS Selectors

```css
/* Element selector */
p { line-height: 1.6; }

/* Class selector */
.card { padding: 1rem; }

/* ID selector */
#main-dashboard { max-width: 1200px; }

/* Descendant selector */
nav a { text-decoration: none; }

/* Child selector */
ul > li { margin-bottom: 0.25rem; }

/* Attribute selector */
input[type="email"] { border-color: steelblue; }

/* Multiple selectors */
h1, h2, h3 { font-family: system-ui, sans-serif; }
```
Prefer classes for reusable styling. IDs are valid but create high specificity and are often better reserved for unique document identification or scripting hooks.
### 4.19 The Cascade, Specificity, and Inheritance

When multiple CSS rules target the same property, the browser decides which declaration wins based on the cascade.

A simplified mental model:

1. Origin and importance.
2. Cascade layers when used.
3. Selector specificity.
4. Source order among equally specific rules.

Example:
```html
<p id="status" class="warning">Database latency elevated.</p>
```
```css
p {
    color: black;
}

.warning {
    color: orange;
}

#status {
    color: red;
}
```
The ID selector is more specific, so the text becomes red.

Do not respond to specificity problems by adding `!important` everywhere. That creates a stylesheet that becomes increasingly difficult to override. Prefer predictable classes, low specificity, and clear stylesheet organization.

Some properties, such as `color` and `font-family`, commonly inherit. Others, such as `margin` and `border`, generally do not.
### 4.20 CSS Box Model

Every normal element is rendered as a box consisting of:

1. Content
2. Padding
3. Border
4. Margin

Example:
```css
.card {
    width: 300px;
    padding: 20px;
    border: 2px solid #333;
    margin: 16px;
}
```
With default `box-sizing: content-box`, the declared `width: 300px` applies only to the content box. The visible box becomes wider after padding and border are added.

A common baseline is:
```css
*,
*::before,
*::after {
    box-sizing: border-box;
}
```
With `border-box`, the declared width includes content, padding, and border, which generally makes layout calculations easier.
### 4.21 Units: px, %, em, rem, vw, vh and Modern Viewport Units

Use units based on what the value should relate to:

- `px` — CSS pixels; useful for borders and precise small dimensions.
- `%` — relative to another computed dimension.
- `em` — relative to the element's font size in many contexts.
- `rem` — relative to the root font size.
- `vw` / `vh` — fractions of viewport width/height.
- Modern browsers also support viewport units such as `dvh` that better reflect dynamic mobile viewport behavior.

Example:
```css
:root {
    font-size: 100%;
}

body {
    font-size: 1rem;
}

.container {
    width: min(90%, 75rem);
    margin-inline: auto;
}

.hero-title {
    font-size: clamp(2rem, 5vw, 4rem);
}
```
### 4.22 Normal Flow and Positioning

By default, elements participate in normal document flow. CSS positioning changes how boxes are located.

- `position: static` — normal default.
- `relative` — remains in flow but can be offset and becomes a positioning reference.
- `absolute` — removed from normal flow and positioned relative to a containing block.
- `fixed` — positioned relative to the viewport.
- `sticky` — behaves like normal flow until a scrolling threshold is reached.

Avoid absolute positioning as your main page-layout tool. Flexbox and Grid are normally more robust.
### 4.23 Flexbox

```html
<div class="toolbar">
    <strong>Operations</strong>
    <nav>
        <a href="#">Dashboard</a>
        <a href="#">Alerts</a>
    </nav>
</div>
```
```css
.toolbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
}

.toolbar nav {
    display: flex;
    gap: 0.75rem;
}
```
Flexbox is primarily one-dimensional: it is excellent when laying items out along a row or column.

Important properties:

Container:
- `display: flex`
- `flex-direction`
- `justify-content`
- `align-items`
- `flex-wrap`
- `gap`

Item:
- `flex-grow`
- `flex-shrink`
- `flex-basis`
- shorthand `flex`
- `align-self`

Use Flexbox for navigation bars, toolbars, button groups, card internals, and other one-dimensional alignment problems.
### 4.24 CSS Grid

```html
<div class="dashboard">
    <article>CPU</article>
    <article>Memory</article>
    <article>Disk</article>
    <article>Network</article>
</div>
```
```css
.dashboard {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 1rem;
}
```
Grid is designed for two-dimensional layout: rows and columns together.

Useful concepts:

- Explicit tracks using `grid-template-columns`.
- Fractional units (`fr`).
- `minmax()`.
- `repeat()`.
- Named grid areas.
- Automatic placement.
- Row and column gaps.

For responsive cards, `repeat(auto-fit, minmax(...))` can often reduce the number of media queries you need.
### 4.25 Responsive Design and Mobile-First CSS

```css
.page {
    padding: 1rem;
}

.sidebar {
    display: none;
}

@media (min-width: 768px) {
    .page {
        display: grid;
        grid-template-columns: 16rem 1fr;
        gap: 1.5rem;
    }

    .sidebar {
        display: block;
    }
}
```
A mobile-first approach starts with the narrowest practical layout and progressively adds complexity as space becomes available.

Do not choose breakpoints based only on device brand names. Add a breakpoint when the content/layout actually needs one.

Responsive design also includes:

- Flexible images.
- Touch-friendly controls.
- Readable text lengths.
- Avoiding horizontal scrolling.
- Testing zoom and large text.
### 4.26 Pseudo-classes and Pseudo-elements

```css
a:hover {
    text-decoration: underline;
}

button:focus-visible {
    outline: 3px solid currentColor;
    outline-offset: 3px;
}

input:invalid {
    border-color: crimson;
}

.card::before {
    content: "";
    display: block;
    height: 4px;
    background: currentColor;
}
```
Pseudo-classes describe state or structure, such as `:hover`, `:focus-visible`, `:checked`, `:disabled`, `:first-child`, and `:nth-child()`.

Pseudo-elements create stylable conceptual parts such as `::before`, `::after`, `::first-line`, and `::marker`.

Never remove focus styles without replacing them with a clear keyboard-visible alternative.
### 4.27 CSS Custom Properties

```css
:root {
    --space-1: 0.5rem;
    --space-2: 1rem;
    --radius: 0.5rem;
}

.card {
    padding: var(--space-2);
    border-radius: var(--radius);
}
```
Custom properties allow reusable values and can participate in the cascade. They are useful for design tokens such as spacing, typography scales, surface colors, and component configuration.
### 4.28 Transitions and Animations

```css
.button {
    transform: translateY(0);
    transition: transform 150ms ease;
}

.button:hover {
    transform: translateY(-2px);
}
```
Animation should communicate state or improve continuity, not distract. Respect reduced-motion preferences:
```css
@media (prefers-reduced-motion: reduce) {
    *,
    *::before,
    *::after {
        scroll-behavior: auto !important;
        transition-duration: 0.01ms !important;
        animation-duration: 0.01ms !important;
    }
}
```
### 4.29 Accessibility Fundamentals

Accessibility is not a separate feature that should be added at the end.

Core practices:

- Use semantic HTML before adding ARIA.
- Associate form controls with labels.
- Provide meaningful alternative text.
- Preserve keyboard navigation.
- Maintain logical heading order.
- Ensure sufficient visual contrast.
- Do not encode meaning using color alone.
- Make focus indicators visible.
- Use buttons for actions and links for navigation.
- Test at increased zoom.
- Use ARIA only when native HTML cannot express the needed semantics.

Bad:
```html
<div onclick="save()">Save</div>
```
Better:
```html
<button type="button">Save</button>
```
The button already provides keyboard behavior, focusability, semantics, and expected assistive-technology support.
### 4.30 Browser Developer Tools for HTML/CSS Debugging

Developer Tools should be part of your normal workflow.

Practice:

1. Inspect an element.
2. Identify which CSS rules match.
3. Look for crossed-out declarations.
4. Check computed styles.
5. Toggle declarations on/off.
6. Inspect the box model.
7. Switch the responsive device toolbar.
8. Use the accessibility tree when available.
9. Inspect network-loaded stylesheets and images.

When a style "does not work," investigate systematically:
- Did the stylesheet load?
- Does the selector match?
- Is the declaration valid?
- Is another declaration winning the cascade?
- Is the property applicable to this element/layout context?


# Enhanced Deep-Dive — HTML5, CSS3, Rendering, Accessibility, and Responsive UI Engineering

The original module already contains the correct web-foundation topics. This expansion keeps every original concept and adds the browser-rendering, accessibility, CSS-architecture, responsive-design, security-boundary, and debugging knowledge needed before JavaScript, backend/API, application-security, and web-penetration-testing courses.

Use this mental model:

```text
HTTP response
    ↓
HTML parser → DOM
CSS parser  → CSSOM
      \       /
       \     /
       style resolution
            ↓
        render tree
            ↓
          layout
            ↓
           paint
            ↓
        compositing
            ↓
           pixels
```

And this design workflow:

```text
content meaning
    ↓
semantic HTML
    ↓
native accessible controls
    ↓
normal document flow
    ↓
CSS cascade + box model
    ↓
Flexbox / Grid
    ↓
responsive constraints
    ↓
interaction states + motion
    ↓
accessibility + performance review
    ↓
Developer Tools verification
```


### Deep Dive — Browser Rendering Pipeline

A browser does not turn an HTML file directly into pixels. HTML is parsed into a DOM tree. CSS is parsed into a CSS object model. The browser resolves styles for relevant elements, computes geometry during layout, paints visual details, and composites layers.

This explains why a page can be structurally correct while still rendering incorrectly, and why some style changes are more expensive than others.

#### Diagram / Mental Model

```text
HTML bytes ──> DOM ──────┐
                         ├─> style resolution
CSS bytes  ──> CSSOM ────┘
                           ↓
                       render tree
                           ↓
                         layout
                           ↓
                          paint
                           ↓
                       composite
```

#### Why It Matters

Later JavaScript code modifies the DOM and can cause style/layout/paint work, so this rendering model is foundational.



### Deep Dive — HTML Parser Error Recovery

Browsers try to recover from malformed markup instead of stopping. That can hide invalid nesting because the browser may silently close, move, or recreate elements.

Always inspect the live DOM when behavior seems strange.

#### Example

```html
<p>
    Paragraph text
    <div>Invalidly nested block content</div>
</p>
```

#### Why It Matters

The DOM produced by the parser may not match the source indentation.

#### Common Problems / Troubleshooting

A page that 'looks okay' is not proof of valid or semantically correct HTML.



### Deep Dive — URLs and Resource Resolution

HTML references resources by URL, not by your mental model of a local filesystem. A relative URL is resolved from the document's URL/base.

Understand:
- absolute URL
- root-relative URL
- document-relative URL
- parent-relative URL

#### Diagram / Mental Model

```text
Document:
https://site.test/docs/index.html

assets/app.css
→ https://site.test/docs/assets/app.css

/assets/app.css
→ https://site.test/assets/app.css

../assets/app.css
→ https://site.test/assets/app.css
```

#### Why It Matters

Many missing stylesheet/image errors are URL-resolution mistakes.



### Deep Dive — Semantic HTML as Information Architecture

Semantic HTML describes what a region means, not how it should look. The document should remain understandable with CSS disabled.

Use semantic elements when their meaning matches the content, and generic containers only when no semantic element fits.

#### Diagram / Mental Model

```text
body
├─ header
│  └─ nav
├─ main
│  ├─ section: overview
│  ├─ section: service health
│  │  ├─ article: API
│  │  └─ article: database
│  └─ section: maintenance
└─ footer
```

#### Why It Matters

Semantic structure improves accessibility, maintenance, search interpretation, and later DOM scripting.



### Deep Dive — Landmarks and Skip Links

Major semantic regions such as navigation and main content become landmarks. A skip link allows keyboard users to bypass repeated navigation.

#### Example

```html
<a class="skip-link" href="#main-content">
    Skip to main content
</a>

<header>
    <nav aria-label="Primary">...</nav>
</header>

<main id="main-content">
    ...
</main>
```

#### Why It Matters

Keyboard navigation should not require traversing a long menu on every page.



### Deep Dive — Headings as a Hierarchy

Heading levels represent nested document structure. Their visual size is a CSS concern.

A valid hierarchy makes it possible to understand a page by reading its headings alone.

#### Diagram / Mental Model

```text
h1 Cloud Operations
├─ h2 Compute
│  ├─ h3 Production
│  └─ h3 Development
└─ h2 Storage
   └─ h3 Backup
```

#### Why It Matters

Screen-reader users often navigate by headings.



### Deep Dive — Text Semantics for Technical Content

Technical pages benefit from semantic inline elements such as `code`, `kbd`, `samp`, `strong`, `em`, `abbr`, and `time`.

#### Example

```html
<p>
    Press <kbd>Ctrl</kbd> + <kbd>C</kbd>
    to stop <code>python -m http.server</code>.
</p>

<p>
    Output: <samp>Serving HTTP on 0.0.0.0...</samp>
</p>

<time datetime="2026-08-19T10:00:00+03:00">
    19 August 2026, 10:00
</time>
```

#### Why It Matters

Meaning survives styling changes and is more useful to assistive technologies.



### Deep Dive — Links vs Buttons

A link navigates to another location/resource. A button performs an action.

Do not create clickable generic containers when native elements already model the interaction.

#### Example

```html
<a href="/backup-policy">Read the backup policy</a>

<button type="button">Refresh health status</button>
```

#### Why It Matters

Native controls include correct keyboard behavior, semantics, focusability, and platform expectations.



### Deep Dive — Responsive Images

`srcset` and `sizes` let the browser select an appropriate image resource instead of downloading one oversized image for every viewport.

The browser makes the final choice based on the candidates and current rendering conditions.

#### Example

```html
<img
    src="/images/dashboard-800.webp"
    srcset="
        /images/dashboard-480.webp 480w,
        /images/dashboard-800.webp 800w,
        /images/dashboard-1400.webp 1400w
    "
    sizes="(min-width: 70rem) 60rem, 90vw"
    alt="Operations dashboard overview">
```

#### Why It Matters

Responsive images improve performance without sacrificing useful visual quality.



### Deep Dive — Figures and Captions

Use `<figure>` for self-contained visual or illustrative content and `<figcaption>` when a caption belongs with that media.

#### Example

```html
<figure>
    <img
        src="/images/topology.svg"
        alt="Three-tier application topology">

    <figcaption>
        Production application topology.
    </figcaption>
</figure>
```

#### Why It Matters

The relationship between media and caption becomes structural rather than merely visual.



### Deep Dive — Accessible Tables

A table is a data model with row/column relationships. Use `<caption>`, table header cells, and appropriate `scope` for simple header relationships.

Never use tables to create page layout.

#### Example

```html
<table>
    <caption>Production service health</caption>
    <thead>
        <tr>
            <th scope="col">Service</th>
            <th scope="col">Region</th>
            <th scope="col">Status</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th scope="row">API</th>
            <td>Cairo</td>
            <td>Healthy</td>
        </tr>
    </tbody>
</table>
```

#### Why It Matters

Header relationships make tabular data understandable beyond visual alignment.



### Deep Dive — Responsive Table Strategy

A wide table may not fit a narrow screen. Preserve table semantics and place it inside an overflow container rather than turning the entire data model into arbitrary divs.

#### Example

```html
<div class="table-scroll">
    <table>...</table>
</div>
```

#### Why It Matters

The table remains a table while the viewport gains a controlled horizontal scrolling strategy.



### Deep Dive — Form Submission Model

A form is a request-construction interface. Successful controls contribute name/value pairs when the form is submitted.

The `name` attribute is therefore part of the data contract; `id` is primarily a document identifier and label hook.

#### Diagram / Mental Model

```text
controls
name=value
name=value
   ↓ submit
browser encoding
   ↓
HTTP request
   ↓
server validates independently
```

#### Why It Matters

Understanding form submission prepares you for JavaScript FormData and backend request handling.



### Deep Dive — GET vs POST Form Semantics

GET forms usually encode values into the URL query string and fit retrieval/search operations. POST forms normally send form data in the request body and are often used for state-changing operations.

Method choice belongs to HTTP semantics and server design, not visual appearance.

#### Example

```html
<form action="/search" method="get">
    <label>
        Search
        <input name="q">
    </label>
</form>
```

#### Why It Matters

A GET search can be bookmarked or shared because state is represented in the URL.



### Deep Dive — Accessible Names and Descriptions

Every interactive form control needs an accessible name. An explicit `<label for>` relation is a strong default. Additional explanatory text can be connected using `aria-describedby` when appropriate.

#### Example

```html
<label for="replicas">Number of instances</label>

<input
    id="replicas"
    name="replicas"
    type="number"
    min="1"
    max="20"
    aria-describedby="replicas-help">

<p id="replicas-help">
    Production requires at least two instances.
</p>
```

#### Why It Matters

Placeholder text is temporary and should not be the only label.



### Deep Dive — `fieldset` and `legend`

Related controls such as radio groups need a group-level label as well as labels for each individual option.

#### Example

```html
<fieldset>
    <legend>Environment</legend>

    <label>
        <input type="radio"
               name="environment"
               value="dev"
               required>
        Development
    </label>

    <label>
        <input type="radio"
               name="environment"
               value="prod">
        Production
    </label>
</fieldset>
```

#### Why It Matters

Native grouping semantics are more reliable than custom div-based grouping.



### Deep Dive — Native Constraint Validation

HTML supports validation constraints such as `required`, `min`, `max`, `minlength`, `maxlength`, `pattern`, and specialized input types.

These are usability features. The browser is controlled by the user, so server-side validation remains mandatory.

#### Example

```html
<input
    name="replicas"
    type="number"
    min="1"
    max="20"
    required>
```

#### Why It Matters

Client validation reduces accidental bad input; it does not enforce trust.



### Deep Dive — Disabled vs Readonly Controls

Disabled and readonly controls behave differently. A disabled control is generally unavailable and not submitted. A readonly control cannot be edited but can remain part of submission for input types that support it.

#### Example

```html
<input name="asset_id" value="A-1042" readonly>
<input name="obsolete" value="x" disabled>
```

#### Why It Matters

This difference matters for both UX and the resulting request.



### Deep Dive — Button Types in Forms

A `<button>` inside a form defaults to submit behavior unless another type is specified.

Always choose the type intentionally.

#### Example

```html
<button type="button">Preview</button>
<button type="submit">Submit</button>
```

#### Why It Matters

Unexpected form submission is a common bug in interactive pages.



### Deep Dive — iframe Trust Boundary

An iframe creates a nested browsing context, not a simple visual copy of remote HTML.

Third-party frames have security, privacy, performance, and accessibility implications. Use `title`, loading controls, and a deliberately chosen `sandbox` policy when appropriate.

#### Example

```html
<iframe
    src="https://docs.example.test/embed"
    title="Architecture documentation"
    loading="lazy"
    sandbox="allow-scripts allow-same-origin">
</iframe>
```

#### Why It Matters

Embedding content is a trust decision.

#### Common Problems / Troubleshooting

Do not copy a permissive sandbox token list without understanding why each permission is required.



### Deep Dive — Full Cascade Mental Model

CSS conflict resolution is broader than specificity.

A useful simplified order is:
1. relevant declarations
2. origin and importance
3. cascade layers where used
4. specificity
5. source order

Specificity is only one stage.

#### Diagram / Mental Model

```text
matching declarations
       ↓
origin / importance
       ↓
cascade layer
       ↓
specificity
       ↓
source order
       ↓
winner
```

#### Why It Matters

This prevents endless escalation with IDs and `!important`.



### Deep Dive — Cascade Layers

Cascade layers let you establish stylesheet groups whose relative priority is defined intentionally.

A common architecture is reset → base → components → utilities.

#### Example

```css
@layer reset, base, components, utilities;

@layer base {
    body {
        font-family: system-ui, sans-serif;
    }
}

@layer components {
    .button {
        padding: 0.75rem 1rem;
    }
}
```

#### Why It Matters

Layers give stylesheet architecture a formal place in the cascade.



### Deep Dive — Specificity Discipline

Use reusable classes and shallow selectors. High-specificity selectors are hard to override and often create long-term maintenance problems.

#### Example

```css
/* harder to override */
#dashboard .content .card p {}

/* usually easier to maintain */
.card__description {}
```

#### Why It Matters

A stylesheet should be predictable rather than a competition for the strongest selector.



### Deep Dive — Box Model and `border-box`

With `content-box`, declared width applies to content only; padding and border add to the visible box. `border-box` includes border and padding inside the declared dimension.

A global border-box baseline makes component sizing more intuitive.

#### Diagram / Mental Model

```text
margin
└─ border
   └─ padding
      └─ content
```

#### Example

```css
*,
*::before,
*::after {
    box-sizing: border-box;
}
```

#### Why It Matters

Layout calculations become easier to reason about.



### Deep Dive — Margin Collapsing Awareness

Vertical block margins in normal flow can collapse in specific circumstances, so adjacent margins do not always add numerically.

Modern component layouts often prefer `gap` inside Flex/Grid containers for explicit spacing relationships.

#### Why It Matters

If vertical spacing appears to move outside a parent or become smaller than expected, investigate collapsing margins.



### Deep Dive — Logical Properties

Logical properties describe directions using inline/block axes rather than physical left/right/top/bottom.

Examples include `margin-inline`, `padding-block`, `inline-size`, and `border-inline-start`.

#### Example

```css
.container {
    max-inline-size: 75rem;
    margin-inline: auto;
    padding-inline: 1rem;
}
```

#### Why It Matters

Logical properties adapt better to different writing directions.



### Deep Dive — Responsive Sizing with `min()`, `max()`, and `clamp()`

CSS math functions express constraints directly and reduce unnecessary media queries.

#### Example

```css
.container {
    inline-size: min(92%, 75rem);
}

.hero-title {
    font-size:
        clamp(2rem, 2vw + 1rem, 4.5rem);
}
```

#### Why It Matters

Responsive design is fundamentally about constraints, not only breakpoints.



### Deep Dive — Intrinsic Sizing

CSS sizing can respond to content using concepts such as `min-content`, `max-content`, and `fit-content`.

These become especially useful in Grid and content-driven components.

#### Example

```css
.sidebar {
    inline-size: fit-content(20rem);
}
```

#### Why It Matters

Intrinsic sizing lets content participate in layout rather than forcing arbitrary fixed widths.



### Deep Dive — Containing Blocks and Absolute Positioning

Absolutely positioned boxes are positioned relative to a containing block. A common deliberate pattern is to make a component `position: relative` so an overlay child can anchor to it.

#### Example

```css
.card {
    position: relative;
}

.card__badge {
    position: absolute;
    inset-block-start: 0.5rem;
    inset-inline-end: 0.5rem;
}
```

#### Why It Matters

Use positioning for overlays/anchoring, not as the main layout system.



### Deep Dive — Stacking Context and z-index

`z-index` values do not compete globally. Elements can belong to separate stacking contexts. A child with a huge z-index cannot escape its parent's stacking context to outrank an unrelated context.

#### Diagram / Mental Model

```text
Context A
├─ child z=1
└─ child z=9999

Context B
└─ child z=2

If A is below B,
A's 9999 child can still remain below B.
```

#### Why It Matters

When z-index seems broken, identify stacking contexts instead of increasing the number.



### Deep Dive — Overflow and Scroll Containers

`overflow` controls how excess content is handled. A scroll container changes scrolling behavior and can affect sticky positioning.

Do not hide overflow just to conceal a broken layout.

#### Example

```css
.log-panel {
    max-block-size: 24rem;
    overflow: auto;
}
```

#### Why It Matters

Controlled overflow is useful for logs, code, tables, and panels.



### Deep Dive — Flexbox Main/Cross Axes

Flexbox becomes easier when you reason about the main and cross axes. `flex-direction` defines the main axis; alignment properties work relative to those axes.

#### Diagram / Mental Model

```text
flex-direction: row

main axis  ─────────────>
cross axis
    ↓
```

#### Example

```css
.toolbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 1rem;
}
```

#### Why It Matters

Axis-based reasoning works for both row and column layouts.



### Deep Dive — Flex Grow, Shrink, and Basis

Flex sizing has three conceptual inputs:
- basis: preferred starting size
- grow: participation in positive free space
- shrink: participation when available space is too small

#### Example

```css
.sidebar {
    flex: 0 0 16rem;
}

.main {
    flex: 1 1 30rem;
}
```

#### Why It Matters

Unexpected widths often come from shrink behavior rather than the declared width alone.



### Deep Dive — Flex/Grid Intrinsic Overflow and `min-inline-size: 0`

Flex and Grid items may refuse to shrink below intrinsic content size, causing long URLs, code, or tables to overflow.

Allow a flexible child to shrink when that matches the layout.

#### Example

```css
.main-content {
    min-inline-size: 0;
}
```

#### Why It Matters

This is a common real-world fix for flexible layouts.



### Deep Dive — Grid Track Sizing and `minmax(0, 1fr)`

Grid tracks combine explicit, intrinsic, and flexible sizing. `minmax(0, 1fr)` is a useful flexible track that can shrink below intrinsic content minimums.

#### Example

```css
.layout {
    display: grid;
    grid-template-columns:
        16rem minmax(0, 1fr);
    gap: 1.5rem;
}
```

#### Why It Matters

It prevents the flexible content track from unexpectedly overflowing.



### Deep Dive — Responsive Grid with `auto-fit` and `minmax()`

Grid can create a card layout that adapts naturally to available width without device-specific breakpoints.

#### Example

```css
.cards {
    display: grid;
    grid-template-columns:
        repeat(
            auto-fit,
            minmax(min(100%, 18rem), 1fr)
        );
    gap: 1rem;
}
```

#### Why It Matters

The component responds to available space instead of named device sizes.



### Deep Dive — Named Grid Areas

Named grid areas can make larger page layouts readable in CSS.

#### Example

```css
.page {
    display: grid;
    grid-template:
        "header header" auto
        "side   main"   1fr
        / 16rem 1fr;
}

.header { grid-area: header; }
.sidebar { grid-area: side; }
.main { grid-area: main; }
```

#### Why It Matters

The visual structure becomes explicit in the stylesheet.



### Deep Dive — Container Queries Awareness

Media queries respond to viewport/environment conditions. Container queries allow a component to adapt based on the size of its containing layout context.

This is valuable for reusable components that may appear in both wide and narrow columns.

#### Example

```css
.widget-shell {
    container-type: inline-size;
}

@container (min-width: 30rem) {
    .widget {
        display: grid;
        grid-template-columns: 1fr auto;
    }
}
```

#### Why It Matters

Component responsiveness no longer depends entirely on the global viewport.



### Deep Dive — Typography and Readable Measure

Readable typography depends on font family, line height, line length, contrast, and responsive scale.

Long prose is usually easier to read when the line measure is constrained.

#### Example

```css
body {
    font-family:
        system-ui,
        -apple-system,
        "Segoe UI",
        sans-serif;
    line-height: 1.6;
}

.prose {
    max-inline-size: 70ch;
}
```

#### Why It Matters

Typography is a usability system, not simply choosing a font.



### Deep Dive — Design Tokens with CSS Custom Properties

Custom properties can encode a reusable design system: spacing scale, radii, typography, surfaces, and semantic status values.

#### Example

```css
:root {
    --space-1: 0.25rem;
    --space-2: 0.5rem;
    --space-3: 1rem;
    --radius-1: 0.5rem;
    --content-max: 75rem;
}
```

#### Why It Matters

A small token system reduces arbitrary one-off styling decisions.



### Deep Dive — Component CSS Architecture

Organize styles by responsibility rather than letting selectors grow randomly.

A practical component naming convention may use:
- `.card`
- `.card__title`
- `.card--critical`

The specific convention matters less than consistent ownership.

#### Example

```css
.card {}
.card__title {}
.card__meta {}
.card--critical {}
```

#### Why It Matters

Teams need to know which styles belong to which component.



### Deep Dive — Interactive States and Focus

Interactive components require visible states for keyboard, pointer, and disabled behavior.

Do not remove focus outlines without providing an equally clear replacement.

#### Example

```css
.button:hover {
    transform: translateY(-1px);
}

.button:focus-visible {
    outline: 3px solid currentColor;
    outline-offset: 3px;
}

.button:disabled {
    opacity: 0.55;
    cursor: not-allowed;
}
```

#### Why It Matters

Hover alone does not serve keyboard or touch users.



### Deep Dive — Reduced Motion and User Preferences

Motion can cause discomfort or distraction. Respect the user's reduced-motion preference while keeping important state changes understandable.

#### Example

```css
@media (prefers-reduced-motion: reduce) {
    *,
    *::before,
    *::after {
        scroll-behavior: auto !important;
        animation-duration: 0.01ms !important;
        transition-duration: 0.01ms !important;
    }
}
```

#### Why It Matters

Accessibility includes respecting user-level preferences.



### Deep Dive — Dark-Mode Preference

A color scheme is not accessible merely because it is dark. Re-evaluate contrast, states, surfaces, and semantic colors.

#### Example

```css
@media (prefers-color-scheme: dark) {
    :root {
        --surface: #151515;
        --text: #f2f2f2;
    }
}
```

#### Why It Matters

Theme adaptation should preserve information and readability.



### Deep Dive — Print Styles

Print output often needs different priorities than screen UI. Hide navigation/controls and preserve report content.

#### Example

```css
@media print {
    nav,
    .toolbar,
    .button {
        display: none !important;
    }

    body {
        color: black;
        background: white;
    }
}
```

#### Why It Matters

Operational reports and documentation are often printed or exported.



### Deep Dive — Progressive Enhancement

Start with meaningful HTML that performs the core task. Add CSS for presentation, then JavaScript for enhancement.

If one layer fails, the lower layer should remain coherent where practical.

#### Diagram / Mental Model

```text
semantic HTML
    ↓
CSS presentation
    ↓
JavaScript enhancement
```

#### Why It Matters

Progressive enhancement creates resilient interfaces and prepares for the next module.



### Deep Dive — Native HTML Before ARIA

ARIA can add semantics when native HTML cannot express the required widget. It should not replace correct native controls.

Use a real button instead of a clickable div.

#### Example

```html
<button type="button">
    Refresh
</button>
```

#### Why It Matters

Native controls already provide role, focus, keyboard behavior, and assistive-technology integration.



### Deep Dive — Accessibility Tree Mental Model

Assistive technologies consume an accessibility representation derived from the DOM and accessibility semantics.

For an interactive element, ask:
- role?
- accessible name?
- state/value?
- relationships?

#### Diagram / Mental Model

```text
DOM
 ↓
accessibility mapping
 ↓
role + name + state + relationships
 ↓
assistive technology
```

#### Why It Matters

This becomes essential when JavaScript creates dynamic UI.



### Deep Dive — HTML/CSS Security Boundary Awareness

HTML contains security-sensitive contexts such as form actions, link destinations, iframe sources, resource URLs, and later DOM injection points.

Do not confuse visual correctness with trustworthiness.

#### Why It Matters

Course 14 will show how unsafe HTML parsing of untrusted strings can become XSS.



### Deep Dive — Content Security Policy Awareness

Content Security Policy is a browser-enforced policy delivered by a server that can restrict classes of script, style, image, frame, and other resource behavior.

Frontend architecture affects how easy it is to deploy a strong policy.

#### Diagram / Mental Model

```text
HTTP response + CSP
      ↓
browser
      ↓
resource / inline execution attempt
   ├─ allowed
   └─ blocked/reported
```

#### Why It Matters

CSP is defense-in-depth, not a substitute for safe HTML/JavaScript.



### Deep Dive — Developer Tools: CSS Debugging Workflow

When a style does not work, investigate systematically:

1. Did the stylesheet load?
2. Does the selector match?
3. Is the declaration syntactically valid?
4. Is another declaration winning?
5. What is the computed value?
6. What layout context applies?
7. What does the box model show?
8. Is intrinsic sizing/overflow involved?

#### Why It Matters

DevTools turns CSS from trial-and-error into observable engineering.



### Deep Dive — Responsive Stress Testing

A page is not responsive simply because it works at two preset viewport widths.

Test:
- narrow/medium/wide widths
- browser zoom
- text zoom
- long strings
- missing images
- keyboard-only navigation
- reduced motion
- dark preference if implemented

#### Why It Matters

Robust responsive design means the layout survives changing constraints.



### Deep Dive — Final HTML/CSS Engineering Model

A strong frontend foundation combines document meaning, accessible interaction, predictable CSS, responsive layout, and observable debugging.

#### Diagram / Mental Model

```text
content
  ↓
semantic HTML
  ↓
accessible controls
  ↓
cascade + box model
  ↓
normal flow
  ↓
Flex / Grid
  ↓
responsive adaptation
  ↓
states / motion
  ↓
DevTools + accessibility review
```

#### Why It Matters

The objective is a maintainable interface, not a screenshot that only looks correct at one width.



## 5. Hands-on Lab / Practical Exercises


### Lab 1 — Semantic Infrastructure Dashboard

Build a static operations dashboard.

**Step 1 — Create the project**

```text
web-foundations/
├── index.html
└── styles.css
```

**Step 2 — Build semantic page structure**

Include:

- `<header>`
- `<nav>`
- `<main>`
- At least three `<section>` elements
- Status cards
- One data table
- `<footer>`

**Step 3 — Add CSS**

Use:

- Global `box-sizing`
- CSS custom properties
- A centered responsive container
- Flexbox for navigation
- Grid for status cards
- Responsive media query
- Visible keyboard focus

**Step 4 — Test**

- Resize the browser.
- Navigate using only the keyboard.
- Inspect the page with Developer Tools.
- Disable CSS and verify that the document still has meaningful structure.

**Expected result**

A responsive static dashboard whose content remains understandable even without CSS.
### Lab 2 — Accessible Deployment Request Form

Create a form containing:

- Requester name
- Email
- Environment
- Cloud provider
- Region
- Number of instances
- Maintenance window
- Notes
- Agreement checkbox
- Submit button

Requirements:

1. Every control must have a proper label.
2. Use appropriate input types.
3. Add HTML constraints such as `required`, `min`, and `max`.
4. Group related radio controls with `<fieldset>` and `<legend>`.
5. Add CSS focus states.
6. Make the form comfortable on mobile and desktop.
7. Do not rely on placeholder text as the only label.

Example grouping:
```html
<fieldset>
    <legend>Environment</legend>

    <label>
        <input type="radio" name="environment" value="dev" required>
        Development
    </label>

    <label>
        <input type="radio" name="environment" value="prod">
        Production
    </label>
</fieldset>
```
### Lab 3 — Reproduce a Responsive Layout from a Sketch

Create a simple sketch on paper:

```text
Desktop:
+-----------------------------+
| Header                      |
+--------+--------------------+
| Side   | Main               |
| bar    | cards / table      |
+--------+--------------------+

Mobile:
+-----------------------------+
| Header                      |
+-----------------------------+
| Main                        |
| cards                       |
| table                       |
+-----------------------------+
```

Implement it using Grid for the page and Flexbox inside components.

Do **not** use absolute positioning to build the main layout.


## Enhanced Hands-on Labs

### Enhanced Lab 1 — Rendering Pipeline

Inspect DOM, styles, layout, and paint-related information for one page and draw the browser rendering flow.

### Enhanced Lab 2 — Parser Recovery

Create one invalid nesting example, inspect live DOM, then repair it.

### Enhanced Lab 3 — URL Resolution

Predict and verify absolute/root-relative/document-relative resource URLs.

### Enhanced Lab 4 — Semantic Refactor

Convert a div-heavy page into semantic landmarks and sections.

### Enhanced Lab 5 — Skip Link

Add a keyboard-visible skip link to main content.

### Enhanced Lab 6 — Heading Audit

Build a five-section operations page and justify every heading level.

### Enhanced Lab 7 — Technical Text Semantics

Use code, kbd, samp, strong, em, abbr, and time appropriately.

### Enhanced Lab 8 — Links vs Buttons

Classify 20 interactions as navigation or action.

### Enhanced Lab 9 — Responsive Images

Implement srcset/sizes with three image candidates and inspect loading.

### Enhanced Lab 10 — Accessible Table

Create a 30-row inventory table with caption and header relationships.

### Enhanced Lab 11 — Responsive Table

Make a wide table usable on a narrow viewport without destroying table semantics.

### Enhanced Lab 12 — GET Form

Create a search form and inspect the query URL it produces.

### Enhanced Lab 13 — POST Form

Create a maintenance form and inspect request structure using a local server.

### Enhanced Lab 14 — Labels

Create explicit labels and aria-describedby help text.

### Enhanced Lab 15 — Radio Group

Use fieldset/legend for a related group.

### Enhanced Lab 16 — Constraint Validation

Use required/min/max/type, then document why backend validation remains mandatory.

### Enhanced Lab 17 — Readonly vs Disabled

Submit both and inspect which values are included.

### Enhanced Lab 18 — Button Types

Demonstrate submit/button/reset behavior.

### Enhanced Lab 19 — Iframe Review

Create a controlled iframe and document title/loading/sandbox choices.

### Enhanced Lab 20 — Cascade Trace

Create five conflicting declarations and determine the winning rule.

### Enhanced Lab 21 — Cascade Layers

Organize reset/base/components/utilities with @layer.

### Enhanced Lab 22 — Specificity Refactor

Replace overly specific selectors with low-specificity component selectors.

### Enhanced Lab 23 — Box Model

Calculate dimensions under content-box and border-box, then verify.

### Enhanced Lab 24 — Margin Collapse

Create adjacent blocks and inspect vertical margin behavior.

### Enhanced Lab 25 — Logical Properties

Rewrite physical spacing rules using inline/block properties.

### Enhanced Lab 26 — Fluid Sizing

Use min/max/clamp for container and heading sizing.

### Enhanced Lab 27 — Stacking Context

Create two stacking contexts and diagnose an apparently broken z-index.

### Enhanced Lab 28 — Flex Axes

Implement one toolbar as row and column layouts and explain axes.

### Enhanced Lab 29 — Flex Shrink

Build fixed sidebar + flexible main and inspect grow/shrink/basis.

### Enhanced Lab 30 — Intrinsic Overflow

Create long content overflow and repair with min-inline-size:0.

### Enhanced Lab 31 — Grid Tracks

Build sidebar/main with minmax(0,1fr).

### Enhanced Lab 32 — Auto-fit Cards

Create a responsive card grid without a media query.

### Enhanced Lab 33 — Named Areas

Build a page using named grid areas.

### Enhanced Lab 34 — Container Query

Make one card change internal layout based on its container.

### Enhanced Lab 35 — Typography

Build readable prose using line height, system font stack, and 70ch measure.

### Enhanced Lab 36 — Design Tokens

Create spacing/radius/status custom properties.

### Enhanced Lab 37 — Focus States

Design hover/focus/disabled states that remain keyboard accessible.

### Enhanced Lab 38 — Reduced Motion

Add motion then respect prefers-reduced-motion.

### Enhanced Lab 39 — Dark Preference

Add dark mode and manually review contrast.

### Enhanced Lab 40 — Print Styles

Create a print-friendly report.

### Enhanced Lab 41 — Progressive Enhancement

Verify the page remains meaningful with CSS disabled.

### Enhanced Lab 42 — Accessibility Tree

Inspect landmarks, headings, links, table, and form controls.

### Enhanced Lab 43 — Network Debugging

Break a stylesheet/image URL and diagnose it in DevTools.

### Enhanced Lab 44 — Stress Test

Test 200% zoom, long text, narrow viewport, and keyboard navigation.

### Enhanced Lab 45 — Security Review

List trust-sensitive HTML contexts used by the project.

### Enhanced Lab 46 — Capstone

Complete the expanded Cloud Operations Portal.


## 6. Mini Project

### Mini Project — Responsive Cloud Operations Portal

Create a multi-section static portal for an imaginary cloud operations team.

**Required pages or sections**

- Home/overview
- Service status
- Infrastructure inventory
- Maintenance request form
- Documentation/resources

**HTML requirements**

- Semantic structure
- Logical heading hierarchy
- Navigation links
- Accessible images
- A meaningful table
- A complete form
- At least one `<figure>`
- Useful metadata in `<head>`

**CSS requirements**

- Mobile-first responsive design
- Flexbox and Grid
- Custom properties
- Consistent spacing scale
- Reusable classes
- Clear focus states
- Responsive table handling
- At least one tasteful transition
- Reduced-motion consideration

**Quality checks**

- Page works without horizontal overflow at common viewport widths.
- Navigation works with keyboard only.
- Form controls have labels.
- No layout is built entirely with fixed pixel positions.
- Developer Tools show no missing stylesheet or image resources.
- HTML remains understandable if CSS is disabled.

**Stretch goals**

Create a print stylesheet, dark-mode preference support, and an accessible skip link.


### Expanded Capstone — Responsive Cloud Operations Portal

Build a complete static frontend foundation that Course 14 can enhance with JavaScript.

```text
cloud-operations-portal/
├── index.html
├── services.html
├── inventory.html
├── maintenance.html
├── docs.html
├── assets/
│   ├── css/
│   │   ├── reset.css
│   │   ├── tokens.css
│   │   ├── base.css
│   │   ├── layout.css
│   │   └── components.css
│   └── images/
└── README.md
```

Required HTML:

```text
doctype + lang
metadata
skip link
header/nav/main/footer
logical h1-h3 hierarchy
lists
figure/figcaption
responsive image
accessible data table
GET search form
maintenance form
labels
fieldset/legend
help text
required/min/max/email/date/number controls
intentional button types
```

Required CSS:

```text
border-box baseline
custom-property design tokens
logical properties
fluid container
readable text measure
Flexbox
Grid
auto-fit/minmax
content-driven media query
container-query exercise
visible focus
hover/disabled/active states
reduced motion
dark preference
print stylesheet
responsive table
```

Required accessibility checks:

```text
keyboard-only navigation
skip link
logical headings
labels
meaningful link text
alt-text decisions
status not color-only
200% zoom
accessibility-tree inspection
```

Required debugging evidence in README:

```text
one cascade conflict
one box-model/layout problem
one broken-resource problem
one accessibility issue
how DevTools revealed each one
```

Required security notes:

```text
HTML validation is not server security
browser-visible resources are not secrets
iframes/external resources are trust boundaries
native HTML should be preferred to custom ARIA
Course 14 will treat DOM insertion as security-sensitive
```

The final portal must remain understandable when CSS is disabled, images fail, the viewport becomes narrow, or the user relies only on keyboard navigation.


## 7. Recommended Resources

Prioritize official and standards-oriented references:

- MDN Web Docs — HTML.
- MDN Web Docs — CSS.
- WHATWG HTML Living Standard for authoritative HTML behavior.
- W3C Web Accessibility Initiative (WAI) tutorials.
- web.dev articles on responsive design, performance, and accessibility.
- Browser Developer Tools documentation from Chrome/Edge/Firefox.

When a tutorial disagrees with current browser documentation, verify the behavior in MDN, a standard, or browser documentation rather than relying on an old blog post.

## 8. Certification Relevance

HTML and CSS are not central objectives of RHCSA, AWS Solutions Architect, or Kubernetes certifications. However, they are prerequisites for understanding:

- Browser-facing applications.
- Backend/frontend boundaries.
- HTTP forms and requests.
- Web application security.
- Cross-origin behavior.
- Browser storage.
- API consumption.
- Web penetration-testing concepts.

For the unified track, HTML/CSS provide the browser-side foundation needed before Client-Side Technologies, backend development, application security, and web penetration testing.

## 9. Common Mistakes & Best Practices

- **Mistake:** Using `<div>` for everything.  
  **Best practice:** Use semantic HTML when an element expresses the content's meaning.

- **Mistake:** Choosing heading levels for font size.  
  **Best practice:** Choose headings based on document hierarchy, then style with CSS.

- **Mistake:** Using tables for page layout.  
  **Best practice:** Use Grid/Flexbox for layout and tables only for tabular data.

- **Mistake:** Removing focus outlines.  
  **Best practice:** Preserve or replace them with a clearly visible `:focus-visible` style.

- **Mistake:** Using `!important` to solve every CSS conflict.  
  **Best practice:** Understand the cascade and keep selectors predictable.

- **Mistake:** Forgetting mobile viewport metadata.  
  **Best practice:** Include the responsive viewport `<meta>` element.

- **Mistake:** Trusting HTML form validation as security.  
  **Best practice:** Treat it as usability support; server-side validation is still mandatory.

- **Mistake:** Hard-coding every dimension in pixels.  
  **Best practice:** Use flexible units and responsive constraints where appropriate.

- **Mistake:** Using absolute positioning for main layouts.  
  **Best practice:** Prefer normal flow, Flexbox, or Grid.

- **Mistake:** Using color alone for status.  
  **Best practice:** Combine color with text, iconography, or another non-color signal.


### Additional HTML/CSS Mistakes & Best Practices

- **Mistake:** Treating browser error recovery as proof of valid HTML.
  - **Best practice:** Inspect live DOM and keep nesting valid.
- **Mistake:** Confusing filesystem paths with URL resolution.
  - **Best practice:** Resolve from the document/base URL.
- **Mistake:** Using placeholders instead of persistent labels.
  - **Best practice:** Provide real labels.
- **Mistake:** Forgetting disabled controls are normally not submitted.
  - **Best practice:** Choose disabled vs readonly intentionally.
- **Mistake:** Solving every conflict with specificity escalation.
  - **Best practice:** Keep selectors shallow and use cascade architecture.
- **Mistake:** Increasing z-index indefinitely.
  - **Best practice:** Identify stacking contexts.
- **Mistake:** Hiding overflow to conceal layout errors.
  - **Best practice:** Diagnose sizing and flow.
- **Mistake:** Device-brand breakpoints.
  - **Best practice:** Add breakpoints when content needs them.
- **Mistake:** Assuming dark mode automatically has sufficient contrast.
  - **Best practice:** Test semantic colors/states again.
- **Mistake:** Adding ARIA where native HTML already works.
  - **Best practice:** Native HTML first.


## 10. Self-Assessment Questions (with short answers)

1. **What is HTML primarily responsible for?**  
   Structure and semantic meaning.

2. **What is CSS responsible for?**  
   Presentation, visual styling, and layout.

3. **What is the DOM?**  
   The browser's object/tree representation of the parsed document.

4. **Why is semantic HTML important?**  
   It improves meaning, accessibility, maintainability, and machine interpretation.

5. **What is the difference between `<div>` and `<span>`?**  
   Both are generic containers; `<div>` is block-like by default, while `<span>` is inline by default.

6. **Why should a form input have a label?**  
   It identifies the control and improves accessibility and usability.

7. **What does `name` do on a form control?**  
   It identifies the key used when form data is submitted.

8. **What does `box-sizing: border-box` change?**  
   Declared width/height include padding and border.

9. **What is specificity?**  
   A selector-weight mechanism used by the cascade to resolve competing declarations.

10. **When should Flexbox be preferred?**  
    Primarily for one-dimensional alignment and distribution.

11. **When should Grid be preferred?**  
    For two-dimensional row-and-column layouts.

12. **What is mobile-first design?**  
    Starting with a simple narrow-screen layout and progressively enhancing it for larger viewports.

13. **What is `rem` relative to?**  
    The root element's font size.

14. **What does `:focus-visible` help with?**  
    Providing an appropriate visible focus indicator, especially for keyboard interaction.

15. **Why should external input still be validated on the server?**  
    Browser validation can be bypassed.

16. **Why use `alt` text?**  
    To provide a text alternative when an image carries meaningful information.

17. **What is the purpose of `<main>`?**  
    It identifies the dominant content of the document.

18. **Why avoid `!important` everywhere?**  
    It makes the cascade difficult to manage and overrides harder to reason about.

19. **How can you debug CSS rules that do not apply?**  
    Use Developer Tools to inspect selectors, computed styles, specificity, source order, and invalid declarations.

20. **Why is CSS considered cascading?**  
    Multiple style sources and matching rules are combined using defined precedence rules.

## Extended Practice Scenarios

- Build a two-column documentation layout that collapses to one column on small screens.
- Create a server-status badge component with normal, warning, and critical states without relying only on color.
- Create an accessible table containing 20 infrastructure assets.
- Create a responsive login form with visible focus states and browser validation.
- Create an image gallery using Grid without JavaScript.
- Create a navigation bar that wraps cleanly on narrow screens.
- Use `clamp()` to create fluid heading typography.
- Use CSS custom properties to create spacing and typography tokens.
- Create a page that supports the user's dark-mode preference.
- Create a print stylesheet that hides navigation and preserves report content.
- Inspect a real website and identify which parts are semantic elements versus generic containers.
- Disable CSS on your project and evaluate whether the HTML still makes sense.
- Use the accessibility tree in Developer Tools to inspect headings, links, and form controls.
- Create a card grid using both Flexbox and Grid, then explain which solution is clearer.
- Create a form with `fieldset`, `legend`, radio buttons, checkboxes, date, number, and email inputs.


## Extended Self-Assessment

### Extended Q1. What are DOM and CSSOM?

**Answer:** Browser representations of parsed HTML and CSS.

### Extended Q2. What comes after style resolution?

**Answer:** Layout, paint, and compositing at a simplified level.

### Extended Q3. Why inspect live DOM?

**Answer:** Parser error recovery can produce a different tree than expected.

### Extended Q4. What is a root-relative URL?

**Answer:** A URL beginning with `/` resolved from the origin root.

### Extended Q5. Why use a skip link?

**Answer:** Let keyboard users bypass repeated navigation.

### Extended Q6. Why is heading level not a font-size choice?

**Answer:** Headings represent hierarchy; CSS controls appearance.

### Extended Q7. What does srcset provide?

**Answer:** Alternative image resource candidates.

### Extended Q8. Why does form `name` matter?

**Answer:** It identifies the submitted key.

### Extended Q9. GET form use?

**Answer:** Retrieval/search-like request whose state can appear in the URL.

### Extended Q10. Disabled vs readonly?

**Answer:** Disabled is unavailable and normally not submitted; readonly remains non-editable but can be submitted.

### Extended Q11. What precedes specificity in the cascade?

**Answer:** Origin/importance and layer ordering where relevant.

### Extended Q12. Why use border-box?

**Answer:** Declared dimensions include padding and border.

### Extended Q13. What is margin collapse?

**Answer:** Certain vertical margins combine rather than simply add.

### Extended Q14. Why logical properties?

**Answer:** They adapt to writing direction and inline/block axes.

### Extended Q15. What is a stacking context?

**Answer:** A local z-ordering context that limits descendant z-index competition.

### Extended Q16. Why min-inline-size:0?

**Answer:** Allow flexible/grid items to shrink below intrinsic content minimums.

### Extended Q17. Why minmax(0,1fr)?

**Answer:** Allow a flexible grid track to shrink without intrinsic overflow.

### Extended Q18. Media query vs container query?

**Answer:** Environment/viewport response vs container-size response.

### Extended Q19. What is progressive enhancement?

**Answer:** Functional semantic HTML first, then CSS and JS enhancement.

### Extended Q20. Why native HTML before ARIA?

**Answer:** Native controls already include semantics and behavior.

### Extended Q21. What is CSP conceptually?

**Answer:** Browser-enforced policy restricting classes of resource loading/execution.

### Extended Q22. What should responsive testing include?

**Answer:** Widths, zoom, long content, keyboard, accessibility, motion/theme preferences.

### Extended Q23. Why inspect Network panel for CSS bugs?

**Answer:** A missing/failed stylesheet or font/image can masquerade as a styling issue.

### Extended Q24. What is design-token purpose?

**Answer:** Encode reusable design decisions such as spacing/radii/status colors.

### Extended Q25. Final HTML/CSS goal?

**Answer:** Meaningful, accessible, responsive, maintainable, observable UI structure.


## Completion Checklist

- [ ] I can build a valid HTML document from memory.
- [ ] I can explain semantic HTML and choose appropriate elements.
- [ ] I can build accessible forms and tables.
- [ ] I understand the cascade, specificity, inheritance, and source order.
- [ ] I can explain and calculate the CSS box model.
- [ ] I can build layouts using Flexbox and Grid.
- [ ] I can create a responsive mobile-first page.
- [ ] I can debug CSS using browser Developer Tools.
- [ ] I completed all labs and the mini project.


## Enhanced Completion Checklist

- [ ] I can explain DOM, CSSOM, layout, paint, and compositing.
- [ ] I can resolve web-resource URLs correctly.
- [ ] I can design semantic landmarks, headings, links, figures, tables, and forms.
- [ ] I understand form submission and client/server validation boundaries.
- [ ] I can reason about the cascade beyond specificity.
- [ ] I understand box sizing, margin collapse, logical properties, intrinsic sizing, overflow, and stacking contexts.
- [ ] I can build robust Flexbox and Grid layouts.
- [ ] I can use responsive sizing, media queries, container-query concepts, and responsive images.
- [ ] I can create design tokens and reusable component styles.
- [ ] I can design visible focus, disabled, motion, dark, and print states.
- [ ] I understand progressive enhancement and native-HTML-first accessibility.
- [ ] I can use Developer Tools to debug DOM, CSS, layout, accessibility, and resources.
- [ ] I completed the enhanced labs.
- [ ] I completed the expanded Cloud Operations Portal.
