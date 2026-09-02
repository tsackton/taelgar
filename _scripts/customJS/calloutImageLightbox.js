class CalloutImageLightbox {
    constructor() {
        // Obsidian does not attach its Live Preview image widget inside callouts.
        this.imageSelector = [
            '.markdown-source-view .callout[data-callout="image"] img',
            '.markdown-source-view .callout[data-callout="gallery"] img'
        ].join(', ')

        this.onDocumentClick = this.onDocumentClick.bind(this)
        this.onKeydown = this.onKeydown.bind(this)

        const previous = window.taelgarCalloutImageLightbox
        if (previous && previous !== this && typeof previous.deconstructor === "function") {
            previous.deconstructor()
        }
        window.taelgarCalloutImageLightbox = this

        this.invoke()
    }

    invoke() {
        if (this.active) return

        this.active = true
        document.addEventListener("click", this.onDocumentClick, true)

        this.observer = new MutationObserver((mutations) => {
            for (const mutation of mutations) {
                for (const node of mutation.addedNodes) {
                    this.decorateImages(node)
                }
            }
        })
        this.observer.observe(document.body, { childList: true, subtree: true })
        this.decorateImages(document)
    }

    isCalloutImage(element) {
        if (!(element instanceof HTMLImageElement)) return false
        if (!element.closest(".markdown-source-view")) return false

        return Boolean(element.closest(
            '.callout[data-callout="image"], .callout[data-callout="gallery"]'
        ))
    }

    decorateImages(root) {
        const images = []

        if (root instanceof HTMLImageElement && this.isCalloutImage(root)) {
            images.push(root)
        }
        if (root instanceof Element || root instanceof Document) {
            images.push(...root.querySelectorAll(this.imageSelector))
        }

        for (const image of images) {
            this.decorateImage(image)
        }
    }

    decorateImage(image) {
        const frame = image.closest(".image-embed") || image.parentElement
        if (!frame || frame.querySelector(":scope > .taelgar-callout-zoom-button")) return

        frame.classList.add("taelgar-callout-image-frame")

        const button = document.createElement("button")
        button.type = "button"
        button.className = "clickable-icon taelgar-callout-zoom-button"
        button.setAttribute("aria-label", "Zoom in")
        button.setAttribute("data-tooltip-position", "top")

        if (customJS?.obsidian?.setIcon) {
            customJS.obsidian.setIcon(button, "zoom-in")
        } else {
            button.textContent = "+"
        }

        frame.appendChild(button)
    }

    onDocumentClick(event) {
        if (!(event.target instanceof Element)) return

        const button = event.target.closest(".taelgar-callout-zoom-button")
        if (button) {
            const image = button.parentElement?.querySelector("img")
            if (this.isCalloutImage(image)) {
                this.consumeClick(event)
                this.open(image)
            }
            return
        }

        const image = event.target.closest("img")
        if (!this.isCalloutImage(image)) return

        this.consumeClick(event)
        this.open(image)
    }

    consumeClick(event) {
        event.preventDefault()
        event.stopPropagation()
        event.stopImmediatePropagation()
    }

    open(sourceImage) {
        const source = sourceImage.currentSrc || sourceImage.src
        if (!source) return

        this.close()
        this.previouslyFocused = document.activeElement

        const overlay = document.createElement("div")
        overlay.className = "taelgar-live-preview-lightbox"
        overlay.setAttribute("role", "dialog")
        overlay.setAttribute("aria-modal", "true")
        overlay.setAttribute("aria-label", sourceImage.alt || "Image preview")

        const image = document.createElement("img")
        image.className = "taelgar-live-preview-lightbox-image"
        image.src = source
        image.alt = sourceImage.alt || ""

        const closeButton = document.createElement("button")
        closeButton.type = "button"
        closeButton.className = "clickable-icon taelgar-live-preview-lightbox-close"
        closeButton.setAttribute("aria-label", "Close")
        if (customJS?.obsidian?.setIcon) {
            customJS.obsidian.setIcon(closeButton, "x")
        } else {
            closeButton.textContent = "x"
        }

        closeButton.addEventListener("click", () => this.close())
        overlay.addEventListener("click", (event) => {
            if (event.target === overlay) this.close()
        })

        overlay.append(image, closeButton)
        document.body.appendChild(overlay)
        document.body.classList.add("taelgar-lightbox-open")
        document.addEventListener("keydown", this.onKeydown, true)

        this.overlay = overlay
        closeButton.focus()
    }

    onKeydown(event) {
        if (event.key !== "Escape" || !this.overlay) return

        event.preventDefault()
        event.stopPropagation()
        this.close()
    }

    close() {
        if (!this.overlay) return

        this.overlay.remove()
        this.overlay = null
        document.body.classList.remove("taelgar-lightbox-open")
        document.removeEventListener("keydown", this.onKeydown, true)

        if (this.previouslyFocused?.isConnected) {
            this.previouslyFocused.focus()
        }
        this.previouslyFocused = null
    }

    deconstructor() {
        this.close()
        this.observer?.disconnect()
        document.removeEventListener("click", this.onDocumentClick, true)
        document.querySelectorAll(".taelgar-callout-zoom-button").forEach((button) => button.remove())
        document.querySelectorAll(".taelgar-callout-image-frame").forEach((frame) => {
            frame.classList.remove("taelgar-callout-image-frame")
        })

        this.active = false
        if (window.taelgarCalloutImageLightbox === this) {
            delete window.taelgarCalloutImageLightbox
        }
    }
}
