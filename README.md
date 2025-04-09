GooeyEx
---
- Original repo: https://github.com/chriskiehl/Gooey
- Forked from: https://github.com/nicolasbraun/Gooey

Fixes 
---
- Fix wxTimer issue discovered by [abrichr](https://github.com/chriskiehl/Gooey/issues/845)
- Proper fix for https://github.com/chriskiehl/Gooey/issues/826#issuecomment-1240180894 where `TaskBarIcon` is being instantiated multiple times

Enhancements
---
- Better Dark Mode by [nicolasbraun](https://github.com/chriskiehl/Gooey/pull/891)
- Native `tqdm` progress reporting support
- Automatically formatted argument help text

Usage
---
There's *no* breaking API change from the original Gooey - you need to import `GooeyEx` instead of `Gooey` though.

Please refer to the orignal [Table Of Contents](https://github.com/chriskiehl/Gooey?tab=readme-ov-file#table-of-contents) for usage instructions.