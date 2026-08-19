# Implementation

Translating the analyzed design into code without drift, resolving missing detail, and the final clarity check.

Loaded on demand by `image-to-code`. Section numbers are kept from the original skill so cross-references still resolve.

---

## 26. DESIGN-TO-CODE COPY DISCIPLINE

After generating and analyzing the reference image(s), implement the website in a copy-oriented way.

This means:
- follow the references closely
- preserve layout logic
- preserve spacing rhythm
- preserve section ordering
- preserve text/image balance
- preserve typography mood
- preserve component style
- preserve overall visual cleanliness

Do not drift into a different design direction during implementation.
Do not “improve” the design by replacing it with a generic coded layout.

The goal is not:
- inspired by the image

The goal is:
- visually faithful to the image, translated into real frontend

---

## 27. ANTI-DRIFT IMPLEMENTATION RULE

A common failure mode is design drift:
the generated images look strong, but the coded result becomes generic.

Strictly avoid that.

During implementation:
- do not simplify into default templates
- do not replace distinctive sections with generic rows
- do not compress generous spacing into dense layout
- do not replace strong typography with plain hierarchy
- do not remove the page’s visual identity for convenience
- do not merge section logic into repetitive patterns that were not present in the source images
- do not reintroduce nested-box complexity that was intentionally removed during analysis

The final coded result should still feel like the same website as the generated references.

---

## 28. MISSING DETAIL RESOLUTION

When implementing from images, some details may still be unclear.

Resolve ambiguity by following this order:
1. preserve the visible design language
2. preserve layout and spacing logic
3. preserve component family
4. preserve mood and polish level
5. generate an extra detail image if needed
6. regenerate the section as a fresh standalone image if needed
7. only then choose the most implementation-friendly faithful version

Do not fill ambiguity with generic defaults too quickly.

---

## 35. CLARITY CHECK

Before finalizing, verify internally:

1. Has the design been generated first?
2. Have all generated images been deeply analyzed?
3. Is the text readable enough?
4. If not, were extra detail images created?
5. Were enough images generated, or was the image count too lazy?
6. Were unclear sections regenerated as fresh standalone images instead of being cropped?
7. Is the hierarchy obvious?
8. Is the hero clean enough?
9. Is typography analyzed properly?
10. Are spacing relationships understood properly?
11. Are buttons and components extracted properly?
12. Are colors analyzed properly?
13. Is the design visually distinctive?
14. Is it free of obvious AI tells?
15. Can someone code from this faithfully?
16. If multiple images exist, do they clearly belong together?
17. Have you avoided compressing too many sections into one tiny image?
18. Was the analysis clean, structured, and specific?
19. Has unnecessary nested boxing been removed?
20. Is the first screen still clean and readable on a small laptop?
21. Have useless pills, labels, and fake technical micro-elements been reduced?

If not, refine internally before output.

---
