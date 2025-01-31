---
headerVersion: 2023.11.25
tags: [background]
dm_owner: none
dm_notes: none
---
# Spiritual Realms

In the [[Standard Multiversal Model]] taught by the [[Faculty of Metaphysics]] at the [[University of Chardon]], the Spiritual Realms are defined as distinct planes existing within the vast matrix of the far regions of the [[Astral Plane]].  Lying beyond the [[Land of the Dead]], they remain largely inaccessible from the [[Material Plane]] except through astral travel, planar gateways, or the passage of souls. These are largely congruent with the [[Outer Realms]] of [[Yendalism]], although Yendalists also include the [[Land of the Dead|Divine Veil]] and the [[Plane of Creation]] in their list of the Outer Realms. 

All planar geographers distinguish the [[Divine Realms]], the "home of the gods", from other Spiritual Realms, which are thought to have diverse metaphysics, although usually metaphysical cosmologists assume that all spiritual realms, whether divine or not, share some fundamental properties. [[Gaius Devarro]] first codified these, writing the as the following four principles of the metaphysical truth of Spiritual Realms:
- **The Principle of Essential Return** – That which is native to a spiritual realm cannot be unmade beyond its borders, but will return to its essence when struck down elsewhere.
- **The Principle of Shaped Dominion** – Though each spiritual realm is bound to a structure of being—by decree, by nature, or by its ruling power— the faith of mortals may, in time, shape its form.
- **The Principle of Inherent Reality** – The spiritual realms exist according to their own essence, purpose, and form, neither mirroring the Material Plane nor relying upon it for existence; their influence upon mortals is carried only through the manifestation of souls.
- **The Principle of Essential Permanence** – Each spiritual realm is the perfect manifestation of its essence, unshaken by time or decay; only a fundamental shift in that essence may bring change to the immutable.

Followers of [[Yendalism]] typically add a fifth truth to this list:
- **The Principle of Veiled Dominion** – No power within the spiritual realms may act freely upon any of the [[Inner Realms]], for the [[Land of the Dead|Divine Veil]] stands between them; yet through passage, pact, or willing soul, their influence may cross beyond their own dominion.

%%^Campaign:none%%

Open Questions:
- [[Cosmology - Open Questions]]

## List of Spiritual Realms

```dataviewjs
const { util } = customJS
dv.table(["Place"], 
			dv.pages("#place")
				.where(f => util.inLocation("Spiritual Realms", f.file.frontmatter, dv.current().pageTargetDate))
				.sort(b => util.s("<maintype>", b.file))
				.map(b => [util.s("<name:x>", b.file)]))
```

%%^End%%