function regenerateHeader(tp) {
    const targetPath = tp.file.path(true);
    tp.hooks.on_all_templates_executed(() => {
        if (app.workspace.getActiveFile()?.path !== targetPath) return;
        if (!app.commands.executeCommandById("taelgarverse:regenerate-page-header")) {
            new Notice("Enable Taelgarverse to regenerate the page header.");
        }
    });
}

module.exports = regenerateHeader;
