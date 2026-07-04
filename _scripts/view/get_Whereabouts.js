const page = dv.current();
return customJS.OutputHandler.outputWhereabouts(page.file.name, page.file.frontmatter ?? page);
