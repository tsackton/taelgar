# **Coastline**

The master coastline is stored as a vector layer. 

For display / export, you likely want ripples and a raster coast. 

To create ripples:
- select coastline_VEC (master coastline) (option-click to select object)
- expand selection 8 px
- new layer (ripples_1) -> edit/stroke, 3 px fill, color `#444444`
- repeat, expand selection 16 px
- new layer (ripples_2) -> edit/stroke, 3 px fill, color `#7b7b7b`
- repeat, expand selection 32 px (or 24 px for a closer wave)
- new layer (ripples_3) -> edit/stroke, 3 px fill, color `#c1c1c1`

Can make more subtle by adjusting opacity of ripples, e.g. 70% or 50%

Alternatively can do these with the "stroke along path" approach below; stroke-along-path is particularly good for a coastline render layer. 

------

ChatGPT

Artistic export:

Yes, totally – and you can do it _without_ losing the nice clean geometry you’ve got.

You’ve basically got two good options:

- **A. “Automatic” subtle variation** – quickest, great for tiny wobble in opacity/intensity
    
- **B. “Hand-drawn” brush stroke** – more organic, especially if you want a sketchy vibe
    

I’ll walk both – you can mix and match.

---

## A. Quick subtle variation (noise on the line only)

This is great for your **ripple lines** or the raster coastline render: keeps them crisp, just gives a little life so they don’t look like flat vector strokes.

### 1. Lock the line pixels

1. Select the ripple (or coastline render) layer.
    
2. In the Layers panel, click the little **checkerboard icon** (“Lock Transparent Pixels”) at the top.
    
    - Now any edits only affect the existing line pixels, not the empty background.
        

### 2. Add tiny brightness variation

3. With that layer still selected:  
    `Filter → Noise → Add Noise…`
    
4. Settings to try:
    
    - Amount: **1–3%**
        
    - Distribution: **Uniform**
        
    - **Monochromatic**: ON
        
5. Click OK.
    

Optional polish:

6. `Filter → Blur → Gaussian Blur…`
    
    - Radius: **0.3–0.7 px**
        

That softens the speckle into a very gentle variation in intensity instead of obvious grain.

You’ll still have a clean line, but it won’t look like a perfectly uniform vector stroke.

---

## B. “Hand-drawn” lines using your path + a textured brush

Here you keep your **vector master coastline** for selections, but draw the visible line with a **brush** that has opacity/size jitter. Great for the _main_ coastline.

### 1. Set up the brush

1. Pick the **Brush Tool (B)**.
    
2. Choose a basic round or slightly textured brush.
    
3. Open **Brush Settings** (`Window → Brush Settings`):
    
    - **Shape Dynamics**:
        
        - Size Jitter: **5–15%**
            
    - **Transfer** (or “Other Dynamics” depending on version):
        
        - Opacity Jitter: **10–20%**
            
    - Smoothing: ON  
        (You don’t need a tablet – jitter handles variation for you.)
        

### 2. Stroke along the path

4. In the **Paths** panel, select your coastline path.
    
5. Make a **new blank layer** above the ocean, below land – call it `Coast_Brush`.
    
6. Back in Paths panel, click the menu (≡) → **Stroke Path…**
    
7. Choose **Brush** as the tool, **uncheck** “Simulate Pressure” if you want consistent width.
    
8. Click OK.
    

You’ll get a single coastline line, but with slight thickness and opacity variation from the brush jitter → looks more “inked”.

If you don’t like it:

- Undo, tweak the brush settings (less size jitter, more opacity jitter, etc.), and stroke again.
    

You can do the exact same thing for **ripples**:

- Make a path offset from the coast (or just use your selection → `Make Work Path`)
    
- Stroke _that_ with the same brush on another layer.
    

---

## C. Extra finesse with a mask (if you want really subtle, patchy variation)

1. On a line layer you like, click **Add Layer Mask**.
    
2. Click the mask thumbnail.
    
3. `Filter → Noise → Add Noise…` (2–3%, Monochromatic)
    
4. `Filter → Blur → Gaussian Blur…` (1–2 px)
    

Now the **mask** slightly fades parts of the line in and out → gentle, organic intensity variation without moving the line at all. If it’s too strong, just:

- Lower the layer’s **opacity**, or
    
- `Ctrl/Cmd+L` on the mask and push the midtones back toward white.
    

---

### Suggested combo for your world map

For the **main coastline**:

- Keep `VECTOR_Coast_Master` as your clean reference.
    
- Use Method B (brush-stroked path) on a `Coast_Render` layer.
    
- Optionally add the mask from Method C for extra subtlety.
    

For the **ripples**:

- Use your existing 1–2 px Stroke method.
    
- Then apply Method A (lock transparency + noise + tiny blur).
    

You’ll keep all the geometric accuracy you’ve worked for, but visually the coast will feel a lot more “alive” and less like a CAD export.

If you tell me whether you’re going for more **old-school hand-drawn fantasy map** vs. **clean modern atlas**, I can give you specific brush and jitter values tuned for that look.